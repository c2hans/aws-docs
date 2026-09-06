---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationPartition.html
---

# IntegrationPartition
<a name="API_IntegrationPartition"></a>

A structure that describes how data is partitioned on the target.

## Contents
<a name="API_IntegrationPartition_Contents"></a>

 ** ConversionSpec **   <a name="Glue-Type-IntegrationPartition-ConversionSpec"></a>
Specifies the timestamp format of the source data. Valid values are:
+  `epoch_sec` - Unix epoch timestamp in seconds
+  `epoch_milli` - Unix epoch timestamp in milliseconds
+  `iso` - ISO 8601 formatted timestamp
 Only specify `ConversionSpec` when using timestamp-based partition functions (year, month, day, or hour). AWS Glue Zero-ETL uses this parameter to correctly transform source data into timestamp format before partitioning.
 Do not use high-cardinality columns with the `identity` partition function. High-cardinality columns include:
+ Primary keys
+ Timestamp fields (such as `LastModifiedTimestamp`, `CreatedDate`)
+ System-generated timestamps
 Using high-cardinality columns with identity partitioning creates many small partitions, which can significantly degrade ingestion performance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** FieldName **   <a name="Glue-Type-IntegrationPartition-FieldName"></a>
The field name used to partition data on the target. Avoid using columns that have unique values for each row (for example, `LastModifiedTimestamp`, `SystemModTimeStamp`) as the partition column. These columns are not suitable for partitioning because they create a large number of small partitions, which can lead to performance issues.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** FunctionSpec **   <a name="Glue-Type-IntegrationPartition-FunctionSpec"></a>
Specifies the function used to partition data on the target. The accepted values for this parameter are:
+  `identity` - Uses source values directly without transformation
+  `year` - Extracts the year from timestamp values (e.g., 2023)
+  `month` - Extracts the month from timestamp values (e.g., 2023-01)
+  `day` - Extracts the day from timestamp values (e.g., 2023-01-15)
+  `hour` - Extracts the hour from timestamp values (e.g., 2023-01-15-14)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_IntegrationPartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IntegrationPartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IntegrationPartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IntegrationPartition)
