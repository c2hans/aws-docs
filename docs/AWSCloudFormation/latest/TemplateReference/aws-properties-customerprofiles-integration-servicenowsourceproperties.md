---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-servicenowsourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration ServiceNowSourceProperties
<a name="aws-properties-customerprofiles-integration-servicenowsourceproperties"></a>

The properties that are applied when ServiceNow is being used as a source.

## Syntax
<a name="aws-properties-customerprofiles-integration-servicenowsourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-servicenowsourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-customerprofiles-integration-servicenowsourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-servicenowsourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-customerprofiles-integration-servicenowsourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-servicenowsourceproperties-properties"></a>

`Object`  <a name="cfn-customerprofiles-integration-servicenowsourceproperties-object"></a>
The object specified in the ServiceNow flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
