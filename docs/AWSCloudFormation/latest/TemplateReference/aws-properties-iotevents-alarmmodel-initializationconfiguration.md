---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotevents-alarmmodel-initializationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTEvents::AlarmModel InitializationConfiguration
<a name="aws-properties-iotevents-alarmmodel-initializationconfiguration"></a>

Specifies the default alarm state. The configuration applies to all alarms that were created based on this alarm model.

## Syntax
<a name="aws-properties-iotevents-alarmmodel-initializationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotevents-alarmmodel-initializationconfiguration-syntax.json"></a>

```
{
  "[DisabledOnInitialization](#cfn-iotevents-alarmmodel-initializationconfiguration-disabledoninitialization)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iotevents-alarmmodel-initializationconfiguration-syntax.yaml"></a>

```
  [DisabledOnInitialization](#cfn-iotevents-alarmmodel-initializationconfiguration-disabledoninitialization): {{Boolean}}
```

## Properties
<a name="aws-properties-iotevents-alarmmodel-initializationconfiguration-properties"></a>

`DisabledOnInitialization`  <a name="cfn-iotevents-alarmmodel-initializationconfiguration-disabledoninitialization"></a>
The value must be `TRUE` or `FALSE`. If `FALSE`, all alarm instances created based on the alarm model are activated. The default value is `TRUE`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
