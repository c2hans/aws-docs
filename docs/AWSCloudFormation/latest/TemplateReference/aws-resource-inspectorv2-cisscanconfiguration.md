---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspectorv2-cisscanconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CisScanConfiguration
<a name="aws-resource-inspectorv2-cisscanconfiguration"></a>

The CIS scan configuration.

## Syntax
<a name="aws-resource-inspectorv2-cisscanconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-inspectorv2-cisscanconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::InspectorV2::CisScanConfiguration",
  "Properties" : {
      "[ScanName](#cfn-inspectorv2-cisscanconfiguration-scanname)" : {{String}},
      "[Schedule](#cfn-inspectorv2-cisscanconfiguration-schedule)" : {{Schedule}},
      "[SecurityLevel](#cfn-inspectorv2-cisscanconfiguration-securitylevel)" : {{String}},
      "[Tags](#cfn-inspectorv2-cisscanconfiguration-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Targets](#cfn-inspectorv2-cisscanconfiguration-targets)" : {{CisTargets}}
    }
}
```

### YAML
<a name="aws-resource-inspectorv2-cisscanconfiguration-syntax.yaml"></a>

```
Type: AWS::InspectorV2::CisScanConfiguration
Properties:
  [ScanName](#cfn-inspectorv2-cisscanconfiguration-scanname): {{String}}
  [Schedule](#cfn-inspectorv2-cisscanconfiguration-schedule): {{
    Schedule}}
  [SecurityLevel](#cfn-inspectorv2-cisscanconfiguration-securitylevel): {{String}}
  [Tags](#cfn-inspectorv2-cisscanconfiguration-tags): {{
    {{Key}}: {{Value}}}}
  [Targets](#cfn-inspectorv2-cisscanconfiguration-targets): {{
    CisTargets}}
```

## Properties
<a name="aws-resource-inspectorv2-cisscanconfiguration-properties"></a>

`ScanName`  <a name="cfn-inspectorv2-cisscanconfiguration-scanname"></a>
The name of the CIS scan configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-inspectorv2-cisscanconfiguration-schedule"></a>
The CIS scan configuration's schedule.
*Required*: Yes
*Type*: [Schedule](aws-properties-inspectorv2-cisscanconfiguration-schedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityLevel`  <a name="cfn-inspectorv2-cisscanconfiguration-securitylevel"></a>
The CIS scan configuration's CIS Benchmark level.
*Required*: Yes
*Type*: String
*Allowed values*: `LEVEL_1 | LEVEL_2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-inspectorv2-cisscanconfiguration-tags"></a>
The CIS scan configuration's tags.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{2,127}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Targets`  <a name="cfn-inspectorv2-cisscanconfiguration-targets"></a>
The CIS scan configuration's targets.
*Required*: Yes
*Type*: [CisTargets](aws-properties-inspectorv2-cisscanconfiguration-cistargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-inspectorv2-cisscanconfiguration-return-values"></a>

### Ref
<a name="aws-resource-inspectorv2-cisscanconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the CIS scan configuration. For example:

 `arn:aws:inspector2:us-east-1:012345678901:owner/012345678901/cis-configuration/c1c0fe5d28e39baa`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-inspectorv2-cisscanconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-inspectorv2-cisscanconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The CIS scan configuration's scan configuration ARN.
