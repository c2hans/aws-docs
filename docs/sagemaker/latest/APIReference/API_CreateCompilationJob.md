---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html
---

# CreateCompilationJob
<a name="API_CreateCompilationJob"></a>

Starts a model compilation job. After the model has been compiled, Amazon SageMaker AI saves the resulting model artifacts to an Amazon Simple Storage Service (Amazon S3) bucket that you specify.

If you choose to host your model using Amazon SageMaker AI hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts with AWS IoT Greengrass. In that case, deploy them as an ML resource.

In the request body, you provide the following:
+ A name for the compilation job
+  Information about the input model artifacts
+ The output location for the compiled model and the device (target) that the model runs on
+ The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker AI assumes to perform the model compilation job.

You can also provide a `Tag` to track the model compilation job's resource use and costs. The response body contains the `CompilationJobArn` for the compiled job.

To stop a model compilation job, use [StopCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopCompilationJob.html). To get information about a particular model compilation job, use [DescribeCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html). To get information about multiple model compilation jobs, use [ListCompilationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html).

## Request Syntax
<a name="API_CreateCompilationJob_RequestSyntax"></a>

```
{
   "CompilationJobName": "{{string}}",
   "InputConfig": {
      "DataInputConfig": "{{string}}",
      "Framework": "{{string}}",
      "FrameworkVersion": "{{string}}",
      "S3Uri": "{{string}}"
   },
   "ModelPackageVersionArn": "{{string}}",
   "OutputConfig": {
      "CompilerOptions": "{{string}}",
      "KmsKeyId": "{{string}}",
      "S3OutputLocation": "{{string}}",
      "TargetDevice": "{{string}}",
      "TargetPlatform": {
         "Accelerator": "{{string}}",
         "Arch": "{{string}}",
         "Os": "{{string}}"
      }
   },
   "RoleArn": "{{string}}",
   "StoppingCondition": {
      "MaxPendingTimeInSeconds": {{number}},
      "MaxRuntimeInSeconds": {{number}},
      "MaxWaitTimeInSeconds": {{number}}
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateCompilationJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CompilationJobName](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-CompilationJobName"></a>
A name for the model compilation job. The name must be unique within the AWS Region and within your AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [InputConfig](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-InputConfig"></a>
Provides information about the location of input model artifacts, the name and shape of the expected data inputs, and the framework in which the model was trained.
Type: [InputConfig](API_InputConfig.md) object
Required: No

 ** [ModelPackageVersionArn](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-ModelPackageVersionArn"></a>
The Amazon Resource Name (ARN) of a versioned model package. Provide either a `ModelPackageVersionArn` or an `InputConfig` object in the request syntax. The presence of both objects in the `CreateCompilationJob` request will return an exception.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package/[\S]{1,2048}`
Required: No

 ** [OutputConfig](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-OutputConfig"></a>
Provides information about the output location for the compiled model and the target device the model runs on.
Type: [OutputConfig](API_OutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.
During model compilation, Amazon SageMaker AI needs your permission to:
+ Read input data from an S3 bucket
+ Write model artifacts to an S3 bucket
+ Write logs to Amazon CloudWatch Logs
+ Publish metrics to Amazon CloudWatch
You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the `iam:PassRole` permission. For more information, see [Amazon SageMaker AI Roles.](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingCondition](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-StoppingCondition"></a>
Specifies a limit to how long a model compilation job can run. When the job reaches the time limit, Amazon SageMaker AI ends the compilation job. Use this API to cap model training costs.
Type: [StoppingCondition](API_StoppingCondition.md) object
Required: Yes

 ** [Tags](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [VpcConfig](#API_CreateCompilationJob_RequestSyntax) **   <a name="sagemaker-CreateCompilationJob-request-VpcConfig"></a>
A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want your compilation job to connect to. Control access to your models by configuring the VPC. For more information, see [Protect Compilation Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-vpc.html).
Type: [NeoVpcConfig](API_NeoVpcConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateCompilationJob_ResponseSyntax"></a>

```
{
   "CompilationJobArn": "string"
}
```

## Response Elements
<a name="API_CreateCompilationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompilationJobArn](#API_CreateCompilationJob_ResponseSyntax) **   <a name="sagemaker-CreateCompilationJob-response-CompilationJobArn"></a>
If the action is successful, the service sends back an HTTP 200 response. Amazon SageMaker AI returns the following data in JSON format:
+  `CompilationJobArn`: The Amazon Resource Name (ARN) of the compiled job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:compilation-job/.*`

## Errors
<a name="API_CreateCompilationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateCompilationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateCompilationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateCompilationJob)
