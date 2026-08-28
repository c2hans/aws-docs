---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_WorkerSessionSummary.html
---

# WorkerSessionSummary
<a name="API_WorkerSessionSummary"></a>

Summarizes the session for a particular worker.

## Contents
<a name="API_WorkerSessionSummary_Contents"></a>

 ** jobId **   <a name="deadlinecloud-Type-WorkerSessionSummary-jobId"></a>
The job ID for the job associated with the worker's session.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** lifecycleStatus **   <a name="deadlinecloud-Type-WorkerSessionSummary-lifecycleStatus"></a>
The life cycle status for the worker's session.
Type: String
Valid Values: `STARTED | UPDATE_IN_PROGRESS | UPDATE_SUCCEEDED | UPDATE_FAILED | ENDED`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-WorkerSessionSummary-queueId"></a>
The queue ID for the queue associated to the worker.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionId **   <a name="deadlinecloud-Type-WorkerSessionSummary-sessionId"></a>
The session ID for the session action.
Type: String
Pattern: `session-[0-9a-f]{32}`
Required: Yes

 ** startedAt **   <a name="deadlinecloud-Type-WorkerSessionSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: Yes

 ** endedAt **   <a name="deadlinecloud-Type-WorkerSessionSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** targetLifecycleStatus **   <a name="deadlinecloud-Type-WorkerSessionSummary-targetLifecycleStatus"></a>
The life cycle status
Type: String
Valid Values: `ENDED`
Required: No

## See Also
<a name="API_WorkerSessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/WorkerSessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/WorkerSessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/WorkerSessionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
