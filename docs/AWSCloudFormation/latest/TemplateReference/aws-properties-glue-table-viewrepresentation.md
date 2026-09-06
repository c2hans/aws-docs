---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-viewrepresentation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table ViewRepresentation
<a name="aws-properties-glue-table-viewrepresentation"></a>

A structure that contains the dialect of the view, and the query that defines the view.

## Syntax
<a name="aws-properties-glue-table-viewrepresentation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-viewrepresentation-syntax.json"></a>

```
{
  "[Dialect](#cfn-glue-table-viewrepresentation-dialect)" : {{String}},
  "[DialectVersion](#cfn-glue-table-viewrepresentation-dialectversion)" : {{String}},
  "[ValidationConnection](#cfn-glue-table-viewrepresentation-validationconnection)" : {{String}},
  "[ViewExpandedText](#cfn-glue-table-viewrepresentation-viewexpandedtext)" : {{String}},
  "[ViewOriginalText](#cfn-glue-table-viewrepresentation-vieworiginaltext)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-viewrepresentation-syntax.yaml"></a>

```
  [Dialect](#cfn-glue-table-viewrepresentation-dialect): {{String}}
  [DialectVersion](#cfn-glue-table-viewrepresentation-dialectversion): {{String}}
  [ValidationConnection](#cfn-glue-table-viewrepresentation-validationconnection): {{String}}
  [ViewExpandedText](#cfn-glue-table-viewrepresentation-viewexpandedtext): {{String}}
  [ViewOriginalText](#cfn-glue-table-viewrepresentation-vieworiginaltext): {{String}}
```

## Properties
<a name="aws-properties-glue-table-viewrepresentation-properties"></a>

`Dialect`  <a name="cfn-glue-table-viewrepresentation-dialect"></a>
The dialect of the query engine.
*Required*: No
*Type*: String
*Allowed values*: `REDSHIFT | ATHENA | SPARK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DialectVersion`  <a name="cfn-glue-table-viewrepresentation-dialectversion"></a>
The version of the dialect of the query engine. For example, 3.0.0.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationConnection`  <a name="cfn-glue-table-viewrepresentation-validationconnection"></a>
The name of the connection to be used to validate the specific representation of the view.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewExpandedText`  <a name="cfn-glue-table-viewrepresentation-viewexpandedtext"></a>
The expanded SQL for the view. This SQL is used by engines while processing a query on a view. Engines may perform operations during view creation to transform `ViewOriginalText` to `ViewExpandedText`. For example:
+ Fully qualified identifiers: `SELECT * from table1 -> SELECT * from db1.table1`
*Required*: No
*Type*: String
*Maximum*: `409600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewOriginalText`  <a name="cfn-glue-table-viewrepresentation-vieworiginaltext"></a>
The `SELECT` query provided by the customer during `CREATE VIEW DDL`. This SQL is not used during a query on a view (`ViewExpandedText` is used instead). `ViewOriginalText` is used for cases like `SHOW CREATE VIEW` where users want to see the original DDL command that created the view.
*Required*: No
*Type*: String
*Maximum*: `409600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
