---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-graphqlapi-logconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::GraphQLApi LogConfig
<a name="aws-properties-appsync-graphqlapi-logconfig"></a>

The `LogConfig` property type specifies the logging configuration when writing GraphQL operations and tracing to Amazon CloudWatch for an AWS AppSync GraphQL API.

`LogConfig` is a property of the [AWS::AppSync::GraphQLApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html) property type.

## Syntax
<a name="aws-properties-appsync-graphqlapi-logconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-graphqlapi-logconfig-syntax.json"></a>

```
{
  "[CloudWatchLogsRoleArn](#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn)" : {{String}},
  "[ExcludeVerboseContent](#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent)" : {{Boolean}},
  "[FieldLogLevel](#cfn-appsync-graphqlapi-logconfig-fieldloglevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-graphqlapi-logconfig-syntax.yaml"></a>

```
  [CloudWatchLogsRoleArn](#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn): {{String}}
  [ExcludeVerboseContent](#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent): {{Boolean}}
  [FieldLogLevel](#cfn-appsync-graphqlapi-logconfig-fieldloglevel): {{String}}
```

## Properties
<a name="aws-properties-appsync-graphqlapi-logconfig-properties"></a>

`CloudWatchLogsRoleArn`  <a name="cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn"></a>
The service role that AWS AppSync will assume to publish to Amazon CloudWatch Logs in your account.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeVerboseContent`  <a name="cfn-appsync-graphqlapi-logconfig-excludeverbosecontent"></a>
Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldLogLevel`  <a name="cfn-appsync-graphqlapi-logconfig-fieldloglevel"></a>
The field logging level. Values can be NONE, ERROR, INFO, DEBUG, or ALL.
+ **NONE**: No field-level logs are captured.
+ **ERROR**: Logs the following information **only** for the fields that are in the error category:
  + The error section in the server response.
  + Field-level errors.
  + The generated request/response functions that got resolved for error fields.
+ **INFO**: Logs the following information **only** for the fields that are in the info and error categories:
  + Info-level messages.
  + The user messages sent through `$util.log.info` and `console.log`.
  + Field-level tracing and mapping logs are not shown.
+ **DEBUG**: Logs the following information **only** for the fields that are in the debug, info, and error categories:
  + Debug-level messages.
  + The user messages sent through `$util.log.info`, `$util.log.debug`, `console.log`, and `console.debug`.
  + Field-level tracing and mapping logs are not shown.
+ **ALL**: The following information is logged for all fields in the query:
  + Field-level tracing information.
  + The generated request/response functions that were resolved for each field.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | ERROR | ALL | INFO | DEBUG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
