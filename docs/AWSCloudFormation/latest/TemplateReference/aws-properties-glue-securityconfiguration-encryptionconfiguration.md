---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-securityconfiguration-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::SecurityConfiguration EncryptionConfiguration
<a name="aws-properties-glue-securityconfiguration-encryptionconfiguration"></a>

Specifies an encryption configuration.

## Syntax
<a name="aws-properties-glue-securityconfiguration-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-securityconfiguration-encryptionconfiguration-syntax.json"></a>

```
{
  "[CloudWatchEncryption](#cfn-glue-securityconfiguration-encryptionconfiguration-cloudwatchencryption)" : {{CloudWatchEncryption}},
  "[JobBookmarksEncryption](#cfn-glue-securityconfiguration-encryptionconfiguration-jobbookmarksencryption)" : {{JobBookmarksEncryption}},
  "[S3Encryptions](#cfn-glue-securityconfiguration-encryptionconfiguration-s3encryptions)" : {{[ S3Encryption, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-securityconfiguration-encryptionconfiguration-syntax.yaml"></a>

```
  [CloudWatchEncryption](#cfn-glue-securityconfiguration-encryptionconfiguration-cloudwatchencryption): {{
    CloudWatchEncryption}}
  [JobBookmarksEncryption](#cfn-glue-securityconfiguration-encryptionconfiguration-jobbookmarksencryption): {{
    JobBookmarksEncryption}}
  [S3Encryptions](#cfn-glue-securityconfiguration-encryptionconfiguration-s3encryptions): {{
    - S3Encryption}}
```

## Properties
<a name="aws-properties-glue-securityconfiguration-encryptionconfiguration-properties"></a>

`CloudWatchEncryption`  <a name="cfn-glue-securityconfiguration-encryptionconfiguration-cloudwatchencryption"></a>
The encryption configuration for Amazon CloudWatch.
*Required*: No
*Type*: [CloudWatchEncryption](aws-properties-glue-securityconfiguration-cloudwatchencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobBookmarksEncryption`  <a name="cfn-glue-securityconfiguration-encryptionconfiguration-jobbookmarksencryption"></a>
The encryption configuration for job bookmarks.
*Required*: No
*Type*: [JobBookmarksEncryption](aws-properties-glue-securityconfiguration-jobbookmarksencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Encryptions`  <a name="cfn-glue-securityconfiguration-encryptionconfiguration-s3encryptions"></a>
The encyption configuration for Amazon Simple Storage Service (Amazon S3) data.
*Required*: No
*Type*: Array of [S3Encryption](aws-properties-glue-securityconfiguration-s3encryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
