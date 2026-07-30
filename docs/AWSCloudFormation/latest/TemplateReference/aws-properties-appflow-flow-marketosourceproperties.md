---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-marketosourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow MarketoSourceProperties
<a name="aws-properties-appflow-flow-marketosourceproperties"></a>

 The properties that are applied when Marketo is being used as a source.

## Syntax
<a name="aws-properties-appflow-flow-marketosourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-marketosourceproperties-syntax.json"></a>

```
{
  "[Object](#cfn-appflow-flow-marketosourceproperties-object)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-flow-marketosourceproperties-syntax.yaml"></a>

```
  [Object](#cfn-appflow-flow-marketosourceproperties-object): {{String}}
```

## Properties
<a name="aws-properties-appflow-flow-marketosourceproperties-properties"></a>

`Object`  <a name="cfn-appflow-flow-marketosourceproperties-object"></a>
 The object specified in the Marketo flow source.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-marketosourceproperties--seealso"></a>
+ [MarketoSourceProperties](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_MarketoSourceProperties.html) in the *Amazon AppFlow API Reference*.
