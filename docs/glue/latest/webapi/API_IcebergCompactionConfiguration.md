---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergCompactionConfiguration.html
---

# IcebergCompactionConfiguration
<a name="API_IcebergCompactionConfiguration"></a>

The configuration for an Iceberg compaction optimizer. This configuration defines parameters for optimizing the layout of data files in Iceberg tables.

## Contents
<a name="API_IcebergCompactionConfiguration_Contents"></a>

 ** deleteFileThreshold **   <a name="Glue-Type-IcebergCompactionConfiguration-deleteFileThreshold"></a>
The minimum number of deletes that must be present in a data file to make it eligible for compaction. This parameter helps optimize compaction by focusing on files that contain a significant number of delete operations, which can improve query performance by removing deleted records. If an input is not provided, the default value 1 will be used.
Type: Integer
Required: No

 ** minInputFiles **   <a name="Glue-Type-IcebergCompactionConfiguration-minInputFiles"></a>
The minimum number of data files that must be present in a partition before compaction will actually compact files. This parameter helps control when compaction is triggered, preventing unnecessary compaction operations on partitions with few files. If an input is not provided, the default value 100 will be used.
Type: Integer
Required: No

 ** strategy **   <a name="Glue-Type-IcebergCompactionConfiguration-strategy"></a>
The strategy to use for compaction. Valid values are:
+  `binpack`: Combines small files into larger files, typically targeting sizes over 100MB, while applying any pending deletes. This is the recommended compaction strategy for most use cases.
+  `sort`: Organizes data based on specified columns which are sorted hierarchically during compaction, improving query performance for filtered operations. This strategy is recommended when your queries frequently filter on specific columns. To use this strategy, you must first define a sort order in your Iceberg table properties using the `sort_order` table property.
+  `z-order`: Optimizes data organization by blending multiple attributes into a single scalar value that can be used for sorting, allowing efficient querying across multiple dimensions. This strategy is recommended when you need to query data across multiple dimensions simultaneously. To use this strategy, you must first define a sort order in your Iceberg table properties using the `sort_order` table property.
If an input is not provided, the default value 'binpack' will be used.
Type: String
Valid Values: `binpack | sort | z-order`
Required: No

## See Also
<a name="API_IcebergCompactionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergCompactionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergCompactionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergCompactionConfiguration)
