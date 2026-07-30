---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCZonalShift::ZonalAutoshiftConfiguration ControlCondition
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition"></a>

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm*, to monitor application health during practice runs and, optionally, a *blocking alarm*, to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see [ Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the ARC Developer Guide.

## Syntax
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition-syntax.json"></a>

```
{
  "[AlarmIdentifier](#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-alarmidentifier)" : {{String}},
  "[Type](#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition-syntax.yaml"></a>

```
  [AlarmIdentifier](#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-alarmidentifier): {{String}}
  [Type](#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-type): {{String}}
```

## Properties
<a name="aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition-properties"></a>

`AlarmIdentifier`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-alarmidentifier"></a>
The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.
*Required*: Yes
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `8`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-type"></a>
The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]*$`
*Minimum*: `8`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
