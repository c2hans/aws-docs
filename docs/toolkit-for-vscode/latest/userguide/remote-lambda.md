---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/remote-lambda.html
---

# Working with AWS Lambda Functions
<a name="remote-lambda"></a>

The AWS Toolkit for Visual Studio Code allows you to work with your AWS Lambda functions in your local VS Code environment. With the AWS Toolkit, you can create, edit, test, debug, and deploy your Lambda functions, without having to leave the IDE. For detailed information about the AWS Lambda service, see the [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) Developer Guide.

The following sections describe how to get started working with Lambda functions in the AWS Toolkit for Visual Studio Code.

**Note**
If you have already created Lambda functions by using the AWS Management Console, then you can invoke them from the Toolkit. Additionally, you can open your Lambda functions into VS Code from the AWS Lambda console, for additional information, see the [AWS Lambda console to IDE](lambda-console-ide.md) topic in this user guide. To create a new Lambda function in VS Code, follow the steps outlined in the [Creating a new serverless application (local)](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/sam-get-started.html#serverless-apps-create) topic in this user guide.

## Prerequisites
<a name="remote-lambda-prereq"></a>

The following conditions must be met to work with the AWS Lambda service in the AWS Toolkit.
+ The latest version of the AWS Toolkit for Visual Studio Code is installed and set up with your AWS credentials.
+ Your AWS Identity and Access Management (IAM) managed permissions and policies are configured to work with the AWS Lambda service. For detailed information on how to configure your permissions and create a compatible AWS managed policy, see the [AWS Identity and Access Management for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-iam.html) topic in the *AWS Lambda Developer Guide*.
+ You have existing AWS Lambda functions or are familiar with how to create one. For instructions on how to create a Lambda function, see the [Create your first Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) topic in the *AWS Lambda Developer Guide*.

## Invoking a Lambda Function
<a name="invoke-lam-func"></a>

To invoke a Lambda function from your AWS account into VS Code, complete the following steps.

1. From the AWS Toolkit for Visual Studio Code, expand the AWS explorer.

1. From the AWS explorer, expand **Lambda** to view your Lambda resources.

1. Open the context menu for (right-click) the Lambda function your want to invoke, then choose **Invoke in the cloud** or choose the **Invoke in the cloud** icon to open the **Remote invoke configuration** menu in VS Code.

1. From the **Remote invoke configuration** menu, specify your **Payload** settings and add any additional information that is required for the event.
**Note**
The first invoke process may start running as soon as you choose **Invoke in the cloud** in the AWS explorer. The output is displayed in the **OUTPUT** tab of the VS Code terminal.

1. Choose the **Remote Invoke** button to invoke your function, The output is displayed in the **OUTPUT** tab of the VS Code terminal.

## Deleting a Lambda function
<a name="delete-lambda"></a>

To delete a Lambda function, complete the following procedure.

**Warning**
Do not use this procedure to delete Lambda functions that are associated with [CloudFormation](https://docs.aws.amazon.com/cloudformation/). These functions must be deleted through your CloudFormation stack.

1. From the AWS Toolkit for Visual Studio Code, expand the AWS explorer.

1. From the AWS explorer, expand **Lambda** to view your Lambda resources.

1. Right-click the Lambda function your want to delete, then choose **Delete**.

1. When prompted, confirm that you want to delete your function.

After the function is deleted, it's no longer listed in the AWS explorer.

## Downloading a Lambda function
<a name="import-lambda"></a>

You can download code from a remote Lambda function into your VS Code workspace for editing and debugging.

**Note**
To download your Lambda function, you must be working in a VS Code workspace with an accessible folder and the AWS Toolkit only supports this feature with Lambda functions using Node.js and Python runtimes.

1. From the AWS Toolkit for Visual Studio Code, expand the AWS explorer.

1. From the AWS explorer, expand **Lambda** to view your Lambda resources.

1. Right-click the Lambda function your want to download, then choose **Download**.

1. Your Lambda function opens in the VS Code editor and displays in the AWS explorer when the download is complete. The AWS Toolkit also creates a *launch configuration* in the VS Code run panel allowing you to run and debug the Lambda function locally with AWS Serverless Application Model. For more information about using AWS SAM, see [Running and debugging a serverless application from template (local)](sam-get-started.md#serverless-apps-debug).

## Deploying updates for new Lambda functions
<a name="deploy-lambda"></a>

You can deploy updates to new Lambda functions from an unspecified, temporary location on your local machine.

**Note**
When there are un-deployed changes to your lambda files, you're notified by the **M** icon located next to the modified files in the VS Code editor and in the AWS explorer.

**Deploying from the VS Code editor**

1. Open a file from your Lambda function in the VS Code editor, then make a change to the file.

1. Manually save from the VS Code main menu or pressing **option\+s** (Mac) **ctrl\+s** (Windows).

1. VS Code automatically prompts you about deploying your changes to the cloud, choose the **Deploy** button to confirm the deployment.

1. VS Code updates you on the status of your deployment and notifies you when the process is complete.

**Deploying from the AWS Explorer**

1. Open a file from your Lambda function in the VS Code editor, then make a change to the file.

1. From the AWS Toolkit, expand the AWS explorer.

1. From the AWS explorer, expand the AWS region with the Lambda function that you want to deploy changes for.

1. From the AWS region, expand Lambda and navigate the function that you want to deploy changes for.

1. From the quick menu next to your function, choose the **Save and deploy your code** icon.

1. VS Code updates you on the status of your deployment and notifies you when the process is complete.

## Uploading updates for existing Lambda functions
<a name="upload-lambda"></a>

The following procedures describe how to upload local changes made to your existing Lambda functions. This feature supports uploads with any Lambda supported runtime.

**Warning**
Before uploading your lambda function, be aware of the following:
Updating code in this way doesn't use the AWS SAM CLI for deployment or create an CloudFormation stack
The AWS Toolkit doesn't validate code. Validate your code and test your function(s) before uploading any changes to the cloud.

**Uploading a Zip Archive**

1. From the AWS Toolkit for Visual Studio Code, expand the AWS explorer.

1. From the AWS explorer, expand **Lambda** to view your Lambda resources.

1. Right-click the Lambda function your want to upload your changes to, then choose **Upload Lambda...** to open the **Select Upload Type** menu.

1. Choose **ZIP Archive** to locate the `ZIP Archive` in your local directory.

1. When prompted, confirm the upload to start the upload of the selected `ZIP Archive`.

1. The status of your upload is displayed in VS Code and you're notified when the upload process is complete.

**Uploading a directory without building**

1. From the AWS Toolkit for Visual Studio Code, expand the AWS explorer.

1. From the AWS explorer, expand **Lambda** to view your Lambda resources.

1. Right-click the Lambda function your want to upload your changes to, then choose **Upload Lambda...** to open the **Select Upload Type** menu.

1. Choose **Directory** to proceed to the **Build directory** screen.

1. From the **Build directory** screen, choose **No** to choose a local directory for upload.

1. When prompted, confirm the upload to upload the selected directory.

1. The status of your upload is displayed in VS Code and you're notified when the upload process is complete.

**Uploading a directory with a build**
**Note**
Be aware of the following:
This procedure requires the AWS Serverless Application Model CLI.
The AWS Toolkit notifies you a matching handler can't be detected prior to upload.
To change the handler attached to your Lambda function, use the AWS Lambda console or the AWS Command Line Interface.

1. From the AWS Toolkit for Visual Studio Code, expand the AWS explorer.

1. From the AWS explorer, expand **Lambda** to view your Lambda resources.

1. Right-click the Lambda function your want to upload your changes to, then choose **Upload Lambda...** to open the **Select Upload Type** menu.

1. Choose **Directory** to proceed to the **Build directory** screen.

1. From the **Build directory** screen, choose **Yes**, then select a local directory for upload.

1. When prompted, confirm the upload to start building and uploading the selected directory.

1. The status of your upload is displayed in VS Code and you're notified when the upload process is complete.

## Converting your Lambda function to an AWS SAM project
<a name="lambda-sam"></a>

To convert your Lambda function into an AWS SAM stack, complete the following steps.

**Warning**
Currently, only a subset of resources are supported when converting a Lambda function to an AWS SAM project. To locate any missing resources after a conversion, check the Lambda console and add them manually to your AWS SAM template. For additional details about supported and unsupported resources, see the [Resource type support](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) topic in the *AWS CloudFormation Developer Guide*.

1. From the AWS Toolkit, expand the AWS explorer.

1. From the AWS explorer, expand the AWS region with the Lambda function that you want to convert into an AWS SAM project.

1. From the AWS region, expand Lambda and navigate the function that you want to convert into an AWS SAM stack.

1. From the quick menu next to your Lambda function, choose the **Convert to SAM Application** icon to browse your local file system and specify a location for your new AWS SAM project.

1. After specifying a location the AWS Toolkit begins converting your Lambda function into an AWS SAM project, VS Code provides updates on the status of the process.
**Note**
This process may take a few minutes.

1. When prompted by VS Code, enter a stack name, then press the **Enter** key to continue.

1. VS Code continues to update you with the status of your project, then notifies your when the process is complete and opens your new AWS SAM project as a VS Code workspace.
