---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros.html
---

# Automatically validate and deploy IAM policies and roles by using CodePipeline, IAM Access Analyzer, and AWS CloudFormation macros
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros"></a>

*Helton Ribeiro and Guilherme Simoes, Amazon Web Services*

## Summary
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros-summary"></a>

This pattern describes the steps and provides code to create a deployment pipeline that allows your development teams to create AWS Identity and Access Management (IAM) policies and roles in your Amazon Web Services (AWS) accounts. This approach helps your organization reduce overhead for your operational teams and speed up the deployment process. It also helps your developers to create IAM roles and policies that are compatible with your existing governance and security controls.

This pattern’s approach uses [AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html) to validate the IAM policies that you want to attach to IAM roles and uses AWS CloudFormation to deploy the IAM roles. However, instead of directly editing the AWS CloudFormation template file, your development team creates JSON-formatted IAM policies and roles. An AWS CloudFormation macro transforms these JSON-formatted policy files into AWS CloudFormation IAM resource types before beginning the deployment.

The deployment pipeline (`RolesPipeline`) has source, validation, and deployment stages. During the source stage, your development team pushes the JSON files that contain the definition of the IAM roles and policies to an AWS CodeCommit repository. AWS CodeBuild then runs a script to validate those files and copies them to an Amazon Simple Storage Service (Amazon S3) bucket. Because your development teams don’t have direct access to the AWS CloudFormation template file stored in a separate S3 bucket, they must follow the JSON file creation and validation process.

Finally, during the deployment phase, AWS CodeDeploy uses an AWS CloudFormation stack to update or delete the IAM policies and roles in an account.

**Important**
This pattern’s workflow is a proof of concept (POC) and we recommend that you only use it in a test environment. If you want to use this pattern’s approach in a production environment, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation and make the required changes to your IAM roles and AWS services.

## Prerequisites and limitations
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ A new or existing S3 bucket for the `RolesPipeline` pipeline. Make sure that the access credentials you’re using have permissions to upload objects to this bucket.
+ AWS Command Line Interface (AWS CLI), installed and configured. For more information about this, see [Installing, updating, and uninstalling the AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS CLI documentation.
+ AWS Serverless Application Model (AWS SAM) CLI, installed and configured. For more information about this, see [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) in the AWS SAM documentation.
+ Python 3, installed on your local machine. For more information about this, see the [Python documentation](https://www.python.org/).
+ A Git client, installed and configured.
+ The GitHub `IAM roles pipeline` repository, cloned to your local machine.
+ Existing JSON-formatted IAM policies and roles. For more information about this, see the [ReadMe](https://github.com/aws-samples/iam-roles-pipeline/blob/main/README.md) file in the Github `IAM roles pipeline` repository.
+ Your developer team must not have permissions to edit this solution’s AWS CodePipeline, CodeBuild, and CodeDeploy resources.

**Limitations **
+ This pattern’s workflow is a proof of concept (POC) and we recommend that you only use it in a test environment. If you want to use this pattern’s approach in a production environment, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation and make the required changes to your IAM roles and AWS services.

## Architecture
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros-architecture"></a>

The following diagram shows you how to automatically validate and deploy IAM roles and policies to an account by using CodePipeline, IAM Access Analyzer, and AWS CloudFormation macros.

![Steps for validating and deploying IAM policies and roles in an AWS account.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/df1add4d-f211-43e3-8976-5314da75f627/images/832bebaf-27a0-4949-9c30-99fc4c9982b8.png)

The diagram shows the following workflow:

1. A developer writes JSON files that contain the definitions for the IAM policies and roles. The developer pushes the code to a CodeCommit repository and CodePipeline then initiates the `RolesPipeline` pipeline.

1. CodeBuild validates the JSON files by using IAM Access Analyzer. If there are any security or error-related findings, the deployment process is stopped.

1. If there are no security or error-related findings, the JSON files are sent to the `RolesBucket` S3 bucket.

1. An AWS CloudFormation macro implemented as an AWS Lambda function then reads the JSON files from the `RolesBucket` bucket and transforms them into AWS CloudFormation IAM resources types.

1. A predefined AWS CloudFormation stack installs, updates, or deletes the IAM policies and roles in the account.

**Automation and scale**

AWS CloudFormation templates that automatically deploy this pattern are provided in the GitHub [IAM roles pipeline](https://github.com/aws-samples/iam-roles-pipeline) repository.

## Tools
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) helps you identify the resources in your organization and accounts, such as S3 buckets or IAM roles, that are shared with an external entity. This helps you to identify unintended access to your resources and data.
+ [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) is an open-source framework that helps you build serverless applications in the AWS Cloud.

**Code **

The source code and templates for this pattern are available in the GitHub [IAM roles pipeline](https://github.com/aws-samples/iam-roles-pipeline) repository.

## Epics
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros-epics"></a>

### Clone the repository
<a name="clone-the-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Clone the sample repository. | Clone the GitHub [IAM roles pipeline](https://github.com/aws-samples/iam-roles-pipeline) repository to your local machine. | App developer, General AWS |

### Deploy the RolesPipeline pipeline
<a name="deploy-the-rolespipeline-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the pipeline. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros.html) | App developer, General AWS |
| Clone the pipeline’s repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros.html) | App developer, General AWS |

### Test the RolesPipeline pipeline
<a name="test-the-rolespipeline-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the RolesPipeline pipeline with valid IAM policies and roles. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros.html) | App developer, General AWS |
| Test the RolesPipeline pipeline with invalid IAM policies and roles. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros.html) | App developer, General AWS |

### Clean up your resources
<a name="clean-up-your-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare for cleanup. | Empty the S3 buckets and then run the `destroy` command. | App developer, General AWS |
| Delete the RolesStack stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros.html) | App developer, General AWS |
| Delete the RolesPipeline stack. | To delete the `RolesPipeline` AWS CloudFormation stack, follow the instructions from the [ReadMe](https://github.com/aws-samples/iam-roles-pipeline/blob/main/README.md) file in the Github `IAM roles pipeline` repository. | App developer, General AWS |

## Related resources
<a name="automatically-validate-and-deploy-iam-policies-and-roles-in-an-aws-account-by-using-codepipeline-iam-access-analyzer-and-aws-cloudformation-macros-resources"></a>
+ [IAM Access Analyzer - Policy validation](https://aws.amazon.com/blogs/aws/iam-access-analyzer-update-policy-validation/) (AWS News Blog)
+ [Using AWS CloudFormation macros to perform custom processing on templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) (AWS CloudFormation documentation)
+ [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) (AWS Lambda documentation)
