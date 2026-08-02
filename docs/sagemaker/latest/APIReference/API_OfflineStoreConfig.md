---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreConfig.html
---

# OfflineStoreConfig
<a name="API_OfflineStoreConfig"></a>

The configuration of an `OfflineStore`.

Provide an `OfflineStoreConfig` in a request to `CreateFeatureGroup` to create an `OfflineStore`.

To encrypt an `OfflineStore` using at rest data encryption, specify AWS Key Management Service (KMS) key ID, or `KMSKeyId`, in `S3StorageConfig`.

## Contents
<a name="API_OfflineStoreConfig_Contents"></a>

 ** S3StorageConfig **   <a name="sagemaker-Type-OfflineStoreConfig-S3StorageConfig"></a>
The Amazon Simple Storage (Amazon S3) location of `OfflineStore`.
Type: [S3StorageConfig](API_S3StorageConfig.md) object
Required: Yes

 ** DataCatalogConfig **   <a name="sagemaker-Type-OfflineStoreConfig-DataCatalogConfig"></a>
The meta data of the Glue table for the `OfflineStore`. If not provided, Feature Store auto-generates the table name, database, and catalog when the `OfflineStore` is created. You can optionally provide this configuration to specify custom values. This applies to both Glue and Apache Iceberg table formats.
Type: [DataCatalogConfig](API_DataCatalogConfig.md) object
Required: No

 ** DisableGlueTableCreation **   <a name="sagemaker-Type-OfflineStoreConfig-DisableGlueTableCreation"></a>
Set to `True` to disable the automatic creation of an AWS Glue table when configuring an `OfflineStore`. If set to `True` and `DataCatalogConfig` is provided, Feature Store associates the provided catalog configuration with the feature group without creating a table. In this case, you are responsible for creating and managing the Glue table. If set to `True` without `DataCatalogConfig`, no Glue table is created or associated with the feature group. The `Iceberg` table format is only supported when this is set to `False`.
If set to `False` and `DataCatalogConfig` is provided, Feature Store creates the table using the specified names. If set to `False` without `DataCatalogConfig`, Feature Store auto-generates the table name following [Athena's naming recommendations](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html). This applies to both Glue and Apache Iceberg table formats.
The default value is `False`.
Type: Boolean
Required: No

 ** TableFormat **   <a name="sagemaker-Type-OfflineStoreConfig-TableFormat"></a>
Format for the offline store table. Supported formats are Glue (Default) and [Apache Iceberg](https://iceberg.apache.org/).
Type: String
Valid Values: `Default | Glue | Iceberg`
Required: No

## See Also
<a name="API_OfflineStoreConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OfflineStoreConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OfflineStoreConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OfflineStoreConfig)
