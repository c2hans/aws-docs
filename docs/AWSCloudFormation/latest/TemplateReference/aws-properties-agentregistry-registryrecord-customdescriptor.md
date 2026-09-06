---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-customdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord CustomDescriptor
<a name="aws-properties-agentregistry-registryrecord-customdescriptor"></a>

Descriptor that defines the content of a custom registry record.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-customdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-customdescriptor-syntax.json"></a>

```
{
  "[Data](#cfn-agentregistry-registryrecord-customdescriptor-data)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-customdescriptor-syntax.yaml"></a>

```
  [Data](#cfn-agentregistry-registryrecord-customdescriptor-data): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-customdescriptor-properties"></a>

`Data`  <a name="cfn-agentregistry-registryrecord-customdescriptor-data"></a>
The custom descriptor content, serialized as descriptor payload data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `102400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
