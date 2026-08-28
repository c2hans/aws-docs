---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-datalake-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::DataLake EncryptionConfiguration
<a name="aws-properties-securitylake-datalake-encryptionconfiguration"></a>

Provides encryption details of the Amazon Security Lake object. The AWS shared responsibility model applies to data protection in Amazon Security Lake. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. For more details, see [Data protection](https://docs.aws.amazon.com/security-lake/latest/userguide/data-protection.html) in the Amazon Security Lake User Guide.

## Syntax
<a name="aws-properties-securitylake-datalake-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-datalake-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-securitylake-datalake-encryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-datalake-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-securitylake-datalake-encryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-securitylake-datalake-encryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-securitylake-datalake-encryptionconfiguration-kmskeyid"></a>
The ID of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
