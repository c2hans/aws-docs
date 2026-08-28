---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-triggerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration TriggerProperties
<a name="aws-properties-customerprofiles-integration-triggerproperties"></a>

Specifies the configuration details that control the trigger for a flow. Currently, these settings only apply to the Scheduled trigger type.

## Syntax
<a name="aws-properties-customerprofiles-integration-triggerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-triggerproperties-syntax.json"></a>

```
{
  "[Scheduled](#cfn-customerprofiles-integration-triggerproperties-scheduled)" : {{ScheduledTriggerProperties}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-triggerproperties-syntax.yaml"></a>

```
  [Scheduled](#cfn-customerprofiles-integration-triggerproperties-scheduled): {{
    ScheduledTriggerProperties}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-triggerproperties-properties"></a>

`Scheduled`  <a name="cfn-customerprofiles-integration-triggerproperties-scheduled"></a>
Specifies the configuration details of a schedule-triggered flow that you define.
*Required*: No
*Type*: [ScheduledTriggerProperties](aws-properties-customerprofiles-integration-scheduledtriggerproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
