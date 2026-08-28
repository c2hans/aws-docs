---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ProvisionedThroughputOverride.html
---

# ProvisionedThroughputOverride
<a name="API_ProvisionedThroughputOverride"></a>

Replica-specific provisioned throughput settings. If not specified, uses the source table's provisioned throughput settings.

## Contents
<a name="API_ProvisionedThroughputOverride_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ReadCapacityUnits **   <a name="DDB-Type-ProvisionedThroughputOverride-ReadCapacityUnits"></a>
Replica-specific read capacity units. If not specified, uses the source table's read capacity settings.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ProvisionedThroughputOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ProvisionedThroughputOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ProvisionedThroughputOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ProvisionedThroughputOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
