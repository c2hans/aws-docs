---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillsadditionaldata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsAdditionalData

Additional data associated with an agent skills definition descriptor.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-syntax.json"></a>

```json
{
  "[SkillMd](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd)" : {{AgentSkillsMdDescriptor}},
  "[SkillPackage](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillpackage)" : {{AgentSkillsPackageDescriptor}},
  "[SourceConfiguration](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-sourceconfiguration)" : {{AgentSkillsSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-syntax.yaml"></a>

```yaml
  [SkillMd](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd): {{
    AgentSkillsMdDescriptor}}
  [SkillPackage](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillpackage): {{
    AgentSkillsPackageDescriptor}}
  [SourceConfiguration](#cfn-agentregistry-registryrecord-agentskillsadditionaldata-sourceconfiguration): {{
    AgentSkillsSourceConfiguration}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillsadditionaldata-properties"></a>

`SkillMd`  <a name="cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillmd"></a>
The Markdown skill content associated with the agent skills definition.
*Required*: No
*Type*: [AgentSkillsMdDescriptor](aws-properties-agentregistry-registryrecord-agentskillsmddescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkillPackage`  <a name="cfn-agentregistry-registryrecord-agentskillsadditionaldata-skillpackage"></a>
The source that the registry synchronizes a full skill package from. The registry validates and stores the package, and sets `SkillMd.Data` from the package's SKILL.md.
You can't set this property together with `SkillMd.Source` or `SkillMd.Data`.
*Required*: No
*Type*: [AgentSkillsPackageDescriptor](aws-properties-agentregistry-registryrecord-agentskillspackagedescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceConfiguration`  <a name="cfn-agentregistry-registryrecord-agentskillsadditionaldata-sourceconfiguration"></a>
The provider-specific settings of the record's skill source. For an Amazon S3 source, `S3.BucketOwnerAccountId` specifies the AWS account that owns the source bucket.
*Required*: No
*Type*: [AgentSkillsSourceConfiguration](aws-properties-agentregistry-registryrecord-agentskillssourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
