---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-gcpproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 GcpProviderConfiguration

<a name="aws-properties-securityhub-connectorv2-gcpproviderconfiguration-description"></a>The `GcpProviderConfiguration` property type specifies Property description not available. for an [AWS::SecurityHub::ConnectorV2](aws-resource-securityhub-connectorv2.md).

## Syntax
<a name="aws-properties-securityhub-connectorv2-gcpproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-gcpproviderconfiguration-syntax.json"></a>

```json
{
  "[AWSConfigConnectorArn](#cfn-securityhub-connectorv2-gcpproviderconfiguration-awsconfigconnectorarn)" : {{String}},
  "[GCPRegions](#cfn-securityhub-connectorv2-gcpproviderconfiguration-gcpregions)" : {{[ String, ... ]}},
  "[ScopeConfiguration](#cfn-securityhub-connectorv2-gcpproviderconfiguration-scopeconfiguration)" : {{GcpScopeConfiguration}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-gcpproviderconfiguration-syntax.yaml"></a>

```yaml
  [AWSConfigConnectorArn](#cfn-securityhub-connectorv2-gcpproviderconfiguration-awsconfigconnectorarn): {{String}}
  [GCPRegions](#cfn-securityhub-connectorv2-gcpproviderconfiguration-gcpregions): {{
    - String}}
  [ScopeConfiguration](#cfn-securityhub-connectorv2-gcpproviderconfiguration-scopeconfiguration): {{
    GcpScopeConfiguration}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-gcpproviderconfiguration-properties"></a>

`AWSConfigConnectorArn`  <a name="cfn-securityhub-connectorv2-gcpproviderconfiguration-awsconfigconnectorarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GCPRegions`  <a name="cfn-securityhub-connectorv2-gcpproviderconfiguration-gcpregions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeConfiguration`  <a name="cfn-securityhub-connectorv2-gcpproviderconfiguration-scopeconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [GcpScopeConfiguration](aws-properties-securityhub-connectorv2-gcpscopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
