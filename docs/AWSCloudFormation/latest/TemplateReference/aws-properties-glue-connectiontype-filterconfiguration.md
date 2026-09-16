---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-filterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType FilterConfiguration
<a name="aws-properties-glue-connectiontype-filterconfiguration"></a>

<a name="aws-properties-glue-connectiontype-filterconfiguration-description"></a>The `FilterConfiguration` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-filterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-filterconfiguration-syntax.json"></a>

```
{
  "[BetweenConfiguration](#cfn-glue-connectiontype-filterconfiguration-betweenconfiguration)" : {{BetweenConfiguration}},
  "[DateTimeFormat](#cfn-glue-connectiontype-filterconfiguration-datetimeformat)" : {{String}},
  "[FilterMode](#cfn-glue-connectiontype-filterconfiguration-filtermode)" : {{String}},
  "[FilterStringConfiguration](#cfn-glue-connectiontype-filterconfiguration-filterstringconfiguration)" : {{FilterStringConfiguration}},
  "[OperatorMappings](#cfn-glue-connectiontype-filterconfiguration-operatormappings)" : {{{{{Key}}: {{Value}}, ...}}},
  "[StripQuotes](#cfn-glue-connectiontype-filterconfiguration-stripquotes)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-filterconfiguration-syntax.yaml"></a>

```
  [BetweenConfiguration](#cfn-glue-connectiontype-filterconfiguration-betweenconfiguration): {{
    BetweenConfiguration}}
  [DateTimeFormat](#cfn-glue-connectiontype-filterconfiguration-datetimeformat): {{String}}
  [FilterMode](#cfn-glue-connectiontype-filterconfiguration-filtermode): {{String}}
  [FilterStringConfiguration](#cfn-glue-connectiontype-filterconfiguration-filterstringconfiguration): {{
    FilterStringConfiguration}}
  [OperatorMappings](#cfn-glue-connectiontype-filterconfiguration-operatormappings): {{
    {{Key}}: {{Value}}}}
  [StripQuotes](#cfn-glue-connectiontype-filterconfiguration-stripquotes): {{Boolean}}
```

## Properties
<a name="aws-properties-glue-connectiontype-filterconfiguration-properties"></a>

`BetweenConfiguration`  <a name="cfn-glue-connectiontype-filterconfiguration-betweenconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [BetweenConfiguration](aws-properties-glue-connectiontype-betweenconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DateTimeFormat`  <a name="cfn-glue-connectiontype-filterconfiguration-datetimeformat"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterMode`  <a name="cfn-glue-connectiontype-filterconfiguration-filtermode"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `QUERY_PARAMS | FILTER_STRING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilterStringConfiguration`  <a name="cfn-glue-connectiontype-filterconfiguration-filterstringconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FilterStringConfiguration](aws-properties-glue-connectiontype-filterstringconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OperatorMappings`  <a name="cfn-glue-connectiontype-filterconfiguration-operatormappings"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StripQuotes`  <a name="cfn-glue-connectiontype-filterconfiguration-stripquotes"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
