---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-console-ide.html
---

# AWS Lambda console to IDE
<a name="lambda-console-ide"></a>

The AWS Lambda console to IDE feature allows you to download your AWS Lambda functions from the AWS Lambda console into VS Code. Working with your Lambda functions in VS Code gives you access to other local-development options such as AWS Serverless Application Model (AWS SAM) and the AWS Cloud Development Kit (AWS CDK).

For more information about AWS Lambda, see the [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) Developer Guide. To get started working with your Lambda function in the AWS Toolkit, see the [Working with AWS Lambda Functions](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/remote-lambda.html) topic in this user guide. The following sections describe how to move your work flow from the Lambda console to VS Code. For detailed information about moving your Lambda functions from the Lambda console to VS Code, including how to get started working with the Lambda console, see the [Developing Lambda functions locally with VS Code](https://docs.aws.amazon.com/lambda/latest/dg/foundation-iac-local-development.html) topic in the *AWS Lambda Developer Guide*.

## Moving from console to local development
<a name="w2aac17c43c13b7"></a>

To open a Lambda function from the Lambda console in VS Code, complete the following steps:

1. From your web browser, open the [Lambda console](https://console.aws.amazon.com/lambda).

1. From Lambda console, choose the function you want to open in VS Code.

1. From the function view, navigate to the **Code source** tab.

1. From the **Code source** tab, choose **Open in VS Code**.

## Working with your Lambda function in VS Code
<a name="w2aac17c43c13b9"></a>

When your Lambda function opens in VS Code via the Lambda console:
+ VS Code automatically launches on your local machine.
+ Your Lambda function opens as a VS Code workspace.
+ Your Lambda `handler file` opens in the VS Code editor.
**Note**
If there is not a properly configured `handler file` in the workspace, no file opens in the VS Code editor.

Opening your Lambda function in VS Code via the Lambda console allows you to access all of the existing AWS Toolkit Lambda features, including the ability to edit function code with full language support, local testing, remote debugging, deployment support, and dependency management. For more information about Lambda features supported in the AWS Toolkit, see the [AWS Lambda](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/building-lambda.html) service table of contents in this user guide.
