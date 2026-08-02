---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SessionSummary.html
---

# SessionSummary
<a name="API_SessionSummary"></a>

The summary of a session.

## Contents
<a name="API_SessionSummary_Contents"></a>

 ** fleetId **   <a name="deadlinecloud-Type-SessionSummary-fleetId"></a>
The fleet ID.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** lifecycleStatus **   <a name="deadlinecloud-Type-SessionSummary-lifecycleStatus"></a>
The life cycle status for the session.
Type: String
Valid Values: `STARTED | UPDATE_IN_PROGRESS | UPDATE_SUCCEEDED | UPDATE_FAILED | ENDED`
Required: Yes

 ** sessionId **   <a name="deadlinecloud-Type-SessionSummary-sessionId"></a>
The session ID.
Type: String
Pattern: `session-[0-9a-f]{32}`
Required: Yes

 ** startedAt **   <a name="deadlinecloud-Type-SessionSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: Yes

 ** workerId **   <a name="deadlinecloud-Type-SessionSummary-workerId"></a>
The worker ID.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

 ** endedAt **   <a name="deadlinecloud-Type-SessionSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** targetLifecycleStatus **   <a name="deadlinecloud-Type-SessionSummary-targetLifecycleStatus"></a>
The target life cycle status for the session.
Type: String
Valid Values: `ENDED`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-SessionSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-SessionSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionSummary)
