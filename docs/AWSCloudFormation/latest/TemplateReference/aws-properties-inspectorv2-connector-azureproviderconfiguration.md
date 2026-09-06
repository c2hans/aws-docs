---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-connector-azureproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector AzureProviderConfiguration
<a name="aws-properties-inspectorv2-connector-azureproviderconfiguration"></a>

<a name="aws-properties-inspectorv2-connector-azureproviderconfiguration-description"></a>The `AzureProviderConfiguration` property type specifies Property description not available. for an [AWS::InspectorV2::Connector](aws-resource-inspectorv2-connector.md).

## Syntax
<a name="aws-properties-inspectorv2-connector-azureproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-connector-azureproviderconfiguration-syntax.json"></a>

```
{
  "[AutoInstallVMScanner](#cfn-inspectorv2-connector-azureproviderconfiguration-autoinstallvmscanner)" : {{Boolean}},
  "[AwsConfigConnectorArn](#cfn-inspectorv2-connector-azureproviderconfiguration-awsconfigconnectorarn)" : {{String}},
  "[AzureRegions](#cfn-inspectorv2-connector-azureproviderconfiguration-azureregions)" : {{[ String, ... ]}},
  "[ScopeConfiguration](#cfn-inspectorv2-connector-azureproviderconfiguration-scopeconfiguration)" : {{AzureScopeConfigurationMap}}
}
```

### YAML
<a name="aws-properties-inspectorv2-connector-azureproviderconfiguration-syntax.yaml"></a>

```
  [AutoInstallVMScanner](#cfn-inspectorv2-connector-azureproviderconfiguration-autoinstallvmscanner): {{Boolean}}
  [AwsConfigConnectorArn](#cfn-inspectorv2-connector-azureproviderconfiguration-awsconfigconnectorarn): {{String}}
  [AzureRegions](#cfn-inspectorv2-connector-azureproviderconfiguration-azureregions): {{
    - String}}
  [ScopeConfiguration](#cfn-inspectorv2-connector-azureproviderconfiguration-scopeconfiguration): {{
    AzureScopeConfigurationMap}}
```

## Properties
<a name="aws-properties-inspectorv2-connector-azureproviderconfiguration-properties"></a>

`AutoInstallVMScanner`  <a name="cfn-inspectorv2-connector-azureproviderconfiguration-autoinstallvmscanner"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsConfigConnectorArn`  <a name="cfn-inspectorv2-connector-azureproviderconfiguration-awsconfigconnectorarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AzureRegions`  <a name="cfn-inspectorv2-connector-azureproviderconfiguration-azureregions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeConfiguration`  <a name="cfn-inspectorv2-connector-azureproviderconfiguration-scopeconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [AzureScopeConfigurationMap](aws-properties-inspectorv2-connector-azurescopeconfigurationmap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
