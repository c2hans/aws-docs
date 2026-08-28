---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration LocalDiskEncryptionConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration"></a>

<a name="aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-description"></a>The `LocalDiskEncryptionConfiguration` property type specifies Property description not available. for an [AWS::EMRContainers::SecurityConfiguration](aws-resource-emrcontainers-securityconfiguration.md).

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-syntax.json"></a>

```
{
  "[AwsKmsKeyId](#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-awskmskeyid)" : {{String}},
  "[EncryptionKeyProviderType](#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-encryptionkeyprovidertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-syntax.yaml"></a>

```
  [AwsKmsKeyId](#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-awskmskeyid): {{String}}
  [EncryptionKeyProviderType](#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-encryptionkeyprovidertype): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-properties"></a>

`AwsKmsKeyId`  <a name="cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-awskmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionKeyProviderType`  <a name="cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-encryptionkeyprovidertype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AwsKms`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
