---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-dynamodbconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource DynamoDBConfig
<a name="aws-properties-appsync-datasource-dynamodbconfig"></a>

The `DynamoDBConfig` property type specifies the `AwsRegion` and `TableName` for an Amazon DynamoDB table in your account for an AWS AppSync data source.

`DynamoDBConfig` is a property of the [AWS::AppSync::DataSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html) property type.

## Syntax
<a name="aws-properties-appsync-datasource-dynamodbconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-dynamodbconfig-syntax.json"></a>

```
{
  "[AwsRegion](#cfn-appsync-datasource-dynamodbconfig-awsregion)" : {{String}},
  "[DeltaSyncConfig](#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig)" : {{DeltaSyncConfig}},
  "[TableName](#cfn-appsync-datasource-dynamodbconfig-tablename)" : {{String}},
  "[UseCallerCredentials](#cfn-appsync-datasource-dynamodbconfig-usecallercredentials)" : {{Boolean}},
  "[Versioned](#cfn-appsync-datasource-dynamodbconfig-versioned)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-dynamodbconfig-syntax.yaml"></a>

```
  [AwsRegion](#cfn-appsync-datasource-dynamodbconfig-awsregion): {{String}}
  [DeltaSyncConfig](#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig): {{
    DeltaSyncConfig}}
  [TableName](#cfn-appsync-datasource-dynamodbconfig-tablename): {{String}}
  [UseCallerCredentials](#cfn-appsync-datasource-dynamodbconfig-usecallercredentials): {{Boolean}}
  [Versioned](#cfn-appsync-datasource-dynamodbconfig-versioned): {{Boolean}}
```

## Properties
<a name="aws-properties-appsync-datasource-dynamodbconfig-properties"></a>

`AwsRegion`  <a name="cfn-appsync-datasource-dynamodbconfig-awsregion"></a>
The AWS Region.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeltaSyncConfig`  <a name="cfn-appsync-datasource-dynamodbconfig-deltasyncconfig"></a>
The `DeltaSyncConfig` for a versioned datasource.
*Required*: No
*Type*: [DeltaSyncConfig](aws-properties-appsync-datasource-deltasyncconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-appsync-datasource-dynamodbconfig-tablename"></a>
The table name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseCallerCredentials`  <a name="cfn-appsync-datasource-dynamodbconfig-usecallercredentials"></a>
Set to `TRUE` to use AWS Identity and Access Management with this data source.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Versioned`  <a name="cfn-appsync-datasource-dynamodbconfig-versioned"></a>
Set to TRUE to use Conflict Detection and Resolution with this data source.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
