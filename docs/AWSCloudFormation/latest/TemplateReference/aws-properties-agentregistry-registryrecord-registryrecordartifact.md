---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-registryrecordartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord RegistryRecordArtifact

The skill package that the registry stores for a skill record that synchronizes a skill package.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-registryrecordartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-registryrecordartifact-syntax.json"></a>

```json
{
  "[Sha256](#cfn-agentregistry-registryrecord-registryrecordartifact-sha256)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-registryrecordartifact-syntax.yaml"></a>

```yaml
  [Sha256](#cfn-agentregistry-registryrecord-registryrecordartifact-sha256): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-registryrecordartifact-properties"></a>

`Sha256`  <a name="cfn-agentregistry-registryrecord-registryrecordartifact-sha256"></a>
The SHA-256 checksum of the stored skill package, as a lowercase hexadecimal string.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{64}$`
*Minimum*: `64`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
