---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_JobSecondaryStatusTransition.html
---

# JobSecondaryStatusTransition
<a name="API_JobSecondaryStatusTransition"></a>

Represents a secondary status transition for a job. Jobs progress through multiple secondary statuses during execution. Each transition records the status, start time, optional end time, and an optional message with additional details.

## Contents
<a name="API_JobSecondaryStatusTransition_Contents"></a>

 ** Status **   <a name="sagemaker-Type-JobSecondaryStatusTransition-Status"></a>
The secondary status of the job at this transition point.
Type: String
Valid Values: `Starting | Downloading | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Interrupted | Failed | Completed | Restarting | Pending | Evaluating | Deleting | DeleteFailed`
Required: Yes

 ** StatusMessage **   <a name="sagemaker-Type-JobSecondaryStatusTransition-StatusMessage"></a>
A detailed message about the status transition.
Type: String
Required: No

## See Also
<a name="API_JobSecondaryStatusTransition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/JobSecondaryStatusTransition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/JobSecondaryStatusTransition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/JobSecondaryStatusTransition)
