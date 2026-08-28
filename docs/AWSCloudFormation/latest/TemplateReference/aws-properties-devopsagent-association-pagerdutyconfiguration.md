---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-pagerdutyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association PagerDutyConfiguration
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration"></a>

Configuration for PagerDuty integration. Specifies the customer email, service IDs, and webhook settings to enable the Agent Space to access incident data, on-call schedules, and service information.

## Syntax
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-syntax.json"></a>

```
{
  "[CustomerEmail](#cfn-devopsagent-association-pagerdutyconfiguration-customeremail)" : {{String}},
  "[EnableWebhookUpdates](#cfn-devopsagent-association-pagerdutyconfiguration-enablewebhookupdates)" : {{Boolean}},
  "[Services](#cfn-devopsagent-association-pagerdutyconfiguration-services)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-syntax.yaml"></a>

```
  [CustomerEmail](#cfn-devopsagent-association-pagerdutyconfiguration-customeremail): {{String}}
  [EnableWebhookUpdates](#cfn-devopsagent-association-pagerdutyconfiguration-enablewebhookupdates): {{Boolean}}
  [Services](#cfn-devopsagent-association-pagerdutyconfiguration-services): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsagent-association-pagerdutyconfiguration-properties"></a>

`CustomerEmail`  <a name="cfn-devopsagent-association-pagerdutyconfiguration-customeremail"></a>
The email address used in the PagerDuty API request header.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-pagerdutyconfiguration-enablewebhookupdates"></a>
Specifies whether the Agent Space creates and updates webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Services`  <a name="cfn-devopsagent-association-pagerdutyconfiguration-services"></a>
The list of PagerDuty service IDs available for the association.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
