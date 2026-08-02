---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration CisTargets
<a name="aws-properties-inspectorv2-cisscanconfiguration-cistargets"></a>

The CIS targets.

## Syntax
<a name="aws-properties-inspectorv2-cisscanconfiguration-cistargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-cisscanconfiguration-cistargets-syntax.json"></a>

```
{
  "[AccountIds](#cfn-inspectorv2-cisscanconfiguration-cistargets-accountids)" : {{[ String, ... ]}},
  "[TargetResourceTags](#cfn-inspectorv2-cisscanconfiguration-cistargets-targetresourcetags)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-inspectorv2-cisscanconfiguration-cistargets-syntax.yaml"></a>

```
  [AccountIds](#cfn-inspectorv2-cisscanconfiguration-cistargets-accountids): {{
    - String}}
  [TargetResourceTags](#cfn-inspectorv2-cisscanconfiguration-cistargets-targetresourcetags): {{
    - String}}
```

## Properties
<a name="aws-properties-inspectorv2-cisscanconfiguration-cistargets-properties"></a>

`AccountIds`  <a name="cfn-inspectorv2-cisscanconfiguration-cistargets-accountids"></a>
The CIS target account ids.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetResourceTags`  <a name="cfn-inspectorv2-cisscanconfiguration-cistargets-targetresourcetags"></a>
The CIS target resource tags.
*Required*: Yes
*Type*: Array of String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
