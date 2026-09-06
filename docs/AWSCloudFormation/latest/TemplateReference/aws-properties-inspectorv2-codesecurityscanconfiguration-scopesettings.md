---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityScanConfiguration ScopeSettings
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings"></a>

The scope settings that define which repositories will be scanned. If the `ScopeSetting` parameter is `ALL` the scan configuration applies to all existing and future projects imported into Amazon Inspector.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings-syntax.json"></a>

```
{
  "[projectSelectionScope](#cfn-inspectorv2-codesecurityscanconfiguration-scopesettings-projectselectionscope)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings-syntax.yaml"></a>

```
  [projectSelectionScope](#cfn-inspectorv2-codesecurityscanconfiguration-scopesettings-projectselectionscope): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings-properties"></a>

`projectSelectionScope`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-scopesettings-projectselectionscope"></a>
The scope of projects to be selected for scanning within the integrated repositories.
*Required*: No
*Type*: String
*Allowed values*: `ALL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
