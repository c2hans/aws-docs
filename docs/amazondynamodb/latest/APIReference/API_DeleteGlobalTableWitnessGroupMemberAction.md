---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteGlobalTableWitnessGroupMemberAction.html
---

# DeleteGlobalTableWitnessGroupMemberAction
<a name="API_DeleteGlobalTableWitnessGroupMemberAction"></a>

Specifies the action to remove a witness Region from a MRSC global table. You cannot delete a single witness from a MRSC global table - you must delete both a replica and the witness together. The deletion of both a witness and replica converts the remaining replica to a single-Region DynamoDB table.

## Contents
<a name="API_DeleteGlobalTableWitnessGroupMemberAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionName **   <a name="DDB-Type-DeleteGlobalTableWitnessGroupMemberAction-RegionName"></a>
The witness Region name to be removed from the MRSC global table.
Type: String
Required: Yes

## See Also
<a name="API_DeleteGlobalTableWitnessGroupMemberAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DeleteGlobalTableWitnessGroupMemberAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteGlobalTableWitnessGroupMemberAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DeleteGlobalTableWitnessGroupMemberAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
