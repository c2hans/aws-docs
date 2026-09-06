---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/automation-pipelines.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Automation pipelines
<a name="automation-pipelines"></a>

Automated MLOps pipelines can enable formal and repeatable data processing, model training, model evaluation, and model deployment. In addition to process automation, MLOps pipelines can help enforce standards (for example, naming conventions, tagging, and security controls) and enable data and model lineage tracking. MLOps pipelines are built and operated by the MLOps engineering team, and they mainly consist of the following components:
+ **Code repository** — A code repository is the source for an MLOps pipeline run. It contains artifacts such as docker files, training scripts, and other dependency packages for building containers, training models, and deploying models. Other artifacts such as CloudFormation scripts and pipeline configuration templates are also stored in the code repository. A code repository can reside in the Shared Services account or in the on-prem environment.
+ **Code build service** — A code build service is used to build custom artifacts such as custom Docker containers and push containers to a Docker image repository such as Amazon ECR. AWS CodeBuild or other third-party services such as [Jenkins Build Server](https://www.jenkins.io/) can be used as the code build service.
+ **Data processing service** — Data processing service is used to process raw data into training/validation/testing datasets for model training purpose. SageMaker AI Processing can be used in an automated pipeline to process data.
+ **Model training service** — SageMaker AI training service is used for model training in an automated pipeline. SageMaker AI training service takes input data sources from S3, train the model using a training container, and save the models in an S3 output bucket.
+ **Model registry** — A model registry contains the metadata associated with model artifacts such as the location of the model artifacts, the associated inference container image, and the IAM role for running the container. Models can be registered in the Amazon SageMaker AI Model Registry for model inventory management and model deployment.
+ **Model hosting service** — SageMaker AI provides a model hosting service for both real-time inference and batch inference. It takes model artifacts from the SageMaker AI Model Registry and deploys it to a serving endpoint.
+ **Pipeline management** — The end-to-end pipeline management is controlled by the AWS CodePipeline service. AWS CodePipeline integrates with a code repository (such as AWS CodeCommit or [BitBucket](https://bitbucket.org/)), and AWS CodeBuild. It also supports different deployment actions using AWS Lambda, CloudFormation, and AWS Step Functions within the same account or across accounts. One of the main components in an end-to-end pipeline is the model build workflow orchestration for repeatable automated model building. The orchestration can be managed through services like SageMaker AI Pipelines or AWS Step Functions.

The following figure illustrates one MLOps pipeline reference architecture that works across multiple AWS accounts to build a custom container, process data, train a model, and deploy a model to an endpoint.

![A diagram showing cross account CI/CD flow for model training and deployment.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-11.png)

*Cross-account CI/CD flow for model training and deployment*

The pipeline in the figure consists of the following five stages:

1. **Change commit stage** — The data scientist/ML engineer commits code changes into a code repository (such as CodeCommit) from the data science account from the SageMaker AI notebook / Studio.

1. **Pipeline start stage** — A CodePipeline pipeline run is triggered in the Shared Services account. CodePipeline natively integrates with AWS CodeCommit, Enterprise Git, and BitBucket, downloads source codes from the code repository, and saves them into an S3 bucket used for CodePipeline inputs and outputs that's accessible by the different pipeline stages and action.

1. **Container build stage** — A CodeBuild project is then run as the next step in the pipeline in the Shared Services account. It uses the source code saved in the S3 bucket to build a custom Docker container and pushes the container image to the Amazon ECR repository in the Shared Services account.

1. **Model building stage** — Upon the successful Docker image build, the model training step is kicked off across the account (from the Shared Services account to the Test / UAT account) by launching a CloudFormation script in the Test/UAT account. The CloudFormation script first creates an AWS Step Functions state machine workflow consisting of a SageMaker AI processing step, a SageMaker AI model training step, and an endpoint deployment step in the test / UAT account for testing purposes. After the state machine is created, the CodePipeline triggers the Step Functions state machine to run all the steps defined in the state machine. The processing step and training step use containers hosted in the Shared Services account Amazon ECR or public containers (built-in algorithms or managed containers) hosted by the SageMaker AI platform.

   In addition to Step Functions, other workflow orchestration tools such as [SageMaker AI Pipeline](https://aws.amazon.com/sagemaker/pipelines/) and AirFlow can also be used to orchestrate model training steps such as data processing, model training and model registration. SageMaker AI Pipeline enables you to create a workflow definition using the SageMaker AI SDK or a JSON pipeline definition. The CodeBuild job in the Shared Service account builds the SageMaker AI pipeline definition and runs the pipeline in the Test / UAT account by assuming an across-account role. You can also directly visualize the pipelines and track the running of differently pipelines directly inside SageMaker AI Studio.
![A diagram showing CI/CD pipeline with SageMaker AI Pipeline.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-12.png)

   *CI/CD pipeline with SageMaker AI Pipeline*

1. **Model registration stage **— For centralized model management and inventory control. The trained model is registered in the SageMaker AI model registry in the Shared Services account. Any useful model metadata will also be saved in the central model registry for each model.

1. **Production deployment****stage** — When it is ready for production deployment, a separate CodePipeline workflow can be invoked in the Shared Services account to obtain release approval and run a CloudFormation script in the Production account to stand up a SageMaker AI endpoint for real-time inference. The production pipeline can be integrated with a release management ticketing system such as ServiceNow to raise a service ticket for tracking.

## Cross-account CodePipeline setup
<a name="cross-account-codepipeline-setup"></a>

When you create a pipeline with actions from multiple accounts, you must configure your actions with proper permission so that they can access resources within the limitations of cross-account pipelines. The following section reviews some of the key steps and components you need to enable a cross-account pipeline.

![A diagram showing cross account pipeline access.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-13.png)

*Cross account pipeline access*

In the preceding figure, **CodePipeline A** represents the training pipeline, and **CodePipeline A2** represents the production deployment pipeline.
+ **CodePipeline Role A** — This role is assumed by CodePipeline A to run the model training pipeline in the Test / UAT account using CloudFormation. This role has access to the KMS key used for data encryption for CodePipeline A’s input / output bucket. It also has full access to the CodePipeline input / output bucket.
+ **Cross Account Role B** — This role is assumed by CodePipeline Role A to perform operations in the Test / UAT account. Specifically, this role is used to run the CloudFormation script to set up the Step Functions state machine for the training workflow, and invoke the Step Functions state machine after it is created.
+ **Cross Account Role A2** — This role is assumed by CodePipeline A2 to run the model deployment pipeline in the production account.
+ **Cross Account Role C** — This role is assumed by CodePipeline Role A2 to perform operations in the Production account. Specifically, this role is used to run the CloudFormation script to set up the SageMaker AI endpoint and other related resources such as Lambda functions and API Gateway to front the SageMaker AI endpoint.
+ **CodePipeline Input/output bucket** — This bucket is used for sharing artifacts across different pipeline stages and different accounts. AWS Lambda supports bucket policies that can directly be attached to a bucket. In the preceding figure, Policy A is an S3 bucket policy that can provide different accounts with direct bucket access.
+ **KMS Key** — A KMS key is required to encrypt data in the CodePipeline input/output bucket. The KMS key needs to provide access to the Test / UAT account, Production account, and CodePipeline role A. The KMS key is in the same region as the CodePipeline and CodePipeline input / output bucket. CodePipeline Role A will need access to this KMS key.

## Cross-account resource access via VPC endpoint
<a name="cross-account-resource-access-via-vpc-endpoint"></a>

To ensure all network communication takes place within the private network, private endpoints should be used for accessing resources within the same AWS account or across different AWS accounts.

![A diagram showing access resources across account via VPC endpoint.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-14.png)

*Access resources across account via VPC endpoint*

The preceding figure illustrates how Amazon S3 and ECR can be accessed across accounts using VPC endpoints. In this diagram, SageMaker AI is attached to a VPC in the Test / UAT account through an Elastic Network Interface (ENI), and the VPC endpoints for S3 and ECR are attached to the Test / UAT account. To provide SageMaker AI role access to S3 buckets and ECR repositories in both the Test / UAT account and Shared Service account, you need to attach bucket policies and ECR repository policies that permit the SageMaker AI role to access the target S3 buckets and ECR repositories. Note that the S3 endpoint only supports buckets in the same [AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html), and the ECR endpoint also only supports repositories in the same AWS Region.

## Cross-account pipeline example
<a name="cross-account-pipeline-example"></a>

To demonstrate how to build a cross-account pipeline using CodePipeline, review a sample CodePipeline definition with the following 2 stages:
+ **Source stage** — This is the first stage in a pipeline that connects to a AWS CodeCommit repository. AWS CodeCommit is used to store any scripts for model training and CloudFormation templates used in the pipeline. This stage runs in the shared services account.
+ **Deploy training workflow stage** — The second stage is for training and testing models in the Test account. First use a CloudFormation script to create a Step Functions state machine consisting of data processing and a model training step. Later you will invoke the created state machines to train a model.

**Sample CodePipeline definition with cross account support:**

```
{
    "pipeline": {
        "name": "<pipeline name>",
        "roleArn": "arn:aws:iam::<SHARED_SERVICE_ACCOUNT>:role/service-role/<codepipeline_role_name>",
        "artifactStore": {
            "type": "S3",
            "location": "<S3 bucket name>",
            "encryptionKey": {
                "id": "arn:aws:kms:<REGION>: <SHARED_SERVICE_ACCOUNT>:alias/<kms key name>",
                "type": "KMS"
            }
        },
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "CodeCommit",
                            "version": "1"
                        },
                        "runOrder": 1,
                        "configuration": {
                            "BranchName": "<code branch name>",
                            "PollForSourceChanges": "false",
                            "RepositoryName": "<code repository name>"
                        },
                        "outputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ],
                        "inputArtifacts": [],
                        "region": "<region>",
                        "namespace": "SourceVariables"
                    }
                ]
            },
            {
                "name": "Deploy_Training_Workflow",
                "actions": [
                    {
                        "name": "deploy-cf-train-test-external",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "provider": "CloudFormation",
                            "version": "1"
                        },
                        "namespace":"train-stack",
                        "runOrder": 1,
                        "configuration": {
                            "ActionMode": "CREATE_UPDATE",
                            "OutputFileName": "<output file name>",
                            "RoleArn": "arn:aws:iam::TEST_ACCOUNT:role/<cloudformation_role_name>",
                            "StackName": "<CFN stack name>",
                            "TemplatePath": "SourceArtifact::<CFN template file name>"
                        },
                        "outputArtifacts": [
                            {
                                "name": "deploy-cf-train-test-output"
                            }
                        ],
                        "inputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ],
                        "roleArn": "arn:aws:iam::<TEST_ACCOUNT>:role/<Cross Account Role Name>",
                        "region": "<REGION>"
                    },
                    {
                        "name": "invoke-Step-Function",
                        "actionTypeId": {
                            "category": "Invoke",
                            "owner": "AWS",
                            "provider": "StepFunctions",
                            "version": "1"
                        },
                        "runOrder": 2,
                        "configuration": {
                            "InputType": "Literal",
                            "StateMachineArn": "#{train-stack.StateMachineARN}"
                        },
                        "outputArtifacts": [],
                        "inputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ],
                        "roleArn": "arn:aws:iam::<TEST_ACCOUNT>:role/<Cross Account Role Name>",
                        "region": "<REGION>"
                    }
                ]
            }
        ],
        "version": 10
    }
}
```

**Sample CloudFormation template for creating a Step Functions state machine for model training:**

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "An example template for a Step Functions state machine.",
  "Resources": {
    "MyStateMachine": {
      "Type": "AWS::StepFunctions::StateMachine",
      "Properties": {
        "StateMachineName": "SM-train-Step_Function",
        "StateMachineType": "STANDARD",
        "DefinitionSubstitutions": {
          "TrainingImageURL": "<training image ECR URL>",
          "RoleArn_CF": "<Cloudformation execution Role>",
          "Train_data_S3Uri": "<Training dataset S3 URI>",
          "Model_S3OutputPath": "<Model output path>"
        },
        "DefinitionS3Location": {
          "Bucket": "<Shared Services account bucket name>",
          "Key": "<Step Functions state machine definition json file name>"
        },
        "RoleArn": "<Step Function execution role>"
      }
    }
  },
  "Outputs": {
    "StateMachineARN": {
      "Description": "ARN of state machine",
      "Value": {
        "Ref": "MyStateMachine"
      }
    }
  }
}
```
