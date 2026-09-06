---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConfigurationBundle VersionCreatedBySource
<a name="aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource"></a>

The source that created a configuration bundle version.

## Syntax
<a name="aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-configurationbundle-versioncreatedbysource-arn)" : {{String}},
  "[Name](#cfn-bedrockagentcore-configurationbundle-versioncreatedbysource-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-configurationbundle-versioncreatedbysource-arn): {{String}}
  [Name](#cfn-bedrockagentcore-configurationbundle-versioncreatedbysource-name): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-configurationbundle-versioncreatedbysource-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-configurationbundle-versioncreatedbysource-arn"></a>
The Amazon Resource Name (ARN) of the source, if applicable (for example, a user ARN or optimization job ARN).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-configurationbundle-versioncreatedbysource-name"></a>
The name of the source (for example, `user`, `optimization-job`, or `system`).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
