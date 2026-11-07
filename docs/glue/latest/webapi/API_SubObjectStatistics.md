---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SubObjectStatistics.html
---

# SubObjectStatistics
<a name="API_SubObjectStatistics"></a>

Statistics for one sub-object referenced by a materialized view, recorded when the materialized view was created or last fully refreshed. These values describe what that refresh selected from the sub-object, which can be a subset of the table when the materialized view's definition limits the data it reads. The fields present depend on the sub-object's format.

## Contents
<a name="API_SubObjectStatistics_Contents"></a>

 ** FileCount **   <a name="Glue-Type-SubObjectStatistics-FileCount"></a>
The number of sub-object data files selected for that refresh.
Type: Long
Required: No

 ** GlueVersionId **   <a name="Glue-Type-SubObjectStatistics-GlueVersionId"></a>
The AWS Glue version ID of the sub-object that the statistics were captured for.
Type: String
Required: No

 ** PartitionCount **   <a name="Glue-Type-SubObjectStatistics-PartitionCount"></a>
The number of sub-object partitions selected for that refresh. Not present for unpartitioned sub-objects.
Type: Long
Required: No

 ** SourceType **   <a name="Glue-Type-SubObjectStatistics-SourceType"></a>
The source type of the sub-object (for example, its table format), which identifies the sub-object.
Type: String
Valid Values: `HIVE_PARQUET | HIVE_ORC | HIVE_CSV | HIVE_JSON | PLAIN_PARQUET | ICEBERG`
Required: No

 ** TotalFileBytes **   <a name="Glue-Type-SubObjectStatistics-TotalFileBytes"></a>
The total size, in bytes, of the data files counted by `FileCount`.
Type: Long
Required: No

## See Also
<a name="API_SubObjectStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SubObjectStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SubObjectStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SubObjectStatistics)
