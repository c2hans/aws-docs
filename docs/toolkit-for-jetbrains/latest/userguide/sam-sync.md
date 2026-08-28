---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/sam-sync.html
---

# Syncing AWS SAM applications from the AWS Toolkit for JetBrains
<a name="sam-sync"></a>

AWS Serverless Application Model (AWS SAM) `sam sync` is an AWS SAM-CLI-command deployment process that automatically identifies changes made to your serverless applications, then chooses the best way to build and deploy those changes to the AWS Cloud. If you've only made changes to your application code without changing the infrastructure, AWS SAM Sync updates your application without redeploying your CloudFormation stack.

For additional information about `sam sync` and AWS SAM CLI commands, see the [AWS SAM CLI command reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html) topic in the *AWS Serverless Application Model User Guide*.

The following sections describe how to get started working with AWS SAM Sync.

## Prerequisites
<a name="w2aac17c37c11b9"></a>

Prior to working with AWS SAM Sync, the following prerequisites must be met:
+ You have a working AWS SAM application. For more information on creating a AWS SAM application, see the [Working with AWS SAM](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/key-tasks.html#key-tasks-sam-create) topic in this User Guide.
+ You've installed version 1.78.0. (or later) of the AWS SAM CLI. For more information on installing the AWS SAM CLI, see the [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) topic in the *AWS Serverless Application Model User Guide*.
+ Your application is running in a development environment.

**Note**
To sync and deploy a serverless application that contains an AWS Lambda function with any non-default properties, the optional properties must be set in the AWS SAM template file associated with the AWS Lambda function, prior to deployment.
To learn more about AWS Lambda properties, see the [AWS::Serverless::Function](https://github.com/aws/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction) section in the *AWS Serverless Application Model User Guide* on GitHub.

## Getting Started
<a name="w2aac17c37c11c11"></a>

To get started working with AWS SAM Sync, complete the following procedure.

**Note**
Make sure that you're AWS Region is set to the location associated with your serverless application.
To learn more about changing your AWS region from the AWS Toolkit for JetBrains, see the [Switch between AWS Regions](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/key-tasks.html#key-tasks-switch-region) topic in this User Guide.

1. From your serverless application project in the **Project** tool window, open the context menu for (right-click) your `template.yaml` file.

1. From the `template.yaml` context menu, choose **Sync Serverless Application (formerly Deploy)** to open the **Confirm development stack** dialog.

1. Confirm that you are working from a development stack to open the **Sync Serverless Application** dialog.
![Confirm development stack dialog](http://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/images/sam-sync-dev-stack.png)

1. Complete the steps in the **Sync Serverless Application** dialog, then choose **Sync** to begin the AWS SAM Sync process. To learn more about the **Sync Serverless Application** dialog, see the [Sync Serverless Application Dialog](#sam-sync-serverless-app-dialog) section located below.

1. During the sync process, the AWS Toolkit for JetBrains **Run Window** is updated with the deployment status.

1. Following a successful sync, the name of your CloudFormation stack is added to the **AWS Explorer**.

   If the sync fails, troubleshooting details can be found in the JetBrains **Run Window** or the CloudFormation **event logs**. To learn more about viewing CloudFormation event logs, see the [Viewing event logs for a stack](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/key-tasks.html#key-tasks-cloudformation-logs) topic in this User Guide.

## Sync Serverless Application Dialog
<a name="sam-sync-serverless-app-dialog"></a>

The **Sync serverless application dialog** assists you with the AWS SAM sync process. The following sections are descriptions and details for each of the different dialog components.

### Create Stack or Update Stack
<a name="w2aac17c37c11c13b5"></a>

**Required:** To create a new deployment stack, enter a name in the provided field to create and set the CloudFormation stack for your serverless application deployment.

Alternatively, to deploy to an existing CloudFormation stack, select the stack name from the auto-populated list of stacks associated with your AWS account.

### Template Parameters
<a name="w2aac17c37c11c13b7"></a>

**Optional:** Populates with a list of parameters detected from your project `template.yaml` file. To specify parameter values, enter a new parameter value into the provided text-field located in the **value** column.

### S3 Bucket
<a name="w2aac17c37c11c13b9"></a>

**Required:** To choose an existing Amazon Simple Storage Service (Amazon S3) bucket for storing your CloudFormation template, select it from the list.

To create and use new Amazon S3 bucket for storage, choose **Create** and follow the prompts.

### ECR Repository
<a name="w2aac17c37c11c13c11"></a>

**Required, only visible when working with an Image package type:** Choose an existing Amazon Elastic Container Registry (Amazon ECR) repository URI for deployment of your serverless application.

For information about AWS Lambda package types, see the [Lambda deployment packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) section in the *AWS Lambda Developer Guide.*

### CloudFormation Capabilities
<a name="w2aac17c37c11c13c13"></a>

**Required:** Choose the capabilities that CloudFormation is allowed to use when creating stacks.

### Tags
<a name="w2aac17c37c11c13c15"></a>

**Optional:** Enter your preferred tags in the provided text fields to tag a parameter.

### Build Function Inside a Container
<a name="w2aac17c37c11c13c17"></a>

**Optional, Docker required:** Selecting this options builds your serverless-application functions inside of a local Docker container, prior to deployment. This option is useful if a function depends on packages with natively compiled dependencies or programs.

For more information, see the [Building applications](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html) topic in the *AWS Serverless Application Model Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
