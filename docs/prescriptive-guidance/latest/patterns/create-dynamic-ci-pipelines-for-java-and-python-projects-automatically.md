---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-dynamic-ci-pipelines-for-java-and-python-projects-automatically.html
---

# Create dynamic CI pipelines for Java and Python projects automatically

*Aromal Raj Jayarajan, Vijesh Vijayakumaran Nair, MAHESH RAGHUNANDANAN, and Amarnath Reddy, Amazon Web Services*

## Summary
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-summary"></a>

This pattern shows how to create dynamic continuous integration (CI) pipelines for Java and Python projects automatically by using AWS developer tools.

As technology stacks diversify and development activities increase, it can become difficult to create and maintain CI pipelines that are consistent across an organization. By automating the process in [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), you can help keep your CI pipelines consistent across projects.

To automate the creation of dynamic CI pipelines, this pattern uses the following variable inputs:
+ Programming language (Java or Python only)
+ Pipeline name
+ Required pipeline stages

**Note**
Step Functions orchestrates pipeline creation by using multiple AWS services. For more information about the AWS services used in this solution, see the **Tools** section of this pattern.

## Prerequisites and limitations
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket in the same AWS Region where you deploy this solution, with public access blocked
+ An [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/) [principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) that has the AWS CloudFormation permissions required to create the resources needed for this solution, including IAM roles, a customer managed [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/) key, and the Step Functions state machine
+ Access to AWS CodeCommit in your AWS account

**Limitations**
+ This pattern supports Java and Python projects only. The generated pipelines build and test the sample projects with Java 17 (Amazon Corretto) and Python 3.12.
+ The IAM roles provisioned in this pattern are designed to follow the principle of least privilege for the CI pipelines that the solution creates. Update the roles’ permissions based on the specific resources that your CI pipeline needs to create.
+ Deploy one copy of the solution in each AWS account and Region. The IAM roles and policies that the solution creates have fixed names, and the state machine’s permissions are limited to those names.
+ The generated pipelines run only the CI stages that you select. They don’t deploy anything.

## Architecture
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-architecture"></a>

**Target technology stack**
+ AWS CloudFormation
+ AWS CodeBuild
+ AWS CodeCommit
+ AWS CodePipeline
+ AWS IAM
+ AWS Key Management Service (AWS KMS)
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Systems Manager
+ AWS Step Functions
+ AWS Lambda
+ Amazon DynamoDB
+ Amazon CloudWatch Logs

**Target architecture**

The following diagram shows an example workflow for creating dynamic CI pipelines for Java and Python projects automatically by using AWS developer tools.

![Workflow to create dynamic CI pipelines for Java and Python projects automatically using AWS tools.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bef2ccb8-68b3-4c0f-9ee7-4b93e9422d9c/images/b5ed003f-cf16-4130-8bfb-2bc2cb9a0d33.png)

The diagram shows the following workflow:

1. An AWS user provides the input parameters for CI pipeline creation in JSON format. This input starts a Step Functions workflow (*state machine*) that creates a CI pipeline by using AWS developer tools.

1. A Lambda function validates the input, reads a folder named **input-references** from an Amazon S3 bucket, and generates a **buildspec.yml** file that defines the CI pipeline stages. The function stores the **buildspec.yml** file and a zip file in the **generated-artifacts** folder of the same Amazon S3 bucket. The zip file contains the sample source code and the **buildspec.yml** file.

1. Step Functions checks the CI pipeline creation workflow’s dependencies for any changes, and updates the dependencies stack as needed.

1. Step Functions creates the CI pipeline resources in a CloudFormation stack, including a CodeCommit repository, CodeBuild project, and a CodePipeline pipeline.

1. The CloudFormation stack creates a CodeCommit repository from the zip file, which contains the sample source code for the selected technology stack (Java or Python) and the **buildspec.yml** file.

1. An Amazon DynamoDB table, encrypted with an AWS KMS customer managed key, stores CI pipeline runtime details and the status of each request. If an input isn’t valid or a stack fails, the workflow records the failure in the table and stops.

**Automation and scale**
+ This pattern supports a single development environment only. To use it across multiple development environments, you must change the configuration.
+ To add support for more than one CloudFormation stack, you can create additional CloudFormation templates. For more information, see [Getting started with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html) in the CloudFormation documentation.

## Tools
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-tools"></a>

**Tools**
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides secure, hierarchical storage for configuration data management and secrets management.

**Code**

The code for this pattern is available in the GitHub [automated-ci-pipeline-creation](https://github.com/aws-samples/automated-ci-pipeline-creation) repository. The repository contains the AWS CloudFormation templates required to create the target architecture outlined in this pattern.

[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so that you can monitor them and archive them securely.

## Best practices
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-best-practices"></a>
+ Don't enter credentials (*secrets*) such as tokens or passwords directly into AWS CloudFormation templates or Step Functions action configurations. If you do, the information appears in the Step Functions execution history and diagnostic logs. Instead, use AWS Secrets Manager to set up and store secrets. Then, reference the secrets stored in Secrets Manager within the CloudFormation templates and Step Functions action configurations as needed. For more information, see [What is AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the Secrets Manager documentation.
+ Configure server-side encryption for CodePipeline artifacts stored in Amazon S3. For more information, see [Configure server-side encryption for artifacts stored in Amazon S3 for CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/S3-artifact-encryption.html) in the CodePipeline documentation.
+ Apply least-privilege permissions when configuring IAM roles. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the IAM documentation.
+ Make sure that your Amazon S3 bucket is not publicly accessible. For more information, see [Configuring block public access setting for your S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html) in the Amazon S3 documentation.
+ Make sure that you activate versioning for your Amazon S3 bucket. For more information, see [Using versioning in S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) in the Amazon S3 documentation.
+ Use IAM Access Analyzer when configuring IAM policies. The tool provides actionable recommendations to help you author secure and functional IAM policies. For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) in the IAM documentation.
+ When possible, define specific access conditions when configuring IAM policies.
+ Activate Amazon CloudWatch logging for monitoring and auditing purposes. For more information, see [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) in the CloudWatch documentation.
+ Restrict write access to the Amazon S3 bucket that holds the templates and the buildspec fragments. Anyone who can change the fragments changes what the generated pipelines run.
+ Don’t add secrets to the buildspec fragments. Use AWS Secrets Manager instead.

## Epics
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-epics"></a>

### Configure the prerequisites
<a name="configure-the-prerequisites"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon S3 bucket. | Create an Amazon S3 bucket (or use an existing bucket) to store the required AWS CloudFormation templates, source code, and input files for the solution.<br />Block all public access to the bucket, and turn on default encryption and versioning.<br />For more information, see [Step 1: Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) in the Amazon S3 documentation.The Amazon S3 bucket must be in the same AWS Region where you deploy the solution. | AWS DevOps |
| Clone the GitHub repository. | Clone the GitHub [automated-ci-pipeline-creation](https://github.com/aws-samples/automated-ci-pipeline-creation) repository by running the following command in a terminal window:<pre>git clone https://github.com/aws-samples/automated-ci-pipeline-creation.git</pre><br />For more information, see [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) in the GitHub documentation. | AWS DevOps |
| Upload the Solution Templates folder from the cloned GitHub repository to your Amazon S3 bucket.  | Copy the contents from the cloned **Solution-Templates** folder and upload them into the Amazon S3 bucket that you created.<br />For more information, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation.Make sure that you upload the contents of the **Solution-Templates** folder only. You can upload the files at the Amazon S3 bucket’s root level only. | AWS DevOps |

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFormation stack to deploy the solution by using the template.yml file in the cloned GitHub repository. | 1. Sign in to the AWS Management Console and then open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. Choose **Create stack**. A dropdown list appears.<br />3. In the dropdown list, select **With new resources (standard)**. The **Create stack** page opens.<br />4. In the **Specify template** section, select the checkbox next to **Upload a template file**.<br />5. Select **Choose file**. Then, navigate to the cloned GitHub repository’s root folder and select the **template.yml** file. Then, choose **Open**.<br />6. Choose **Next**. The **Specify stack details** page opens.<br />7. In the **Parameters** section, specify the following parameters:For **S3TemplateBucketName**, enter the name of the Amazon S3 bucket that you created earlier, which contains the source code and references for this solution. Make sure that the bucket name parameter is in lowercase.For **DynamoDBTable**, enter a name for the DynamoDB table that the CloudFormation stack creates.For **StateMachineName**, enter a name for the Step Functions state machine that the CloudFormation stack creates.<br />8. Choose **Next**. The **Configure stack options** page opens.<br />9. On the **Configure stack options** page, choose **Next**. Don’t change any of the default values. The **Review** page opens.<br />10. Review the stack creation settings. Select the checkbox to acknowledge that CloudFormation might create IAM resources, and then choose **Create stack** (or **Submit**) to launch your stack.While CloudFormation creates your stack, the stack appears on the **Stacks** page with a status of **CREATE\_IN\_PROGRESS**. Wait for the stack’s status to change to **CREATE\_COMPLETE** before you complete the remaining steps in this pattern. | AWS administrator, AWS DevOps |

### Test the setup
<a name="test-the-setup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the AWS Step Functions state machine that you created. | 1. Sign in to the AWS Management Console and then open the [Step Functions console](https://console.aws.amazon.com/states/).<br />2. Open the state machine that you created.<br />3. Choose **Start execution**. Then, enter your input values for the workflow in JSON format (see the following example inputs).<br />4. Choose **Start execution**.**JSON formatting**<pre>{<br />  "details": {<br />    "tech_stack": "Name of the Tech Stack (python/java)",<br />    "project_name": "Name of the Project that you want to create with",<br />    "pre_build": "Choose the step if it required in the buildspec.yml file i.e., yes/no",<br />    "build": "Choose the step if it required in the buildspec.yml file i.e., yes/no",<br />    "post_build": "Choose the step if it required in the buildspec.yml file i.e., yes/no",<br />    "reports": "Choose the step if it required in the buildspec.yml file i.e., yes/no"<br />  }<br />}</pre>`tech_stack` must be `java` or `python`. `project_name` must have 1 to 40 letters, numbers, or hyphens. `pre_build`, `build`, `post_build`, and `reports` must be `yes` or `no`. The `reports` setting only applies when `build` is `yes`. If an input isn’t valid or a stack fails, the execution fails and the status in the DynamoDB table is "Pipeline creation failed".<br />**Java JSON input example**<pre>{<br />  "details": {<br />    "tech_stack": "java",<br />    "project_name": "pipeline-java-pjt",<br />    "pre_build": "yes",<br />    "build": "yes",<br />    "post_build": "yes",<br />    "reports": "yes"<br />  }<br />}</pre><br />**Python JSON input example**<pre>{<br />  "details": {<br />    "tech_stack": "python",<br />    "project_name": "pipeline-python-pjt",<br />    "pre_build": "yes",<br />    "build": "yes",<br />    "post_build": "yes",<br />    "reports": "yes"<br />  }<br />}</pre> | AWS administrator, AWS DevOps |
| Confirm that the AWS CodeCommit repository for the CI pipeline was created. | 1. Sign in to the AWS Management Console and then open the [CodeCommit console](https://console.aws.amazon.com/codesuite/codecommit/home).<br />2. On the **Repositories** page, verify that the name of the CodeCommit repository that you created appears in the list of repositories. The repository name uses the format **<project\_name>-Repo** (for example, **pipeline-java-pjt-Repo**).<br />3. Open the CodeCommit repository and verify that the sample source code and the **buildspec.yml** file were pushed to the main branch. | AWS DevOps |
| Check the AWS CodeBuild project resources. | 1. Sign in to the AWS Management Console and then open the [CodeBuild console](https://console.aws.amazon.com/codesuite/codebuild/home).<br />2. On the **Build projects** page, verify that the name of the CodeBuild project that you created appears in the list of projects. The project name uses the format **<project\_name>-Build** (for example, **pipeline-java-pjt-Build**).<br />3. Select the name of your CodeBuild project to open the project. Then, review and validate the following configurations:**Project Configuration****Source****Environment****Buildspec****Batch Configuration****Artifacts** | AWS DevOps |
| Validate the CodePipeline stages. | 1. Sign in to the AWS Management Console and then open the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home).<br />2. On the **Pipelines** page, verify that the name of the pipeline that you created appears in the list of pipelines. The pipeline name uses the format **<project\_name>-Pipeline** (for example, **pipeline-java-pjt-Pipeline**).<br />3. Select the name of your pipeline to open the pipeline. Then, review and validate each stage of the pipeline. The pipeline has two stages: **CodeCheckout** and **Build**. | AWS DevOps |
| Confirm that the CI pipeline ran successfully. | 1. In the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home), on the **Pipelines** page, select the name of your pipeline to view the pipeline’s status.<br />2. Verify that each stage of the pipeline has a **Succeeded** status. | AWS DevOps |

### Clean up your resources
<a name="clean-up-your-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the CI pipeline stack. | 1. Sign in to the AWS Management Console and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. Delete the stack named **<project\_name>-Stack** for each project that you created.<br />3. In the CodeBuild console, delete the report groups that CodeBuild created for each project. In the CloudWatch console, delete the log group for each project (`/aws/codebuild/<project_name>-Build`) and the Lambda log group (`/aws/lambda/<stack name>-AWSLambdaFunction-...`). Lambda creates the Lambda log group automatically, and the stack doesn’t delete it. | AWS DevOps |
| Delete the CI pipeline’s dependencies. | 1. Empty the Amazon S3 buckets whose names start with **deployment-artifact-bucket** and **deployment-artifact-bucket-logs**. Because versioning is turned on, delete all object versions. For more information, see [Emptying a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html) in the Amazon S3 documentation.<br />2. Delete the stack named **pipeline-creation-dependencies-stack**. If the deletion fails because the log bucket received new objects, empty the bucket again and retry the deletion. | AWS DevOps |
| Delete the solution stack and the template bucket. | 1. Delete the stack that you created from the **template.yml** file. The AWS KMS key that the stack created goes into a pending deletion period and is deleted automatically.<br />2. Delete the Amazon S3 bucket that you created in the **Configure the prerequisites** section of this pattern. For more information, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon S3 documentation. | AWS DevOps |

## Related resources
<a name="create-dynamic-ci-pipelines-for-java-and-python-projects-automatically-resources"></a>
+ [Creating a Step Functions state machine that uses Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-lambda-state-machine.html) (AWS Step Functions documentation)
+ [AWS Step Functions Workflow Studio](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio.html) (AWS Step Functions documentation)
+ [DevOps and AWS](https://aws.amazon.com/devops/)
+ [How does AWS CloudFormation work?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html) (AWS CloudFormation documentation)
+ [Complete CI/CD with AWS CodeCommit, AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/) (AWS blog post)
+ [IAM and AWS STS quotas, name requirements, and character limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) (IAM documentation)
+ [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (AWS CodeBuild User Guide)
+ [Using CloudWatch Logs to log execution history in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html) (AWS Step Functions Developer Guide)
