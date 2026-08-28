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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
