---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-eventsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy EventSource
<a name="aws-properties-dlm-lifecyclepolicy-eventsource"></a>

**[Event-based policies only]** Specifies an event that activates an event-based policy.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-eventsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-eventsource-syntax.json"></a>

```
{
  "[Parameters](#cfn-dlm-lifecyclepolicy-eventsource-parameters)" : {{EventParameters}},
  "[Type](#cfn-dlm-lifecyclepolicy-eventsource-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-eventsource-syntax.yaml"></a>

```
  [Parameters](#cfn-dlm-lifecyclepolicy-eventsource-parameters): {{
    EventParameters}}
  [Type](#cfn-dlm-lifecyclepolicy-eventsource-type): {{String}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-eventsource-properties"></a>

`Parameters`  <a name="cfn-dlm-lifecyclepolicy-eventsource-parameters"></a>
Information about the event.
*Required*: No
*Type*: [EventParameters](aws-properties-dlm-lifecyclepolicy-eventparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-dlm-lifecyclepolicy-eventsource-type"></a>
The source of the event. Currently only managed Amazon EventBridge (formerly known as Amazon CloudWatch) events are supported.
*Required*: Yes
*Type*: String
*Allowed values*: `MANAGED_CWE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
