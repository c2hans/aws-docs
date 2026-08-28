---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild.html
---

# Deploy code in multiple AWS Regions using AWS CodePipeline, AWS CodeCommit, and AWS CodeBuild
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild"></a>

*Anand Krishna Varanasi, Amazon Web Services*

## Summary
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-summary"></a>

This pattern demonstrates how to build infrastructure or architecture across multiple Amazon Web Services (AWS) Regions by using AWS CloudFormation. It includes continuous integration (CI)/continuous deployment (CD) across multiple AWS Regions for faster deployments.** **The steps in this pattern have been tested for the creation of an AWS CodePipeline job to deploy to three AWS Regions as an example. You can change the number of Regions based on your use case.

## Prerequisites and limitations
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+
  + A CodeBuild role with the *AmazonS3FullAccess* and *CloudWatchFullAccess* policies. These policies give CodeBuild access to watch events of AWS CodeCommit through Amazon CloudWatch and to use Amazon Simple Storage Service (Amazon S3) as an artifact store.
  + An AWS CloudFormation role with the following policies, which give AWS CloudFormation, in the final Build stage, the ability to create or update AWS Lambda functions, push or watch Amazon CloudWatch logs, and to create and update change sets.
    + *AWSLambdaFullAccess*
    + *AWSCodeDeployFullAccess*
    + *CloudWatchFullAccess*
    + *AWSCloudFormationFullAccess*
    + *AWSCodePipelineFullAccess*
**Note**
Two AWS Identity and Access Management (IAM) roles for AWS CodeBuild and AWS CloudFormation with proper policies for CodeBuild to perform the CI tasks of testing, bundling, packaging the artifacts, and deploying to multiple AWS Regions in parallel.  Cross-check the policies created by CodePipeline to verify that CodeBuild and AWS CloudFormation have proper permissions in the CI and CD phases.

## Architecture
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-architecture"></a>

![An AWS CodePipeline job that deploys to three AWS Regions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d44c393c-7243-4d4e-8b84-88a8503af98f/images/5c27fc35-5e62-4292-8b18-a7bc7faf2631.png)

This pattern's multiple-Region architecture and workflow comprise the following steps.

1. You send your code to a CodeCommit repository.

1. Upon receiving any code update or commit, CodeCommit invokes a CloudWatch event, which in turn starts a CodePipeline job.

1. CodePipeline engages the CI that is handled by CodeBuild. The following tasks are performed.
   + Testing of the AWS CloudFormation templates (optional)
   + Packaging of the AWS CloudFormation templates for each Region included in the deployment. For example, this pattern deploys in parallel to three AWS Regions, so CodeBuild packages the AWS CloudFormation templates into three S3 buckets, one in each specified Region. The S3 buckets are used by CodeBuild as artifact repositories only.

1. CodeBuild packages the artifacts as input for next Deploy phase, which runs in parallel in the three AWS Regions. If you specify a different number of Regions, CodePipeline will deploy to those Regions.

## Tools
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-tools"></a>

**Tools**
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) – CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software changes continuously.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) – CodeBuild is a fully managed build service that compiles your source code, runs unit tests, and produces artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) – CodeCommit is a version control service hosted by Amazon Web Services that you can use to privately store and manage assets (such as source code and binary files) in the cloud.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation is a service that helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS.
+ [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) – AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet. It is designed to make web-scale computing easier for developers.

**Code**

The following sample code is for the `BuildSpec.yaml` file (Build phase).

```
---
artifacts:
discard-paths: true
files:
- packaged-first-region.yaml
- packaged-second-region.yaml
- packaged-third-region.yaml
phases:
build:
commands:
- echo "********BUILD PHASE - CF PACKAGING**********"
- "aws cloudformation package --template-file sam-template.yaml --s3-bucket $S3_FIRST_REGION --output-template-file packaged-first-region.yaml --region $FIRST_REGION"
- "aws cloudformation package --template-file sam-template.yaml --s3-bucket $S3_SECOND_REGION --output-template-file packaged-second-region.yaml --region $SECOND_REGION"
- "aws cloudformation package --template-file sam-template-anand.yaml --s3-bucket $S3_THIRD_REGION --output-template-file packaged-third-region.yaml --region $THIRD_REGION"
install:
commands:
- echo "********BUILD PHASE - PYTHON SETUP**********"
runtime-versions:
python: 3.8
post_build:
commands:
- echo "********BUILD PHASE - PACKAGING COMPLETION**********"
pre_build:
commands:
- echo "********BUILD PHASE - DEPENDENCY SETUP**********"
- "npm install --silent --no-progress"
- echo "********BUILD PHASE - DEPENDENCY SETUP DONE**********"
version: 0.2
```

## Epics
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-epics"></a>

### Prepare the code and the CodeCommit repository
<a name="prepare-the-code-and-the-codecommit-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select the primary AWS Region for the deployment. | Sign in to your AWS account and choose the primary Region for the deployment. The CodeCommit repository will be in the primary Region. | DevOps |
| Create the CodeCommit repository. | Create the CodeCommit repository, and push the required code into it. The code generally includes the AWS CloudFormation or AWS SAM templates, Lambda code if any, and the CodeBuild `buildspec.yaml` files as input to the AWS CodePipeline. | DevOps |
| Push the code into the CodeCommit repository. | In the *Attachments* section, download the code for this example, and then push the required code into it. Generally, the code can include AWS CloudFormation or AWS SAM templates, Lambda code and the CodeBuild `buildspec.yaml` files as input to the pipeline. | DevOps |

### Source phase: Create the pipeline
<a name="source-phase-create-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CodePipeline job. | On the CodePipeline console, choose **Create pipeline**. | DevOps |
| Name the CodePipeline job and choose the service role setting. | Enter a name for the job, and keep the default service role setting so that CodePipeline creates the role with the necessary policies attached. | DevOps |
| Specify the location for the artifact store. | Under **Advanced settings**, keep the default option so that CodePipeline creates an S3 bucket to use for code artifact storage. If you use an existing S3 bucket instead, the bucket must be in the primary Region that you specified in the first epic. | DevOps |
| Specify the encryption key. | Keep the default option, **Default AWS Managed Key**, or choose to use your own AWS Key Management Service (AWS KMS) customer managed key. | DevOps |
| Specify the source provider. | Under **Source provider**, choose **AWS CodeCommit**. | DevOps |
| Specify the repository. | Choose the CodeCommit repository that you created in the first epic. If you placed the code in a branch, choose the branch. | DevOps |
| Specify how code changes are detected. | Keep the default, **Amazon CloudWatch Events**, as the change trigger for CodeCommit to start the CodePipeline job. | DevOps |

### Build phase: Configure the pipeline
<a name="build-phase-configure-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Specify the build provider. | For the build provider, choose **AWS CodeBuild**. | DevOps |
| Specify the AWS Region. | Choose the primary Region, which you specified in the first epic. | DevOps |

### Build phase: Create and configure the project
<a name="build-phase-create-and-configure-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the project | Choose **Create project**, and enter a name for the project. | DevOps |
| Specify the environment image. | For this pattern demonstration, use the default CodeBuild managed image. You also have the option to use a custom Docker image if you have one. | DevOps |
| Specify the operating system. | Choose either Amazon Linux 2 or Ubuntu.Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/). | DevOps |
| Specify the service role. | Choose the role you created for CodeBuild before you started to create the CodePipeline job. (See the *Prerequisites* section.) | DevOps |
| Set additional options. | For **Timeout** and **Queued timeout**, keep the default values. For certificate, keep the default setting unless you have a custom certificate that you want to use. | DevOps |
| Create the environment variables. | For each AWS Region that you want to deploy to, create environment variables by providing the S3 bucket name and the Region name (for example, us-east-1). | DevOps |
| Provide the buildspec file name, if it is not buildspec.yml. | Keep this field blank if the file name is the default, `buildspec.yaml`. If you renamed the buildspec file, enter the name here. Make sure it matches the name of the file that is in the CodeCommit repository. | DevOps |
| Specify logging. | To see logs for Amazon CloudWatch Events, keep the default setting. Or you can define any specific group or logger names. | DevOps |

### Skip the Deploy phase
<a name="skip-the-deploy-phase"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Skip the deploy phase and complete the creation of the pipeline. | When you set up the pipeline, CodePipeline allows you to create only one stage in the Deploy phase. To deploy to multiple AWS Regions, skip this phase. After the pipeline is created, you can add multiple Deploy phase stages. | DevOps |

### Deploy phase: Configure the pipeline for deployment to the first Region
<a name="deploy-phase-configure-the-pipeline-for-deployment-to-the-first-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add a stage to the Deploy phase. | Edit the pipeline and choose **Add stage** in the Deploy phase. This first stage is for the primary Region. | DevOps |
| Provide an action name for the stage. | Enter a unique name that reflects the first (primary) stage and Region. For example, enter **primary\_<region>\_deploy**. | DevOps |
| Specify the action provider. | For **Action provider**, choose AWS CloudFormation. | DevOps |
| Configure the Region for the first stage. | Choose the first (primary) Region, the same Region where CodePipeline and CodeBuild are set up. This is the primary Region where you want to deploy the stack. | DevOps |
| Specify the input artifact. | Choose **BuildArtifact**. This is the output of the build phase. | DevOps |
| Specify the action to take. | For **Action mode**, choose **Create or update a stack**. | DevOps |
| Enter a name for the CloudFormation stack. |  | DevOps |
| Specify the template for the first Region. | Select the Region-specific package name that was packaged by CodeBuild and dumped into the S3 bucket for the first (primary) Region. | DevOps |
| Specify the capabilities. | Capabilities are required if the stack template includes IAM resources or if you create a stack directly from a template that contains macros. For this pattern, use CAPABILITY\_IAM, CAPABILITY\_NAMED\_IAM, CAPABILITY\_AUTO\_EXPAND. | DevOps |

### Deploy phase: Configure the pipeline for deployment to the second Region
<a name="deploy-phase-configure-the-pipeline-for-deployment-to-the-second-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the second stage to the Deploy phase. | To add a stage for the second Region, edit the pipeline and choose **Add stage** in the Deploy phase. Important: The process of creating the second Region is the same as that of the first Region, except for the following values. | DevOps |
| Provide an action name for the second stage. | Enter a unique name that reflects the second stage and the second Region. | DevOps |
| Configure the Region for the second stage. | Choose the second Region where you want to deploy the stack. | DevOps |
| Specify the template for the second Region. | Select the Region-specific package name that was packaged by CodeBuild and dumped into the S3 bucket for the second Region. | DevOps |

### Deploy phase: Configure the pipeline for deployment to the third Region
<a name="deploy-phase-configure-the-pipeline-for-deployment-to-the-third-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the third stage to the Deploy phase. | To add a stage for the third Region, edit the pipeline and choose **Add stage** in the Deploy phase. Important: The process of creating the second Region is the same as that of the previous two Regions, except for the following values. | DevOps |
| Provide an action name for the third stage. | Enter a unique name that reflects the third stage and the third Region. | DevOps |
| Configure the Region for the third stage. | Choose the third Region where you want to deploy the stack. | DevOps |
| Specify the template for the third Region. | Select the Region-specific package name that was packaged by CodeBuild and dumped into the S3 bucket for the third Region. | DevOps |

### Clean up the deployment
<a name="clean-up-the-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the AWS resources. | To clean up the deployment, delete the CloudFormation stacks in each Region. Then delete the CodeCommit, CodeBuild, and CodePipeline resources from the primary Region. | DevOps |

## Related resources
<a name="deploy-code-in-multiple-aws-regions-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-resources"></a>
+ [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation architecture structure reference for AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CloudFormation.html)

## Attachments
<a name="attachments-d44c393c-7243-4d4e-8b84-88a8503af98f"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/d44c393c-7243-4d4e-8b84-88a8503af98f/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
