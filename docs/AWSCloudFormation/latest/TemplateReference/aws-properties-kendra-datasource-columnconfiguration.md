---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-columnconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource ColumnConfiguration
<a name="aws-properties-kendra-datasource-columnconfiguration"></a>

Provides information about how Amazon Kendra should use the columns of a database in an index.

## Syntax
<a name="aws-properties-kendra-datasource-columnconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-columnconfiguration-syntax.json"></a>

```
{
  "[ChangeDetectingColumns](#cfn-kendra-datasource-columnconfiguration-changedetectingcolumns)" : {{[ String, ... ]}},
  "[DocumentDataColumnName](#cfn-kendra-datasource-columnconfiguration-documentdatacolumnname)" : {{String}},
  "[DocumentIdColumnName](#cfn-kendra-datasource-columnconfiguration-documentidcolumnname)" : {{String}},
  "[DocumentTitleColumnName](#cfn-kendra-datasource-columnconfiguration-documenttitlecolumnname)" : {{String}},
  "[FieldMappings](#cfn-kendra-datasource-columnconfiguration-fieldmappings)" : {{[ DataSourceToIndexFieldMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-columnconfiguration-syntax.yaml"></a>

```
  [ChangeDetectingColumns](#cfn-kendra-datasource-columnconfiguration-changedetectingcolumns): {{
    - String}}
  [DocumentDataColumnName](#cfn-kendra-datasource-columnconfiguration-documentdatacolumnname): {{String}}
  [DocumentIdColumnName](#cfn-kendra-datasource-columnconfiguration-documentidcolumnname): {{String}}
  [DocumentTitleColumnName](#cfn-kendra-datasource-columnconfiguration-documenttitlecolumnname): {{String}}
  [FieldMappings](#cfn-kendra-datasource-columnconfiguration-fieldmappings): {{
    - DataSourceToIndexFieldMapping}}
```

## Properties
<a name="aws-properties-kendra-datasource-columnconfiguration-properties"></a>

`ChangeDetectingColumns`  <a name="cfn-kendra-datasource-columnconfiguration-changedetectingcolumns"></a>
One to five columns that indicate when a document in the database has changed.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentDataColumnName`  <a name="cfn-kendra-datasource-columnconfiguration-documentdatacolumnname"></a>
The column that contains the contents of the document.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentIdColumnName`  <a name="cfn-kendra-datasource-columnconfiguration-documentidcolumnname"></a>
The column that provides the document's identifier.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentTitleColumnName`  <a name="cfn-kendra-datasource-columnconfiguration-documenttitlecolumnname"></a>
The column that contains the title of the document.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldMappings`  <a name="cfn-kendra-datasource-columnconfiguration-fieldmappings"></a>
An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the [UpdateIndex](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html) operation.
*Required*: No
*Type*: Array of [DataSourceToIndexFieldMapping](aws-properties-kendra-datasource-datasourcetoindexfieldmapping.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
