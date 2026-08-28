---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-schedulingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job SchedulingConfig
<a name="aws-properties-iot-job-schedulingconfig"></a>

<a name="aws-properties-iot-job-schedulingconfig-description"></a>The `SchedulingConfig` property type specifies Property description not available. for an [AWS::IoT::Job](aws-resource-iot-job.md).

## Syntax
<a name="aws-properties-iot-job-schedulingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-schedulingconfig-syntax.json"></a>

```
{
  "[EndBehavior](#cfn-iot-job-schedulingconfig-endbehavior)" : {{String}},
  "[EndTime](#cfn-iot-job-schedulingconfig-endtime)" : {{String}},
  "[MaintenanceWindows](#cfn-iot-job-schedulingconfig-maintenancewindows)" : {{[ MaintenanceWindow, ... ]}},
  "[StartTime](#cfn-iot-job-schedulingconfig-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-job-schedulingconfig-syntax.yaml"></a>

```
  [EndBehavior](#cfn-iot-job-schedulingconfig-endbehavior): {{String}}
  [EndTime](#cfn-iot-job-schedulingconfig-endtime): {{String}}
  [MaintenanceWindows](#cfn-iot-job-schedulingconfig-maintenancewindows): {{
    - MaintenanceWindow}}
  [StartTime](#cfn-iot-job-schedulingconfig-starttime): {{String}}
```

## Properties
<a name="aws-properties-iot-job-schedulingconfig-properties"></a>

`EndBehavior`  <a name="cfn-iot-job-schedulingconfig-endbehavior"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `STOP_ROLLOUT | CANCEL | FORCE_CANCEL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndTime`  <a name="cfn-iot-job-schedulingconfig-endtime"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceWindows`  <a name="cfn-iot-job-schedulingconfig-maintenancewindows"></a>
Property description not available.
*Required*: No
*Type*: Array of [MaintenanceWindow](aws-properties-iot-job-maintenancewindow.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-iot-job-schedulingconfig-starttime"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
