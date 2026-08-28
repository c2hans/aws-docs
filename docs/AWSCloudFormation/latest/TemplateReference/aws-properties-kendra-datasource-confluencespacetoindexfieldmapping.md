---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource ConfluenceSpaceToIndexFieldMapping
<a name="aws-properties-kendra-datasource-confluencespacetoindexfieldmapping"></a>

Maps attributes or field names of Confluence spaces to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The Confluence data source field names must exist in your Confluence custom metadata.

## Syntax
<a name="aws-properties-kendra-datasource-confluencespacetoindexfieldmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-confluencespacetoindexfieldmapping-syntax.json"></a>

```
{
  "[DataSourceFieldName](#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datasourcefieldname)" : {{String}},
  "[DateFieldFormat](#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datefieldformat)" : {{String}},
  "[IndexFieldName](#cfn-kendra-datasource-confluencespacetoindexfieldmapping-indexfieldname)" : {{String}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-confluencespacetoindexfieldmapping-syntax.yaml"></a>

```
  [DataSourceFieldName](#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datasourcefieldname): {{String}}
  [DateFieldFormat](#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datefieldformat): {{String}}
  [IndexFieldName](#cfn-kendra-datasource-confluencespacetoindexfieldmapping-indexfieldname): {{String}}
```

## Properties
<a name="aws-properties-kendra-datasource-confluencespacetoindexfieldmapping-properties"></a>

`DataSourceFieldName`  <a name="cfn-kendra-datasource-confluencespacetoindexfieldmapping-datasourcefieldname"></a>
The name of the field in the data source.
*Required*: Yes
*Type*: String
*Allowed values*: `DISPLAY_URL | ITEM_TYPE | SPACE_KEY | URL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateFieldFormat`  <a name="cfn-kendra-datasource-confluencespacetoindexfieldmapping-datefieldformat"></a>
The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.
*Required*: No
*Type*: String
*Minimum*: `4`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexFieldName`  <a name="cfn-kendra-datasource-confluencespacetoindexfieldmapping-indexfieldname"></a>
The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
