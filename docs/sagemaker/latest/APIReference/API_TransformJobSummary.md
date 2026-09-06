---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformJobSummary.html
---

# TransformJobSummary
<a name="API_TransformJobSummary"></a>

Provides a summary of a transform job. Multiple `TransformJobSummary` objects are returned as a list after in response to a [ListTransformJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTransformJobs.html) call.

## Contents
<a name="API_TransformJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-TransformJobSummary-CreationTime"></a>
A timestamp that shows when the transform Job was created.
Type: Timestamp
Required: Yes

 ** TransformJobArn **   <a name="sagemaker-Type-TransformJobSummary-TransformJobArn"></a>
The Amazon Resource Name (ARN) of the transform job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:transform-job/.*`
Required: Yes

 ** TransformJobName **   <a name="sagemaker-Type-TransformJobSummary-TransformJobName"></a>
The name of the transform job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TransformJobStatus **   <a name="sagemaker-Type-TransformJobSummary-TransformJobStatus"></a>
The status of the transform job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-TransformJobSummary-FailureReason"></a>
If the transform job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-TransformJobSummary-LastModifiedTime"></a>
Indicates when the transform job was last modified.
Type: Timestamp
Required: No

 ** TransformEndTime **   <a name="sagemaker-Type-TransformJobSummary-TransformEndTime"></a>
Indicates when the transform job ends on compute instances. For successful jobs and stopped jobs, this is the exact time recorded after the results are uploaded. For failed jobs, this is when Amazon SageMaker detected that the job failed.
Type: Timestamp
Required: No

## See Also
<a name="API_TransformJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TransformJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TransformJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TransformJobSummary)
