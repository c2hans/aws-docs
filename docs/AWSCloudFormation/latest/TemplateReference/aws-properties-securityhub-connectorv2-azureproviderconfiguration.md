---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-azureproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 AzureProviderConfiguration
<a name="aws-properties-securityhub-connectorv2-azureproviderconfiguration"></a>

The configuration for connecting to an Azure environment.

## Syntax
<a name="aws-properties-securityhub-connectorv2-azureproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-azureproviderconfiguration-syntax.json"></a>

```
{
  "[AWSConfigConnectorArn](#cfn-securityhub-connectorv2-azureproviderconfiguration-awsconfigconnectorarn)" : {{String}},
  "[AzureRegions](#cfn-securityhub-connectorv2-azureproviderconfiguration-azureregions)" : {{[ String, ... ]}},
  "[ScopeConfiguration](#cfn-securityhub-connectorv2-azureproviderconfiguration-scopeconfiguration)" : {{AzureScopeConfiguration}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-azureproviderconfiguration-syntax.yaml"></a>

```
  [AWSConfigConnectorArn](#cfn-securityhub-connectorv2-azureproviderconfiguration-awsconfigconnectorarn): {{String}}
  [AzureRegions](#cfn-securityhub-connectorv2-azureproviderconfiguration-azureregions): {{
    - String}}
  [ScopeConfiguration](#cfn-securityhub-connectorv2-azureproviderconfiguration-scopeconfiguration): {{
    AzureScopeConfiguration}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-azureproviderconfiguration-properties"></a>

`AWSConfigConnectorArn`  <a name="cfn-securityhub-connectorv2-azureproviderconfiguration-awsconfigconnectorarn"></a>
The ARN of the multi-cloud configuration connector used to establish the connection to Azure.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AzureRegions`  <a name="cfn-securityhub-connectorv2-azureproviderconfiguration-azureregions"></a>
The list of Azure regions to monitor.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeConfiguration`  <a name="cfn-securityhub-connectorv2-azureproviderconfiguration-scopeconfiguration"></a>
The scope configuration that defines which Azure resources are monitored.
*Required*: Yes
*Type*: [AzureScopeConfiguration](aws-properties-securityhub-connectorv2-azurescopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
