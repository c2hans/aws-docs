---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobSummary.html
---

# LabelingJobSummary
<a name="API_LabelingJobSummary"></a>

Provides summary information about a labeling job.

## Contents
<a name="API_LabelingJobSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-LabelingJobSummary-CreationTime"></a>
The date and time that the job was created (timestamp).
Type: Timestamp
Required: Yes

 ** LabelCounters **   <a name="sagemaker-Type-LabelingJobSummary-LabelCounters"></a>
Counts showing the progress of the labeling job.
Type: [LabelCounters](API_LabelCounters.md) object
Required: Yes

 ** LabelingJobArn **   <a name="sagemaker-Type-LabelingJobSummary-LabelingJobArn"></a>
The Amazon Resource Name (ARN) assigned to the labeling job when it was created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`
Required: Yes

 ** LabelingJobName **   <a name="sagemaker-Type-LabelingJobSummary-LabelingJobName"></a>
The name of the labeling job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** LabelingJobStatus **   <a name="sagemaker-Type-LabelingJobSummary-LabelingJobStatus"></a>
The current status of the labeling job.
Type: String
Valid Values: `Initializing | InProgress | Completed | Failed | Stopping | Stopped`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-LabelingJobSummary-LastModifiedTime"></a>
The date and time that the job was last modified (timestamp).
Type: Timestamp
Required: Yes

 ** WorkteamArn **   <a name="sagemaker-Type-LabelingJobSummary-WorkteamArn"></a>
The Amazon Resource Name (ARN) of the work team assigned to the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`
Required: Yes

 ** AnnotationConsolidationLambdaArn **   <a name="sagemaker-Type-LabelingJobSummary-AnnotationConsolidationLambdaArn"></a>
The Amazon Resource Name (ARN) of the Lambda function used to consolidate the annotations from individual workers into a label for a data object. For more information, see [Annotation Consolidation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:lambda:[a-z0-9\-]*:[0-9]{12}:function:.*`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-LabelingJobSummary-FailureReason"></a>
If the `LabelingJobStatus` field is `Failed`, this field contains a description of the error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** InputConfig **   <a name="sagemaker-Type-LabelingJobSummary-InputConfig"></a>
Input configuration for the labeling job.
Type: [LabelingJobInputConfig](API_LabelingJobInputConfig.md) object
Required: No

 ** LabelingJobOutput **   <a name="sagemaker-Type-LabelingJobSummary-LabelingJobOutput"></a>
The location of the output produced by the labeling job.
Type: [LabelingJobOutput](API_LabelingJobOutput.md) object
Required: No

 ** PreHumanTaskLambdaArn **   <a name="sagemaker-Type-LabelingJobSummary-PreHumanTaskLambdaArn"></a>
The Amazon Resource Name (ARN) of a Lambda function. The function is run before each data object is sent to a worker.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:lambda:[a-z0-9\-]*:[0-9]{12}:function:.*`
Required: No

## See Also
<a name="API_LabelingJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobSummary)
