---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-eventbridgeparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule EventBridgeParameters
<a name="aws-properties-scheduler-schedule-eventbridgeparameters"></a>

The templated target type for the EventBridge [`PutEvents`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) API operation.

## Syntax
<a name="aws-properties-scheduler-schedule-eventbridgeparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-eventbridgeparameters-syntax.json"></a>

```
{
  "[DetailType](#cfn-scheduler-schedule-eventbridgeparameters-detailtype)" : {{String}},
  "[Source](#cfn-scheduler-schedule-eventbridgeparameters-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-eventbridgeparameters-syntax.yaml"></a>

```
  [DetailType](#cfn-scheduler-schedule-eventbridgeparameters-detailtype): {{String}}
  [Source](#cfn-scheduler-schedule-eventbridgeparameters-source): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-eventbridgeparameters-properties"></a>

`DetailType`  <a name="cfn-scheduler-schedule-eventbridgeparameters-detailtype"></a>
A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-scheduler-schedule-eventbridgeparameters-source"></a>
The source of the event.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
