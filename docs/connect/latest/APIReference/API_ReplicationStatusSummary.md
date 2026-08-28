---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicationStatusSummary.html
---

# ReplicationStatusSummary
<a name="API_ReplicationStatusSummary"></a>

Status information about the replication process, where you use the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API to create a replica of your Connect Customer instance in another AWS Region. For more information, see [Set up Connect Customer Global Resiliency](https://docs.aws.amazon.com/connect/latest/adminguide/setup-connect-global-resiliency.html) in the *Connect Customer Administrator Guide*.

## Contents
<a name="API_ReplicationStatusSummary_Contents"></a>

 ** Region **   <a name="connect-Type-ReplicationStatusSummary-Region"></a>
The AWS Region. This can be either the source or the replica Region, depending where it appears in the summary list.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** ReplicationStatus **   <a name="connect-Type-ReplicationStatusSummary-ReplicationStatus"></a>
The state of the replication.
Type: String
Valid Values: `INSTANCE_REPLICATION_COMPLETE | INSTANCE_REPLICATION_IN_PROGRESS | INSTANCE_REPLICATION_FAILED | INSTANCE_REPLICA_DELETING | INSTANCE_REPLICATION_DELETION_FAILED | RESOURCE_REPLICATION_NOT_STARTED`
Required: No

 ** ReplicationStatusReason **   <a name="connect-Type-ReplicationStatusSummary-ReplicationStatusReason"></a>
A description of the replication status. Use this information to resolve any issues that are preventing the successful replication of your Connect Customer instance to another Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ReplicationStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ReplicationStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ReplicationStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ReplicationStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
