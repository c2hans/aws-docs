---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/lambda-rekognition-example.html
---

# Tutorial: Creating an Amazon Rekognition Lambda Application
<a name="lambda-rekognition-example"></a>

This tutorial shows you how to create an Lambda application that uses Amazon Rekognition to tag Amazon S3 objects with detected labels.

For prerequisites and information about setting up the AWS Toolkit for Visual Studio, see [Using the AWS Lambda Templates in the AWS Toolkit for Visual Studio](lambda-index.md).

## Create a Visual Studio .NET Core Lambda Image Rekognition Project
<a name="create-a-visual-studio-net-core-lam-image-rekognition-project"></a>

The following procedure describes how to create an Amazon Rekognition Lambda application from the AWS Toolkit for Visual Studio.

**Note**
Upon creation, your application has a solution with two projects: the source project that contains your Lambda function code to deploy to Lambda, and a test project using xUnit for testing your function locally.
Sometimes Visual Studio can't find all NuGet references for your projects. This is because blueprints require dependencies that must be retrieved from NuGet. When new projects are created, Visual Studio only pulls in local references and not remote references from NuGet. To fix NuGet errors: right-click your references and choose **Restore Packages**.

1. From Visual Studio expand the **File** menu, expand **New**, then choose **Project**.

1. In the **New Project** dialog box, ensure that the **Language**, **Platform**, and **Project type** drop-down boxes are set to "All ..." and enter **aws lambda** in the **Search** field.

1. Select the **AWS Lambda with Tests (.NET Core - C\#)** template.

1. Click **Next** to open the **Configure your new project** dialog.

1. From the **Configure your new project** dialog, enter "ImageRekognition" for the **Name**, then complete the remaining fields to your preference. Choose the **Create** button to proceed to the **Select Blueprint** dialog.

1. From the **Select Blueprint** dialog, choose the **Detect Image Labels** blueprint, then choose **Finish** to create the Visual Studio project.
**Note**
This blueprint provides code for listening to Amazon S3 events and uses Amazon Rekognition to detect labels and add them to the S3 object as tags.

## Reviewing Project Files
<a name="examine-the-files"></a>

The following sections examine these project files:

1. `Function.cs`

1. `aws-lambda-tools-defaults.json`

### 1. Function.cs
<a name="functioncs"></a>

Inside the `Function.cs` file, the first segment of code is the assembly attribute, located at the top of the file. By default, Lambda only accepts input parameters and return types of type `System.IO.Stream`. You must register a serializer to use typed classes for input parameters and return types. The assembly attribute registers the Lambda JSON serializer, which uses `Newtonsoft.Json` to convert streams to typed classes. You can set the serializer at the assembly or method level.

The following is an example of the assembly attribute:

```
// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]
```

The class has two constructors. The first is a default constructor that is used when Lambda invokes your function. This constructor creates the Amazon S3 and Amazon Rekognition service clients. The constructor also retrieves the AWS credentials for these clients from the IAM role you assign to the function when you deploy it. The AWS Region for the clients is set to the region your Lambda function is running in. In this blueprint, you only want to add tags to the Amazon S3 object if the Amazon Rekognition service has a minimum level of confidence about the label. This constructor checks the environment variable `MinConfidence` to determine the acceptable confidence level. You can set this environment variable when you deploy the Lambda function.

The following is an example of the first class constructor in `Function.cs`:

```
public Function()
{
    this.S3Client = new AmazonS3Client();
    this.RekognitionClient = new AmazonRekognitionClient();

    var environmentMinConfidence = System.Environment.GetEnvironmentVariable(MIN_CONFIDENCE_ENVIRONMENT_VARIABLE_NAME);
    if(!string.IsNullOrWhiteSpace(environmentMinConfidence))
    {
        float value;
        if(float.TryParse(environmentMinConfidence, out value))
        {
            this.MinConfidence = value;
            Console.WriteLine($"Setting minimum confidence to {this.MinConfidence}");
        }
        else
        {
            Console.WriteLine($"Failed to parse value {environmentMinConfidence} for minimum confidence. Reverting back to default of {this.MinConfidence}");
        }
    }
    else
    {
        Console.WriteLine($"Using default minimum confidence of {this.MinConfidence}");
    }
}
```

The following example demonstrates how the second constructor can be utilized for testing. The test project configures its own S3 and Rekognition clients and passes them in:

```
public Function(IAmazonS3 s3Client, IAmazonRekognition rekognitionClient, float minConfidence)
{
    this.S3Client = s3Client;
    this.RekognitionClient = rekognitionClient;
    this.MinConfidence = minConfidence;
}
```

The following is an example of the `FunctionHandler` method inside the `Function.cs` file.

```
public async Task FunctionHandler(S3Event input, ILambdaContext context)
{
    foreach(var record in input.Records)
    {
        if(!SupportedImageTypes.Contains(Path.GetExtension(record.S3.Object.Key)))
        {
            Console.WriteLine($"Object {record.S3.Bucket.Name}:{record.S3.Object.Key} is not a supported image type");
            continue;
        }

        Console.WriteLine($"Looking for labels in image {record.S3.Bucket.Name}:{record.S3.Object.Key}");
        var detectResponses = await this.RekognitionClient.DetectLabelsAsync(new DetectLabelsRequest
        {
            MinConfidence = MinConfidence,
            Image = new Image
            {
                S3Object = new Amazon.Rekognition.Model.S3Object
                {
                    Bucket = record.S3.Bucket.Name,
                    Name = record.S3.Object.Key
                }
            }
        });

        var tags = new List();
        foreach(var label in detectResponses.Labels)
        {
            if(tags.Count < 10)
            {
                Console.WriteLine($"\tFound Label {label.Name} with confidence {label.Confidence}");
                tags.Add(new Tag { Key = label.Name, Value = label.Confidence.ToString() });
            }
            else
            {
                Console.WriteLine($"\tSkipped label {label.Name} with confidence {label.Confidence} because maximum number of tags reached");
            }
        }

        await this.S3Client.PutObjectTaggingAsync(new PutObjectTaggingRequest
        {
            BucketName = record.S3.Bucket.Name,
            Key = record.S3.Object.Key,
            Tagging = new Tagging
            {
                TagSet = tags
            }
        });
    }
    return;
}
```

 `FunctionHandler` is the method Lambda calls after it constructs the instance. Notice that the input parameter is of type `S3Event` and not a `Stream`. You can do this because of the registered Lambda JSON serializer. The `S3Event` contains all the information about the event triggered in Amazon S3. The function loops through all the S3 objects that were part of the event and tells Rekognition to detect labels. After the labels are detected, they are added as tags to the S3 object.

**Note**
The code contains calls to `Console.WriteLine()`. When the function is running in Lambda, all calls to `Console.WriteLine()` redirect to Amazon CloudWatch Logs.

### 2. aws-lambda-tools-defaults.json
<a name="toolsdefaults"></a>

The `aws-lambda-tools-defaults.json` file contains default values that the blueprint has set to prepopulate some of the fields in the deployment wizard. It's also helpful in setting command-line options for integration with the .NET Core CLI.

To access the .NET Core CLI integration, navigate to the function's project directory and type **dotnet lambda help**.

**Note**
The function handler indicates what method for Lambda to call in response to the invoked function. The format of this field is: `<assembly-name>::<full-type-name>::<method-name>`. The namespace must be included with the type name.

## Deploy the Function
<a name="deploy-the-function"></a>

The following procedure describes how to deploy your Lambda function.

1. From the **Solution Explorer**, right-click the Lambda project and choose **Publish to AWS Lambda** to open the **Upload to AWS Lambda** window.
**Note**
The preset values are retrieved from the `aws-lambda-tools-defaults.json` file.

1. From the **Upload to AWS Lambda** window, enter a name into the **Function Name** field, then choose the **Next** button to advance to the **Advanced Function Details** window.
**Note**
This example, uses the **Function Name** **ImageRekognition**.
![Upload Lambda Function dialog with fields for package type, runtime, architecture, and function name.](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/lambda-upload-imgrek-03192024.png)

1. From the **Advanced Function Details** window, select an IAM role that gives permission for your code to access your Amazon S3 and Amazon Rekognition resources.
**Note**
If you're following along with this example, select the `AWSLambda_FullAccess` role.

1. Set the environment variable `MinConfidence` to 60, then choose **Upload** to launch the deployment process. The publishing process is complete when the **Function** view displays in the **AWS Explorer**.
![Advanced Function Details dialog with MinConfidence environment variable set to 60.](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/lambda-upload-imgrek-advanced-03192024.png)

1. Following a successful deployment, configure Amazon S3 to send its events to your new function by navigating to the **Event Sources** tab.

1. From the **Event Sources** tab, choose the **Add** button, then select the Amazon S3 bucket to connect with your Lambda function.
**Note**
The bucket must be in the same AWS region as your Lambda function.

## Test the Function
<a name="test-the-function"></a>

Now that the function is deployed and an S3 bucket is configured as an event source for it, open the S3 bucket browser from the **AWS Explorer** for the bucket you selected. Then upload some images.

When the upload is complete, you can confirm that your function ran by looking at the logs from your function view. Or, right-click the images in the bucket browser and choose **Properties**. On the **Tags** tab, you can view the tags that were applied to your object.

![Properties dialog showing metadata tags with tag names such as Dirt Road and Road with numerical values.](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/images/lambda-object-properties.png)
