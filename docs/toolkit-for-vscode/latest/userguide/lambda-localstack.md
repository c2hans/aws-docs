---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-localstack.html
---

# AWS Lambda with LocalStack support
<a name="lambda-localstack"></a>

Build, test, and debug your serverless applications with LocalStack support in the AWS Toolkit for Visual Studio Code. LocalStack is an AWS Cloud emulator that allows for local testing of serverless applications.

For additional information about AWS Lambda, see the [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) *Developer Guide*. To learn more about LocalStack, visit their website [LocalStack](https://www.localstack.cloud/).

## Prerequisites
<a name="prereq"></a>

 The following are prerequisites to working with LocalStack in VS Code.

**Note**
The LocalStack CLI is installed during the setup process, but if you prefer a different version of the LocalStack CLI, the minium required version is *4.8.0*.
+ A LocalStack Web Application account is required for access to all features available for the free and paid LocalStack tiers. LocalStack community edition is available without an account.
+ Docker is required to work with LocalStack in VS Code. For more information about LocalStack requirements for Docker, see the LocalStack [Docker Images](https://docs.localstack.cloud/aws/capabilities/config/docker-images/) topic in the LocalStack documentation.
+ **Recommended:** The AWS Command Line Interface (AWS CLI) assists you in working with services in your simulated cloud environment.

## Installing LocalStack
<a name="install"></a>

 To install LocalStack free and paid tiered versions, complete the following steps.

**Note**
For instructions on how to set up LocalStack Community edition, see the *LocalStack Community* content in the *Setting up LocalStack* section of this topic.

1. From the AWS Toolkit, expand the **APPLICATION BUILDER** explorer.

1. Choose the **Open Walkthrough** button to open the **Get started building your application** walkthrough tab in the VS Code editor.

1. From the walkthrough, choose the **Install LocalStack** to start the LocalStack installation process in VS Code.

## Setting up LocalStack
<a name="setup"></a>

After you install the LocalStack extension for VS Code, you may see one of the following indicators when setup is needed:
+ In the VS Code Status Bar, located in the lower-left corner of the IDE by default, the LocalStack status is red.
+ VS Code prompts you to set up LocalStack.

There are two types of setup and configurations for LocalStack, depending on which version of LocalStack you're using. The following tabbed sections describe each LocalStack setup process.

**Note**
LocalStack auth tokens are required for the free and paid tier versions of LocalStack. For specific information about LocalStack pricing, see their [Choose your plan](https://www.localstack.cloud/pricing) pricing guide.

### LocalStack free and paid tiers
<a name="free-paid"></a>

There are 2 ways to set up LocalStack.
+ From the VS Code **Setup LocalStack to get started** prompt, choose the **Setup** button.
+ From the VS Code status bar, choose the LocalStack status icon to open the **Setup LocalStack to get started** prompt, then choose the **Setup** button.

During setup, the system goes through the following steps:

1. Installs the LocalStack CLI.

1. Checks to see if you have a LocalStack account.

1. If you have a LocalStack account, the system guides you through the authentication process in your default web browser. Similarly, if you do not have a LocalStack account, the system guides you through account setup before the authentication process.

After LocalStack is set up, the LocalStack status updates in the VS Code status bar.

**Note**
If you haven't created an AWS profile for LocalStack, then a new one is automatically created for you as part of the LocalStack setup process.

### LocalStack Community
<a name="community"></a>

The Community edition of LocalStack is free to use and doesn't require you to sign up for an account, it runs from a Docker image that doesn't require a license. For additional details about LocalStack Community Edition, see the [LocalStack Community image](https://docs.localstack.cloud/references/docker-images/) documentation. The following sections describe prerequisites and the basic setup that is required to work with LocalStack community edition in VS Code.

**Launching a new instance**

 To launch a new instance of LocalStack Community, complete the following procedure.

**Note**
The following example starts a container instance of LocalStack on port 4566. If you specify different port values, you must update the port value specified in the procedure located in the *Configuring the AWS CLI and AWS Toolkit* section.

1. From VS Code, open the VS Code terminal by pressing **ctrl \+ `(backtick)**.

1. Enter the following into the terminal.

   **Mac:**

   ```
   docker run -d --name localstack_main \
   >> -p 4566:4566 \
   >> -v /var/run/docker.sock:/var/run/docker.sock \
   >> localstack/localstack
   ```

   **Windows:**

   ```
   docker run -d --name localstack_main `
   >> -p 4566:4566 `
   >> -v /var/run/docker.sock:/var/run/docker.sock `
   >> localstack/localstack
   ```

1. The terminal updates with the status of your Docker instance when the process is complete.

This containerized instance of LocalStack gives you access to the AWS services that you specified during the download process.

**Configuring the CLI for LocalStack and Docker.**

 To configure the AWS CLI and AWS Toolkit to work with LocalStack in Docker, set up a new profile by completing the following steps:

1. From VS Code, open the VS Code terminal by pressing **ctrl \+ `(backtick)**.

1. Enter the following into the terminal.

   ```
   ~/.aws/credentials
   [localstack]
   aws_access_key_id = test
   aws_secret_access_key = test
   ~/.aws/config
   [profile localstack]
   region = us-east-1
   output = json
   endpoint_url = http://localhost:4566 [default localstack endpoint]
   ```

1. The AWS Toolkit detects your LocalStack profile and updates the connection status menu.

After setup, choosing your LocalStack profile from the AWS profile section of the status bar makes your LocalStack resources visible in the AWS explorer. Additionally, you can view your LocalStack logs in the **Output** tab of the VS Code terminal.

## Starting LocalStack in VS Code
<a name="w2aac17c43c17c13"></a>

You can start LocalStack using any of the following methods:

**Starting LocalStack from the VS Code Status Bar**

1. From VS Code, navigate to the status bar, then choose the **Start LocalStack** button to launch LocalStack.

1. The VS Code Status Bar updates when LocalStack has launched successfully.

**Starting LocalStack from the VS Code **Command Palette****

1. From VS Code, open the **Command Palette** by pressing **Cmd \+ Shift \+ P** (Mac) or **Control \+ Shift \+ P** (Windows).

1. From the **Command Palette**, enter **Start LocalStack** in the search bar and choose it from the list when it populates in the results.

1. The VS Code Status Bar updates when LocalStack has launched successfully.

**Starting LocalStack from the VS Code terminal**

1. From VS Code, open the VS Code terminal by pressing **ctrl \+ `(backtick)**.

1. From the VS Code terminal, enter **localstack start** CLI command.

1. The VS Code Status Bar updates when LocalStack has launched successfully.

## Building a sample serverless application
<a name="serverless"></a>

 To start working with LocalStack in VS Code, you need a sample serverless application. If you already have an existing application in your AWS account you can deploy it locally using LocalStack or you can create a new application with AWS Serverless Land.

For additional information about creating an application with Serverless Land in the AWS Toolkit, see the [Working with AWS Serverless Land](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/serverlessland-overview.html) topic in this User Guide. For detailed information about Serverless Land, see the [Serverless Land](https://serverlessland.com/) web-application main landing page.

## Testing and debugging Lambda functions with LocalStack
<a name="test-debug"></a>

Testing and debugging your Lambda functions in the LocalStack VS Code extension is similar to working with your functions deployed to the AWS cloud. The main difference is that your AWS Toolkit instance must be authenticated with your LocalStack account to deploy and debug your functions with LocalStack.

**Note**
The testing and debugging features described in this section are not available for LocalStack Community edition.
To work with LocalStack in VS Code, connect to your LocalStack profile in the AWS Toolkit. When your LocalStack profile is active, the VS Code status bar shows **AWS: profile:localstack (custom endpoint)** with a check mark.

For detailed information about working with your Lambda functions in the AWS Toolkit, see the [Working with AWS Lambda functions](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/remote-lambda.html) topic in this user guide.
