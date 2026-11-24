---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsMdDescriptor

Markdown-format descriptor containing an agent skills document.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-syntax.json"></a>

```json
{
  "[Data](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-data)" : {{String}},
  "[DataSchemaVersion](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-dataschemaversion)" : {{String}},
  "[Source](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-source)" : {{SkillMdSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-syntax.yaml"></a>

```yaml
  [Data](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-data): {{String}}
  [DataSchemaVersion](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-dataschemaversion): {{String}}
  [Source](#cfn-agentregistry-registryrecord-agentskillsmddescriptor-source): {{
    SkillMdSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillsmddescriptor-properties"></a>

`Data`  <a name="cfn-agentregistry-registryrecord-agentskillsmddescriptor-data"></a>
The agent skills Markdown content, serialized as descriptor payload data.
Don't set this property when `Source` or `SkillPackage` names an Amazon S3 source. Each synchronization replaces it with the content of the source's SKILL.md.
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
The source that the registry synchronizes the SKILL.md document from. Specify an `s3://` URL of a SKILL.md object in Amazon S3. You can't set this property together with `SkillPackage`.
*Required*: No
*Type*: [SkillMdSource](aws-properties-agentregistry-registryrecord-skillmdsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
