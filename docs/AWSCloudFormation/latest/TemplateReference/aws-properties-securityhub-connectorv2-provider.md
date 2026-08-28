---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-provider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 Provider
<a name="aws-properties-securityhub-connectorv2-provider"></a>

The third-party provider detail for a service configuration.

## Syntax
<a name="aws-properties-securityhub-connectorv2-provider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-provider-syntax.json"></a>

```
{
  "[Azure](#cfn-securityhub-connectorv2-provider-azure)" : {{AzureProviderConfiguration}},
  "[JiraCloud](#cfn-securityhub-connectorv2-provider-jiracloud)" : {{JiraCloudProviderConfiguration}},
  "[ServiceNow](#cfn-securityhub-connectorv2-provider-servicenow)" : {{ServiceNowProviderConfiguration}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-provider-syntax.yaml"></a>

```
  [Azure](#cfn-securityhub-connectorv2-provider-azure): {{
    AzureProviderConfiguration}}
  [JiraCloud](#cfn-securityhub-connectorv2-provider-jiracloud): {{
    JiraCloudProviderConfiguration}}
  [ServiceNow](#cfn-securityhub-connectorv2-provider-servicenow): {{
    ServiceNowProviderConfiguration}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-provider-properties"></a>

`Azure`  <a name="cfn-securityhub-connectorv2-provider-azure"></a>
Property description not available.
*Required*: No
*Type*: [AzureProviderConfiguration](aws-properties-securityhub-connectorv2-azureproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JiraCloud`  <a name="cfn-securityhub-connectorv2-provider-jiracloud"></a>
Details about a Jira Cloud integration.
*Required*: No
*Type*: [JiraCloudProviderConfiguration](aws-properties-securityhub-connectorv2-jiracloudproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNow`  <a name="cfn-securityhub-connectorv2-provider-servicenow"></a>
Details about a ServiceNow ITSM integration.
*Required*: No
*Type*: [ServiceNowProviderConfiguration](aws-properties-securityhub-connectorv2-servicenowproviderconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
