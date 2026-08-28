---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-servicenowconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association ServiceNowConfiguration
<a name="aws-properties-devopsagent-association-servicenowconfiguration"></a>

Configuration for ServiceNow integration. Defines the ServiceNow instance URL, instance ID, and webhook update settings required for the Agent Space to create, update, and manage incidents and change requests.

## Syntax
<a name="aws-properties-devopsagent-association-servicenowconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-servicenowconfiguration-syntax.json"></a>

```
{
  "[EnableWebhookUpdates](#cfn-devopsagent-association-servicenowconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[InstanceId](#cfn-devopsagent-association-servicenowconfiguration-instanceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-servicenowconfiguration-syntax.yaml"></a>

```
  [EnableWebhookUpdates](#cfn-devopsagent-association-servicenowconfiguration-enablewebhookupdates): {{Boolean}}
  [InstanceId](#cfn-devopsagent-association-servicenowconfiguration-instanceid): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-servicenowconfiguration-properties"></a>

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-servicenowconfiguration-enablewebhookupdates"></a>
When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceId`  <a name="cfn-devopsagent-association-servicenowconfiguration-instanceid"></a>
ServiceNow instance ID.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
