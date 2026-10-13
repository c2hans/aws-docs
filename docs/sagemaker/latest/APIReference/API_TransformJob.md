---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformJob.html
---

# TransformJob
<a name="API_TransformJob"></a>

A batch transform job. For information about SageMaker batch transform, see [Use Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html).

## Contents
<a name="API_TransformJob_Contents"></a>

 ** AutoMLJobArn **   <a name="sagemaker-Type-TransformJob-AutoMLJobArn"></a>
The Amazon Resource Name (ARN) of the AutoML job that created the transform job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:automl-job/.*`
Required: No

 ** BatchStrategy **   <a name="sagemaker-Type-TransformJob-BatchStrategy"></a>
Specifies the number of records to include in a mini-batch for an HTTP inference request. A record is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.
Type: String
Valid Values: `MultiRecord | SingleRecord`
Required: No

 ** CreationTime **   <a name="sagemaker-Type-TransformJob-CreationTime"></a>
A timestamp that shows when the transform Job was created.
Type: Timestamp
Required: No

 ** DataCaptureConfig **   <a name="sagemaker-Type-TransformJob-DataCaptureConfig"></a>
Configuration to control how SageMaker captures inference data for batch transform jobs.
Type: [BatchDataCaptureConfig](API_BatchDataCaptureConfig.md) object
Required: No

 ** DataProcessing **   <a name="sagemaker-Type-TransformJob-DataProcessing"></a>
The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html).
Type: [DataProcessing](API_DataProcessing.md) object
Required: No

 ** Environment **   <a name="sagemaker-Type-TransformJob-Environment"></a>
The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 16 items.
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]{0,1023}`
Value Length Constraints: Minimum length of 0. Maximum length of 10240.
Value Pattern: `[\S\s]*`
Required: No

 ** ExperimentConfig **   <a name="sagemaker-Type-TransformJob-ExperimentConfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
Type: [ExperimentConfig](API_ExperimentConfig.md) object
Required: No

 ** FailureReason **   <a name="sagemaker-Type-TransformJob-FailureReason"></a>
If the transform job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LabelingJobArn **   <a name="sagemaker-Type-TransformJob-LabelingJobArn"></a>
The Amazon Resource Name (ARN) of the labeling job that created the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`
Required: No

 ** MaxConcurrentTransforms **   <a name="sagemaker-Type-TransformJob-MaxConcurrentTransforms"></a>
The maximum number of parallel requests that can be sent to each instance in a transform job. If `MaxConcurrentTransforms` is set to 0 or left unset, SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is 1. For built-in algorithms, you don't need to set a value for `MaxConcurrentTransforms`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxPayloadInMB **   <a name="sagemaker-Type-TransformJob-MaxPayloadInMB"></a>
The maximum allowed size of the payload, in MB. A payload is the data portion of a record (without metadata). The value in `MaxPayloadInMB` must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is 6 MB. For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0. This feature works only in supported algorithms. Currently, SageMaker built-in algorithms do not support HTTP chunked encoding.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ModelClientConfig **   <a name="sagemaker-Type-TransformJob-ModelClientConfig"></a>
Configures the timeout and maximum number of retries for processing a transform job invocation.
Type: [ModelClientConfig](API_ModelClientConfig.md) object
Required: No

 ** ModelName **   <a name="sagemaker-Type-TransformJob-ModelName"></a>
The name of the model associated with the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: No

 ** Tags **   <a name="sagemaker-Type-TransformJob-Tags"></a>
A list of tags associated with the transform job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** TransformEndTime **   <a name="sagemaker-Type-TransformJob-TransformEndTime"></a>
Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of `TransformStartTime`.
Type: Timestamp
Required: No

 ** TransformInput **   <a name="sagemaker-Type-TransformJob-TransformInput"></a>
Describes the input source of a transform job and the way the transform job consumes it.
Type: [TransformInput](API_TransformInput.md) object
Required: No

 ** TransformJobArn **   <a name="sagemaker-Type-TransformJob-TransformJobArn"></a>
The Amazon Resource Name (ARN) of the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:transform-job/.*`
Required: No

 ** TransformJobName **   <a name="sagemaker-Type-TransformJob-TransformJobName"></a>
The name of the transform job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** TransformJobStatus **   <a name="sagemaker-Type-TransformJob-TransformJobStatus"></a>
The status of the transform job.
Transform job statuses are:
+  `InProgress` - The job is in progress.
+  `Completed` - The job has completed.
+  `Failed` - The transform job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTransformJob` call.
+  `Stopping` - The transform job is stopping.
+  `Stopped` - The transform job has stopped.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: No

 ** TransformOutput **   <a name="sagemaker-Type-TransformJob-TransformOutput"></a>
Describes the results of a transform job.
Type: [TransformOutput](API_TransformOutput.md) object
Required: No

 ** TransformResources **   <a name="sagemaker-Type-TransformJob-TransformResources"></a>
Describes the resources, including ML instance types and ML instance count, to use for transform job.
Type: [TransformResources](API_TransformResources.md) object
Required: No

 ** TransformStartTime **   <a name="sagemaker-Type-TransformJob-TransformStartTime"></a>
Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of `TransformEndTime`.
Type: Timestamp
Required: No

## See Also
<a name="API_TransformJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TransformJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TransformJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TransformJob)
