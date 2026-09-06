---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-pardotsourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow PardotSourceProperties
<a name="aws-properties-appflow-flow-pardotsourceproperties"></a>

The properties that are applied when Salesforce Pardot is being used as a source.

## Syntax
<a name="aws-properties-appflow-flow-pardotsourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-pardotsourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-appflow-flow-pardotsourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-pardotsourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-appflow-flow-pardotsourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-pardotsourceproperties-properties"></a>

`Object`  <a name="cfn-appflow-flow-pardotsourceproperties-object"></a>
The object specified in the Salesforce Pardot flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
