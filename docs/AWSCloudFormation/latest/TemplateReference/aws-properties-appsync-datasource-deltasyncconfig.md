---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-datasource-deltasyncconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DataSource DeltaSyncConfig
<a name="aws-properties-appsync-datasource-deltasyncconfig"></a>

Describes a Delta Sync configuration.

## Syntax
<a name="aws-properties-appsync-datasource-deltasyncconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-datasource-deltasyncconfig-syntax.json"></a>

```
{
  "[BaseTableTTL](#cfn-appsync-datasource-deltasyncconfig-basetablettl)" : {{String}},
  "[DeltaSyncTableName](#cfn-appsync-datasource-deltasyncconfig-deltasynctablename)" : {{String}},
  "[DeltaSyncTableTTL](#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-datasource-deltasyncconfig-syntax.yaml"></a>

```
  [BaseTableTTL](#cfn-appsync-datasource-deltasyncconfig-basetablettl): {{String}}
  [DeltaSyncTableName](#cfn-appsync-datasource-deltasyncconfig-deltasynctablename): {{String}}
  [DeltaSyncTableTTL](#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl): {{String}}
```

## Properties
<a name="aws-properties-appsync-datasource-deltasyncconfig-properties"></a>

`BaseTableTTL`  <a name="cfn-appsync-datasource-deltasyncconfig-basetablettl"></a>
The number of minutes that an Item is stored in the data source.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeltaSyncTableName`  <a name="cfn-appsync-datasource-deltasyncconfig-deltasynctablename"></a>
The Delta Sync table name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeltaSyncTableTTL`  <a name="cfn-appsync-datasource-deltasyncconfig-deltasynctablettl"></a>
The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
