---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/appbuilder-overview-overview.html
---

# Working with AWS Application Builder
<a name="appbuilder-overview-overview"></a>

 The following sections describe how to access AWS Application Builder in the AWS Toolkit for Visual Studio Code. With Application Builder, you can build projects visually, iterate on them locally, and deploy them to AWS. For an overview of features and potential use cases for Application Builder and your local AWS Lambda experience, see the AWS Developer YouTube video [\*New\* AWS Lambda Local IDE Experience\!](https://www.youtube.com/watch?v=rhBOuJqzABY).

## Working with the AWS Application Builder explorer
<a name="appbuilder-overview-explorer"></a>

To access Application Builder in the AWS Toolkit, open the AWS Toolkit in VS Code, then expand the **AWS Application Builder** explorer. The AWS Application Builder explorer contains a link to open the **Walkthrough of Application Builder** in a VS Code editor tab, and displays folders within your current VS Code workspace that contain AWS Application Builder related resources.

From the Application Builder explorer in the AWS Toolkit, there are 4 project-folder-level actions that are accessible from the button icons located next to your project folder or by opening the context menu for (right-clicking) the project folder:
+ **Open Template File**: Opens your template file in the VS Code explorer.
+ **Open with Infrastructure Composer**: Opens your template file with AWS Infrastructure Composer in the VS Code editor. For detailed information about working with AWS Infrastructure Composer, see the [What is AWS Infrastructure Composer](https://docs.aws.amazon.com/application-composer/latest/dg/what-is-composer.html) topic in the *AWS Infrastructure Composer* Developer Guide.
+ **Build SAM Template**: Opens the **Specify parameters for build** dialog in the AWS Toolkit. You can choose to **Specify build flags** for the build or **Use default values from samconfig**. For detailed information about AWS SAM templates, see the [Template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) topic in the *AWS Serverless Application Model* Developer Guide.
+ **Deploy SAM Application**: Opens the **Select deployment command** dialog in VS Code where your can choose to **Deploy** your application or **Sync**, to update an application you've already deployed. For detailed information on deploying AWS SAM applications see the [Deploy your application and resources](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying.html) topic in the *AWS Serverless Application Model* Developer Guide.

There are 2 actions that are accessible from the button icons located next to the AWS Lambda function in your project folder or by right-clicking the AWS Lambda function:
+ **Local Invoke and Debug Configuration**: Opens the **Local Invoke and Debug Configuration** form in your VS Code editor. With this form you can create, edit, and run launch-configs of type:`aws-sam`. For additional information about SAM Debug configurations, see the [Configuration options for debugging serverless applications](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/serverless-apps-run-debug-config-ref.html) topic in this User Guide.
**Note**
At present, debugging a .NET Core application on an ARM64 architecture is not supported by VS Code. If you attempt to debug a .NET Core application the following error is displayed:
`The vsdbg debugger does not currently support the arm64 architecture. Function will run locally without debug.`
For additional details about this issue, see this [VSCode-csharp](https://github.com/dotnet/vscode-csharp/issues/2771) issue in the DotNet GitHub repository.
+ **Open Function Handler**: Opens your project file that contains the function handler.

There are 2 additional actions available for deployed AWS Lambda functions.
+ **Remote invoke**: opens the **Remote invoke configuration** menu in the VS Code editor.
+ **Search logs**: Opens the **Search logs** dialog in VS Code.

## Walkthrough of Application Builder
<a name="appbuilder-overview-walkthrough"></a>

The **Walkthrough of Application Builder** is a step-by-step interactive guide that takes you through the process of building a new application with AWS Application Builder. You can access the **Walkthrough of Application Builder** from two places: the Application Builder explorer in the AWS Toolkit for Visual Studio Code and the VS Code **Welcome** tab. When you select **Walkthrough of Application Builder** from the Application Builder explorer in the AWS Toolkit, it opens the **Walkthrough of Application Builder** in the VS Code **Welcome** tab in the VS Code **Editor** window.

The **Walkthrough of Application Builder** is comprised of 5 main sections:

### 1. Installation
<a name="w2aac17c19b9b7b7"></a>

The Installation section checks to see if you have installed the AWS CLI tools required by Application Builder and other optional tools. If you don't have the required tools or your tools are out of date, you're guided through the process of installing the correct versions.

To see if you have the correct AWS CLI and optional tools installed, select the button for the AWS CLI or another tool that you want to test. After selecting a button, your **AWS Toolkit Logs** update and VS Code displays an alert message with the status of your tools. If you need to install or update your tools, the **Walkthrough of Application Builder** updates with the instructions and resources your need to proceed.

For detailed information on installing the AWS CLI, see the [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) topic in the *AWS CLI* Developer Guide. For detailed information on installing the AWS SAM CLI, see the [Install AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) topic in the *AWS SAM CLI* Developer Guide.

### 2. Choose your application template
<a name="w2aac17c19b9b7b9"></a>

The Choose your application template section guides you through the process of building a new application from a template.

To choose a template and initialize your application, complete the following steps.

1. From the **Walkthrough of Application Builder**, select the **Choose your application template** section to display a list of template options on your screen.

1. Choose a template from the list, then choose the **Initialize your project** button to open a VS Code dialog.

1. Complete the steps in the VS Code dialog to initialize your new application.

1. The AWS Toolkit logs update with the status of your application during the initialization process.

1. To view your application in the Application Builder explorer, choose the **Refresh Application Builder Explorer** icon to update the explorer with your changes.

### 3. Iterate locally
<a name="w2aac17c19b9b7c11"></a>

The Iterate locally section contains example images that demonstrate how you can iterate with the Application Builder features available in the VS Code and AWS Toolkit explorers.

For additional information about all of the Application Builder features available in the VS Code and AWS Toolkit explorers, see the *Working with the Application Builder explorer* section, located in this User Guide topic.

### 4. Deploy to AWS
<a name="w2aac17c19b9b7c13"></a>

The Deploy to AWS section contains information on how to configure your credentials to connect with AWS for the purposes of deploying your application and examples of how to deploy your application with Application Builder.

To connect to AWS with your existing credentials from the **Walkthrough of Application Builder**, complete one of the following procedures.

**Workforce: Sign in to AWS with single sign-on.**

1. From the **Deploy to AWS** section in the **Walkthrough of Application Builder**, choose the **Configure credentials** button to open the **AWS: LOGIN** menu in the AWS Toolkit explorer.

1. From the **AWS: LOGIN** menu, choose **Workforce**, then choose the **Continue** button to proceed.

1. Enter your **Start URL** into the provided field, choose your **AWS Region** from the drop-down menu, then choose the **Continue** button to proceed.

1. From the VS Code pop-up window, confirm that you want to open the AWS Authentication site in your default browser.

1. From your default browser, complete the authentication steps, you're notified when authentication is complete and it's safe to close your browser window.

**IAM Credentials: Store keys for use with AWS CLI tools.**

1. From the **Deploy to AWS** section in the **Walkthrough of Application Builder**, choose the **Configure credentials** button to open the **AWS: LOGIN** menu in the AWS Toolkit explorer.

1. From the **AWS: LOGIN** menu, choose **IAM Credentials**, then choose the **Continue** button to proceed.

1. Enter a **Profile Name** into the provided field, then input your **Access Key** and **Secret Key**, then choose the **Continue** button to proceed.

1. VS Code displays the status of your authentication, notifying you if authentication is complete or your credentials are invalid.

For detailed information on configuring your credentials for deployment with the AWS CLI, see the [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) topic in the *AWS CLI* Developer Guide. For additional information about connecting to AWS from the AWS Toolkit using your existing credentials, see the [Connecting to AWS](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html) topic in this User Guide.
