---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-maintenancewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job MaintenanceWindow
<a name="aws-properties-iot-job-maintenancewindow"></a>

<a name="aws-properties-iot-job-maintenancewindow-description"></a>The `MaintenanceWindow` property type specifies Property description not available. for an [AWS::IoT::Job](aws-resource-iot-job.md).

## Syntax
<a name="aws-properties-iot-job-maintenancewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-maintenancewindow-syntax.json"></a>

```
{
  "[DurationInMinutes](#cfn-iot-job-maintenancewindow-durationinminutes)" : {{Integer}},
  "[StartTime](#cfn-iot-job-maintenancewindow-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-job-maintenancewindow-syntax.yaml"></a>

```
  [DurationInMinutes](#cfn-iot-job-maintenancewindow-durationinminutes): {{Integer}}
  [StartTime](#cfn-iot-job-maintenancewindow-starttime): {{String}}
```

## Properties
<a name="aws-properties-iot-job-maintenancewindow-properties"></a>

`DurationInMinutes`  <a name="cfn-iot-job-maintenancewindow-durationinminutes"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1430`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-iot-job-maintenancewindow-starttime"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
