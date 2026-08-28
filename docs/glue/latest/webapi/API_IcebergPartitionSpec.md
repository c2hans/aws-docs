---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergPartitionSpec.html
---

# IcebergPartitionSpec
<a name="API_IcebergPartitionSpec"></a>

Defines the partitioning specification for an Iceberg table, determining how table data will be organized and partitioned for optimal query performance.

## Contents
<a name="API_IcebergPartitionSpec_Contents"></a>

 ** Fields **   <a name="Glue-Type-IcebergPartitionSpec-Fields"></a>
The list of partition fields that define how the table data should be partitioned, including source fields and their transformations.
Type: Array of [IcebergPartitionField](API_IcebergPartitionField.md) objects
Required: Yes

 ** SpecId **   <a name="Glue-Type-IcebergPartitionSpec-SpecId"></a>
The unique identifier for this partition specification within the Iceberg table's metadata history.
Type: Integer
Required: No

## See Also
<a name="API_IcebergPartitionSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergPartitionSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergPartitionSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergPartitionSpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
