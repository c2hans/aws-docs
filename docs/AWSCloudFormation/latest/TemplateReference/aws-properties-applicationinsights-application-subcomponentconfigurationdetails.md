---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application SubComponentConfigurationDetails
<a name="aws-properties-applicationinsights-application-subcomponentconfigurationdetails"></a>

The `AWS::ApplicationInsights::Application SubComponentConfigurationDetails` property type specifies the configuration settings of the sub-components.

## Syntax
<a name="aws-properties-applicationinsights-application-subcomponentconfigurationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-subcomponentconfigurationdetails-syntax.json"></a>

```
{
  "[AlarmMetrics](#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics)" : {{[ AlarmMetric, ... ]}},
  "[Logs](#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs)" : {{[ Log, ... ]}},
  "[Processes](#cfn-applicationinsights-application-subcomponentconfigurationdetails-processes)" : {{[ Process, ... ]}},
  "[WindowsEvents](#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents)" : {{[ WindowsEvent, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-subcomponentconfigurationdetails-syntax.yaml"></a>

```
  [AlarmMetrics](#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics): {{
    - AlarmMetric}}
  [Logs](#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs): {{
    - Log}}
  [Processes](#cfn-applicationinsights-application-subcomponentconfigurationdetails-processes): {{
    - Process}}
  [WindowsEvents](#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents): {{
    - WindowsEvent}}
```

## Properties
<a name="aws-properties-applicationinsights-application-subcomponentconfigurationdetails-properties"></a>

`AlarmMetrics`  <a name="cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics"></a>
A list of metrics to monitor for the component. All component types can use `AlarmMetrics`.
*Required*: No
*Type*: Array of [AlarmMetric](aws-properties-applicationinsights-application-alarmmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logs`  <a name="cfn-applicationinsights-application-subcomponentconfigurationdetails-logs"></a>
A list of logs to monitor for the component. Only Amazon EC2 instances can use `Logs`.
*Required*: No
*Type*: Array of [Log](aws-properties-applicationinsights-application-log.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Processes`  <a name="cfn-applicationinsights-application-subcomponentconfigurationdetails-processes"></a>
Property description not available.
*Required*: No
*Type*: Array of [Process](aws-properties-applicationinsights-application-process.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WindowsEvents`  <a name="cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents"></a>
A list of Windows Events to monitor for the component. Only Amazon EC2 instances running on Windows can use `WindowsEvents`.
*Required*: No
*Type*: Array of [WindowsEvent](aws-properties-applicationinsights-application-windowsevent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
