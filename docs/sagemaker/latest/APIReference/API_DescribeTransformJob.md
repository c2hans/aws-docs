---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTransformJob.html
---

# DescribeTransformJob
<a name="API_DescribeTransformJob"></a>

Returns information about a transform job.

## Request Syntax
<a name="API_DescribeTransformJob_RequestSyntax"></a>

```
{
   "TransformJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTransformJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TransformJobName](#API_DescribeTransformJob_RequestSyntax) **   <a name="sagemaker-DescribeTransformJob-request-TransformJobName"></a>
The name of the transform job that you want to view details of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeTransformJob_ResponseSyntax"></a>

```
{
   "AutoMLJobArn": "string",
   "BatchStrategy": "string",
   "CreationTime": number,
   "DataCaptureConfig": {
      "DestinationS3Uri": "string",
      "GenerateInferenceId": boolean,
      "KmsKeyId": "string"
   },
   "DataProcessing": {
      "InputFilter": "string",
      "JoinSource": "string",
      "OutputFilter": "string"
   },
   "Environment": {
      "string" : "string"
   },
   "ExperimentConfig": {
      "ExperimentName": "string",
      "RunName": "string",
      "TrialComponentDisplayName": "string",
      "TrialName": "string"
   },
   "FailureReason": "string",
   "LabelingJobArn": "string",
   "MaxConcurrentTransforms": number,
   "MaxPayloadInMB": number,
   "ModelClientConfig": {
      "InvocationsMaxRetries": number,
      "InvocationsTimeoutInSeconds": number
   },
   "ModelName": "string",
   "TransformEndTime": number,
   "TransformInput": {
      "CompressionType": "string",
      "ContentType": "string",
      "DataSource": {
         "S3DataSource": {
            "S3DataType": "string",
            "S3Uri": "string"
         }
      },
      "SplitType": "string"
   },
   "TransformJobArn": "string",
   "TransformJobName": "string",
   "TransformJobStatus": "string",
   "TransformOutput": {
      "Accept": "string",
      "AssembleWith": "string",
      "KmsKeyId": "string",
      "S3OutputPath": "string"
   },
   "TransformResources": {
      "InstanceCount": number,
      "InstanceType": "string",
      "TransformAmiVersion": "string",
      "VolumeKmsKeyId": "string"
   },
   "TransformStartTime": number
}
```

## Response Elements
<a name="API_DescribeTransformJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMLJobArn](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-AutoMLJobArn"></a>
The Amazon Resource Name (ARN) of the AutoML transform job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`

 ** [BatchStrategy](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-BatchStrategy"></a>
Specifies the number of records to include in a mini-batch for an HTTP inference request. A *record* ** is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.
To enable the batch strategy, you must set `SplitType` to `Line`, `RecordIO`, or `TFRecord`.
Type: String
Valid Values: `MultiRecord | SingleRecord`

 ** [CreationTime](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-CreationTime"></a>
A timestamp that shows when the transform Job was created.
Type: Timestamp

 ** [DataCaptureConfig](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-DataCaptureConfig"></a>
Configuration to control how SageMaker captures inference data.
Type: [BatchDataCaptureConfig](API_BatchDataCaptureConfig.md) object

 ** [DataProcessing](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-DataProcessing"></a>
The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html).
Type: [DataProcessing](API_DataProcessing.md) object

 ** [Environment](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-Environment"></a>
The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 16 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]{0,1023}`
Value Length Constraints: Minimum length of 0. Maximum length of 10240.
Value Pattern: `[\S\s]*`

 ** [ExperimentConfig](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object

 ** [FailureReason](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-FailureReason"></a>
If the transform job failed, `FailureReason` describes why it failed. A transform job creates a log file, which includes error messages, and stores it as an Amazon S3 object. For more information, see [Log Amazon SageMaker Events with Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LabelingJobArn](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-LabelingJobArn"></a>
The Amazon Resource Name (ARN) of the Amazon SageMaker Ground Truth labeling job that created the transform or training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`

 ** [MaxConcurrentTransforms](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-MaxConcurrentTransforms"></a>
The maximum number of parallel requests on each instance node that can be launched in a transform job. The default value is 1.
Type: Integer
Valid Range: Minimum value of 0.

 ** [MaxPayloadInMB](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-MaxPayloadInMB"></a>
The maximum payload size, in MB, used in the transform job.
Type: Integer
Valid Range: Minimum value of 0.

 ** [ModelClientConfig](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-ModelClientConfig"></a>
The timeout and maximum number of retries for processing a transform job invocation.
Type: [ModelClientConfig](API_ModelClientConfig.md) object

 ** [ModelName](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-ModelName"></a>
The name of the model used in the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`

 ** [TransformEndTime](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformEndTime"></a>
Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of `TransformStartTime`.
Type: Timestamp

 ** [TransformInput](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformInput"></a>
Describes the dataset to be transformed and the Amazon S3 location where it is stored.
Type: [TransformInput](API_TransformInput.md) object

 ** [TransformJobArn](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformJobArn"></a>
The Amazon Resource Name (ARN) of the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:transform-job/.*`

 ** [TransformJobName](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformJobName"></a>
The name of the transform job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [TransformJobStatus](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformJobStatus"></a>
The status of the transform job. If the transform job failed, the reason is returned in the `FailureReason` field.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`

 ** [TransformOutput](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformOutput"></a>
Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
Type: [TransformOutput](API_TransformOutput.md) object

 ** [TransformResources](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformResources"></a>
Describes the resources, including ML instance types and ML instance count, to use for the transform job.
Type: [TransformResources](API_TransformResources.md) object

 ** [TransformStartTime](#API_DescribeTransformJob_ResponseSyntax) **   <a name="sagemaker-DescribeTransformJob-response-TransformStartTime"></a>
Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of `TransformEndTime`.
Type: Timestamp

## Errors
<a name="API_DescribeTransformJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTransformJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTransformJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTransformJob)
