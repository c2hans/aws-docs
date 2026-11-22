---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-connector-connectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::Connector ConnectorConfiguration

Configuration for connecting to a third-party cloud service provider. You must specify exactly one provider configuration: `Azure` or `Gcp`.

## Syntax
<a name="aws-properties-config-connector-connectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-connector-connectorconfiguration-syntax.json"></a>

```json
{
  "[Azure](#cfn-config-connector-connectorconfiguration-azure)" : {{AzureConnectorConfiguration}},
  "[Gcp](#cfn-config-connector-connectorconfiguration-gcp)" : {{GcpConnectorConfiguration}}
}
```

### YAML
<a name="aws-properties-config-connector-connectorconfiguration-syntax.yaml"></a>

```yaml
  [Azure](#cfn-config-connector-connectorconfiguration-azure): {{
    AzureConnectorConfiguration}}
  [Gcp](#cfn-config-connector-connectorconfiguration-gcp): {{
    GcpConnectorConfiguration}}
```

## Properties
<a name="aws-properties-config-connector-connectorconfiguration-properties"></a>

`Azure`  <a name="cfn-config-connector-connectorconfiguration-azure"></a>
The configuration for an Azure connector.
*Required*: No
*Type*: [AzureConnectorConfiguration](aws-properties-config-connector-azureconnectorconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Gcp`  <a name="cfn-config-connector-connectorconfiguration-gcp"></a>
The configuration for a Google Cloud connector.
*Required*: No
*Type*: [GcpConnectorConfiguration](aws-properties-config-connector-gcpconnectorconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
