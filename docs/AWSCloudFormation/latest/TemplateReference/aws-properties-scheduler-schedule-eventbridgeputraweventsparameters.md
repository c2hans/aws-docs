---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-eventbridgeputraweventsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule EventBridgePutRawEventsParameters

The templated target type for the EventBridge Custom event bus (eventsv2) [PutRawEvents](https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutRawEvents.html) API operation.

## Syntax
<a name="aws-properties-scheduler-schedule-eventbridgeputraweventsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-eventbridgeputraweventsparameters-syntax.json"></a>

```json
{
  "[Metadata](#cfn-scheduler-schedule-eventbridgeputraweventsparameters-metadata)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-eventbridgeputraweventsparameters-syntax.yaml"></a>

```yaml
  [Metadata](#cfn-scheduler-schedule-eventbridgeputraweventsparameters-metadata): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-scheduler-schedule-eventbridgeputraweventsparameters-properties"></a>

`Metadata`  <a name="cfn-scheduler-schedule-eventbridgeputraweventsparameters-metadata"></a>
Optional metadata key-value pairs you define. Keys must be 1-128 characters and must not contain "/".
*Required*: No
*Type*: Object of String
*Pattern*: `^[^/]{1,128}$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
