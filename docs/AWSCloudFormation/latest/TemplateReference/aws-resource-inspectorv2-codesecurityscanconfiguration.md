---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspectorv2-codesecurityscanconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityScanConfiguration
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration"></a>

Creates a scan configuration for code security scanning.

## Syntax
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::InspectorV2::CodeSecurityScanConfiguration",
  "Properties" : {
      "[Configuration](#cfn-inspectorv2-codesecurityscanconfiguration-configuration)" : {{CodeSecurityScanConfiguration}},
      "[Level](#cfn-inspectorv2-codesecurityscanconfiguration-level)" : {{String}},
      "[Name](#cfn-inspectorv2-codesecurityscanconfiguration-name)" : {{String}},
      "[ScopeSettings](#cfn-inspectorv2-codesecurityscanconfiguration-scopesettings)" : {{ScopeSettings}},
      "[Tags](#cfn-inspectorv2-codesecurityscanconfiguration-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-syntax.yaml"></a>

```
Type: AWS::InspectorV2::CodeSecurityScanConfiguration
Properties:
  [Configuration](#cfn-inspectorv2-codesecurityscanconfiguration-configuration): {{
    CodeSecurityScanConfiguration}}
  [Level](#cfn-inspectorv2-codesecurityscanconfiguration-level): {{String}}
  [Name](#cfn-inspectorv2-codesecurityscanconfiguration-name): {{String}}
  [ScopeSettings](#cfn-inspectorv2-codesecurityscanconfiguration-scopesettings): {{
    ScopeSettings}}
  [Tags](#cfn-inspectorv2-codesecurityscanconfiguration-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-properties"></a>

`Configuration`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-configuration"></a>
The configuration settings for the code security scan.
*Required*: No
*Type*: [CodeSecurityScanConfiguration](aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-level"></a>
The security level for the scan configuration.
*Required*: No
*Type*: String
*Allowed values*: `ORGANIZATION | ACCOUNT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-name"></a>
The name of the scan configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_$:.]*$`
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScopeSettings`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-scopesettings"></a>
The scope settings that define which repositories will be scanned.
*Required*: No
*Type*: [ScopeSettings](aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-tags"></a>
The tags to apply to the scan configuration.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{2,127}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-return-values"></a>

### Ref
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the scan configuration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-inspectorv2-codesecurityscanconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the scan configuration.
