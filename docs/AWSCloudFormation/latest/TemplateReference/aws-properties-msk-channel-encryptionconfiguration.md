---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-channel-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Channel EncryptionConfiguration
<a name="aws-properties-msk-channel-encryptionconfiguration"></a>

<a name="aws-properties-msk-channel-encryptionconfiguration-description"></a>The `EncryptionConfiguration` property type specifies Property description not available. for an [AWS::MSK::Channel](aws-resource-msk-channel.md).

## Syntax
<a name="aws-properties-msk-channel-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-channel-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-msk-channel-encryptionconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-channel-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-msk-channel-encryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-msk-channel-encryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-msk-channel-encryptionconfiguration-kmskeyarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:kms:[\w-]+:\d+:key.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
