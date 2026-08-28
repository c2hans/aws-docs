---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-eventbus-logconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::EventBus LogConfig
<a name="aws-properties-events-eventbus-logconfig"></a>

The logging configuration settings for the event bus.

For more information, see [Configuring logs for event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-properties-events-eventbus-logconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-eventbus-logconfig-syntax.json"></a>

```
{
  "[IncludeDetail](#cfn-events-eventbus-logconfig-includedetail)" : {{String}},
  "[Level](#cfn-events-eventbus-logconfig-level)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-eventbus-logconfig-syntax.yaml"></a>

```
  [IncludeDetail](#cfn-events-eventbus-logconfig-includedetail): {{String}}
  [Level](#cfn-events-eventbus-logconfig-level): {{String}}
```

## Properties
<a name="aws-properties-events-eventbus-logconfig-properties"></a>

`IncludeDetail`  <a name="cfn-events-eventbus-logconfig-includedetail"></a>
Whether EventBridge include detailed event information in the records it generates. Detailed data can be useful for troubleshooting and debugging. This information includes details of the event itself, as well as target details.
For more information, see [Including detail data in event bus logs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-logs-data) in the *EventBridge User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `FULL | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-events-eventbus-logconfig-level"></a>
The level of logging detail to include. This applies to all log destinations for the event bus.
For more information, see [Specifying event bus log level](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-bus-logs-level) in the *EventBridge User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `INFO | ERROR | TRACE | OFF`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
