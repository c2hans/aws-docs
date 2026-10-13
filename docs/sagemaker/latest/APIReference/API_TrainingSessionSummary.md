---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingSessionSummary.html
---

# TrainingSessionSummary
<a name="API_TrainingSessionSummary"></a>

Contains summary information about a training session.

## Contents
<a name="API_TrainingSessionSummary_Contents"></a>

 ** CreationTime **   <a name="sagemaker-Type-TrainingSessionSummary-CreationTime"></a>
The date and time that the training session was created.
Type: Timestamp
Required: Yes

 ** TrainingSessionArn **   <a name="sagemaker-Type-TrainingSessionSummary-TrainingSessionArn"></a>
The Amazon Resource Name (ARN) of the training session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:training-session/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** TrainingSessionStatus **   <a name="sagemaker-Type-TrainingSessionSummary-TrainingSessionStatus"></a>
The current status of the training session.
Type: String
Valid Values: `Created | Blocked | Running | Failed | Scheduled | Stopping | Stopped | Expired | Deleting | DeletionFailed`
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-TrainingSessionSummary-LastModifiedTime"></a>
The date and time that the training session was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_TrainingSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingSessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingSessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingSessionSummary)
