---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexUpdate.html
---

# GlobalSecondaryIndexUpdate
<a name="API_GlobalSecondaryIndexUpdate"></a>

Represents one of the following:
+ A new global secondary index to be added to an existing table.
+ New provisioned throughput parameters for an existing global secondary index.
+ An existing global secondary index to be removed from an existing table.

## Contents
<a name="API_GlobalSecondaryIndexUpdate_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Create **   <a name="DDB-Type-GlobalSecondaryIndexUpdate-Create"></a>
The parameters required for creating a global secondary index on an existing table:
+  `IndexName `
+  `KeySchema `
+  `AttributeDefinitions `
+  `Projection `
+  `ProvisionedThroughput `
Type: [CreateGlobalSecondaryIndexAction](API_CreateGlobalSecondaryIndexAction.md) object
Required: No

 ** Delete **   <a name="DDB-Type-GlobalSecondaryIndexUpdate-Delete"></a>
The name of an existing global secondary index to be removed.
Type: [DeleteGlobalSecondaryIndexAction](API_DeleteGlobalSecondaryIndexAction.md) object
Required: No

 ** Update **   <a name="DDB-Type-GlobalSecondaryIndexUpdate-Update"></a>
The name of an existing global secondary index, along with new provisioned throughput settings to be applied to that index.
Type: [UpdateGlobalSecondaryIndexAction](API_UpdateGlobalSecondaryIndexAction.md) object
Required: No

## See Also
<a name="API_GlobalSecondaryIndexUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalSecondaryIndexUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalSecondaryIndexUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalSecondaryIndexUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
