---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsDynamoDbTableProvisionedThroughput.html
---

# AwsDynamoDbTableProvisionedThroughput
<a name="API_AwsDynamoDbTableProvisionedThroughput"></a>

Information about the provisioned throughput for the table or for a global secondary index.

## Contents
<a name="API_AwsDynamoDbTableProvisionedThroughput_Contents"></a>

 ** LastDecreaseDateTime **   <a name="securityhub-Type-AwsDynamoDbTableProvisionedThroughput-LastDecreaseDateTime"></a>
Indicates when the provisioned throughput was last decreased.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastIncreaseDateTime **   <a name="securityhub-Type-AwsDynamoDbTableProvisionedThroughput-LastIncreaseDateTime"></a>
Indicates when the provisioned throughput was last increased.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** NumberOfDecreasesToday **   <a name="securityhub-Type-AwsDynamoDbTableProvisionedThroughput-NumberOfDecreasesToday"></a>
The number of times during the current UTC calendar day that the provisioned throughput was decreased.
Type: Integer
Required: No

 ** ReadCapacityUnits **   <a name="securityhub-Type-AwsDynamoDbTableProvisionedThroughput-ReadCapacityUnits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`.
Type: Integer
Required: No

 ** WriteCapacityUnits **   <a name="securityhub-Type-AwsDynamoDbTableProvisionedThroughput-WriteCapacityUnits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`.
Type: Integer
Required: No

## See Also
<a name="API_AwsDynamoDbTableProvisionedThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsDynamoDbTableProvisionedThroughput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsDynamoDbTableProvisionedThroughput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsDynamoDbTableProvisionedThroughput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
