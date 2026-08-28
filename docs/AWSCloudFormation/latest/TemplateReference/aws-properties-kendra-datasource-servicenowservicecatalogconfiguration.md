---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource ServiceNowServiceCatalogConfiguration
<a name="aws-properties-kendra-datasource-servicenowservicecatalogconfiguration"></a>

Provides the configuration information for crawling service catalog items in the ServiceNow site

## Syntax
<a name="aws-properties-kendra-datasource-servicenowservicecatalogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-servicenowservicecatalogconfiguration-syntax.json"></a>

```
{
  "[CrawlAttachments](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-crawlattachments)" : {{Boolean}},
  "[DocumentDataFieldName](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documentdatafieldname)" : {{String}},
  "[DocumentTitleFieldName](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documenttitlefieldname)" : {{String}},
  "[ExcludeAttachmentFilePatterns](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-excludeattachmentfilepatterns)" : {{[ String, ... ]}},
  "[FieldMappings](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-fieldmappings)" : {{[ DataSourceToIndexFieldMapping, ... ]}},
  "[IncludeAttachmentFilePatterns](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-includeattachmentfilepatterns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-servicenowservicecatalogconfiguration-syntax.yaml"></a>

```
  [CrawlAttachments](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-crawlattachments): {{Boolean}}
  [DocumentDataFieldName](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documentdatafieldname): {{String}}
  [DocumentTitleFieldName](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documenttitlefieldname): {{String}}
  [ExcludeAttachmentFilePatterns](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-excludeattachmentfilepatterns): {{
    - String}}
  [FieldMappings](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-fieldmappings): {{
    - DataSourceToIndexFieldMapping}}
  [IncludeAttachmentFilePatterns](#cfn-kendra-datasource-servicenowservicecatalogconfiguration-includeattachmentfilepatterns): {{
    - String}}
```

## Properties
<a name="aws-properties-kendra-datasource-servicenowservicecatalogconfiguration-properties"></a>

`CrawlAttachments`  <a name="cfn-kendra-datasource-servicenowservicecatalogconfiguration-crawlattachments"></a>
`TRUE` to index attachments to service catalog items.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentDataFieldName`  <a name="cfn-kendra-datasource-servicenowservicecatalogconfiguration-documentdatafieldname"></a>
The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentTitleFieldName`  <a name="cfn-kendra-datasource-servicenowservicecatalogconfiguration-documenttitlefieldname"></a>
The name of the ServiceNow field that is mapped to the index document title field.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeAttachmentFilePatterns`  <a name="cfn-kendra-datasource-servicenowservicecatalogconfiguration-excludeattachmentfilepatterns"></a>
A list of regular expression patterns to exclude certain attachments of catalogs in your ServiceNow. Item that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.
The regex is applied to the file name of the attachment.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldMappings`  <a name="cfn-kendra-datasource-servicenowservicecatalogconfiguration-fieldmappings"></a>
Maps attributes or field names of catalogs to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to ServiceNow fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The ServiceNow data source field names must exist in your ServiceNow custom metadata.
*Required*: No
*Type*: Array of [DataSourceToIndexFieldMapping](aws-properties-kendra-datasource-datasourcetoindexfieldmapping.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeAttachmentFilePatterns`  <a name="cfn-kendra-datasource-servicenowservicecatalogconfiguration-includeattachmentfilepatterns"></a>
A list of regular expression patterns to include certain attachments of catalogs in your ServiceNow. Item that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.
The regex is applied to the file name of the attachment.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
