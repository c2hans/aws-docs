---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityScanConfiguration ContinuousIntegrationScanConfiguration
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration"></a>

Configuration settings for continuous integration scans that run automatically when code changes are made.

## Syntax
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-syntax.json"></a>

```
{
  "[supportedEvents](#cfn-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-supportedevents)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-syntax.yaml"></a>

```
  [supportedEvents](#cfn-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-supportedevents): {{
    - String}}
```

## Properties
<a name="aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-properties"></a>

`supportedEvents`  <a name="cfn-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-supportedevents"></a>
The repository events that trigger continuous integration scans, such as pull requests or commits.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
