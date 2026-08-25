---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-descriptorsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord DescriptorSource
<a name="aws-properties-agentregistry-registryrecord-descriptorsource"></a>

The source configuration that defines where descriptor content is retrieved from.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-descriptorsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-descriptorsource-syntax.json"></a>

```
{
  "[FromUrl](#cfn-agentregistry-registryrecord-descriptorsource-fromurl)" : {{DescriptorSourceFromUrl}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-descriptorsource-syntax.yaml"></a>

```
  [FromUrl](#cfn-agentregistry-registryrecord-descriptorsource-fromurl): {{
    DescriptorSourceFromUrl}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-descriptorsource-properties"></a>

`FromUrl`  <a name="cfn-agentregistry-registryrecord-descriptorsource-fromurl"></a>
URL-based descriptor source, populated when descriptor content is synchronized from a URL.
*Required*: No
*Type*: [DescriptorSourceFromUrl](aws-properties-agentregistry-registryrecord-descriptorsourcefromurl.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
