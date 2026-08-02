---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html
---

# CreateTransformJob
<a name="API_CreateTransformJob"></a>

Starts a transform job. A transform job uses a trained model to get inferences on a dataset and saves these results to an Amazon S3 location that you specify.

To perform batch transformations, you create a transform job and use the data that you have readily available.

In the request body, you provide the following:
+  `TransformJobName` - Identifies the transform job. The name must be unique within an AWS Region in an AWS account.
+  `ModelName` - Identifies the model to use. `ModelName` must be the name of an existing Amazon SageMaker model in the same AWS Region and AWS account. For information on creating a model, see [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html).
+  `TransformInput` - Describes the dataset to be transformed and the Amazon S3 location where it is stored.
+  `TransformOutput` - Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
+  `TransformResources` - Identifies the ML compute instances and AMI image versions for the transform job.

For more information about how batch transformation works, see [Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html).

## Request Syntax
<a name="API_CreateTransformJob_RequestSyntax"></a>

```
{
   "BatchStrategy": "{{string}}",
   "DataCaptureConfig": {
      "DestinationS3Uri": "{{string}}",
      "GenerateInferenceId": {{boolean}},
      "KmsKeyId": "{{string}}"
   },
   "DataProcessing": {
      "InputFilter": "{{string}}",
      "JoinSource": "{{string}}",
      "OutputFilter": "{{string}}"
   },
   "Environment": {
      "{{string}}" : "{{string}}"
   },
   "ExperimentConfig": {
      "ExperimentName": "{{string}}",
      "RunName": "{{string}}",
      "TrialComponentDisplayName": "{{string}}",
      "TrialName": "{{string}}"
   },
   "MaxConcurrentTransforms": {{number}},
   "MaxPayloadInMB": {{number}},
   "ModelClientConfig": {
      "InvocationsMaxRetries": {{number}},
      "InvocationsTimeoutInSeconds": {{number}}
   },
   "ModelName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TransformInput": {
      "CompressionType": "{{string}}",
      "ContentType": "{{string}}",
      "DataSource": {
         "S3DataSource": {
            "S3DataType": "{{string}}",
            "S3Uri": "{{string}}"
         }
      },
      "SplitType": "{{string}}"
   },
   "TransformJobName": "{{string}}",
   "TransformOutput": {
      "Accept": "{{string}}",
      "AssembleWith": "{{string}}",
      "KmsKeyId": "{{string}}",
      "S3OutputPath": "{{string}}"
   },
   "TransformResources": {
      "InstanceCount": {{number}},
      "InstanceType": "{{string}}",
      "TransformAmiVersion": "{{string}}",
      "VolumeKmsKeyId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateTransformJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BatchStrategy](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-BatchStrategy"></a>
Specifies the number of records to include in a mini-batch for an HTTP inference request. A *record* ** is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.
To enable the batch strategy, you must set the `SplitType` property to `Line`, `RecordIO`, or `TFRecord`.
To use only one record when making an HTTP invocation request to a container, set `BatchStrategy` to `SingleRecord` and `SplitType` to `Line`.
To fit as many records in a mini-batch as can fit within the `MaxPayloadInMB` limit, set `BatchStrategy` to `MultiRecord` and `SplitType` to `Line`.
Type: String
Valid Values: `MultiRecord | SingleRecord`
Required: No

 ** [DataCaptureConfig](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-DataCaptureConfig"></a>
Configuration to control how SageMaker captures inference data.
Type: [BatchDataCaptureConfig](API_BatchDataCaptureConfig.md) object
Required: No

 ** [DataProcessing](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-DataProcessing"></a>
The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html).
Type: [DataProcessing](API_DataProcessing.md) object
Required: No

 ** [Environment](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-Environment"></a>
The environment variables to set in the Docker container. Don't include any sensitive data in your environment variables. We support up to 16 key and values entries in the map.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 16 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]{0,1023}`
Value Length Constraints: Minimum length of 0. Maximum length of 10240.
Value Pattern: `[\S\s]*`
Required: No

 ** [ExperimentConfig](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object
Required: No

 ** [MaxConcurrentTransforms](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-MaxConcurrentTransforms"></a>
The maximum number of parallel requests that can be sent to each instance in a transform job. If `MaxConcurrentTransforms` is set to `0` or left unset, Amazon SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is `1`. For more information on execution-parameters, see [How Containers Serve Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-batch-code.html#your-algorithms-batch-code-how-containe-serves-requests). For built-in algorithms, you don't need to set a value for `MaxConcurrentTransforms`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [MaxPayloadInMB](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-MaxPayloadInMB"></a>
The maximum allowed size of the payload, in MB. A *payload* is the data portion of a record (without metadata). The value in `MaxPayloadInMB` must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is `6` MB.
The value of `MaxPayloadInMB` cannot be greater than 100 MB. If you specify the `MaxConcurrentTransforms` parameter, the value of `(MaxConcurrentTransforms * MaxPayloadInMB)` also cannot exceed 100 MB.
For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to `0`. This feature works only in supported algorithms. Currently, Amazon SageMaker built-in algorithms do not support HTTP chunked encoding.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [ModelClientConfig](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-ModelClientConfig"></a>
Configures the timeout and maximum number of retries for processing a transform job invocation.
Type: [ModelClientConfig](API_ModelClientConfig.md) object
Required: No

 ** [ModelName](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-ModelName"></a>
The name of the model that you want to use for the transform job. `ModelName` must be the name of an existing Amazon SageMaker model within an AWS Region in an AWS account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

 ** [Tags](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-Tags"></a>
(Optional) An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TransformInput](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-TransformInput"></a>
Describes the input source and the way the transform job consumes it.
Type: [TransformInput](API_TransformInput.md) object
Required: Yes

 ** [TransformJobName](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-TransformJobName"></a>
The name of the transform job. The name must be unique within an AWS Region in an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [TransformOutput](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-TransformOutput"></a>
Describes the results of the transform job.
Type: [TransformOutput](API_TransformOutput.md) object
Required: Yes

 ** [TransformResources](#API_CreateTransformJob_RequestSyntax) **   <a name="sagemaker-CreateTransformJob-request-TransformResources"></a>
Describes the resources, including ML instance types and ML instance count, to use for the transform job.
Type: [TransformResources](API_TransformResources.md) object
Required: Yes

## Response Syntax
<a name="API_CreateTransformJob_ResponseSyntax"></a>

```
{
   "TransformJobArn": "string"
}
```

## Response Elements
<a name="API_CreateTransformJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransformJobArn](#API_CreateTransformJob_ResponseSyntax) **   <a name="sagemaker-CreateTransformJob-response-TransformJobArn"></a>
The Amazon Resource Name (ARN) of the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:transform-job/.*`

## Errors
<a name="API_CreateTransformJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateTransformJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateTransformJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateTransformJob)
