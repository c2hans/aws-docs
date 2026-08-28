---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_SourceTableDetails.html
---

# SourceTableDetails
<a name="API_SourceTableDetails"></a>

Contains the details of the table when the backup was created.

## Contents
<a name="API_SourceTableDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** KeySchema **   <a name="DDB-Type-SourceTableDetails-KeySchema"></a>
Schema of the table.
Type: Array of [KeySchemaElement](API_KeySchemaElement.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** ProvisionedThroughput **   <a name="DDB-Type-SourceTableDetails-ProvisionedThroughput"></a>
Read IOPs and Write IOPS on the table when the backup was created.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: Yes

 ** TableCreationDateTime **   <a name="DDB-Type-SourceTableDetails-TableCreationDateTime"></a>
Time when the source table was created.
Type: Timestamp
Required: Yes

 ** TableId **   <a name="DDB-Type-SourceTableDetails-TableId"></a>
Unique identifier for the table for which the backup was created.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** TableName **   <a name="DDB-Type-SourceTableDetails-TableName"></a>
The name of the table for which the backup was created.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** BillingMode **   <a name="DDB-Type-SourceTableDetails-BillingMode"></a>
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.
+  `PROVISIONED` - Sets the read/write capacity mode to `PROVISIONED`. We recommend using `PROVISIONED` for predictable workloads.
+  `PAY_PER_REQUEST` - Sets the read/write capacity mode to `PAY_PER_REQUEST`. We recommend using `PAY_PER_REQUEST` for unpredictable workloads.
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** ItemCount **   <a name="DDB-Type-SourceTableDetails-ItemCount"></a>
Number of items in the table. Note that this is an approximate value.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** OnDemandThroughput **   <a name="DDB-Type-SourceTableDetails-OnDemandThroughput"></a>
Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** TableArn **   <a name="DDB-Type-SourceTableDetails-TableArn"></a>
ARN of the table for which backup was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** TableSizeBytes **   <a name="DDB-Type-SourceTableDetails-TableSizeBytes"></a>
Size of the table in bytes. Note that this is an approximate value.
Type: Long
Required: No

## See Also
<a name="API_SourceTableDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/SourceTableDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/SourceTableDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/SourceTableDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
