---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-cloudconnectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector CloudConnectorConfiguration
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration"></a>

The configuration for the cloud connector. Currently supports Azure.

## Syntax
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-syntax.json"></a>

```
{
  "[AzureConfiguration](#cfn-ssm-cloudconnector-cloudconnectorconfiguration-azureconfiguration)" : {{AzureConfiguration}},
  "[GcpConfiguration](#cfn-ssm-cloudconnector-cloudconnectorconfiguration-gcpconfiguration)" : {{GcpConfiguration}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-syntax.yaml"></a>

```
  [AzureConfiguration](#cfn-ssm-cloudconnector-cloudconnectorconfiguration-azureconfiguration): {{
    AzureConfiguration}}
  [GcpConfiguration](#cfn-ssm-cloudconnector-cloudconnectorconfiguration-gcpconfiguration): {{
    GcpConfiguration}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-properties"></a>

`AzureConfiguration`  <a name="cfn-ssm-cloudconnector-cloudconnectorconfiguration-azureconfiguration"></a>
The Azure connection configuration.
*Required*: No
*Type*: [AzureConfiguration](aws-properties-ssm-cloudconnector-azureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GcpConfiguration`  <a name="cfn-ssm-cloudconnector-cloudconnectorconfiguration-gcpconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [GcpConfiguration](aws-properties-ssm-cloudconnector-gcpconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
