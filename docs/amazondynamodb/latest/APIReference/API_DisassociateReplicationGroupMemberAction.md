---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DisassociateReplicationGroupMemberAction.html
---

# DisassociateReplicationGroupMemberAction
<a name="API_DisassociateReplicationGroupMemberAction"></a>

The parameters for disassociating the local replica from a global table using Version 2019.11.21 with multi-Region eventual consistency (MREC).

After disassociation completes, the replica remains a standalone regional table that keeps its data, indexes, and table settings.

For request requirements, see [UpdateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html). For prerequisites, the protection update, and completion checks, see [Disassociating a global table replica](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-disassociate.html) in the *Amazon DynamoDB Developer Guide*.

## Contents
<a name="API_DisassociateReplicationGroupMemberAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DisassociationMode **   <a name="DDB-Type-DisassociateReplicationGroupMemberAction-DisassociationMode"></a>
The mode for handling pending replication before disassociation completes. You must specify `WAIT_FOR_REPLICATION`. For more information, see [Disassociating a global table replica](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-disassociate.html) in the *Amazon DynamoDB Developer Guide*.
Type: String
Valid Values: `WAIT_FOR_REPLICATION`
Required: Yes

 ** RegionName **   <a name="DDB-Type-DisassociateReplicationGroupMemberAction-RegionName"></a>
The Region of the replica to disassociate. Set this value to the Region where you send the `UpdateTable` request. You must use credentials for the account that owns the replica.
Type: String
Required: Yes

## See Also
<a name="API_DisassociateReplicationGroupMemberAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DisassociateReplicationGroupMemberAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DisassociateReplicationGroupMemberAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DisassociateReplicationGroupMemberAction)
