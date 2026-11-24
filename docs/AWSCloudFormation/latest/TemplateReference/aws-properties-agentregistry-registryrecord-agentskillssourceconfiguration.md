---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-agentskillssourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgentSkillsSourceConfiguration

The provider-specific settings of a skill source. Specify the member that matches the source's provider, such as `S3` for an Amazon S3 source.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-agentskillssourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-agentskillssourceconfiguration-syntax.json"></a>

```json
{
  "[S3](#cfn-agentregistry-registryrecord-agentskillssourceconfiguration-s3)" : {{S3SourceConfiguration}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-agentskillssourceconfiguration-syntax.yaml"></a>

```yaml
  [S3](#cfn-agentregistry-registryrecord-agentskillssourceconfiguration-s3): {{
    S3SourceConfiguration}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-agentskillssourceconfiguration-properties"></a>

`S3`  <a name="cfn-agentregistry-registryrecord-agentskillssourceconfiguration-s3"></a>
The settings of an Amazon S3 source.
*Required*: Yes
*Type*: [S3SourceConfiguration](aws-properties-agentregistry-registryrecord-s3sourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
