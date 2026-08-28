---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ResourceSyncAttempt.html
---

# ResourceSyncAttempt
<a name="API_ResourceSyncAttempt"></a>

Information about a resource sync attempt.

## Contents
<a name="API_ResourceSyncAttempt_Contents"></a>

 ** Events **   <a name="codeconnections-Type-ResourceSyncAttempt-Events"></a>
The events related to a resource sync attempt.
Type: Array of [ResourceSyncEvent](API_ResourceSyncEvent.md) objects
Required: Yes

 ** InitialRevision **   <a name="codeconnections-Type-ResourceSyncAttempt-InitialRevision"></a>
The current state of the resource as defined in the resource's `config-file` in the linked repository.
Type: [Revision](API_Revision.md) object
Required: Yes

 ** StartedAt **   <a name="codeconnections-Type-ResourceSyncAttempt-StartedAt"></a>
The start time for a resource sync attempt.
Type: Timestamp
Required: Yes

 ** Status **   <a name="codeconnections-Type-ResourceSyncAttempt-Status"></a>
The status for a resource sync attempt. The follow are valid statuses:
+ SYNC-INITIATED - A resource sync attempt has been created and will begin soon.
+ SYNCING - Syncing has started and work is being done to reconcile state.
+ SYNCED - Syncing has completed successfully.
+ SYNC\_FAILED - A resource sync attempt has failed.
Type: String
Valid Values: `FAILED | INITIATED | IN_PROGRESS | SUCCEEDED`
Required: Yes

 ** Target **   <a name="codeconnections-Type-ResourceSyncAttempt-Target"></a>
The name of the AWS resource that is attempted to be synchronized.
Type: String
Required: Yes

 ** TargetRevision **   <a name="codeconnections-Type-ResourceSyncAttempt-TargetRevision"></a>
The desired state of the resource as defined in the resource's `config-file` in the linked repository. Git sync attempts to update the resource to this state.
Type: [Revision](API_Revision.md) object
Required: Yes

## See Also
<a name="API_ResourceSyncAttempt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/ResourceSyncAttempt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/ResourceSyncAttempt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/ResourceSyncAttempt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
