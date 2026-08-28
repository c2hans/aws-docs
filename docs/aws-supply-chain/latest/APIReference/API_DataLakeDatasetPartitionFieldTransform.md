---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataLakeDatasetPartitionFieldTransform.html
---

# DataLakeDatasetPartitionFieldTransform
<a name="API_DataLakeDatasetPartitionFieldTransform"></a>

The detail of the partition field transformation.

## Contents
<a name="API_DataLakeDatasetPartitionFieldTransform_Contents"></a>

 ** type **   <a name="supplychain-Type-DataLakeDatasetPartitionFieldTransform-type"></a>
The type of partitioning transformation for this field. The available options are:
+  **IDENTITY** - Partitions data on a given field by its exact values.
+  **YEAR** - Partitions data on a timestamp field using year granularity.
+  **MONTH** - Partitions data on a timestamp field using month granularity.
+  **DAY** - Partitions data on a timestamp field using day granularity.
+  **HOUR** - Partitions data on a timestamp field using hour granularity.
Type: String
Valid Values: `YEAR | MONTH | DAY | HOUR | IDENTITY`
Required: Yes

## See Also
<a name="API_DataLakeDatasetPartitionFieldTransform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataLakeDatasetPartitionFieldTransform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataLakeDatasetPartitionFieldTransform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataLakeDatasetPartitionFieldTransform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
