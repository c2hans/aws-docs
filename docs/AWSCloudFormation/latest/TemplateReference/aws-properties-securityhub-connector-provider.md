---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connector-provider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Connector Provider

<a name="aws-properties-securityhub-connector-provider-description"></a>The `Provider` property type specifies Property description not available. for an [AWS::SecurityHub::Connector](aws-resource-securityhub-connector.md).

## Syntax
<a name="aws-properties-securityhub-connector-provider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connector-provider-syntax.json"></a>

```json
{
  "[Azure](#cfn-securityhub-connector-provider-azure)" : {{AzureProviderConfiguration}},
  "[GCP](#cfn-securityhub-connector-provider-gcp)" : {{GcpProviderConfiguration}}
}
```

### YAML
<a name="aws-properties-securityhub-connector-provider-syntax.yaml"></a>

```yaml
  [Azure](#cfn-securityhub-connector-provider-azure): {{
    AzureProviderConfiguration}}
  [GCP](#cfn-securityhub-connector-provider-gcp): {{
    GcpProviderConfiguration}}
```

## Properties
<a name="aws-properties-securityhub-connector-provider-properties"></a>

`Azure`  <a name="cfn-securityhub-connector-provider-azure"></a>
Property description not available.
*Required*: No
*Type*: [AzureProviderConfiguration](aws-properties-securityhub-connector-azureproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GCP`  <a name="cfn-securityhub-connector-provider-gcp"></a>
Property description not available.
*Required*: No
*Type*: [GcpProviderConfiguration](aws-properties-securityhub-connector-gcpproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
