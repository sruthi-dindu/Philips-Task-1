import boto3

# Specify your SageMaker role ARN and workteam ARN
sagemaker_role_arn = 'arn:aws:iam::525419040953:role/service-role/AmazonSageMaker-ExecutionRole-20210505T152517'
workteam_arn = 'arn:aws:sagemaker:ap-south-1:525419040953:workteam/private-crowd/TestWorkteam'

# Initialize the SageMaker client
sagemaker = boto3.client('sagemaker')

# Define the labeling job parameters
labeling_job_name = 'labelling-job-1'
input_data_s3_uri = 's3://caf-workflow/data.jsonl'
output_data_s3_uri = 's3://caf-workflow/test/data/input/'
PRE_HUMAN_TASK_LAMBDA_ARN = (
        "arn:aws:lambda:ap-south-1:565803892007:function:PRE-BoundingBox"
    )
ANNOTATION_CONSOLIDATION_LAMBDA_ARN = (
        "arn:aws:lambda:ap-south-1:565803892007:function:ACS-BoundingBox"
    )

UI_TEMPLATE_S3_URI = "s3://mlops-aicoe/template/bounding-box-ui-template.html"


labeling_job_params = {
    
    'LabelingJobName': labeling_job_name,
    'LabelAttributeName': 'labels',
    'RoleArn': sagemaker_role_arn,
    'InputConfig': {
        'DataSource': {
            'S3DataSource': {
                'ManifestS3Uri': input_data_s3_uri
            }
        },
        'DataAttributes': {
            'ContentClassifiers': ['FreeOfPersonallyIdentifiableInformation', 'FreeOfAdultContent']
        }
    },
    
    'OutputConfig': {
        'S3OutputPath': output_data_s3_uri
    },
    
    'LabelCategoryConfigS3Uri': 's3://caf-workflow/test/data/labeller.json',
    'HumanTaskConfig': {
        'WorkteamArn': workteam_arn,
        'UiConfig': {
            'UiTemplateS3Uri': UI_TEMPLATE_S3_URI
        },
        'TaskKeywords': ['bounding box', 'image labeling'],
        'TaskTitle': 'Bounding Box Labeling Task',
        'TaskDescription': 'Label objects with bounding boxes in images',
        'NumberOfHumanWorkersPerDataObject': 1,
        'TaskTimeLimitInSeconds': 1800,
        'TaskAvailabilityLifetimeInSeconds': 86400,
        'MaxConcurrentTaskCount': 1,
        'AnnotationConsolidationConfig': {
            'AnnotationConsolidationLambdaArn': ANNOTATION_CONSOLIDATION_LAMBDA_ARN
        }, 
        'PreHumanTaskLambdaArn' : PRE_HUMAN_TASK_LAMBDA_ARN
        
    }
}

# Create the labeling job
response = sagemaker.create_labeling_job(**labeling_job_params,)

# Print the response
print("Labeling job created with the following response:")
print(response)