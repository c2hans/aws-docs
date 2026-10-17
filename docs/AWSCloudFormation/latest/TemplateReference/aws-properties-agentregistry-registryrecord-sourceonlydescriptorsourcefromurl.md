---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::RegistryRecord SourceOnlyDescriptorSourceFromUrl
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl"></a>

The URL-based source configuration for a source-only descriptor.

## Syntax
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-syntax.json"></a>

```
{
  "[Url](#cfn-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-syntax.yaml"></a>

```
  [Url](#cfn-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-url): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-properties"></a>

`Url`  <a name="cfn-agentregistry-registryrecord-sourceonlydescriptorsourcefromurl-url"></a>
The URL from which the descriptor content is retrieved. The URL must use HTTPS.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
