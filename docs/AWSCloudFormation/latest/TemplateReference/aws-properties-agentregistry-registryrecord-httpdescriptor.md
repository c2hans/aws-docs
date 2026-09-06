---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-httpdescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord HttpDescriptor
<a name="aws-properties-agentregistry-registryrecord-httpdescriptor"></a>

A registry record descriptor for the HTTP protocol. This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-httpdescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-httpdescriptor-syntax.json"></a>

```
{
  "[Source](#cfn-agentregistry-registryrecord-httpdescriptor-source)" : {{SourceOnlyDescriptorSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-httpdescriptor-syntax.yaml"></a>

```
  [Source](#cfn-agentregistry-registryrecord-httpdescriptor-source): {{
    SourceOnlyDescriptorSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-httpdescriptor-properties"></a>

`Source`  <a name="cfn-agentregistry-registryrecord-httpdescriptor-source"></a>
Property description not available.
*Required*: No
*Type*: [SourceOnlyDescriptorSource](aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
