---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergOptimizationProperties.html
---

# IcebergOptimizationProperties
<a name="API_IcebergOptimizationProperties"></a>

A structure that specifies Iceberg table optimization properties for the catalog, including configurations for compaction, retention, and orphan file deletion operations.

## Contents
<a name="API_IcebergOptimizationProperties_Contents"></a>

 ** Compaction **   <a name="Glue-Type-IcebergOptimizationProperties-Compaction"></a>
A map of key-value pairs that specify configuration parameters for Iceberg table compaction operations, which optimize the layout of data files to improve query performance.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** OrphanFileDeletion **   <a name="Glue-Type-IcebergOptimizationProperties-OrphanFileDeletion"></a>
A map of key-value pairs that specify configuration parameters for Iceberg orphan file deletion operations, which identify and remove files that are no longer referenced by the table metadata.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** Retention **   <a name="Glue-Type-IcebergOptimizationProperties-Retention"></a>
A map of key-value pairs that specify configuration parameters for Iceberg table retention operations, which manage the lifecycle of table snapshots to control storage costs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** RoleArn **   <a name="Glue-Type-IcebergOptimizationProperties-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that will be assumed to perform Iceberg table optimization operations.
Type: String
Pattern: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`
Required: No

## See Also
<a name="API_IcebergOptimizationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergOptimizationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergOptimizationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergOptimizationProperties)
