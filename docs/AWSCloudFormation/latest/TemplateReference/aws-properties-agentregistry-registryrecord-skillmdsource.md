---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-skillmdsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SkillMdSource

The source that the registry synchronizes agent skills content from. Both `SkillMd.Source` and `SkillPackage.Source` use this type.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-syntax.json"></a>

```json
{
  "[FromUrl](#cfn-agentregistry-registryrecord-skillmdsource-fromurl)" : {{SkillMdSourceFromUrl}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-syntax.yaml"></a>

```yaml
  [FromUrl](#cfn-agentregistry-registryrecord-skillmdsource-fromurl): {{
    SkillMdSourceFromUrl}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-skillmdsource-properties"></a>

`FromUrl`  <a name="cfn-agentregistry-registryrecord-skillmdsource-fromurl"></a>
The URL-based source of the agent skills content.
*Required*: No
*Type*: [SkillMdSourceFromUrl](aws-properties-agentregistry-registryrecord-skillmdsourcefromurl.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
