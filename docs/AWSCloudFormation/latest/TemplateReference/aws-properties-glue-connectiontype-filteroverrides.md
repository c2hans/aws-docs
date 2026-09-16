---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-filteroverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType FilterOverrides
<a name="aws-properties-glue-connectiontype-filteroverrides"></a>

<a name="aws-properties-glue-connectiontype-filteroverrides-description"></a>The `FilterOverrides` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-filteroverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-filteroverrides-syntax.json"></a>

```
{
  "[BetweenConfiguration](#cfn-glue-connectiontype-filteroverrides-betweenconfiguration)" : {{BetweenConfiguration}},
  "[DateTimeFormat](#cfn-glue-connectiontype-filteroverrides-datetimeformat)" : {{String}},
  "[FieldName](#cfn-glue-connectiontype-filteroverrides-fieldname)" : {{String}},
  "[OperatorMappings](#cfn-glue-connectiontype-filteroverrides-operatormappings)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-filteroverrides-syntax.yaml"></a>

```
  [BetweenConfiguration](#cfn-glue-connectiontype-filteroverrides-betweenconfiguration): {{
    BetweenConfiguration}}
  [DateTimeFormat](#cfn-glue-connectiontype-filteroverrides-datetimeformat): {{String}}
  [FieldName](#cfn-glue-connectiontype-filteroverrides-fieldname): {{String}}
  [OperatorMappings](#cfn-glue-connectiontype-filteroverrides-operatormappings): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-glue-connectiontype-filteroverrides-properties"></a>

`BetweenConfiguration`  <a name="cfn-glue-connectiontype-filteroverrides-betweenconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [BetweenConfiguration](aws-properties-glue-connectiontype-betweenconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DateTimeFormat`  <a name="cfn-glue-connectiontype-filteroverrides-datetimeformat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldName`  <a name="cfn-glue-connectiontype-filteroverrides-fieldname"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OperatorMappings`  <a name="cfn-glue-connectiontype-filteroverrides-operatormappings"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
