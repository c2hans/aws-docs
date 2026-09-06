---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsDefinitionDescriptor
<a name="aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor"></a>

Descriptor that defines an agent skills registry record and its associated content.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor-syntax.json"></a>

```
{
  "[AdditionalData](#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-additionaldata)" : {{AgentSkillsAdditionalData}},
  "[Data](#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-data)" : {{String}},
  "[DataSchemaVersion](#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-dataschemaversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor-syntax.yaml"></a>

```
  [AdditionalData](#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-additionaldata): {{
    AgentSkillsAdditionalData}}
  [Data](#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-data): {{String}}
  [DataSchemaVersion](#cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-dataschemaversion): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillsdefinitiondescriptor-properties"></a>

`AdditionalData`  <a name="cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-additionaldata"></a>
Additional data associated with the agent skills definition descriptor.
*Required*: No
*Type*: [AgentSkillsAdditionalData](aws-properties-agentregistry-registryrecord-agentskillsadditionaldata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Data`  <a name="cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-data"></a>
The agent skills definition content, serialized as descriptor payload data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSchemaVersion`  <a name="cfn-agentregistry-registryrecord-agentskillsdefinitiondescriptor-dataschemaversion"></a>
The schema version of the descriptor payload.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
