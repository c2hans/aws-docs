---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicaUpdate.html
---

# ReplicaUpdate
<a name="API_ReplicaUpdate"></a>

Represents one of the following:
+ A new replica to be added to an existing global table.
+ New parameters for an existing replica.
+ An existing replica to be removed from an existing global table.

## Contents
<a name="API_ReplicaUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Create **   <a name="DDB-Type-ReplicaUpdate-Create"></a>
The parameters required for creating a replica on an existing global table.
Type: [CreateReplicaAction](API_CreateReplicaAction.md) object
Required: No

 ** Delete **   <a name="DDB-Type-ReplicaUpdate-Delete"></a>
The name of the existing replica to be removed.
Type: [DeleteReplicaAction](API_DeleteReplicaAction.md) object
Required: No

## See Also
<a name="API_ReplicaUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ReplicaUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ReplicaUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ReplicaUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
