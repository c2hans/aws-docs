---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::LoggingConfiguration LogDestinationConfig
<a name="aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig"></a>

Defines where AWS Network Firewall sends logs for the firewall for one log type. This is used in logging configuration. You can send each type of log to an Amazon S3 bucket, a CloudWatch log group, or a Kinesis Data Firehose delivery stream.

Network Firewall generates logs for stateful rule groups. You can save alert and flow log types. The stateful rules engine records flow logs for all network traffic that it receives. It records alert logs for traffic that matches stateful rules that have the rule action set to `DROP` or `ALERT`.

## Syntax
<a name="aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig-syntax.json"></a>

```
{
  "[LogDestination](#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination)" : {{{{{Key}}: {{Value}}, ...}}},
  "[LogDestinationType](#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype)" : {{String}},
  "[LogType](#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig-syntax.yaml"></a>

```
  [LogDestination](#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination): {{
    {{Key}}: {{Value}}}}
  [LogDestinationType](#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype): {{String}}
  [LogType](#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype): {{String}}
```

## Properties
<a name="aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig-properties"></a>

`LogDestination`  <a name="cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination"></a>
The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type.
+ For an Amazon S3 bucket, provide the name of the bucket, with key `bucketName`, and optionally provide a prefix, with key `prefix`.

  The following example specifies an Amazon S3 bucket named `DOC-EXAMPLE-BUCKET` and the prefix `alerts`:

   `"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }`
+ For a CloudWatch log group, provide the name of the CloudWatch log group, with key `logGroup`. The following example specifies a log group named `alert-log-group`:

   `"LogDestination": { "logGroup": "alert-log-group" }`
+ For a Firehose delivery stream, provide the name of the delivery stream, with key `deliveryStream`. The following example specifies a delivery stream named `alert-delivery-stream`:

   `"LogDestination": { "deliveryStream": "alert-delivery-stream" }`
*Required*: Yes
*Type*: Object of String
*Pattern*: `^[0-9A-Za-z.\-_@\/]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogDestinationType`  <a name="cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype"></a>
The type of storage destination to send these logs to. You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.
*Required*: Yes
*Type*: String
*Allowed values*: `S3 | CloudWatchLogs | KinesisDataFirehose`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogType`  <a name="cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype"></a>
The type of log to record. You can record the following types of logs from your Network Firewall stateful engine.
+ `ALERT` - Logs for traffic that matches your stateful rules and that have an action that sends an alert. A stateful rule sends alerts for the rule actions DROP, ALERT, and REJECT. For more information, see the `StatefulRule` property.
+ `FLOW` - Standard network traffic flow logs. The stateful rules engine records flow logs for all network traffic that it receives. Each flow log record captures the network flow for a specific standard stateless rule group.
+ `TLS` - Logs for events that are related to TLS inspection. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html) in the *Network Firewall Developer Guide*.
*Required*: Yes
*Type*: String
*Allowed values*: `ALERT | FLOW | TLS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
