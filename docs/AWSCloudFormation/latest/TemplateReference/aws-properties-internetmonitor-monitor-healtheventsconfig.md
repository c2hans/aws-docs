---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-internetmonitor-monitor-healtheventsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InternetMonitor::Monitor HealthEventsConfig
<a name="aws-properties-internetmonitor-monitor-healtheventsconfig"></a>

Define the health event threshold percentages for the performance score and availability score for your application's monitor. Amazon CloudWatch Internet Monitor creates a health event when there's an internet issue that affects your application end users where a health score percentage is at or below a set threshold.

If you don't set a health event threshold, the default value is 95%.

## Syntax
<a name="aws-properties-internetmonitor-monitor-healtheventsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-internetmonitor-monitor-healtheventsconfig-syntax.json"></a>

```
{
  "[AvailabilityLocalHealthEventsConfig](#cfn-internetmonitor-monitor-healtheventsconfig-availabilitylocalhealtheventsconfig)" : {{LocalHealthEventsConfig}},
  "[AvailabilityScoreThreshold](#cfn-internetmonitor-monitor-healtheventsconfig-availabilityscorethreshold)" : {{Number}},
  "[PerformanceLocalHealthEventsConfig](#cfn-internetmonitor-monitor-healtheventsconfig-performancelocalhealtheventsconfig)" : {{LocalHealthEventsConfig}},
  "[PerformanceScoreThreshold](#cfn-internetmonitor-monitor-healtheventsconfig-performancescorethreshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-internetmonitor-monitor-healtheventsconfig-syntax.yaml"></a>

```
  [AvailabilityLocalHealthEventsConfig](#cfn-internetmonitor-monitor-healtheventsconfig-availabilitylocalhealtheventsconfig): {{
    LocalHealthEventsConfig}}
  [AvailabilityScoreThreshold](#cfn-internetmonitor-monitor-healtheventsconfig-availabilityscorethreshold): {{Number}}
  [PerformanceLocalHealthEventsConfig](#cfn-internetmonitor-monitor-healtheventsconfig-performancelocalhealtheventsconfig): {{
    LocalHealthEventsConfig}}
  [PerformanceScoreThreshold](#cfn-internetmonitor-monitor-healtheventsconfig-performancescorethreshold): {{Number}}
```

## Properties
<a name="aws-properties-internetmonitor-monitor-healtheventsconfig-properties"></a>

`AvailabilityLocalHealthEventsConfig`  <a name="cfn-internetmonitor-monitor-healtheventsconfig-availabilitylocalhealtheventsconfig"></a>
The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local availability issue.
*Required*: No
*Type*: [LocalHealthEventsConfig](aws-properties-internetmonitor-monitor-localhealtheventsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailabilityScoreThreshold`  <a name="cfn-internetmonitor-monitor-healtheventsconfig-availabilityscorethreshold"></a>
The health event threshold percentage set for availability scores. When the overall availability score is at or below this percentage, Internet Monitor creates a health event.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformanceLocalHealthEventsConfig`  <a name="cfn-internetmonitor-monitor-healtheventsconfig-performancelocalhealtheventsconfig"></a>
The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance issue.
*Required*: No
*Type*: [LocalHealthEventsConfig](aws-properties-internetmonitor-monitor-localhealtheventsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformanceScoreThreshold`  <a name="cfn-internetmonitor-monitor-healtheventsconfig-performancescorethreshold"></a>
The health event threshold percentage set for performance scores. When the overall performance score is at or below this percentage, Internet Monitor creates a health event.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
