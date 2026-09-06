---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalTableWitnessGroupMemberAction.html
---

# CreateGlobalTableWitnessGroupMemberAction
<a name="API_CreateGlobalTableWitnessGroupMemberAction"></a>

Specifies the action to add a new witness Region to a MRSC global table. A MRSC global table can be configured with either three replicas, or with two replicas and one witness.

## Contents
<a name="API_CreateGlobalTableWitnessGroupMemberAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-CreateGlobalTableWitnessGroupMemberAction-RegionName"></a>
The AWS Region name to be added as a witness Region for the MRSC global table. The witness must be in a different Region than the replicas and within the same Region set:
+ US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)
+ EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt)
+ AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka)
Type: String
Required: Yes

## See Also
<a name="API_CreateGlobalTableWitnessGroupMemberAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CreateGlobalTableWitnessGroupMemberAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CreateGlobalTableWitnessGroupMemberAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CreateGlobalTableWitnessGroupMemberAction)
