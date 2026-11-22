---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-eventbridgeputeventsv2parameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule EventBridgePutEventsV2Parameters

The templated target type for the EventBridge Custom event bus (eventsv2) [PutEvents](https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutEvents.html) API operation.

## Syntax
<a name="aws-properties-scheduler-schedule-eventbridgeputeventsv2parameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-eventbridgeputeventsv2parameters-syntax.json"></a>

```json
{
  "[DetailType](#cfn-scheduler-schedule-eventbridgeputeventsv2parameters-detailtype)" : {{String}},
  "[Source](#cfn-scheduler-schedule-eventbridgeputeventsv2parameters-source)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-eventbridgeputeventsv2parameters-syntax.yaml"></a>

```yaml
  [DetailType](#cfn-scheduler-schedule-eventbridgeputeventsv2parameters-detailtype): {{String}}
  [Source](#cfn-scheduler-schedule-eventbridgeputeventsv2parameters-source): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-eventbridgeputeventsv2parameters-properties"></a>

`DetailType`  <a name="cfn-scheduler-schedule-eventbridgeputeventsv2parameters-detailtype"></a>
A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-scheduler-schedule-eventbridgeputeventsv2parameters-source"></a>
The source of the event. The source can't start with the `aws.` prefix.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
