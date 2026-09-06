---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/lambda-build-test-severless-app.html
---

# Tutorial: Build and Test a Serverless Application with AWS Lambda
<a name="lambda-build-test-severless-app"></a>

You can build a serverless Lambda application by using an AWS Toolkit for Visual Studio template. The Lambda project templates include one for an **AWS Serverless Application**, which is the AWS Toolkit for Visual Studio implementation of the [AWS Serverless Application Model (AWS SAM)](https://github.com/awslabs/serverless-application-model). Using this project type you can develop a collection of AWS Lambda functions and deploy them with any necessary AWS resources as a whole application, using AWS CloudFormation to orchestrate the deployment.

For prerequisites and information about setting up the AWS Toolkit for Visual Studio, see [Using the AWS Lambda Templates in the AWS Toolkit for Visual Studio](lambda-index.md).

**Topics**
+ [Create a New AWS Serverless Application Project](#create-a-new-aws-serverless-application-project)
+ [Reviewing the Serverless Application files](#examine-the-files-in-the-serverless-application)
+ [Deploying the Serverless Application](#deploy-the-serverless-application)
+ [Test the Serverless Application](#test-the-serverless-application)

## Create a New AWS Serverless Application Project
<a name="create-a-new-aws-serverless-application-project"></a>

AWS Serverless Application projects create Lambda functions with a serverless CloudFormation template. CloudFormation templates enable you to define additional resources such as databases, add IAM roles, and deploy multiple functions at one time. This differs from AWS Lambda projects, which focus on developing and deploying a single Lambda function.

The following procedure describes how to create a new AWS Serverless Application Project.

1. From Visual Studio expand the **File** menu, expand **New**, then choose **Project**.

1. In the **New Project** dialog box, ensure that the **Language**, **Platform**, and **Project type** drop-down boxes are set to "All ..." and enter **aws lambda** in the **Search** field.

1. Select the **AWS Serverless Application with Tests (.NET Core - C\#)** template.
**Note**
It's possible that the **AWS Serverless Application with Tests (.NET Core - C\#)** template may not populate at the top of the results.

1. Click **Next** to open the **Configure your new project** dialog.

1. From the **Configure your new project** dialog, enter **ServerlessPowertools** for the **Name**, then complete the remaining fields to your preference. Choose the **Create** button to proceed to the **Select Blueprint** dialog.

1. From the **Select Blueprint** dialog choose the **Powertools for AWS Lambda** blueprint, and then choose **Finish** to create the Visual Studio project.

## Reviewing the Serverless Application files
<a name="examine-the-files-in-the-serverless-application"></a>

The following sections provide a detailed look at three Serverless Application files created for your project:

1. serverless.template

1. Functions.cs

1. aws-lambda-tools-defaults.json

### 1. serverless.template
<a name="blogcs"></a>

A `serverless.template` file is an AWS CloudFormation template for declaring your Serverless functions and other AWS resources. The file included with this project contains a declaration for a single Lambda function that will be exposed through the Amazon API Gateway as an `HTTP *Get*` operation. You can edit this template to customize the existing function or add more functions and other resources that are required by your application.

The following is an example of a `serverless.template` file:

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Transform": "AWS::Serverless-2016-10-31",
  "Description": "An AWS Serverless Application.",
  "Resources": {
    "Get": {
      "Type": "AWS::Serverless::Function",
      "Properties": {
         "Architectures": [
            "x86_64"
            ],
         "Handler": "ServerlessPowertools::ServerlessPowertools.Functions::Get",
         "Runtime": "dotnet8",
         "CodeUri": "",
         "MemorySize": 512,
         "Timeout": 30,
         "Role": null,
         "Policies": [
            "AWSLambdaBasicExecutionRole"
            ],
         "Environment": {
            "Variables": {
               "POWERTOOLS_SERVICE_NAME": "ServerlessGreeting",
               "POWERTOOLS_LOG_LEVEL": "Info",
               "POWERTOOLS_LOGGER_CASE": "PascalCase",
               "POWERTOOLS_TRACER_CAPTURE_RESPONSE": true,
               "POWERTOOLS_TRACER_CAPTURE_ERROR": true,
               "POWERTOOLS_METRICS_NAMESPACE": "ServerlessGreeting"
               }
            },
         "Events": {
            "RootGet": {
               "Type": "Api",
               "Properties": {
                  "Path": "/",
                  "Method": "GET"
                  }
               }
            }
         }
      }
   },
  "Outputs": {
    "ApiURL": {
      "Description": "API endpoint URL for Prod environment",
      "Value": {
        "Fn::Sub": "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/"
      }
    }
  }
}
```

Notice that many of the `...AWS:: Serverless::Function...` declaration fields are similar to the fields of a Lambda project deployment. Powertools Logging, Metrics and Tracing are configured through the following environment variables:
+ POWERTOOLS\_SERVICE\_NAME=ServerlessGreeting
+ POWERTOOLS\_LOG\_LEVEL=Info
+ POWERTOOLS\_LOGGER\_CASE=PascalCase
+ POWERTOOLS\_TRACER\_CAPTURE\_RESPONSE=true
+ POWERTOOLS\_TRACER\_CAPTURE\_ERROR=true
+ POWERTOOLS\_METRICS\_NAMESPACE=ServerlessGreeting

For definitions and additional details about the environment variables, see the [Powertools for AWS Lambda references](https://awslabs.github.io/aws-lambda-powertools-dotnet/references/) website.

### 2. Functions.cs
<a name="functionscs"></a>

`Functions.cs` is a class file containing a C\# method that's mapped to a single function declared in the template file. The Lambda function responds to `HTTP Get` methods from API Gateway. The following is an example of the `Functions.cs` file:

```
public class Functions
{
    [Logging(LogEvent = true, CorrelationIdPath = CorrelationIdPaths.ApiGatewayRest)]
    [Metrics(CaptureColdStart = true)]
    [Tracing(CaptureMode = TracingCaptureMode.ResponseAndError)]
    public APIGatewayProxyResponse Get(APIGatewayProxyRequest request, ILambdaContext context)
    {
        Logger.LogInformation("Get Request");

        var greeting = GetGreeting();

        var response = new APIGatewayProxyResponse
        {
            StatusCode = (int)HttpStatusCode.OK,
            Body = greeting,
            Headers = new Dictionary (string, string) { { "Content-Type", "text/plain" } }
        };

        return response;
    }

    [Tracing(SegmentName = "GetGreeting Method")]
    private static string GetGreeting()
    {
        Metrics.AddMetric("GetGreeting_Invocations", 1, MetricUnit.Count);

        return "Hello Powertools for AWS Lambda (.NET)";
    }
}
```

### 3. aws-lambda-tools-defaults.json
<a name="functionscs"></a>

`aws-lambda-tools-defaults.json` provides the default values for the AWS deployment wizard inside Visual Studio and the AWS Lambda commands added to the .NET Core CLI. The following is an example of the `aws-lambda-tools-defaults.json` file included with this project:

```
{
  "profile": "Default",
  "region": "us-east-1",
  "configuration": "Release",
  "s3-prefix": "ServerlessPowertools/",
  "template": "serverless.template",
  "template-parameters": ""
}
```

## Deploying the Serverless Application
<a name="deploy-the-serverless-application"></a>

To deploy your serverless application complete the following steps

1. From the **Solution Explorer**, open the context menu for (right click) your project and choose **Publish to AWS Lambda** to open the **Publish AWS Serverless Application** dialog.

1. From the **Publish AWS Serverless Application** dialog, enter a name for the CloudFormation stack container in the **Stack Name** field.

1. In the **S3 Bucket** field, choose an Amazon S3 bucket that your application bundle will upload to or choose the **New...** button and enter the name of a new Amazon S3 bucket. Then choose **Publish** to publish to deploy your application.
**Note**
Your CloudFormation stack and Amazon S3 Bucket must exist in the same AWS region. The remaining settings for your project are defined in the `serverless.template` file.
![Image of the Publish AWS Serverless Application dialog.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/lambda-upload-serverless-03192024.png)

1. The **Stack** view window opens during the publishing process, when deployment is complete the **Status** field displays: `CREATE_COMPLETE`.
![Image of the deployment stack view window in visual studio.](http://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/lambda-upload-stackview-03192024.png)

## Test the Serverless Application
<a name="test-the-serverless-application"></a>

When the stack creation is complete, you can view your application using the **AWS Serverless URL**. If you've completed this tutorial without adding any additional functions or parameters, accessing your AWS serverless URL displays the following phrase in your web browser: `Hello Powertools for AWS Lambda (.NET)`.
