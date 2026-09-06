---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet LogConfiguration
<a name="aws-properties-gamelift-containerfleet-logconfiguration"></a>

A method for collecting container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. You can select from the following methods:

## Syntax
<a name="aws-properties-gamelift-containerfleet-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-logconfiguration-syntax.json"></a>

```
{
  "[LogDestination](#cfn-gamelift-containerfleet-logconfiguration-logdestination)" : {{String}},
  "[LogGroupArn](#cfn-gamelift-containerfleet-logconfiguration-loggrouparn)" : {{String}},
  "[S3BucketName](#cfn-gamelift-containerfleet-logconfiguration-s3bucketname)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-logconfiguration-syntax.yaml"></a>

```
  [LogDestination](#cfn-gamelift-containerfleet-logconfiguration-logdestination): {{String}}
  [LogGroupArn](#cfn-gamelift-containerfleet-logconfiguration-loggrouparn): {{String}}
  [S3BucketName](#cfn-gamelift-containerfleet-logconfiguration-s3bucketname): {{String}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-logconfiguration-properties"></a>

`LogDestination`  <a name="cfn-gamelift-containerfleet-logconfiguration-logdestination"></a>
The type of log collection to use for a fleet.
+ `CLOUDWATCH` -- (default value) Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group.
+ `S3` -- Store logs in an Amazon S3 bucket that you define. This bucket must reside in the fleet's home AWS Region.
+ `NONE` -- Don't collect container logs.
*Required*: No
*Type*: String
*Allowed values*: `NONE | CLOUDWATCH | S3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupArn`  <a name="cfn-gamelift-containerfleet-logconfiguration-loggrouparn"></a>
If log destination is `CLOUDWATCH`, logs are sent to the specified log group in Amazon CloudWatch.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:/\-\*]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketName`  <a name="cfn-gamelift-containerfleet-logconfiguration-s3bucketname"></a>
If log destination is `S3`, logs are sent to the specified Amazon S3 bucket name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
