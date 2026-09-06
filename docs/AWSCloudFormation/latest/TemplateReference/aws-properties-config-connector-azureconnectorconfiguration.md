---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-connector-azureconnectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::Connector AzureConnectorConfiguration
<a name="aws-properties-config-connector-azureconnectorconfiguration"></a>

The configuration details for connecting to Microsoft Azure.

## Syntax
<a name="aws-properties-config-connector-azureconnectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-connector-azureconnectorconfiguration-syntax.json"></a>

```
{
  "[ClientIdentifier](#cfn-config-connector-azureconnectorconfiguration-clientidentifier)" : {{String}},
  "[TenantIdentifier](#cfn-config-connector-azureconnectorconfiguration-tenantidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-connector-azureconnectorconfiguration-syntax.yaml"></a>

```
  [ClientIdentifier](#cfn-config-connector-azureconnectorconfiguration-clientidentifier): {{String}}
  [TenantIdentifier](#cfn-config-connector-azureconnectorconfiguration-tenantidentifier): {{String}}
```

## Properties
<a name="aws-properties-config-connector-azureconnectorconfiguration-properties"></a>

`ClientIdentifier`  <a name="cfn-config-connector-azureconnectorconfiguration-clientidentifier"></a>
The Azure client identifier.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TenantIdentifier`  <a name="cfn-config-connector-azureconnectorconfiguration-tenantidentifier"></a>
The Azure tenant identifier.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
