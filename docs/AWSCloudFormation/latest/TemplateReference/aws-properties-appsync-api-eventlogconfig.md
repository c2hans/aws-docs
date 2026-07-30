---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-eventlogconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api EventLogConfig
<a name="aws-properties-appsync-api-eventlogconfig"></a>

Describes the CloudWatch Logs configuration for the Event API.

## Syntax
<a name="aws-properties-appsync-api-eventlogconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-eventlogconfig-syntax.json"></a>

```
{
  "[CloudWatchLogsRoleArn](#cfn-appsync-api-eventlogconfig-cloudwatchlogsrolearn)" : {{String}},
  "[LogLevel](#cfn-appsync-api-eventlogconfig-loglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-api-eventlogconfig-syntax.yaml"></a>

```
  [CloudWatchLogsRoleArn](#cfn-appsync-api-eventlogconfig-cloudwatchlogsrolearn): {{String}}
  [LogLevel](#cfn-appsync-api-eventlogconfig-loglevel): {{String}}
```

## Properties
<a name="aws-properties-appsync-api-eventlogconfig-properties"></a>

`CloudWatchLogsRoleArn`  <a name="cfn-appsync-api-eventlogconfig-cloudwatchlogsrolearn"></a>
The IAM service role that AWS AppSync assumes to publish CloudWatch Logs in your account.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogLevel`  <a name="cfn-appsync-api-eventlogconfig-loglevel"></a>
The type of information to log for the Event API.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | ERROR | ALL | INFO | DEBUG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
