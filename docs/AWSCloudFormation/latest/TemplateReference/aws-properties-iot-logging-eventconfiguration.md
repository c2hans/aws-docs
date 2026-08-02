---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-logging-eventconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Logging EventConfiguration
<a name="aws-properties-iot-logging-eventconfiguration"></a>

Configuration for event-based logging that specifies which event types to log and their logging settings. Used for account-level logging overrides.

## Syntax
<a name="aws-properties-iot-logging-eventconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-logging-eventconfiguration-syntax.json"></a>

```
{
  "[EventType](#cfn-iot-logging-eventconfiguration-eventtype)" : {{String}},
  "[LogDestination](#cfn-iot-logging-eventconfiguration-logdestination)" : {{String}},
  "[LogLevel](#cfn-iot-logging-eventconfiguration-loglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-logging-eventconfiguration-syntax.yaml"></a>

```
  [EventType](#cfn-iot-logging-eventconfiguration-eventtype): {{String}}
  [LogDestination](#cfn-iot-logging-eventconfiguration-logdestination): {{String}}
  [LogLevel](#cfn-iot-logging-eventconfiguration-loglevel): {{String}}
```

## Properties
<a name="aws-properties-iot-logging-eventconfiguration-properties"></a>

`EventType`  <a name="cfn-iot-logging-eventconfiguration-eventtype"></a>
The type of event to log. These include event types like Connect, Publish, and Disconnect.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDestination`  <a name="cfn-iot-logging-eventconfiguration-logdestination"></a>
CloudWatch Log Group for event-based logging. Specifies where log events should be sent. The log destination for event-based logging overrides default Log Group for the specified event type and applies to all resources associated with that event.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws/)[a-zA-Z0-9_\-/.#]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogLevel`  <a name="cfn-iot-logging-eventconfiguration-loglevel"></a>
The logging level for the specified event type. Determines the verbosity of log messages generated for this event type. Valid Values: `ERROR | WARN | INFO | DEBUG | DISABLED`
*Required*: No
*Type*: String
*Allowed values*: `ERROR | WARN | INFO | DEBUG | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
