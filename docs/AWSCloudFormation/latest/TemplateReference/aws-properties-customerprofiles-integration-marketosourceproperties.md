---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-marketosourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration MarketoSourceProperties
<a name="aws-properties-customerprofiles-integration-marketosourceproperties"></a>

The properties that are applied when Marketo is being used as a source.

## Syntax
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-customerprofiles-integration-marketosourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-customerprofiles-integration-marketosourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-marketosourceproperties-properties"></a>

`Object`  <a name="cfn-customerprofiles-integration-marketosourceproperties-object"></a>
The object specified in the Marketo flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
