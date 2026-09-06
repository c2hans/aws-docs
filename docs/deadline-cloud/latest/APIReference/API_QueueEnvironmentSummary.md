---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_QueueEnvironmentSummary.html
---

# QueueEnvironmentSummary
<a name="API_QueueEnvironmentSummary"></a>

The summary of a queue environment.

## Contents
<a name="API_QueueEnvironmentSummary_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-QueueEnvironmentSummary-name"></a>
The name of the queue environment.
Type: String
Required: Yes

 ** priority **   <a name="deadlinecloud-Type-QueueEnvironmentSummary-priority"></a>
The queue environment's priority.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: Yes

 ** queueEnvironmentId **   <a name="deadlinecloud-Type-QueueEnvironmentSummary-queueEnvironmentId"></a>
The queue environment ID.
Type: String
Pattern: `queueenv-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_QueueEnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueEnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueEnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueEnvironmentSummary)
