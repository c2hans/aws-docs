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

 ** metadata **   <a name="deadlinecloud-Type-AssignedSession-metadata"></a>
Key-value hints that the service provides to guide how the session runs. This value is used by the worker agent.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_AssignedSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSession)
