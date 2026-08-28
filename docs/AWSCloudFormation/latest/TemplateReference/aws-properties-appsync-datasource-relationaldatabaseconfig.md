---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-relationaldatabaseconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource RelationalDatabaseConfig
<a name="aws-properties-appsync-datasource-relationaldatabaseconfig"></a>

Use the `RelationalDatabaseConfig` property type to specify `RelationalDatabaseConfig` for an AWS AppSync data source.

`RelationalDatabaseConfig` is a property of the [AWS::AppSync::DataSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html) property type.

## Syntax
<a name="aws-properties-appsync-datasource-relationaldatabaseconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-relationaldatabaseconfig-syntax.json"></a>

```
{
  "[RdsHttpEndpointConfig](#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig)" : {{RdsHttpEndpointConfig}},
  "[RelationalDatabaseSourceType](#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-relationaldatabaseconfig-syntax.yaml"></a>

```
  [RdsHttpEndpointConfig](#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig): {{
    RdsHttpEndpointConfig}}
  [RelationalDatabaseSourceType](#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-relationaldatabaseconfig-properties"></a>

`RdsHttpEndpointConfig`  <a name="cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig"></a>
Information about the Amazon RDS resource.
*Required*: No
*Type*: [RdsHttpEndpointConfig](aws-properties-appsync-datasource-rdshttpendpointconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelationalDatabaseSourceType`  <a name="cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype"></a>
The type of relational data source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
