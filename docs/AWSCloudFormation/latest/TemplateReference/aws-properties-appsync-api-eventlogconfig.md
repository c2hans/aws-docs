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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
