---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::NetworkAnalyzerConfiguration TraceContent
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent"></a>

Trace content for your wireless gateway and wireless device resources.

## Syntax
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent-syntax.json"></a>

```
{
  "[LogLevel](#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-loglevel)" : {{String}},
  "[WirelessDeviceFrameInfo](#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-wirelessdeviceframeinfo)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent-syntax.yaml"></a>

```
  [LogLevel](#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-loglevel): {{String}}
  [WirelessDeviceFrameInfo](#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-wirelessdeviceframeinfo): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent-properties"></a>

`LogLevel`  <a name="cfn-iotwireless-networkanalyzerconfiguration-tracecontent-loglevel"></a>
The log level for a log message. The log levels can be disabled, or set to `ERROR` to display less verbose logs containing only error information, or to `INFO` for more detailed logs
*Required*: No
*Type*: String
*Allowed values*: `INFO | ERROR | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WirelessDeviceFrameInfo`  <a name="cfn-iotwireless-networkanalyzerconfiguration-tracecontent-wirelessdeviceframeinfo"></a>
`FrameInfo` of your wireless device resources for the trace content. Use FrameInfo to debug the communication between your LoRaWAN end devices and the network server.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
