---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillsadditionaldata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsAdditionalData
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata"></a>

Additional data associated with an agent skills definition descriptor.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-syntax.json"></a>

```
{
  "[SkillMd](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd)" : {{AgentSkillsMdDescriptor}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-syntax.yaml"></a>

```
  [SkillMd](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd): {{
    AgentSkillsMdDescriptor}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-properties"></a>

`SkillMd`  <a name="cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd"></a>
The Markdown skill content associated with the agent skills definition.
*Required*: No
*Type*: [AgentSkillsMdDescriptor](aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
