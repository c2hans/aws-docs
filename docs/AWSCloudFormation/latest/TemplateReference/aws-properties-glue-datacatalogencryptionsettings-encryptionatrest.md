---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-datacatalogencryptionsettings-encryptionatrest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::DataCatalogEncryptionSettings EncryptionAtRest
<a name="aws-properties-glue-datacatalogencryptionsettings-encryptionatrest"></a>

Specifies the encryption-at-rest configuration for the Data Catalog.

## Syntax
<a name="aws-properties-glue-datacatalogencryptionsettings-encryptionatrest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-datacatalogencryptionsettings-encryptionatrest-syntax.json"></a>

```
{
  "[CatalogEncryptionMode](#cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionmode)" : {{String}},
  "[CatalogEncryptionServiceRole](#cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionservicerole)" : {{String}},
  "[SseAwsKmsKeyId](#cfn-glue-datacatalogencryptionsettings-encryptionatrest-sseawskmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-datacatalogencryptionsettings-encryptionatrest-syntax.yaml"></a>

```
  [CatalogEncryptionMode](#cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionmode): {{String}}
  [CatalogEncryptionServiceRole](#cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionservicerole): {{String}}
  [SseAwsKmsKeyId](#cfn-glue-datacatalogencryptionsettings-encryptionatrest-sseawskmskeyid): {{String}}
```

## Properties
<a name="aws-properties-glue-datacatalogencryptionsettings-encryptionatrest-properties"></a>

`CatalogEncryptionMode`  <a name="cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionmode"></a>
The encryption-at-rest mode for encrypting Data Catalog data.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | SSE-KMS | SSE-KMS-WITH-SERVICE-ROLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CatalogEncryptionServiceRole`  <a name="cfn-glue-datacatalogencryptionsettings-encryptionatrest-catalogencryptionservicerole"></a>
The role that AWS Glue assumes to encrypt and decrypt the Data Catalog objects on the caller's behalf.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SseAwsKmsKeyId`  <a name="cfn-glue-datacatalogencryptionsettings-encryptionatrest-sseawskmskeyid"></a>
The ID of the AWS KMS key to use for encryption at rest.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
