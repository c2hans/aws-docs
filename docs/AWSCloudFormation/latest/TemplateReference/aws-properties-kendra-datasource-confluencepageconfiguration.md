---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-confluencepageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource ConfluencePageConfiguration
<a name="aws-properties-kendra-datasource-confluencepageconfiguration"></a>

Configuration of the page settings for the Confluence data source.

## Syntax
<a name="aws-properties-kendra-datasource-confluencepageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-confluencepageconfiguration-syntax.json"></a>

```
{
  "[PageFieldMappings](#cfn-kendra-datasource-confluencepageconfiguration-pagefieldmappings)" : {{[ ConfluencePageToIndexFieldMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-confluencepageconfiguration-syntax.yaml"></a>

```
  [PageFieldMappings](#cfn-kendra-datasource-confluencepageconfiguration-pagefieldmappings): {{
    - ConfluencePageToIndexFieldMapping}}
```

## Properties
<a name="aws-properties-kendra-datasource-confluencepageconfiguration-properties"></a>

`PageFieldMappings`  <a name="cfn-kendra-datasource-confluencepageconfiguration-pagefieldmappings"></a>
Maps attributes or field names of Confluence pages to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The Confluence data source field names must exist in your Confluence custom metadata.
If you specify the `PageFieldMappings` parameter, you must specify at least one field mapping.
*Required*: No
*Type*: Array of [ConfluencePageToIndexFieldMapping](aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.md)
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
