---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-rdshttpendpointconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource RdsHttpEndpointConfig
<a name="aws-properties-appsync-datasource-rdshttpendpointconfig"></a>

Use the `RdsHttpEndpointConfig` property type to specify the `RdsHttpEndpoint` for an AWS AppSync relational database.

`RdsHttpEndpointConfig` is a property of the [AWS AppSync DataSource RelationalDatabaseConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html) resource.

## Syntax
<a name="aws-properties-appsync-datasource-rdshttpendpointconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-rdshttpendpointconfig-syntax.json"></a>

```
{
  "[AwsRegion](#cfn-appsync-datasource-rdshttpendpointconfig-awsregion)" : {{String}},
  "[AwsSecretStoreArn](#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn)" : {{String}},
  "[DatabaseName](#cfn-appsync-datasource-rdshttpendpointconfig-databasename)" : {{String}},
  "[DbClusterIdentifier](#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier)" : {{String}},
  "[Schema](#cfn-appsync-datasource-rdshttpendpointconfig-schema)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-rdshttpendpointconfig-syntax.yaml"></a>

```
  [AwsRegion](#cfn-appsync-datasource-rdshttpendpointconfig-awsregion): {{String}}
  [AwsSecretStoreArn](#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn): {{String}}
  [DatabaseName](#cfn-appsync-datasource-rdshttpendpointconfig-databasename): {{String}}
  [DbClusterIdentifier](#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier): {{String}}
  [Schema](#cfn-appsync-datasource-rdshttpendpointconfig-schema): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-rdshttpendpointconfig-properties"></a>

`AwsRegion`  <a name="cfn-appsync-datasource-rdshttpendpointconfig-awsregion"></a>
AWS Region for RDS HTTP endpoint.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsSecretStoreArn`  <a name="cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn"></a>
The ARN for database credentials stored in AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-appsync-datasource-rdshttpendpointconfig-databasename"></a>
Logical database name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DbClusterIdentifier`  <a name="cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier"></a>
Amazon RDS cluster Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-appsync-datasource-rdshttpendpointconfig-schema"></a>
Logical schema name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
