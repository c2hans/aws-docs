---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-composition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Composition
<a name="aws-resource-ivs-composition"></a>

<a name="aws-resource-ivs-composition-description"></a>The `AWS::IVS::Composition` resource Property description not available. for IVS.

## Syntax
<a name="aws-resource-ivs-composition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-composition-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::Composition",
  "Properties" : {
      "[Destinations](#cfn-ivs-composition-destinations)" : {{[ DestinationConfiguration, ... ]}},
      "[Layout](#cfn-ivs-composition-layout)" : {{LayoutConfiguration}},
      "[StageArn](#cfn-ivs-composition-stagearn)" : {{String}},
      "[Tags](#cfn-ivs-composition-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ivs-composition-syntax.yaml"></a>

```
Type: AWS::IVS::Composition
Properties:
  [Destinations](#cfn-ivs-composition-destinations): {{
    - DestinationConfiguration}}
  [Layout](#cfn-ivs-composition-layout): {{
    LayoutConfiguration}}
  [StageArn](#cfn-ivs-composition-stagearn): {{String}}
  [Tags](#cfn-ivs-composition-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ivs-composition-properties"></a>

`Destinations`  <a name="cfn-ivs-composition-destinations"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [DestinationConfiguration](aws-properties-ivs-composition-destinationconfiguration.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Layout`  <a name="cfn-ivs-composition-layout"></a>
Property description not available.
*Required*: No
*Type*: [LayoutConfiguration](aws-properties-ivs-composition-layoutconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StageArn`  <a name="cfn-ivs-composition-stagearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ivs-composition-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-composition-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ivs-composition-return-values"></a>

### Ref
<a name="aws-resource-ivs-composition-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ivs-composition-return-values-fn--getatt"></a>

####
<a name="aws-resource-ivs-composition-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`StartTime`  <a name="StartTime-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.
