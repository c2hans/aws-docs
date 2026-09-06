---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/lambda-remote-debug.html
---

# AWS Lambda remote debugging
<a name="lambda-remote-debug"></a>

The AWS Toolkit for Visual Studio Code enables you to debug your AWS Lambda functions that are running in the cloud, directly in VS Code. With AWS Lambda remote debugging you can inspect running functions, set breakpoints, examine variables, and step-through debugging without modifying their existing development workflow.

The following sections describe how to work with Lambda remote debugging in the AWS Toolkit for Visual Studio Code.

## How Lambda remote debugging works
<a name="w2aac17c43c19b7"></a>

The AWS Toolkit enables remote debugging by temporarily modifying your Lambda functions with an additional Lambda debugging layer and extending the Lambda invoke timeout limit to 900 seconds. A secure connection is established between your local debugger and the Lambda runtime environment using AWS IoT Secure Tunneling. This connection allows you to use your local-code breakpoints to step through the function as it executes remotely. After your debugging session is complete, all of the temporary modifications are automatically reverted to their original settings.

## Getting Started
<a name="w2aac17c43c19b9"></a>

### Supported runtimes
<a name="w2aac17c43c19b9b3"></a>

The following runtimes are supported by Lambda remote debugging.
+ Python (Amazon Linux 2023)
+ Java
+ Typescript/JavaScript/Node.js (Amazon Linux 2023)

**Note**
Lambda managed instances and OCI image function types are not supported by Lambda remote debugging.

### Prerequisites
<a name="w2aac17c43c19b9b5"></a>

Before you begin, the following prerequisites must be met.
+ You must have valid AWS credentials configured in the AWS Toolkit. For additional details about installing the AWS Toolkit and configuring your credentials, see the [Getting started](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setting-up.html) topic in this user guide.
+ A Lambda function has been deployed to your AWS account. For details on deploying a Lambda function, see the [Create your first Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) topic in the *AWS Lambda* Developer Guide.
+ You must have appropriate AWS Identity and Access Management (IAM) policy and permissions to debug your function. For additional details on Lambda permissions, see the [AWS managed policies for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-iam-awsmanpol.html) topic in the *AWS Lambda* Developer Guide. The following is an example of a policy that contains the minimum required permissions for working with Lambda remote debugging in the AWS Toolkit.
**Note**
Remote debugging is enabled through AWS AWS IoT Secure Tunneling. This allows your local debugger to establish a secure connection to the Lambda runtime environment.

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "lambda:ListFunctions",
          "lambda:GetFunction",
          "lambda:GetFunctionConfiguration",
          "lambda:GetLayerVersion",
          "lambda:UpdateFunctionConfiguration",
          "lambda:InvokeFunction",
          "lambda:PublishVersion",
          "lambda:DeleteFunction",
          "iot:OpenTunnel",
          "iot:RotateTunnelAccessToken",
          "iot:ListTunnels"
        ],
        "Resource": "*"
      }
    ]
  }
  ```

## Accessing Lambda remote debugging
<a name="w2aac17c43c19c11"></a>

There are two main paths to access Lambda remote debugging in the AWS Toolkit: the AWS explorer or the Application Builder explorer. From the AWS explorer, you can access Lambda remote debugging through your AWS Lambda nodes. From the Application Builder explorer, you can access Lambda remote debugging through your local AWS SAM projects.

**Accessing Lambda remote debugging from the AWS explorer**

1. From VS Code, open the AWS Toolkit extension.

1. From the AWS Toolkit, expand the AWS explorer.

1. From the explorer, expand the **Lambda** node.

1. Navigate to the function you want to debug, then choose the **Invoke remotely** icon from the context menu to open the **Remote invoke configuration** screen.

**Accessing Lambda remote debugging from the Application Builder explorer.**

1. From VS Code, open the AWS Toolkit extension.

1. From the AWS Toolkit, expand the application builder explorer.

1. From the explorer expand the `AWS SAM` project that contains the Lambda project you want to debug.

1. Expand the deployed `Lambda` function that you want to debug.

1. Navigate to the function remote, then choose the **Invoke remotely** icon from the context menu to open the **Remote invoke configuration** screen.

## Working with Lambda remote debugging
<a name="w2aac17c43c19c13"></a>

The following sections describe how to work with Lambda remote debugging in the AWS Toolkit for Visual Studio Code.

**Note**
Lambda functions have a 5-layer limit and a 250MB combined limit for function code and all attached layers. Lambda remote debugging requires at least 1 free layer to run.

### Setting up a debugging session
<a name="w2aac17c43c19c13b7"></a>

Before you begin, configure your debugging session by completing the following procedure.

1. Open the **Remote invoke configuration** menu by completing the *Accessing Lambda remote debugging from the AWS explorer* or the *Accessing Lambda remote debugging from the Application Builder explorer* procedure, located in the previous section.

1. From the **Remote invoke configuration** menu, select the **Remote Debugging** check box to display the remote debugging properties.

1. Specify the **Local Root Path** to your local handler file.
**Note**
The local root path is the location of your source code that matches the deployed Lambda function. If you're working from a deployed function in the Application Builder explorer, your local root path is automatically detected.
If you don't have the source code stored locally, choose the **Download remote code** button to retrieve your Lambda function source code. This will open your `handler file` in the VS Code editor.

1. From the **Payload** section, specify where your test-event data is obtained.

### Setting breakpoints and debugging
<a name="w2aac17c43c19c13b9"></a>

Set breakpoints and begin debugging by completing the following procedure.

1. From your `handler file` in the VS Code editor, click in the gutter-margin to set breakpoints at the line numbers where you want to pause debugging.

1. When you're satisfied with the breakpoints, return to the **Remote invoke configuration** menu to verify that your settings are configured correctly, then choose the **Remote invoke** button to start debugging.

1. The AWS Toolkit updates your Lambda function with debugging capabilities, establishes a secure tunnel for the debugging session, invokes your function with the specified payload, then pauses the process when it reaches a breakpoint.

1. At a breakpoint pause, use the **RUN AND DEBUG** pane to view your **VARIABLES**, **CALL STACK**, and **BREAKPOINTS**.

### Updating and testing your function
<a name="w2aac17c43c19c13c11"></a>

To modify your code and test changes with a quick deployment, complete the following procedure.

1. With your debugging session active, make changes to your `handler file` in the VS Code editor.

1. Save your changes (**Command\+S on macOS**,**Ctrl\+S on Windows**)

1. When prompted, confirm that you wish to proceed to deploy your changes. The AWS Toolkit will update your Lambda function with the modified code.

1. Continue debugging and testing your changes by setting new breakpoints and selecting the **Remote invoke** button again.
**Note**
 Alternatively, you can deselect the **Attach debugger** option in the VS Code debugging controls and choose the **Remote invoke** button to run your function without debugging.

### Ending a debugging session
<a name="w2aac17c43c19c13c13"></a>

Each of the following options ends your remote debugging session and removes the debug layer from your project.
+ Choosing the **Remove Debug Setup** option from the **Remote invoke configuration** screen.
+ Choosing the **disconnect** icon from the VS Code debugging controls.
+ Closing the `handler file` in the VS Code editor.

**Note**
Take note of the following:
The Lambda debug layer is automatically removed after 60 seconds of inactivity. The count begins when your last invoke is complete.
If you made code changes to your infrastructure-as-code (IaC) managed (AWS SAM, AWS CDK, Terraform) functions during the debugging process, save them to your local project and consider updating your source-control repository. Unsaved changes are overwritten when your IaC function redeploys.
If you made temporary changes for debugging purposes only, you may want to redeploy your function from your source control to ensure it matches your production code.

### Debugging TypeScript Lambda functions with source maps
<a name="typescript-source-maps"></a>

The following sections describe how to debug your TypeScript Lambda functions with source maps.

#### Prerequisites
<a name="w2aac17c43c19c13c15b5"></a>

To debug your TypeScript Lambda functions, the following prerequisites must be met.
+ Your TypeScript must be compiled with the source map option enabled. For additional information, see the [JavaScript source map support](https://code.visualstudio.com/docs/typescript/typescript-debugging#_javascript-source-map-support) topic in the VS Code documentation.
+ In-line source maps are not supported. You must use a separate `.js.map` file to store the source map.

#### Configuration
<a name="w2aac17c43c19c13c15b7"></a>

To configure Lambda remote debugging for TypeScript Lambda functions in the AWS Toolkit, complete the following steps.

1. From the AWS Toolkit, expand the AWS explorer.

1. From the explorer, expand the **Lambda** node.

1. Navigate to the function you want to configure for TypeScript, then choose the **Invoke remotely** icon from the context menu to open the **Remote invoke configuration** screen.

1. Enable remote debugging by select the **Remote debugging** check box.

1. Configure your **Local Root Path** by pointing to the directory containing your `TypeScript handler file`.
**Note**
The `TypeScript handler file` is where you set your debugging breakpoints.

1. Expand **Remote debug additional configuration** settings.

1. Enable source mapping by selecting the **Source map** check box.

1. Set the **Out files** field to the local directory of your Lambda function copy.
**Example**

   If `app.js` and `app.map` are in `.aws-sam/build/HelloWorldFunction`, then make the **Out files** location `/Users/user/project/aws-sam/build/HelloWorldFunction/*`.
**Note**
The **Out file** path should be an absolute path.
For AWS SAM and AWS CDK projects, the AWS Toolkit supports automatic source map detection. If the **Out files** field is left empty for these projects, the toolkit will automatically attempt to detect the source map location.

1. When you're satisfied with the settings, choose the **Remote invoke** button to begin debugging your TypeScript function.

## Troubleshooting and advanced use cases
<a name="troubleshooting"></a>

If your debug session fails, start the troubleshooting process by completing these steps.

1. Update the AWS Toolkit to the latest version.

1. Refresh the web view by closing the **Remote invoke configuration** web view and reopening it.

1. Restart VS Code by closing it completely and reopening it.

1. Open the VS Code Command Palette and enter the command **AWS: Reset Lambda Remote Debugging Snapshot**, select it when it populates in the results to reset your Lambda remote debugging snapshot.

1. If you're not able to troubleshoot the problem, submit an issue to [AWS Toolkit for Visual Studio Code GitHub Issues](https://github.com/aws/aws-toolkit-vscode/issues).

### Advanced use case: code-signing configuration
<a name="troubleshooting-code-signing-configuration"></a>

Remote debugging requires attaching a debug layer to your Lambda function. If your function has code-signing configuration enabled and enforced, the AWS Toolkit can't automatically attach the debug layer to your function.

There are two options to resolve the code-signing configuration issue.
+ Temporarily remove code signing.
+ Use a signed debug layer.

#### Temporarily removing code signing
<a name="troubleshooting-code-signing-configuration-temp-remove"></a>

Update the code-signing configuration by setting `UntrustedArtifactOnDeployment : Warn`, then re-enable it back to `Enforced` after the debugging process is complete.

For more information, see the [UpdateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateCodeSigningConfig.html) reference in the *AWS Lambda API Reference*.

#### Using a signed debug layer
<a name="troubleshooting-code-signing-configuration-signed-debug-layer"></a>

1. From Lambda remote debugging in the AWS Toolkit, expand the **Remote debug additional configuration** section.

1. From the **Remote debug additional configuration** section, copy your Region layer ARN from the **Layer override** field.

1. From the AWS CLI, use the following command to download the layer version `aws lambda get-layer-version-by-arn --arn layer-arn`, replacing *layer-arn* with your layer ARN. For detailed instructions on how to download the signed debug layer, see the [get-layer-version-by-arn](https://docs.aws.amazon.com/cli/latest/reference/lambda/get-layer-version-by-arn.html) reference in the *AWS CLI Command Reference*.

1. Sign the layer with your code-signing configuration and publish it to your account. For signing and publishing guidance, see the [Set up code signing for your AWS SAM application](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/authoring-codesigning.html) topic in the *AWS Serverless Application Model Developer Guide*.

1. After the layer has been signed and published to your account, return to the **Remote debug additional configuration** section of Lambda remote debugging, then enter the new layer ARN into the **Layer override** field. When the process is complete, Lambda remote debugging uses your signed layer instead of the default layer.

### Advanced use case: debugging functions with SnapStart or provisioned concurrency
<a name="troubleshooting-snapstart-provisioned-concurrency"></a>

For Lambda functions configured with SnapStart or provisioned concurrency, publishing a new version takes significantly more time. To speed up your debugging workflow, you can configure Lambda remote debugging to update only the `$LATEST` version of your function instead of publishing a new version.

1. From the **Remote invoke configuration** screen, expand the **Remote debug additional configuration** settings.

1. Deselect the **Publish version** option.

1. The AWS Toolkit will now only update your function's `$LATEST` version and debug using it.

**Note**
As a side effect of debugging with the `$LATEST` version, you should avoid other traffic that may invoke your `$LATEST` version to ensure an undisturbed debugging environment.

### Supported regions
<a name="troubleshooting-regions"></a>

The following error occurs when a region doesn't support remote debugging.

```
Region ${region} doesn't support remote debugging yet
```

The following is a list of supported regions.
+ ap-east-1
+ ap-northeast-1
+ ap-northeast-2
+ ap-south-1
+ ap-southeast-1
+ ap-southeast-2
+ ca-central-1
+ eu-central-1
+ eu-north-1
+ eu-west-1
+ eu-west-2
+ eu-west-3
+ me-central-1
+ me-south-1
+ sa-east-1
+ us-east-1
+ us-east-2
+ us-west-1
+ us-west-2

### Lambda RequestEntityTooLargeException
<a name="troubleshooting-storage-limit"></a>

Lambda functions have a 5-layer limit and a 250MB combined limit for function code and all attached layers. The remote debugging layer is approximately 40MB, which may cause your function to exceed this limit if you have a large function package or multiple layers. For additional details, see the [Lambda: InvalidParameterValueException or RequestEntityTooLargeException](https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-deployment.html#troubleshooting-deployment-InvalidParameterValueException1) topic section in the *AWS Lambda Developer Guide*.

The following list describes ways to troubleshoot and correct this error.
+ **Reduce function size**: Optimize your function code and remove unnecessary dependencies.
+ **Remove unused layers**: Temporarily remove non-essential layers during debugging.
+ **Use external dependencies**: Move large dependencies to external storage, such as Amazon S3, and load them at runtime.

### Troubleshooting Java debugging
<a name="troubleshooting-java-debugging"></a>

To debug a Java Lambda function, you must have the same Java version installed locally that matches your Lambda function's runtime version.

For example, when debugging a Java 25 function, you must have Java 25 installed in your local environment where the AWS Toolkit is running. If you attempt to debug a Java 25 function with Java 21 or an earlier version installed locally, remote debugging will not be able to stop at the breakpoints you set.

Ensure your local Java version matches your Lambda function's runtime version before starting a debugging session.

### IoT secure tunneling quota exceeded
<a name="troubleshooting-tunnel-quota"></a>

The following is an example of the *tunnel quota exceeded error* that occurs when you've reached the daily limit for AWS IoT secure tunneling connections in Lambda remote debugging.

```
Error creating/reusing tunnel: LimitExceededException: Exceeded quota of Lambda debugging tunnels
```

AWS IoT Secure Tunneling connection have the following quotas:
+ Free-tier IoT secure tunneling is allotted 10 connections per day.
+ Each tunnel supports one VS Code instance for up to 12 hours.
+ The quota applies per AWS account, per day.

If you encounter the AWS IoT secure tunneling error, wait for the daily quota reset or contact AWS support to request a quota-limit increase. For AWS support contact info, see the [AWS support contact portal](https://aws.amazon.com/contact-us/). For detailed information about AWS IoT secure tunneling, see the [AWS IoT secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html) topic in the *AWS IoT Developer Guide*.
