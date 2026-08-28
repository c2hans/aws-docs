---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource SalesforceStandardKnowledgeArticleTypeConfiguration
<a name="aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration"></a>

Provides the configuration information for standard Salesforce knowledge articles.

## Syntax
<a name="aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-syntax.json"></a>

```
{
  "[DocumentDataFieldName](#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documentdatafieldname)" : {{String}},
  "[DocumentTitleFieldName](#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documenttitlefieldname)" : {{String}},
  "[FieldMappings](#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-fieldmappings)" : {{[ DataSourceToIndexFieldMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-syntax.yaml"></a>

```
  [DocumentDataFieldName](#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documentdatafieldname): {{String}}
  [DocumentTitleFieldName](#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documenttitlefieldname): {{String}}
  [FieldMappings](#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-fieldmappings): {{
    - DataSourceToIndexFieldMapping}}
```

## Properties
<a name="aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-properties"></a>

`DocumentDataFieldName`  <a name="cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documentdatafieldname"></a>
The name of the field that contains the document data to index.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentTitleFieldName`  <a name="cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documenttitlefieldname"></a>
The name of the field that contains the document title.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldMappings`  <a name="cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-fieldmappings"></a>
Maps attributes or field names of the knowledge article to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Salesforce fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The Salesforce data source field names must exist in your Salesforce custom metadata.
*Required*: No
*Type*: Array of [DataSourceToIndexFieldMapping](aws-properties-kendra-datasource-datasourcetoindexfieldmapping.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
