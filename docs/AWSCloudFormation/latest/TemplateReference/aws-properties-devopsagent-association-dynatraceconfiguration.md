---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-dynatraceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association DynatraceConfiguration
<a name="aws-properties-devopsagent-association-dynatraceconfiguration"></a>

Configuration for Dynatrace monitoring integration. Defines the Dynatrace environment ID, list of resources to monitor, and webhook update settings required for the Agent Space to access metrics, traces, and logs from Dynatrace.

## Syntax
<a name="aws-properties-devopsagent-association-dynatraceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-dynatraceconfiguration-syntax.json"></a>

```
{
  "[EnableWebhookUpdates](#cfn-devopsagent-association-dynatraceconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[EnvId](#cfn-devopsagent-association-dynatraceconfiguration-envid)" : {{String}},
  "[Resources](#cfn-devopsagent-association-dynatraceconfiguration-resources)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-dynatraceconfiguration-syntax.yaml"></a>

```
  [EnableWebhookUpdates](#cfn-devopsagent-association-dynatraceconfiguration-enablewebhookupdates): {{Boolean}}
  [EnvId](#cfn-devopsagent-association-dynatraceconfiguration-envid): {{String}}
  [Resources](#cfn-devopsagent-association-dynatraceconfiguration-resources): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-dynatraceconfiguration-properties"></a>

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-dynatraceconfiguration-enablewebhookupdates"></a>
When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvId`  <a name="cfn-devopsagent-association-dynatraceconfiguration-envid"></a>
The Dynatrace environment ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resources`  <a name="cfn-devopsagent-association-dynatraceconfiguration-resources"></a>
List of Dynatrace resources to monitor.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
