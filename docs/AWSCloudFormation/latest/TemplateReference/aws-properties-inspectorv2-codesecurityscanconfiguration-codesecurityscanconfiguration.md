---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityScanConfiguration CodeSecurityScanConfiguration
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration"></a>

Contains the configuration settings for code security scans.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-syntax.json"></a>

```
{
  "[continuousIntegrationScanConfiguration](#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-continuousintegrationscanconfiguration)" : {{ContinuousIntegrationScanConfiguration}},
  "[periodicScanConfiguration](#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-periodicscanconfiguration)" : {{PeriodicScanConfiguration}},
  "[ruleSetCategories](#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-rulesetcategories)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-syntax.yaml"></a>

```
  [continuousIntegrationScanConfiguration](#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-continuousintegrationscanconfiguration): {{
    ContinuousIntegrationScanConfiguration}}
  [periodicScanConfiguration](#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-periodicscanconfiguration): {{
    PeriodicScanConfiguration}}
  [ruleSetCategories](#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-rulesetcategories): {{
    - String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-properties"></a>

`continuousIntegrationScanConfiguration`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-continuousintegrationscanconfiguration"></a>
Configuration settings for continuous integration scans that run automatically when code changes are made.
*Required*: No
*Type*: [ContinuousIntegrationScanConfiguration](aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`periodicScanConfiguration`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-periodicscanconfiguration"></a>
Configuration settings for periodic scans that run on a scheduled basis.
*Required*: No
*Type*: [PeriodicScanConfiguration](aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ruleSetCategories`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-rulesetcategories"></a>
The categories of security rules to be applied during the scan.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
