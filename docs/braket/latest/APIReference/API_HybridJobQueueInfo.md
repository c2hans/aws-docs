---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_HybridJobQueueInfo.html
---

# HybridJobQueueInfo
<a name="API_HybridJobQueueInfo"></a>

Information about the queue for a specified hybrid job.

## Contents
<a name="API_HybridJobQueueInfo_Contents"></a>

 ** position **   <a name="braket-Type-HybridJobQueueInfo-position"></a>
Current position of the hybrid job in the jobs queue.
Type: String
Required: Yes

 ** queue **   <a name="braket-Type-HybridJobQueueInfo-queue"></a>
The name of the queue.
Type: String
Valid Values: `QUANTUM_TASKS_QUEUE | JOBS_QUEUE`
Required: Yes

 ** message **   <a name="braket-Type-HybridJobQueueInfo-message"></a>
Optional. Provides more information about the queue position. For example, if the hybrid job is complete and no longer in the queue, the message field contains that information.
Type: String
Required: No

## See Also
<a name="API_HybridJobQueueInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/HybridJobQueueInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/HybridJobQueueInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/HybridJobQueueInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
