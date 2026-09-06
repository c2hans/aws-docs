---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-logdeliveryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::LogDeliveryConfiguration
<a name="aws-resource-cognito-logdeliveryconfiguration"></a>

Sets up or modifies the logging configuration of a user pool. User pools can export user notification logs and, when threat protection is active, user-activity logs. For more information, see [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html).

## Syntax
<a name="aws-resource-cognito-logdeliveryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-logdeliveryconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::LogDeliveryConfiguration",
  "Properties" : {
      "[LogConfigurations](#cfn-cognito-logdeliveryconfiguration-logconfigurations)" : {{[ LogConfiguration, ... ]}},
      "[UserPoolId](#cfn-cognito-logdeliveryconfiguration-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-logdeliveryconfiguration-syntax.yaml"></a>

```
Type: AWS::Cognito::LogDeliveryConfiguration
Properties:
  [LogConfigurations](#cfn-cognito-logdeliveryconfiguration-logconfigurations): {{
    - LogConfiguration}}
  [UserPoolId](#cfn-cognito-logdeliveryconfiguration-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-logdeliveryconfiguration-properties"></a>

`LogConfigurations`  <a name="cfn-cognito-logdeliveryconfiguration-logconfigurations"></a>
A logging destination of a user pool. User pools can have multiple logging destinations for message-delivery and user-activity logs.
*Required*: No
*Type*: Array of [LogConfiguration](aws-properties-cognito-logdeliveryconfiguration-logconfiguration.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-logdeliveryconfiguration-userpoolid"></a>
The ID of the user pool where you configured logging.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-logdeliveryconfiguration-return-values"></a>

### Ref
<a name="aws-resource-cognito-logdeliveryconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a resource identifier. A log delivery configuration attached to a user pool returns a user pool ID like `us-east-1_EXAMPLE`.

### Fn::GetAtt
<a name="aws-resource-cognito-logdeliveryconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cognito-logdeliveryconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
A user pool ID, for example `us-east-1_EXAMPLE`.

## Examples
<a name="aws-resource-cognito-logdeliveryconfiguration--examples"></a>

### Creating a new log delivery configuration for a user pool
<a name="aws-resource-cognito-logdeliveryconfiguration--examples--Creating_a_new_log_delivery_configuration_for_a_user_pool"></a>

The following example creates log delivery of user message-delivery errors to a log group and threat-protection logs to a stream.

#### JSON
<a name="aws-resource-cognito-logdeliveryconfiguration--examples--Creating_a_new_log_delivery_configuration_for_a_user_pool--json"></a>

```
{
    "LogDeliveryConfiguration": {
        "Properties": {
            "LogConfigurations": [
                {
                    "CloudWatchLogsConfiguration": {
                        "LogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:cognito-exported"
                    },
                    "EventSource": "userNotification",
                    "LogLevel": "ERROR"
                },
                {
                    "EventSource": "userAuthEvents",
                    "FirehoseConfiguration": {
                        "StreamArn": "arn:aws:firehose:us-west-2:123456789012:deliverystream/test-deliverystream"
                    },
                    "LogLevel": "INFO"
                }
            ],
            "UserPoolId": "us-west-2_EXAMPLE"
        },
        "Type": "AWS::Cognito::LogDeliveryConfiguration"
    }
}
```

#### YAML
<a name="aws-resource-cognito-logdeliveryconfiguration--examples--Creating_a_new_log_delivery_configuration_for_a_user_pool--yaml"></a>

```
LogDeliveryConfiguration:
    Type: AWS::Cognito::LogDeliveryConfiguration
    Properties:
      LogConfigurations:
        - CloudWatchLogsConfiguration:
            LogGroupArn: arn:aws:logs:us-west-2:123456789012:log-group:cognito-exported
          EventSource: userNotification
          LogLevel: ERROR
        - EventSource: userAuthEvents
          FirehoseConfiguration:
            StreamArn: arn:aws:firehose:us-west-2:123456789012:deliverystream/test-deliverystream
          LogLevel: INFO
      UserPoolId: us-west-2_EXAMPLE
```
