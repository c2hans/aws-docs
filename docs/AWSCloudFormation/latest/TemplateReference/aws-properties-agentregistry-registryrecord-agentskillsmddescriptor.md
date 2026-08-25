---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsMdDescriptor
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor"></a>

Markdown-format descriptor containing an agent skills document.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-syntax.json"></a>

```
{
  "[Data](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-data)" : {{String}},
  "[DataSchemaVersion](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-dataschemaversion)" : {{String}},
  "[Source](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-source)" : {{SkillMdSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-syntax.yaml"></a>

```
  [Data](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-data): {{String}}
  [DataSchemaVersion](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-dataschemaversion): {{String}}
  [Source](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-source): {{
    SkillMdSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-properties"></a>

`Data`  <a name="cfn-agentregistry-registryrecord-agentskillsmddescriptor-data"></a>
The agent skills Markdown content, serialized as descriptor payload data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSchemaVersion`  <a name="cfn-agentregistry-registryrecord-agentskillsmddescriptor-dataschemaversion"></a>
The schema version of the descriptor payload.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-agentregistry-registryrecord-agentskillsmddescriptor-source"></a>
The optional source configuration used to synchronize the agent skills Markdown content.
*Required*: No
*Type*: [SkillMdSource](aws-properties-agentregistry-registryrecord-skillmdsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
