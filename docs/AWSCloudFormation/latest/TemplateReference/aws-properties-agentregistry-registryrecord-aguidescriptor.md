---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-aguidescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord AgUiDescriptor
<a name="aws-properties-agentregistry-registryrecord-aguidescriptor"></a>

A registry record descriptor for the Agent-User Interaction (AG-UI) protocol. This descriptor is source-only. Its content is synchronized from the configured source URL rather than supplied inline.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-aguidescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-aguidescriptor-syntax.json"></a>

```
{
  "[Source](#cfn-agentregistry-registryrecord-aguidescriptor-source)" : {{SourceOnlyDescriptorSource}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-aguidescriptor-syntax.yaml"></a>

```
  [Source](#cfn-agentregistry-registryrecord-aguidescriptor-source): {{
    SourceOnlyDescriptorSource}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-aguidescriptor-properties"></a>

`Source`  <a name="cfn-agentregistry-registryrecord-aguidescriptor-source"></a>
The source configuration from which the AG-UI descriptor content is synchronized.
*Required*: No
*Type*: [SourceOnlyDescriptorSource](aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
