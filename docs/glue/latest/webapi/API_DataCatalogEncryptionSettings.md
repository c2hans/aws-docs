---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataCatalogEncryptionSettings.html
---

# DataCatalogEncryptionSettings
<a name="API_DataCatalogEncryptionSettings"></a>

Contains configuration information for maintaining Data Catalog security.

## Contents
<a name="API_DataCatalogEncryptionSettings_Contents"></a>

 ** ConnectionPasswordEncryption **   <a name="Glue-Type-DataCatalogEncryptionSettings-ConnectionPasswordEncryption"></a>
When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of `CreateConnection` or `UpdateConnection` and store it in the `ENCRYPTED_PASSWORD` field in the connection properties. You can enable catalog encryption or only password encryption.
Type: [ConnectionPasswordEncryption](API_ConnectionPasswordEncryption.md) object
Required: No

 ** EncryptionAtRest **   <a name="Glue-Type-DataCatalogEncryptionSettings-EncryptionAtRest"></a>
Specifies the encryption-at-rest configuration for the Data Catalog.
Type: [EncryptionAtRest](API_EncryptionAtRest.md) object
Required: No

## See Also
<a name="API_DataCatalogEncryptionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataCatalogEncryptionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataCatalogEncryptionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataCatalogEncryptionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
