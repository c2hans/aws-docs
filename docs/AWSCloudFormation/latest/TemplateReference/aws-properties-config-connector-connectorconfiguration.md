---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-connector-connectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::Connector ConnectorConfiguration
<a name="aws-properties-config-connector-connectorconfiguration"></a>

The provider-specific configuration for connecting to the third-party cloud service provider. You must specify exactly one provider configuration.

## Syntax
<a name="aws-properties-config-connector-connectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-connector-connectorconfiguration-syntax.json"></a>

```
{
  "[Azure](#cfn-config-connector-connectorconfiguration-azure)" : {{AzureConnectorConfiguration}}
}
```

### YAML
<a name="aws-properties-config-connector-connectorconfiguration-syntax.yaml"></a>

```
  [Azure](#cfn-config-connector-connectorconfiguration-azure): {{
    AzureConnectorConfiguration}}
```

## Properties
<a name="aws-properties-config-connector-connectorconfiguration-properties"></a>

`Azure`  <a name="cfn-config-connector-connectorconfiguration-azure"></a>
The configuration for an Azure connector.
*Required*: No
*Type*: [AzureConnectorConfiguration](aws-properties-config-connector-azureconnectorconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
