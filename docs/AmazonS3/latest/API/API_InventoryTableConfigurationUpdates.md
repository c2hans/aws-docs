---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryTableConfigurationUpdates.html
---

# InventoryTableConfigurationUpdates
<a name="API_InventoryTableConfigurationUpdates"></a>

 The specified updates to the S3 Metadata inventory table configuration.

## Contents
<a name="API_InventoryTableConfigurationUpdates_Contents"></a>

 ** ConfigurationState **   <a name="AmazonS3-Type-InventoryTableConfigurationUpdates-ConfigurationState"></a>
 The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** EncryptionConfiguration **   <a name="AmazonS3-Type-InventoryTableConfigurationUpdates-EncryptionConfiguration"></a>
 The encryption configuration for the inventory table.
Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md) data type
Required: No

## See Also
<a name="API_InventoryTableConfigurationUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryTableConfigurationUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryTableConfigurationUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryTableConfigurationUpdates)
