---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration AtRestEncryptionConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration"></a>

<a name="aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration-description"></a>The `AtRestEncryptionConfiguration` property type specifies Property description not available. for an [AWS::EMRContainers::SecurityConfiguration](aws-resource-emrcontainers-securityconfiguration.md).

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration-syntax.json"></a>

```
{
  "[LocalDiskEncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-localdiskencryptionconfiguration)" : {{LocalDiskEncryptionConfiguration}},
  "[S3EncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-s3encryptionconfiguration)" : {{S3EncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration-syntax.yaml"></a>

```
  [LocalDiskEncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-localdiskencryptionconfiguration): {{
    LocalDiskEncryptionConfiguration}}
  [S3EncryptionConfiguration](#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-s3encryptionconfiguration): {{
    S3EncryptionConfiguration}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration-properties"></a>

`LocalDiskEncryptionConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-localdiskencryptionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [LocalDiskEncryptionConfiguration](aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3EncryptionConfiguration`  <a name="cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-s3encryptionconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [S3EncryptionConfiguration](aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
