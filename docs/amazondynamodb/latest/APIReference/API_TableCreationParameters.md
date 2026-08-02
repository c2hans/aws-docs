---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableCreationParameters.html
---

# TableCreationParameters
<a name="API_TableCreationParameters"></a>

 The parameters for the table created as part of the import operation.

## Contents
<a name="API_TableCreationParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeDefinitions **   <a name="DDB-Type-TableCreationParameters-AttributeDefinitions"></a>
 The attributes of the table created as part of the import operation.
Type: Array of [AttributeDefinition](API_AttributeDefinition.md) objects
Required: Yes

 ** KeySchema **   <a name="DDB-Type-TableCreationParameters-KeySchema"></a>
 The primary key and option sort key of the table created as part of the import operation.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** TableName **   <a name="DDB-Type-TableCreationParameters-TableName"></a>
 The name of the table created as part of the import operation.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** BillingMode **   <a name="DDB-Type-TableCreationParameters-BillingMode"></a>
 The billing mode for provisioning the table created as part of the import operation.
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-TableCreationParameters-GlobalSecondaryIndexes"></a>
 The Global Secondary Indexes (GSI) of the table to be created as part of the import operation.
Type: Array of [GlobalSecondaryIndex](API_GlobalSecondaryIndex.md) objects
Required: No

 ** OnDemandThroughput **   <a name="DDB-Type-TableCreationParameters-OnDemandThroughput"></a>
Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-TableCreationParameters-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index. You must use `ProvisionedThroughput` or `OnDemandThroughput` based on your table’s capacity mode.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** SSESpecification **   <a name="DDB-Type-TableCreationParameters-SSESpecification"></a>
Represents the settings used to enable server-side encryption.
Type: [SSESpecification](API_SSESpecification.md) object
Required: No

## See Also
<a name="API_TableCreationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TableCreationParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TableCreationParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TableCreationParameters)
