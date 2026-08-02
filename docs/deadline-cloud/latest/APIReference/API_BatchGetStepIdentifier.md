---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetStepIdentifier.html
---

# BatchGetStepIdentifier
<a name="API_BatchGetStepIdentifier"></a>

The identifiers for a step.

## Contents
<a name="API_BatchGetStepIdentifier_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchGetStepIdentifier-farmId"></a>
The farm ID of the step.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetStepIdentifier-jobId"></a>
The job ID of the step.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetStepIdentifier-queueId"></a>
The queue ID of the step.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-BatchGetStepIdentifier-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetStepIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetStepIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetStepIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetStepIdentifier)
