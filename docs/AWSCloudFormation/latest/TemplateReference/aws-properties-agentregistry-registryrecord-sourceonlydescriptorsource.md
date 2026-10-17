---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SourceOnlyDescriptorSource
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource"></a>

The source configuration for a source-only descriptor, such as an HTTP or Agent-User Interaction (AG-UI) descriptor. Unlike other descriptor sources, a source-only descriptor source doesn't support credential providers.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource-syntax.json"></a>

```
{
  "[FromUrl](#cfn-agentregistry-registryrecord-sourceonlydescriptorsource-fromurl)" : {{SourceOnlyDescriptorSourceFromUrl}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource-syntax.yaml"></a>

```
  [FromUrl](#cfn-agentregistry-registryrecord-sourceonlydescriptorsource-fromurl): {{
    SourceOnlyDescriptorSourceFromUrl}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsource-properties"></a>

`FromUrl`  <a name="cfn-agentregistry-registryrecord-sourceonlydescriptorsource-fromurl"></a>
The URL-based source for the descriptor content.
*Required*: No
*Type*: [SourceOnlyDescriptorSourceFromUrl](aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
