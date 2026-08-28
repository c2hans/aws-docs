---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalSecondaryIndexAction.html
---

# CreateGlobalSecondaryIndexAction
<a name="API_CreateGlobalSecondaryIndexAction"></a>

Represents a new global secondary index to be added to an existing table.

## Contents
<a name="API_CreateGlobalSecondaryIndexAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-CreateGlobalSecondaryIndexAction-IndexName"></a>
The name of the global secondary index to be created.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** KeySchema **   <a name="DDB-Type-CreateGlobalSecondaryIndexAction-KeySchema"></a>
The key schema for the global secondary index. Global secondary index supports up to 4 partition and up to 4 sort keys.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Projection **   <a name="DDB-Type-CreateGlobalSecondaryIndexAction-Projection"></a>
Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.
Type: [Projection](API_Projection.md) object
Required: Yes

 ** OnDemandThroughput **   <a name="DDB-Type-CreateGlobalSecondaryIndexAction-OnDemandThroughput"></a>
The maximum number of read and write units for the global secondary index being created. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both. You must use either `OnDemand Throughput` or `ProvisionedThroughput` based on your table's capacity mode.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-CreateGlobalSecondaryIndexAction-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** WarmThroughput **   <a name="DDB-Type-CreateGlobalSecondaryIndexAction-WarmThroughput"></a>
Represents the warm throughput value (in read units per second and write units per second) when creating a secondary index.
Type: [WarmThroughput](API_WarmThroughput.md) object
Required: No

## See Also
<a name="API_CreateGlobalSecondaryIndexAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CreateGlobalSecondaryIndexAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CreateGlobalSecondaryIndexAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CreateGlobalSecondaryIndexAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
