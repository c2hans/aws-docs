---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/sam-get-started.html
---

# Getting Started with serverless applications
<a name="sam-get-started"></a>

The following sections describe how to get started creating an AWS Serverless Application from the AWS Toolkit for Visual Studio Code, using AWS Serverless Application Model (AWS SAM) and CloudFormation stacks.

## Prerequisites
<a name="serverless-apps-assumptions"></a>

Before you can create or work with an AWS Serverless Application, the following prerequisites must be completed.

**Note**
The following operations may require you to exit or restart VS Code before the changes are complete.
+ Install the AWS SAM command line interface (CLI). For additional information and instructions on how to install the AWS SAM CLI, see the [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) topic in this *AWS Serverless Application Model User Guide*.
+ From your AWS config file, identify your default AWS Region. For more information on your config file, see the [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) topic in the *AWS Command Line Interface User Guide*.
+ Install your language SDK and configure your toolchain. For additional information on how to configure your toolchain from the AWS Toolkit for Visual Studio Code see the [configure your toolchain](setup-toolchain.md) topic in this User Guide.
+ Install the [YAML language support extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) from the VS Code marketplace. This is required for the CodeLens feature of AWS SAM template files are accessible. For additional information about CodeLens, see the [CodeLens](https://code.visualstudio.com/api/language-extensions/programmatic-language-features#codelens-show-actionable-context-information-within-source-code) section in the VS Code documentation

## IAM permissions for serverless applications
<a name="serverless-apps-permissions"></a>

In the Toolkit for VS Code you must have a credentials profile that contains the AWS Identity and Access Management (IAM) permissions necessary to deploy and run serverless applications. You must have appropriate read/write access to the following services: CloudFormation, IAM, Lambda, Amazon API Gateway, Amazon Simple Storage Service (Amazon S3), and Amazon Elastic Container Registry (Amazon ECR).

For additional information about setting up authentication required to deploy and run serverless applications, see the [Managing resource access and permissions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-permissions.html) in the *AWS Serverless Application Model Developer Guide*. For information on how to set up your credentials, see the [AWS IAM credentials](setup-credentials.md) in this User Guide.

## Creating a new serverless application (local)
<a name="serverless-apps-create"></a>

This procedure shows how to create a serverless application with the Toolkit for VS Code by using AWS SAM. The output of this procedure is a local directory on your development host containing a sample serverless application, which you can build, locally test, modify, and deploy to the AWS Cloud.<a name="serverless-apps-create-proc"></a>

1. To open the **Command Palette**, choose **View**, **Command Palette**, and then enter **AWS**.

1. Choose **AWS Toolkit Create Lambda SAM Application**.
![Command palette dialog box.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/sam-create-app-cmdlet-updated.png)
**Note**
If the AWS SAM CLI isn't installed, you get an error in the lower-right corner of the VS Code editor. If this happens, verify that you've met all the [assumptions and prerequisites](#serverless-apps-assumptions).

1. Choose the runtime for your AWS SAM application.
**Note**
If you select one of the runtimes with "(Image)", your application is package type `Image`. If you select one of the runtimes without "(Image)", your application is type `Zip`. For more information about the difference between `Image` and `Zip` package types, see [Lambda deployment packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) in the *AWS Lambda Developer Guide*.

1. Depending on the runtime you select, you may be asked to select a dependency manager and a runtime architecture for your SAM application.

------
#### [ Dependency Manager ]

   Choose between **Gradle** or **Maven**.

**Note**
This choice of build automation tools is available only for Java runtimes.

------
#### [ Architecture ]

   Choose between **x86\_64** or **arm64**.

   The option to run your serverless application in an ARM64-based emulated environment instead of the default x86\_64-based environment is available for the following runtimes:
   + nodejs12.x (ZIP and image)
   + nodejs14.x (ZIP and image)
   + python3.8 (ZIP and image)
   + python3.9 (ZIP and image)
   + python3.10 (ZIP and image)
   + python3.11 (ZIP and image)
   + python3.12 (ZIP and image)
   + java8.al2 with Gradle (ZIP and image)
   + java8.al2 with Maven (ZIP only)
   + java11 with Gradle (ZIP and image)
   + java11 with Maven (ZIP only)

**Important**
You must install AWS CLI version 1.33.0 or later to allow applications to run in ARM64-based environments. For more information, see [Prerequisites](setup-toolkit.md#setup-prereq).

------

1. Choose a location for your new project. You can use an existing workspace folder if one is open, **Select a different folder** that already exists, or create a new folder and select it. For this example, choose **There are no workspace folders open** to create a folder named `MY-SAM-APP`.

1. Enter a name for your new project. For this example, use `my-sam-app-nodejs`. After you press **Enter**, the Toolkit for VS Code takes a few moments to create the project.

When the project is created, your application is added to your current workspace. You should see it listed in the **Explorer** window.

## Opening a serverless application (local)
<a name="serverless-apps-open"></a>

To open a serverless application on your local development host, open the folder that contains the application's template file.

1. From the **File**, choose **Open Folder...**.

1. In the **Open Folder** dialog box, navigate to the serverless application folder that you want to open.

1. Choose the **Select Folder** button.

When you open an application's folder, it is added to the **Explorer** window.

## Running and debugging a serverless application from template (local)
<a name="serverless-apps-debug"></a>

You can use the Toolkit for VS Code to configure how to debug serverless applications and run them locally in your development environment.

You start to configure debug behavior by using the VS Code [CodeLens](https://code.visualstudio.com/api/language-extensions/programmatic-language-features#codelens-show-actionable-context-information-within-source-code) feature to identify an eligible Lambda function. CodeLens enables content-aware interactions with your source code. For information about ensuring that you can access the CodeLens feature, review the [Prerequisites](#serverless-apps-assumptions) section from earlier in this topic.

**Note**
In this example, you debug an application that uses JavaScript. However, you can use Toolkit for VS Code debugging features with the following languages and runtimes:
C\# – .NET Core 2.1, 3.1; .NET 5.0
JavaScript/TypeScript – Node.js 12.*x*, 14.*x*
Python – 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12
Java – 8, 8.al2, 11
Go – 1.x
Your language choice also affects how CodeLens detects eligible Lambda handlers. For more information, see [Running and debugging Lambda functions directly from code](serverless-apps-run-debug-no-template.md).

In this procedure, you use the example application created in the [Creating a new serverless application (local)](#serverless-apps-create) section earlier in this topic.

1. To view your application files in VS Code's File Explorer, choose **View**, **Explorer**.

1. From the application folder (for example, *my-sample-app*), open the `template.yaml` file.
**Note**
If you use a template with a name that's different from `template.yaml`, the CodeLens indicator isn't automatically available in the YAML file. This means that you must manually add a debug configuration.

1. In the editor for `template.yaml`, go to the `Resources` section of the template that defines serverless resources. In this case, this is the `HelloWorldFunction` resource of type `AWS::Serverless::Function`.

   In the CodeLens indicator for this resource, choose **Add Debug Configuration**.
![Using the CodeLens indicator in the template.yaml file to add a debug configuration.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/yaml_template_debug.png)

1. In the **Command Palette**, select the runtime in which your AWS SAM application will run.

1. In the editor for the `launch.json` file, edit or confirm values for the following configuration properties:
   + `"name"` – Enter a reader-friendly name to appear in the **Configuration** drop-down field in the **Run** view.
   + `"target"` – Ensure that the value is `"template"` so that the AWS SAM template is the entry point for the debug session.
   + `"templatePath"` – Enter a relative or absolute path for the `template.yaml` file.
   + `"logicalId"` – Ensure that the name matches the one specified in the **Resources** section of the AWS SAM template. In this case, it's the `HelloWorldFunction` of type `AWS::Serverless::Function`.
![Configuring the launch.json file for template-based debugging.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/template_based_config_updated.png)

   For more information about these and other entries in the `launch.json` file, see [Configuration options for debugging serverless applications](serverless-apps-run-debug-config-ref.md).

1. If you're satisfied with your debug configuration, save `launch.json`. Then, to start debugging, choose the green "play" button in the **RUN** view.

   When the debugging sessions starts, the **DEBUG CONSOLE** panel shows debugging output and displays any values returned by the Lambda function. (When debugging AWS SAM applications, the **AWS Toolkit** is selected as the **Output** channel in the **Output** panel.)

## Syncing AWS SAM applications
<a name="serverless-apps-deploy"></a>

The AWS Toolkit for Visual Studio Code runs the AWS SAM CLI command `sam sync` to deploy your serverless applications to the AWS Cloud. For additional information about AWS SAM sync, see the [AWS SAM CLI command reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html) topic in the *AWS Serverless Application Model Developer Guide*

The following procedure describes how to deploy your serverless applications to the AWS Cloud with `sam sync` from the Toolkit for VS Code.

1. From the main menu in VS Code, open the **Command Palette** by expanding **View** and choosing **Command Palette**.

1. From the **Command Palette** search for **AWS** and choose **Sync SAM Application** to start setting up your sync.
![Command to sync a serverless application.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/samsync032023.png)

1. Choose the AWS Region to sync your serverless application to.

1. Choose the `template.yaml` file to use for the deployment.

1. Select an existing Amazon S3 bucket or enter a new Amazon S3 bucket name to deploy your application to.
**Important**
Your Amazon S3 bucket must meet the following requirements:
The bucket must be in the Region that you're syncing to.
The Amazon S3 bucket name must be globally unique across all existing bucket names in Amazon S3.

1. If your serverless application includes a function with package type `Image`, enter the name of an Amazon ECR repository that this deployment can use. The repository must be in the Region that you're deploying to.

1. Select a deployment stack from the list of your previous deployments, or create a new deployment stack be entering a new stack name. Then, proceed to begin the sync process.
**Note**
Stacks used in previous deployments are recalled per workspace and region.

1. During the syncing process, the status of your deployment is captured in the **Terminal** tab of VS Code. Verify that your sync was successful from the terminal tab, if an error occurs you receive a notification.
![An error pop-up while deploying a serverless application.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/sam-deploy-error.png)
**Note**
For additional details about your sync, the AWS Toolkit for Visual Studio Code logs are accessible from the **Command Palette**.

   To access the your AWS Toolkit for Visual Studio Code logs from the Command Palette, expand **View**, choose **Command Palette**, then search for **AWS: View AWS Toolkits Logs**, and select it when it populates in the list.

When the deployment is complete, you see your application listed in the **AWS Explorer**. For more information about how to invoke the Lambda function created as part of the application, see the [Working with AWS Lambda Functions](remote-lambda.md) topic in this User Guide.

## Deleting a serverless application from the AWS Cloud
<a name="serverless-apps-delete"></a>

Deleting a serverless application involves deleting the CloudFormation stack that you previously deployed to the AWS Cloud. Note that this procedure does not delete your application directory from your local host.

1. Open the [AWS Explorer](aws-explorer.md).

1. In the **AWS Toolkit Explorer** window, expand the Region containing the deployed application that you want to delete, and then expand **CloudFormation**.

1. Open the context (right-click) menu for the name of the CloudFormation stack that corresponds to the serverless application that you want to delete, and then choose **Delete CloudFormation Stack**.

1. To confirm that you want to delete the selected stack, choose **Yes**.

If the stack deletion succeeds, the Toolkit for VS Code removes the stack name from the CloudFormation list in **AWS Explorer**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
