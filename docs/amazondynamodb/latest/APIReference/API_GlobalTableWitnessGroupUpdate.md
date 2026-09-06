---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableWitnessGroupUpdate.html
---

# GlobalTableWitnessGroupUpdate
<a name="API_GlobalTableWitnessGroupUpdate"></a>

Represents one of the following:
+ A new witness to be added to a new global table.
+ An existing witness to be removed from an existing global table.

You can configure one witness per MRSC global table.

## Contents
<a name="API_GlobalTableWitnessGroupUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Create **   <a name="DDB-Type-GlobalTableWitnessGroupUpdate-Create"></a>
Specifies a witness Region to be added to a new MRSC global table. The witness must be added when creating the MRSC global table.
Type: [CreateGlobalTableWitnessGroupMemberAction](API_CreateGlobalTableWitnessGroupMemberAction.md) object
Required: No

 ** Delete **   <a name="DDB-Type-GlobalTableWitnessGroupUpdate-Delete"></a>
Specifies a witness Region to be removed from an existing global table. Must be done in conjunction with removing a replica. The deletion of both a witness and replica converts the remaining replica to a single-Region DynamoDB table.
Type: [DeleteGlobalTableWitnessGroupMemberAction](API_DeleteGlobalTableWitnessGroupMemberAction.md) object
Required: No

## See Also
<a name="API_GlobalTableWitnessGroupUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalTableWitnessGroupUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalTableWitnessGroupUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalTableWitnessGroupUpdate)
