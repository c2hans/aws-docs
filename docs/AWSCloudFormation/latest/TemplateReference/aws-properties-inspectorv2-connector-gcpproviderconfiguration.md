---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-connector-gcpproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector GcpProviderConfiguration

<a name="aws-properties-inspectorv2-connector-gcpproviderconfiguration-description"></a>The `GcpProviderConfiguration` property type specifies Property description not available. for an [AWS::InspectorV2::Connector](aws-resource-inspectorv2-connector.md).

## Syntax
<a name="aws-properties-inspectorv2-connector-gcpproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-connector-gcpproviderconfiguration-syntax.json"></a>

```json
{
  "[AutoInstallVMScanner](#cfn-inspectorv2-connector-gcpproviderconfiguration-autoinstallvmscanner)" : {{Boolean}},
  "[AwsConfigConnectorArn](#cfn-inspectorv2-connector-gcpproviderconfiguration-awsconfigconnectorarn)" : {{String}},
  "[GcpRegions](#cfn-inspectorv2-connector-gcpproviderconfiguration-gcpregions)" : {{[ String, ... ]}},
  "[ScopeConfiguration](#cfn-inspectorv2-connector-gcpproviderconfiguration-scopeconfiguration)" : {{GcpScopeConfigurationMap}}
}
```

### YAML
<a name="aws-properties-inspectorv2-connector-gcpproviderconfiguration-syntax.yaml"></a>

```yaml
  [AutoInstallVMScanner](#cfn-inspectorv2-connector-gcpproviderconfiguration-autoinstallvmscanner): {{Boolean}}
  [AwsConfigConnectorArn](#cfn-inspectorv2-connector-gcpproviderconfiguration-awsconfigconnectorarn): {{String}}
  [GcpRegions](#cfn-inspectorv2-connector-gcpproviderconfiguration-gcpregions): {{
    - String}}
  [ScopeConfiguration](#cfn-inspectorv2-connector-gcpproviderconfiguration-scopeconfiguration): {{
    GcpScopeConfigurationMap}}
```

## Properties
<a name="aws-properties-inspectorv2-connector-gcpproviderconfiguration-properties"></a>

`AutoInstallVMScanner`  <a name="cfn-inspectorv2-connector-gcpproviderconfiguration-autoinstallvmscanner"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsConfigConnectorArn`  <a name="cfn-inspectorv2-connector-gcpproviderconfiguration-awsconfigconnectorarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GcpRegions`  <a name="cfn-inspectorv2-connector-gcpproviderconfiguration-gcpregions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeConfiguration`  <a name="cfn-inspectorv2-connector-gcpproviderconfiguration-scopeconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [GcpScopeConfigurationMap](aws-properties-inspectorv2-connector-gcpscopeconfigurationmap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
