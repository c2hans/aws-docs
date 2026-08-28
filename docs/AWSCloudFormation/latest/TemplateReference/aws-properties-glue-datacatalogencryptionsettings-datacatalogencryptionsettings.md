---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::DataCatalogEncryptionSettings DataCatalogEncryptionSettings
<a name="aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings"></a>

Contains configuration information for maintaining Data Catalog security.

## Syntax
<a name="aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-syntax.json"></a>

```
{
  "[ConnectionPasswordEncryption](#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-connectionpasswordencryption)" : {{ConnectionPasswordEncryption}},
  "[EncryptionAtRest](#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-encryptionatrest)" : {{EncryptionAtRest}}
}
```

### YAML
<a name="aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-syntax.yaml"></a>

```
  [ConnectionPasswordEncryption](#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-connectionpasswordencryption): {{
    ConnectionPasswordEncryption}}
  [EncryptionAtRest](#cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-encryptionatrest): {{
    EncryptionAtRest}}
```

## Properties
<a name="aws-properties-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-properties"></a>

`ConnectionPasswordEncryption`  <a name="cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-connectionpasswordencryption"></a>
When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of `CreateConnection` or `UpdateConnection` and store it in the `ENCRYPTED_PASSWORD` field in the connection properties. You can enable catalog encryption or only password encryption.
*Required*: No
*Type*: [ConnectionPasswordEncryption](aws-properties-glue-datacatalogencryptionsettings-connectionpasswordencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionAtRest`  <a name="cfn-glue-datacatalogencryptionsettings-datacatalogencryptionsettings-encryptionatrest"></a>
Specifies the encryption-at-rest configuration for the Data Catalog.
*Required*: No
*Type*: [EncryptionAtRest](aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
