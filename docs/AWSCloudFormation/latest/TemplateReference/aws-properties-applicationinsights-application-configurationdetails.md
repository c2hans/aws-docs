---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationinsights-application-configurationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationInsights::Application ConfigurationDetails
<a name="aws-properties-applicationinsights-application-configurationdetails"></a>

The `AWS::ApplicationInsights::Application ConfigurationDetails` property type specifies the configuration settings.

## Syntax
<a name="aws-properties-applicationinsights-application-configurationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationinsights-application-configurationdetails-syntax.json"></a>

```
{
  "[AlarmMetrics](#cfn-applicationinsights-application-configurationdetails-alarmmetrics)" : {{[ AlarmMetric, ... ]}},
  "[Alarms](#cfn-applicationinsights-application-configurationdetails-alarms)" : {{[ Alarm, ... ]}},
  "[HAClusterPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-haclusterprometheusexporter)" : {{HAClusterPrometheusExporter}},
  "[HANAPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-hanaprometheusexporter)" : {{HANAPrometheusExporter}},
  "[JMXPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter)" : {{JMXPrometheusExporter}},
  "[Logs](#cfn-applicationinsights-application-configurationdetails-logs)" : {{[ Log, ... ]}},
  "[NetWeaverPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-netweaverprometheusexporter)" : {{NetWeaverPrometheusExporter}},
  "[Processes](#cfn-applicationinsights-application-configurationdetails-processes)" : {{[ Process, ... ]}},
  "[SQLServerPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-sqlserverprometheusexporter)" : {{SQLServerPrometheusExporter}},
  "[WindowsEvents](#cfn-applicationinsights-application-configurationdetails-windowsevents)" : {{[ WindowsEvent, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationinsights-application-configurationdetails-syntax.yaml"></a>

```
  [AlarmMetrics](#cfn-applicationinsights-application-configurationdetails-alarmmetrics): {{
    - AlarmMetric}}
  [Alarms](#cfn-applicationinsights-application-configurationdetails-alarms): {{
    - Alarm}}
  [HAClusterPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-haclusterprometheusexporter): {{
    HAClusterPrometheusExporter}}
  [HANAPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-hanaprometheusexporter): {{
    HANAPrometheusExporter}}
  [JMXPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter): {{
    JMXPrometheusExporter}}
  [Logs](#cfn-applicationinsights-application-configurationdetails-logs): {{
    - Log}}
  [NetWeaverPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-netweaverprometheusexporter): {{
    NetWeaverPrometheusExporter}}
  [Processes](#cfn-applicationinsights-application-configurationdetails-processes): {{
    - Process}}
  [SQLServerPrometheusExporter](#cfn-applicationinsights-application-configurationdetails-sqlserverprometheusexporter): {{
    SQLServerPrometheusExporter}}
  [WindowsEvents](#cfn-applicationinsights-application-configurationdetails-windowsevents): {{
    - WindowsEvent}}
```

## Properties
<a name="aws-properties-applicationinsights-application-configurationdetails-properties"></a>

`AlarmMetrics`  <a name="cfn-applicationinsights-application-configurationdetails-alarmmetrics"></a>
A list of metrics to monitor for the component. All component types can use `AlarmMetrics`.
*Required*: No
*Type*: Array of [AlarmMetric](aws-properties-applicationinsights-application-alarmmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Alarms`  <a name="cfn-applicationinsights-application-configurationdetails-alarms"></a>
A list of alarms to monitor for the component. All component types can use `Alarm`.
*Required*: No
*Type*: Array of [Alarm](aws-properties-applicationinsights-application-alarm.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HAClusterPrometheusExporter`  <a name="cfn-applicationinsights-application-configurationdetails-haclusterprometheusexporter"></a>
The HA cluster Prometheus Exporter settings.
*Required*: No
*Type*: [HAClusterPrometheusExporter](aws-properties-applicationinsights-application-haclusterprometheusexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HANAPrometheusExporter`  <a name="cfn-applicationinsights-application-configurationdetails-hanaprometheusexporter"></a>
The HANA DB Prometheus Exporter settings.
*Required*: No
*Type*: [HANAPrometheusExporter](aws-properties-applicationinsights-application-hanaprometheusexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JMXPrometheusExporter`  <a name="cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter"></a>
A list of Java metrics to monitor for the component.
*Required*: No
*Type*: [JMXPrometheusExporter](aws-properties-applicationinsights-application-jmxprometheusexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logs`  <a name="cfn-applicationinsights-application-configurationdetails-logs"></a>
A list of logs to monitor for the component. Only Amazon EC2 instances can use `Logs`.
*Required*: No
*Type*: Array of [Log](aws-properties-applicationinsights-application-log.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetWeaverPrometheusExporter`  <a name="cfn-applicationinsights-application-configurationdetails-netweaverprometheusexporter"></a>
Property description not available.
*Required*: No
*Type*: [NetWeaverPrometheusExporter](aws-properties-applicationinsights-application-netweaverprometheusexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Processes`  <a name="cfn-applicationinsights-application-configurationdetails-processes"></a>
Property description not available.
*Required*: No
*Type*: Array of [Process](aws-properties-applicationinsights-application-process.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SQLServerPrometheusExporter`  <a name="cfn-applicationinsights-application-configurationdetails-sqlserverprometheusexporter"></a>
Property description not available.
*Required*: No
*Type*: [SQLServerPrometheusExporter](aws-properties-applicationinsights-application-sqlserverprometheusexporter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WindowsEvents`  <a name="cfn-applicationinsights-application-configurationdetails-windowsevents"></a>
A list of Windows Events to monitor for the component. Only Amazon EC2 instances running on Windows can use `WindowsEvents`.
*Required*: No
*Type*: Array of [WindowsEvent](aws-properties-applicationinsights-application-windowsevent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
