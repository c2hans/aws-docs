---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalSecondaryIndexWarmThroughputDescription.html
---

# GlobalSecondaryIndexWarmThroughputDescription
<a name="API_GlobalSecondaryIndexWarmThroughputDescription"></a>

The description of the warm throughput value on a global secondary index.

## Contents
<a name="API_GlobalSecondaryIndexWarmThroughputDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ReadUnitsPerSecond **   <a name="DDB-Type-GlobalSecondaryIndexWarmThroughputDescription-ReadUnitsPerSecond"></a>
Represents warm throughput read units per second value for a global secondary index.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** Status **   <a name="DDB-Type-GlobalSecondaryIndexWarmThroughputDescription-Status"></a>
Represents the warm throughput status being created or updated on a global secondary index. The status can only be `UPDATING` or `ACTIVE`.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE`
Required: No

 ** WriteUnitsPerSecond **   <a name="DDB-Type-GlobalSecondaryIndexWarmThroughputDescription-WriteUnitsPerSecond"></a>
Represents warm throughput write units per second value for a global secondary index.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_GlobalSecondaryIndexWarmThroughputDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalSecondaryIndexWarmThroughputDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalSecondaryIndexWarmThroughputDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalSecondaryIndexWarmThroughputDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
