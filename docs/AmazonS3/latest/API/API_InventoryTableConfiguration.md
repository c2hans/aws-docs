---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryTableConfiguration.html
---

# InventoryTableConfiguration
<a name="API_InventoryTableConfiguration"></a>

 The inventory table configuration for an S3 Metadata configuration.

## Contents
<a name="API_InventoryTableConfiguration_Contents"></a>

 ** ConfigurationState **   <a name="AmazonS3-Type-InventoryTableConfiguration-ConfigurationState"></a>
 The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** EncryptionConfiguration **   <a name="AmazonS3-Type-InventoryTableConfiguration-EncryptionConfiguration"></a>
 The encryption configuration for the inventory table.
Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md) data type
Required: No

## See Also
<a name="API_InventoryTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryTableConfiguration)
