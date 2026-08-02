---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-featuregroup-offlinestoreconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::FeatureGroup OfflineStoreConfig
<a name="aws-properties-sagemaker-featuregroup-offlinestoreconfig"></a>

The configuration of an `OfflineStore`.

Provide an `OfflineStoreConfig` in a request to `CreateFeatureGroup` to create an `OfflineStore`.

To encrypt an `OfflineStore` using at rest data encryption, specify AWS Key Management Service (KMS) key ID, or `KMSKeyId`, in `S3StorageConfig`.

## Syntax
<a name="aws-properties-sagemaker-featuregroup-offlinestoreconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-featuregroup-offlinestoreconfig-syntax.json"></a>

```
{
  "[DataCatalogConfig](#cfn-sagemaker-featuregroup-offlinestoreconfig-datacatalogconfig)" : {{DataCatalogConfig}},
  "[DisableGlueTableCreation](#cfn-sagemaker-featuregroup-offlinestoreconfig-disablegluetablecreation)" : {{Boolean}},
  "[S3StorageConfig](#cfn-sagemaker-featuregroup-offlinestoreconfig-s3storageconfig)" : {{S3StorageConfig}},
  "[TableFormat](#cfn-sagemaker-featuregroup-offlinestoreconfig-tableformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-featuregroup-offlinestoreconfig-syntax.yaml"></a>

```
  [DataCatalogConfig](#cfn-sagemaker-featuregroup-offlinestoreconfig-datacatalogconfig): {{
    DataCatalogConfig}}
  [DisableGlueTableCreation](#cfn-sagemaker-featuregroup-offlinestoreconfig-disablegluetablecreation): {{Boolean}}
  [S3StorageConfig](#cfn-sagemaker-featuregroup-offlinestoreconfig-s3storageconfig): {{
    S3StorageConfig}}
  [TableFormat](#cfn-sagemaker-featuregroup-offlinestoreconfig-tableformat): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-featuregroup-offlinestoreconfig-properties"></a>

`DataCatalogConfig`  <a name="cfn-sagemaker-featuregroup-offlinestoreconfig-datacatalogconfig"></a>
The meta data of the Glue table for the `OfflineStore`. If not provided, Feature Store auto-generates the table name, database, and catalog when the `OfflineStore` is created. You can optionally provide this configuration to specify custom values. This applies to both Glue and Apache Iceberg table formats.
*Required*: No
*Type*: [DataCatalogConfig](aws-properties-sagemaker-featuregroup-datacatalogconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisableGlueTableCreation`  <a name="cfn-sagemaker-featuregroup-offlinestoreconfig-disablegluetablecreation"></a>
Set to `True` to disable the automatic creation of an AWS Glue table when configuring an `OfflineStore`. If set to `True` and `DataCatalogConfig` is provided, Feature Store associates the provided catalog configuration with the feature group without creating a table. In this case, you are responsible for creating and managing the Glue table. If set to `True` without `DataCatalogConfig`, no Glue table is created or associated with the feature group. The `Iceberg` table format is only supported when this is set to `False`.
If set to `False` and `DataCatalogConfig` is provided, Feature Store creates the table using the specified names. If set to `False` without `DataCatalogConfig`, Feature Store auto-generates the table name following [Athena's naming recommendations](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html). This applies to both Glue and Apache Iceberg table formats.
The default value is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3StorageConfig`  <a name="cfn-sagemaker-featuregroup-offlinestoreconfig-s3storageconfig"></a>
The Amazon Simple Storage (Amazon S3) location of `OfflineStore`.
*Required*: Yes
*Type*: [S3StorageConfig](aws-properties-sagemaker-featuregroup-s3storageconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableFormat`  <a name="cfn-sagemaker-featuregroup-offlinestoreconfig-tableformat"></a>
Format for the offline store table. Supported formats are Glue (Default) and [Apache Iceberg](https://iceberg.apache.org/).
*Required*: No
*Type*: String
*Allowed values*: `Iceberg | Glue`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
