---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connector-azureproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Connector AzureProviderConfiguration
<a name="aws-properties-securityhub-connector-azureproviderconfiguration"></a>

The configuration for connecting to an Azure environment.

## Syntax
<a name="aws-properties-securityhub-connector-azureproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connector-azureproviderconfiguration-syntax.json"></a>

```
{
  "[AWSConfigConnectorArn](#cfn-securityhub-connector-azureproviderconfiguration-awsconfigconnectorarn)" : {{String}},
  "[AzureRegions](#cfn-securityhub-connector-azureproviderconfiguration-azureregions)" : {{[ String, ... ]}},
  "[ScopeConfiguration](#cfn-securityhub-connector-azureproviderconfiguration-scopeconfiguration)" : {{AzureScopeConfiguration}}
}
```

### YAML
<a name="aws-properties-securityhub-connector-azureproviderconfiguration-syntax.yaml"></a>

```
  [AWSConfigConnectorArn](#cfn-securityhub-connector-azureproviderconfiguration-awsconfigconnectorarn): {{String}}
  [AzureRegions](#cfn-securityhub-connector-azureproviderconfiguration-azureregions): {{
    - String}}
  [ScopeConfiguration](#cfn-securityhub-connector-azureproviderconfiguration-scopeconfiguration): {{
    AzureScopeConfiguration}}
```

## Properties
<a name="aws-properties-securityhub-connector-azureproviderconfiguration-properties"></a>

`AWSConfigConnectorArn`  <a name="cfn-securityhub-connector-azureproviderconfiguration-awsconfigconnectorarn"></a>
The ARN of the multi-cloud configuration connector used to establish the connection to Azure.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AzureRegions`  <a name="cfn-securityhub-connector-azureproviderconfiguration-azureregions"></a>
The list of Azure regions to monitor.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeConfiguration`  <a name="cfn-securityhub-connector-azureproviderconfiguration-scopeconfiguration"></a>
The scope configuration that defines which Azure resources are monitored.
*Required*: Yes
*Type*: [AzureScopeConfiguration](aws-properties-securityhub-connector-azurescopeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
