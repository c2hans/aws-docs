---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-logging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Logging
<a name="aws-resource-iot-logging"></a>

Configure logging.

**Note**
If you already set the log function of AWS IoT Core, you can't deploy the AWS Cloud Development Kit (AWS CDK) to change the logging settings. You can change the logging settings by either:
Importing the existing logging resource into your CloudFormation stack, such as with the [infrastructure as code generator (IaC generator)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html).
Calling `aws iot set-v2-logging-options --disable-all-logs` before creating a new CloudFormation stack. This command disables all AWS IoT logging. As a result, no AWS IoT logs will be delivered to Amazon CloudWatch until you re-enable logging.

## Syntax
<a name="aws-resource-iot-logging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-logging-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::Logging",
  "Properties" : {
      "[AccountId](#cfn-iot-logging-accountid)" : {{String}},
      "[DefaultLogLevel](#cfn-iot-logging-defaultloglevel)" : {{String}},
      "[EventConfigurations](#cfn-iot-logging-eventconfigurations)" : {{[ EventConfiguration, ... ]}},
      "[RoleArn](#cfn-iot-logging-rolearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-logging-syntax.yaml"></a>

```
Type: AWS::IoT::Logging
Properties:
  [AccountId](#cfn-iot-logging-accountid): {{String}}
  [DefaultLogLevel](#cfn-iot-logging-defaultloglevel): {{String}}
  [EventConfigurations](#cfn-iot-logging-eventconfigurations): {{
    - EventConfiguration}}
  [RoleArn](#cfn-iot-logging-rolearn): {{String}}
```

## Properties
<a name="aws-resource-iot-logging-properties"></a>

`AccountId`  <a name="cfn-iot-logging-accountid"></a>
The account ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultLogLevel`  <a name="cfn-iot-logging-defaultloglevel"></a>
The default log level. Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`
*Required*: Yes
*Type*: String
*Allowed values*: `ERROR | WARN | INFO | DEBUG | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventConfigurations`  <a name="cfn-iot-logging-eventconfigurations"></a>
Configurations for event-based logging that specifies which event types to log and their logging settings. Overrides account-level logging for the specified event.
*Required*: No
*Type*: Array of [EventConfiguration](aws-properties-iot-logging-eventconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-logging-rolearn"></a>
The role ARN used for the log.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-logging-return-values"></a>

### Ref
<a name="aws-resource-iot-logging-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the log ID. For example:

 `{"Ref": "Log-12345"}`
