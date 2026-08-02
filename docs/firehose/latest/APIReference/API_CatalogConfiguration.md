---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_CatalogConfiguration.html
---

# CatalogConfiguration
<a name="API_CatalogConfiguration"></a>

 Describes the containers where the destination Apache Iceberg Tables are persisted.

## Contents
<a name="API_CatalogConfiguration_Contents"></a>

 ** CatalogARN **   <a name="Firehose-Type-CatalogConfiguration-CatalogARN"></a>
 Specifies the Glue catalog ARN identifier of the destination Apache Iceberg Tables. You must specify the ARN in the format `arn:aws:glue:region:account-id:catalog`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:glue:.*:\d{12}:catalog(?:(/[a-z0-9_-]+){1,2})?`
Required: No

 ** WarehouseLocation **   <a name="Firehose-Type-CatalogConfiguration-WarehouseLocation"></a>
The warehouse location for Apache Iceberg tables. You must configure this when schema evolution and table creation is enabled.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `s3:\/\/.*`
Required: No

## See Also
<a name="API_CatalogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/CatalogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/CatalogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/CatalogConfiguration)
