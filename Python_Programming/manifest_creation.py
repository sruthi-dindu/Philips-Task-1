import boto3
import botocore
import json
from urllib.parse import urlparse
from PIL import Image
from io import BytesIO
def get_bucket_name_object_key(s3_path):
    try:
        # Parse the S3 URL to extract the bucket name and object key
        parsed_url = urlparse(s3_path)
        if parsed_url.scheme != 's3':
            raise ValueError("Invalid S3 URL. Make sure it starts with 's3://'.")
        
        bucket_name = parsed_url.netloc
        object_key = parsed_url.path.lstrip('/')
        
        return bucket_name, object_key

    except ValueError as e:
        # Handle the ValueError and provide a custom error message or take appropriate action
        print(f"Error: {e}")
        return None, None
        
    
def get_jsonl_data_from_s3(s3_path):
    try:
        bucket_name,object_key = get_bucket_name_object_key(s3_path)

        # Initialize an S3 client
        s3 = boto3.client('s3')

        # Get the JSON Lines object from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        json_lines = response['Body'].read().decode('utf-8').splitlines()
        json_list = []

        # Process each line as a separate JSON object
        for line in json_lines:
            json_obj = json.loads(line)
            json_list.append(json_obj)
        return json_list

    except botocore.exceptions.NoCredentialsError:
        print("AWS credentials not found. Please configure your AWS credentials.")
    except botocore.exceptions.EndpointConnectionError:
        print("Unable to connect to AWS. Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def fetch_image_from_s3(s3_path):
    try:
        bucket_name,object_key = get_bucket_name_object_key(s3_path)

        # Initialize an S3 client
        s3 = boto3.client('s3')

        # Fetch the image from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)

        # Read the image data from the response
        image_data = response['Body'].read()

        # Open the image using Pillow
        image = Image.open(BytesIO(image_data))

        # return the image 
        return image

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_prediction(image):
    s3_path = 's3://caf-workflow/test/generate_AL_manifest_files/output/output_VIA_tool/via_project_6Sep2023_9h59m_json (4).json'
    return s3_path

def get_json_data_from_s3(s3_path):
    try:
        bucket_name, object_key = get_bucket_name_object_key(s3_path)

        # Initialize an S3 client
        s3 = boto3.client('s3')

        # Get the JSON object from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        json_data = response['Body'].read().decode('utf-8')

        # Parse the JSON data
        json_obj = json.loads(json_data)

        return json_obj

    except botocore.exceptions.NoCredentialsError:
        print("AWS credentials not found. Please configure your AWS credentials.")
    except botocore.exceptions.EndpointConnectionError:
        print("Unable to connect to AWS. Please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

def sagemaker_bb_format(json_data):
    result_dict = {}  # Use a different variable name to avoid overwriting the built-in dict type
    
    try:
        for key in json_data:
            # Small snippet to slice the image path from key
            extensions = [".png", ".jpg", ".jpeg"]
            file_name = None
            for ext in extensions:
                index = key.find(ext)
                if index != -1:
                    file_name = key[:index] + ext
                    break  # Stop searching once an extension is found
            if file_name is None:
                file_name = key
            
            parsed_url = urlparse(file_name)
            hostname = parsed_url.netloc.split('.')[0]
            path = parsed_url.path.lstrip('/')
            s3_path = f's3://{hostname}/{path}'

            # Create the 'source-ref' entry in the result_dict
            result_dict['source-ref'] = s3_path

            overall_annotation = json_data[key]['regions']
            id = 0
            annotation_list = []
            class_map = {}
            label = {}
            label_metadata = {}
            
            for i in overall_annotation:
                annotation = {}
                shape = i['shape_attributes']
                annotation["class_id"] = id
                annotation["top"] = shape['y']
                annotation["left"] = shape['x']
                annotation["height"] = shape['height']
                annotation["width"] = shape['width']
                annotation_list.append(annotation)
                class_map[id] = i['region_attributes']['label']
                id += 1

            label['annotations'] = annotation_list
            label_metadata['class-map'] = class_map
            result_dict['label'] = label
            result_dict['label-metadata'] = label_metadata
            result_dict['label-metadata']['type'] = 'groundtruth/object-detection'
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Return None to indicate that an error occurred

    return result_dict 

def sage_maker_format(s3_path, job_type):
    if(job_type == 'Bounding Box'):
        json_data = get_json_data_from_s3(s3_path)
        json_bb_data = sagemaker_bb_format(json_data)
        return json_bb_data

def al_inference(image_path):
    image = fetch_image_from_s3(image_path)
    prediction = get_prediction(image)#call the VIA function instead(now I am using the output which is manually stored in s3 bucket)
    return prediction

# Specify the SageMaker role ARN
sagemaker_role_arn = 'arn:aws:sagemaker:ap-south-1:525419040953:notebook-instance/spike-task'

# Initialize the SageMaker client
sagemaker = boto3.client('sagemaker')

#final_dict = {}
input_manifest_file_path = 's3://caf-workflow/test/generate_AL_manifest_files/input/input (3).jsonl'
job_type = 'Bounding Box'
caf_task_bucket = 'caf-workflow'
def generate_AL_manifest(input_manifest_file_path, job_type, caf_task_bucket):
    jsonl_obj = get_jsonl_data_from_s3(input_manifest_file_path)
    if jsonl_obj:
        for json_data in jsonl_obj:
            image_path = json_data['source-ref']
            raw_output = al_inference(image_path)
            if raw_output:
                formatted_output = sage_maker_format(raw_output, job_type)
                if formatted_output:
                    final_dict = json.dumps(formatted_output, indent=None)
                    #print(final_dict)
                    return formatted_output
                    #final_dict.update(json_data)
                else:
                    print("Error in formatting output for SageMaker.")
            else:
                print("Error in AI inference.")
    else:
        print("Unable to connect to the file path. Please check your file path")

final_dict = generate_AL_manifest(input_manifest_file_path, job_type, caf_task_bucket)
#print(final_dict, type(final_dict))
create_manifest_file(caf_task_bucket, final_dict)

def create_manifest_file(bucket_name, json_data):

    import json

    # Define your JSON object
    data = json_data

    # Define the file name for the JSONL file
    file_name = 'data.jsonl'
    #print(data)

    # Create the JSONL file and write the JSON object to it
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=None)
        file.write('\n')

    # Create an S3 client without specifying access keys (AWS IAM role is assumed)
    s3 = boto3.client('s3')

    # Upload the JSONL file to the S3 bucket
    s3.upload_file(file_name, bucket_name, file_name)

    # Clean up: Delete the local JSONL file (optional)
    import os
    os.remove(file_name)

    print(f"File '{file_name}' has been uploaded to '{bucket_name}' successfully.")
