---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicationGroupUpdate.html
---

# ReplicationGroupUpdate
<a name="API_ReplicationGroupUpdate"></a>

Represents one of the following:
+ A new replica to be added to an existing regional table or global table. This request invokes the `CreateTableReplica` action in the destination Region.
+ New parameters for an existing replica. This request invokes the `UpdateTable` action in the destination Region.
+ An existing replica to be deleted. The request invokes the `DeleteTableReplica` action in the destination Region, deleting the replica and all if its items in the destination Region.

**Note**
When you manually remove a table or global table replica, you do not automatically remove any associated scalable targets, scaling policies, or CloudWatch alarms.

## Contents
<a name="API_ReplicationGroupUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Create **   <a name="DDB-Type-ReplicationGroupUpdate-Create"></a>
The parameters required for creating a replica for the table.
Type: [CreateReplicationGroupMemberAction](API_CreateReplicationGroupMemberAction.md) object
Required: No

 ** Delete **   <a name="DDB-Type-ReplicationGroupUpdate-Delete"></a>
The parameters required for deleting a replica for the table.
Type: [DeleteReplicationGroupMemberAction](API_DeleteReplicationGroupMemberAction.md) object
Required: No

 ** Update **   <a name="DDB-Type-ReplicationGroupUpdate-Update"></a>
The parameters required for updating a replica for the table.
Type: [UpdateReplicationGroupMemberAction](API_UpdateReplicationGroupMemberAction.md) object
Required: No

## See Also
<a name="API_ReplicationGroupUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicationGroupUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicationGroupUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicationGroupUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
