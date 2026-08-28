---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SessionActionSummary.html
---

# SessionActionSummary
<a name="API_SessionActionSummary"></a>

The details of a session action.

## Contents
<a name="API_SessionActionSummary_Contents"></a>

 ** definition **   <a name="deadlinecloud-Type-SessionActionSummary-definition"></a>
The session action definition.
Type: [SessionActionDefinitionSummary](API_SessionActionDefinitionSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sessionActionId **   <a name="deadlinecloud-Type-SessionActionSummary-sessionActionId"></a>
The session action ID.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

 ** status **   <a name="deadlinecloud-Type-SessionActionSummary-status"></a>
The status of the session action.
Type: String
Valid Values: `ASSIGNED | RUNNING | CANCELING | SUCCEEDED | FAILED | INTERRUPTED | CANCELED | NEVER_ATTEMPTED | SCHEDULED | RECLAIMING | RECLAIMED`
Required: Yes

 ** endedAt **   <a name="deadlinecloud-Type-SessionActionSummary-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** manifests **   <a name="deadlinecloud-Type-SessionActionSummary-manifests"></a>
The list of manifest properties that describe file attachments for the task run.
Type: Array of [TaskRunManifestPropertiesResponse](API_TaskRunManifestPropertiesResponse.md) objects
Required: No

 ** progressPercent **   <a name="deadlinecloud-Type-SessionActionSummary-progressPercent"></a>
The completion percentage for the session action.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-SessionActionSummary-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** workerUpdatedAt **   <a name="deadlinecloud-Type-SessionActionSummary-workerUpdatedAt"></a>
The Linux timestamp of the last date and time that the session action was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_SessionActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SessionActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SessionActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SessionActionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
