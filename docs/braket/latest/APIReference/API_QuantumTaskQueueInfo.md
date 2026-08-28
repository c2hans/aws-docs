---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_QuantumTaskQueueInfo.html
---

# QuantumTaskQueueInfo
<a name="API_QuantumTaskQueueInfo"></a>

The queue information for the specified quantum task.

## Contents
<a name="API_QuantumTaskQueueInfo_Contents"></a>

 ** position **   <a name="braket-Type-QuantumTaskQueueInfo-position"></a>
Current position of the quantum task in the quantum tasks queue.
Type: String
Required: Yes

 ** queue **   <a name="braket-Type-QuantumTaskQueueInfo-queue"></a>
The name of the queue.
Type: String
Valid Values: `QUANTUM_TASKS_QUEUE | JOBS_QUEUE`
Required: Yes

 ** message **   <a name="braket-Type-QuantumTaskQueueInfo-message"></a>
Optional. Provides more information about the queue position. For example, if the quantum task is complete and no longer in the queue, the message field contains that information.
Type: String
Required: No

 ** queuePriority **   <a name="braket-Type-QuantumTaskQueueInfo-queuePriority"></a>
Optional. Specifies the priority of the queue. Quantum tasks in a priority queue are processed before the quantum tasks in a normal queue.
Type: String
Valid Values: `Normal | Priority`
Required: No

## See Also
<a name="API_QuantumTaskQueueInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/QuantumTaskQueueInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/QuantumTaskQueueInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/QuantumTaskQueueInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
