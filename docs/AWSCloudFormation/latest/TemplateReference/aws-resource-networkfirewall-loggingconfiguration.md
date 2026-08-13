---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networkfirewall-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkFirewall::LoggingConfiguration
<a name="aws-resource-networkfirewall-loggingconfiguration"></a>

Use the logging configuration to define the destinations and logging options for an firewall.

You must change the logging configuration by changing one `LogDestinationConfig` setting at a time in your `LogDestinationConfigs`.

You can make only one of the following changes to your logging configuration resource:
+ Create a new log destination object by adding a single `LogDestinationConfig` array element to `LogDestinationConfigs`.
+ Delete a log destination object by removing a single `LogDestinationConfig` array element from `LogDestinationConfigs`.
+ Change the `LogDestination` setting in a single `LogDestinationConfig` array element.

You can't change the `LogDestinationType` or `LogType` in a `LogDestinationConfig`. To change these settings, delete the existing `LogDestinationConfig` object and create a new one, in two separate modifications.

## Syntax
<a name="aws-resource-networkfirewall-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networkfirewall-loggingconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::NetworkFirewall::LoggingConfiguration",
  "Properties" : {
      "[EnableMonitoringDashboard](#cfn-networkfirewall-loggingconfiguration-enablemonitoringdashboard)" : {{Boolean}},
      "[FirewallArn](#cfn-networkfirewall-loggingconfiguration-firewallarn)" : {{String}},
      "[FirewallName](#cfn-networkfirewall-loggingconfiguration-firewallname)" : {{String}},
      "[LoggingConfiguration](#cfn-networkfirewall-loggingconfiguration-loggingconfiguration)" : {{LoggingConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-networkfirewall-loggingconfiguration-syntax.yaml"></a>

```
Type: AWS::NetworkFirewall::LoggingConfiguration
Properties:
  [EnableMonitoringDashboard](#cfn-networkfirewall-loggingconfiguration-enablemonitoringdashboard): {{Boolean}}
  [FirewallArn](#cfn-networkfirewall-loggingconfiguration-firewallarn): {{String}}
  [FirewallName](#cfn-networkfirewall-loggingconfiguration-firewallname): {{String}}
  [LoggingConfiguration](#cfn-networkfirewall-loggingconfiguration-loggingconfiguration): {{
    LoggingConfiguration}}
```

## Properties
<a name="aws-resource-networkfirewall-loggingconfiguration-properties"></a>

`EnableMonitoringDashboard`  <a name="cfn-networkfirewall-loggingconfiguration-enablemonitoringdashboard"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallArn`  <a name="cfn-networkfirewall-loggingconfiguration-firewallarn"></a>
The Amazon Resource Name (ARN) of the firewallthat the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws.*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirewallName`  <a name="cfn-networkfirewall-loggingconfiguration-firewallname"></a>
The name of the firewall that the logging configuration is associated with. You can't change the firewall specification after you create the logging configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfiguration`  <a name="cfn-networkfirewall-loggingconfiguration-loggingconfiguration"></a>
Defines how AWS Network Firewall performs logging for a firewall.
*Required*: Yes
*Type*: [LoggingConfiguration](aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networkfirewall-loggingconfiguration-return-values"></a>

### Ref
<a name="aws-resource-networkfirewall-loggingconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the firewall that the logging configuration is associated with. For example:

 `{ "Ref": "arn:aws:network-firewall:us-east-1:012345678901:firewall/myFirewallName" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-networkfirewall-loggingconfiguration--examples"></a>

**Topics**
+ [Create a logging configuration for CloudWatch Logs and Kinesis Data Firehose](#aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_and_Kinesis_Data_Firehose)
+ [Create a logging configuration for Amazon S3](#aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_Amazon_S3)

### Create a logging configuration for CloudWatch Logs and Kinesis Data Firehose
<a name="aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_and_Kinesis_Data_Firehose"></a>

The following shows example logging configuration specifications for alert logs that go to an Amazon CloudWatch Logs log group and flow logs that go to an Amazon Kinesis Data Firehose delivery stream.

#### JSON
<a name="aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_and_Kinesis_Data_Firehose--json"></a>

```
"SampleLoggingConfiguration": {
    "Type": "AWS::NetworkFirewall::LoggingConfiguration",
    "Properties": {
        "FirewallArn": {
            "Ref": "SampleFirewallArn"
        },
        "LoggingConfiguration": {
            "LogDestinationConfigs": [
                {
                    "LogType": "ALERT",
                    "LogDestinationType": "CloudWatchLogs",
                    "LogDestination": {
                        "logGroup": "SampleLogGroup"
                    }
                },
                {
                    "LogType": "FLOW",
                    "LogDestinationType": "KinesisDataFirehose",
                    "LogDestination": {
                        "deliveryStream": "SampleStream"
                    }
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_and_Kinesis_Data_Firehose--yaml"></a>

```
SampleLoggingConfiguration:
  Type: 'AWS::NetworkFirewall::LoggingConfiguration'
  Properties:
    FirewallArn: !Ref SampleFirewallArn
    LoggingConfiguration:
      LogDestinationConfigs:
        - LogType: ALERT
          LogDestinationType: CloudWatchLogs
          LogDestination:
            logGroup: SampleLogGroup
        - LogType: FLOW
          LogDestinationType: KinesisDataFirehose
          LogDestination:
            deliveryStream: SampleStream
```

### Create a logging configuration for Amazon S3
<a name="aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_Amazon_S3"></a>

The following shows example logging configuration specifications for flow logs that go to an Amazon S3 bucket.

#### JSON
<a name="aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_Amazon_S3--json"></a>

```
"SampleLoggingConfiguration": {
    "Type": "AWS::NetworkFirewall::LoggingConfiguration",
    "Properties": {
        "FirewallArn": {
            "Ref": "SampleFirewallArn"
        },
        "LoggingConfiguration": {
            "LogDestinationConfigs": [
                {
                    "LogType": "FLOW",
                    "LogDestinationType": "S3",
                    "LogDestination": {
                        "bucketName": "sample-bucket-name",
                        "prefix": "sample/s3/prefix"
                    }
                }
            ]
        }
    }
}
```

#### YAML
<a name="aws-resource-networkfirewall-loggingconfiguration--examples--Create_a_logging_configuration_for_Amazon_S3--yaml"></a>

```
SampleLoggingConfiguration:
  Type: 'AWS::NetworkFirewall::LoggingConfiguration'
  Properties:
    FirewallArn: !Ref SampleFirewallArn
    LoggingConfiguration:
      LogDestinationConfigs:
        - LogType: FLOW
          LogDestinationType: S3
          LogDestination:
            bucketName: sample-bucket-name
            prefix: sample/s3/prefix
```
