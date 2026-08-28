---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssignedSession.html
---

# AssignedSession
<a name="API_AssignedSession"></a>

The assigned session for the worker.

## Contents
<a name="API_AssignedSession_Contents"></a>

 ** jobId **   <a name="deadlinecloud-Type-AssignedSession-jobId"></a>
The job ID for the assigned session.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** logConfiguration **   <a name="deadlinecloud-Type-AssignedSession-logConfiguration"></a>
The log configuration for the worker's assigned session.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-AssignedSession-queueId"></a>
The queue ID of the assigned session.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionActions **   <a name="deadlinecloud-Type-AssignedSession-sessionActions"></a>
The session actions to apply to the assigned session.
Type: Array of [AssignedSessionAction](API_AssignedSessionAction.md) objects
Required: Yes

## See Also
<a name="API_AssignedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
