---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-zendesksourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration ZendeskSourceProperties
<a name="aws-properties-customerprofiles-integration-zendesksourceproperties"></a>

The properties that are applied when using Zendesk as a flow source.

## Syntax
<a name="aws-properties-customerprofiles-integration-zendesksourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-zendesksourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-customerprofiles-integration-zendesksourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-zendesksourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-customerprofiles-integration-zendesksourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-zendesksourceproperties-properties"></a>

`Object`  <a name="cfn-customerprofiles-integration-zendesksourceproperties-object"></a>
The object specified in the Zendesk flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
