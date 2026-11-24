---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillspackagedescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsPackageDescriptor

The skill package descriptor. It names the source that the registry synchronizes a skill package from. A skill package is a ZIP archive that follows the Agent Skills specification.

The registry validates the package, stores it, and sets `SkillMd.Data` from the package's SKILL.md.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillspackagedescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillspackagedescriptor-syntax.json"></a>

```json
{
  "[Source](#cfn-agentregistry-registryrecord-agentskillspackagedescriptor-source)" : {{SkillMdSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillspackagedescriptor-syntax.yaml"></a>

```yaml
  [Source](#cfn-agentregistry-registryrecord-agentskillspackagedescriptor-source): {{
    SkillMdSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillspackagedescriptor-properties"></a>

`Source`  <a name="cfn-agentregistry-registryrecord-agentskillspackagedescriptor-source"></a>
The source of the skill package, as an `s3://` URL of a ZIP object in Amazon S3.
*Required*: No
*Type*: [SkillMdSource](aws-properties-agentregistry-registryrecord-skillmdsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
