---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-cloudconnectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector CloudConnectorConfiguration
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration"></a>

The configuration that provides access details and targets for connecting to a third-party cloud environment.

## Syntax
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-syntax.json"></a>

```
{
  "[AzureConfiguration](#cfn-ssm-cloudconnector-cloudconnectorconfiguration-azureconfiguration)" : {{AzureConfiguration}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-syntax.yaml"></a>

```
  [AzureConfiguration](#cfn-ssm-cloudconnector-cloudconnectorconfiguration-azureconfiguration): {{
    AzureConfiguration}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-cloudconnectorconfiguration-properties"></a>

`AzureConfiguration`  <a name="cfn-ssm-cloudconnector-cloudconnectorconfiguration-azureconfiguration"></a>
The access details and targets for connecting to a Microsoft Azure environment.
*Required*: Yes
*Type*: [AzureConfiguration](aws-properties-ssm-cloudconnector-azureconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
