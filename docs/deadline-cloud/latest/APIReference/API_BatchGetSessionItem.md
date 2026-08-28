---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionItem.html
---

# BatchGetSessionItem
<a name="API_BatchGetSessionItem"></a>

The details of a session returned in a batch get operation.

## Contents
<a name="API_BatchGetSessionItem_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchGetSessionItem-farmId"></a>
The farm ID of the session.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** fleetId **   <a name="deadlinecloud-Type-BatchGetSessionItem-fleetId"></a>
The fleet ID of the session.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetSessionItem-jobId"></a>
The job ID of the session.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** lifecycleStatus **   <a name="deadlinecloud-Type-BatchGetSessionItem-lifecycleStatus"></a>
The life cycle status of the session.
Type: String
Valid Values: `STARTED | UPDATE_IN_PROGRESS | UPDATE_SUCCEEDED | UPDATE_FAILED | ENDED`
Required: Yes

 ** log **   <a name="deadlinecloud-Type-BatchGetSessionItem-log"></a>
The session log.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetSessionItem-queueId"></a>
The queue ID of the session.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionId **   <a name="deadlinecloud-Type-BatchGetSessionItem-sessionId"></a>
The session ID.
Type: String
Pattern: `session-[0-9a-f]{32}`
Required: Yes

 ** startedAt **   <a name="deadlinecloud-Type-BatchGetSessionItem-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: Yes

 ** workerId **   <a name="deadlinecloud-Type-BatchGetSessionItem-workerId"></a>
The worker ID of the session.
Type: String
Pattern: `worker-[0-9a-f]{32}`
Required: Yes

 ** endedAt **   <a name="deadlinecloud-Type-BatchGetSessionItem-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** hostProperties **   <a name="deadlinecloud-Type-BatchGetSessionItem-hostProperties"></a>
The host properties for the session.
Type: [HostPropertiesResponse](API_HostPropertiesResponse.md) object
Required: No

 ** targetLifecycleStatus **   <a name="deadlinecloud-Type-BatchGetSessionItem-targetLifecycleStatus"></a>
The target life cycle status for the session.
Type: String
Valid Values: `ENDED`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-BatchGetSessionItem-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-BatchGetSessionItem-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

 ** workerLog **   <a name="deadlinecloud-Type-BatchGetSessionItem-workerLog"></a>
The worker log for the session.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

## See Also
<a name="API_BatchGetSessionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
