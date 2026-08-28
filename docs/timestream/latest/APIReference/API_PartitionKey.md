---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_PartitionKey.html
---

# PartitionKey
<a name="API_PartitionKey"></a>

 An attribute used in partitioning data in a table. A dimension key partitions data using the values of the dimension specified by the dimension-name as partition key, while a measure key partitions data using measure names (values of the 'measure\_name' column).

## Contents
<a name="API_PartitionKey_Contents"></a>

 ** Type **   <a name="timestream-Type-PartitionKey-Type"></a>
 The type of the partition key. Options are DIMENSION (dimension key) and MEASURE (measure key).
Type: String
Valid Values: `DIMENSION | MEASURE`
Required: Yes

 ** EnforcementInRecord **   <a name="timestream-Type-PartitionKey-EnforcementInRecord"></a>
 The level of enforcement for the specification of a dimension key in ingested records. Options are REQUIRED (dimension key must be specified) and OPTIONAL (dimension key does not have to be specified).
Type: String
Valid Values: `REQUIRED | OPTIONAL`
Required: No

 ** Name **   <a name="timestream-Type-PartitionKey-Name"></a>
 The name of the attribute used for a dimension key.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_PartitionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/PartitionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/PartitionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/PartitionKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
