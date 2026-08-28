---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-relationalfilterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RelationalFilterConfiguration
<a name="aws-properties-datazone-datasource-relationalfilterconfiguration"></a>

The relational filter configuration for the data source.

## Syntax
<a name="aws-properties-datazone-datasource-relationalfilterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-relationalfilterconfiguration-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-datazone-datasource-relationalfilterconfiguration-databasename)" : {{String}},
  "[FilterExpressions](#cfn-datazone-datasource-relationalfilterconfiguration-filterexpressions)" : {{[ FilterExpression, ... ]}},
  "[SchemaName](#cfn-datazone-datasource-relationalfilterconfiguration-schemaname)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-relationalfilterconfiguration-syntax.yaml"></a>

```
  [DatabaseName](#cfn-datazone-datasource-relationalfilterconfiguration-databasename): {{String}}
  [FilterExpressions](#cfn-datazone-datasource-relationalfilterconfiguration-filterexpressions): {{
    - FilterExpression}}
  [SchemaName](#cfn-datazone-datasource-relationalfilterconfiguration-schemaname): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-relationalfilterconfiguration-properties"></a>

`DatabaseName`  <a name="cfn-datazone-datasource-relationalfilterconfiguration-databasename"></a>
The database name specified in the relational filter configuration for the data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterExpressions`  <a name="cfn-datazone-datasource-relationalfilterconfiguration-filterexpressions"></a>
The filter expressions specified in the relational filter configuration for the data source.
*Required*: No
*Type*: Array of [FilterExpression](aws-properties-datazone-datasource-filterexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaName`  <a name="cfn-datazone-datasource-relationalfilterconfiguration-schemaname"></a>
The schema name specified in the relational filter configuration for the data source.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
