---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughputDescription.html
---

# ProvisionedThroughputDescription
<a name="API_ProvisionedThroughputDescription"></a>

Represents the provisioned throughput settings for the table, consisting of read and write capacity units, along with data about increases and decreases.

## Contents
<a name="API_ProvisionedThroughputDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LastDecreaseDateTime **   <a name="DDB-Type-ProvisionedThroughputDescription-LastDecreaseDateTime"></a>
The date and time of the last provisioned throughput decrease for this table.
Type: Timestamp
Required: No

 ** LastIncreaseDateTime **   <a name="DDB-Type-ProvisionedThroughputDescription-LastIncreaseDateTime"></a>
The date and time of the last provisioned throughput increase for this table.
Type: Timestamp
Required: No

 ** NumberOfDecreasesToday **   <a name="DDB-Type-ProvisionedThroughputDescription-NumberOfDecreasesToday"></a>
The number of provisioned throughput decreases for this table during this UTC calendar day. For current maximums on provisioned throughput decreases, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** ReadCapacityUnits **   <a name="DDB-Type-ProvisionedThroughputDescription-ReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`. Eventually consistent reads require less effort than strongly consistent reads, so a setting of 50 `ReadCapacityUnits` per second provides 100 eventually consistent `ReadCapacityUnits` per second.
For a table or global secondary index that uses on-demand capacity mode (`PAY_PER_REQUEST`), this value is `0`, because on-demand mode does not use provisioned throughput.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** WriteCapacityUnits **   <a name="DDB-Type-ProvisionedThroughputDescription-WriteCapacityUnits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`.
For a table or global secondary index that uses on-demand capacity mode (`PAY_PER_REQUEST`), this value is `0`, because on-demand mode does not use provisioned throughput.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ProvisionedThroughputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ProvisionedThroughputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ProvisionedThroughputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ProvisionedThroughputDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
