---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-confluencespaceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource ConfluenceSpaceConfiguration
<a name="aws-properties-kendra-datasource-confluencespaceconfiguration"></a>

Configuration information for indexing Confluence spaces.

## Syntax
<a name="aws-properties-kendra-datasource-confluencespaceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-confluencespaceconfiguration-syntax.json"></a>

```
{
  "[CrawlArchivedSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-crawlarchivedspaces)" : {{Boolean}},
  "[CrawlPersonalSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-crawlpersonalspaces)" : {{Boolean}},
  "[ExcludeSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-excludespaces)" : {{[ String, ... ]}},
  "[IncludeSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-includespaces)" : {{[ String, ... ]}},
  "[SpaceFieldMappings](#cfn-kendra-datasource-confluencespaceconfiguration-spacefieldmappings)" : {{[ ConfluenceSpaceToIndexFieldMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-confluencespaceconfiguration-syntax.yaml"></a>

```
  [CrawlArchivedSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-crawlarchivedspaces): {{Boolean}}
  [CrawlPersonalSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-crawlpersonalspaces): {{Boolean}}
  [ExcludeSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-excludespaces): {{
    - String}}
  [IncludeSpaces](#cfn-kendra-datasource-confluencespaceconfiguration-includespaces): {{
    - String}}
  [SpaceFieldMappings](#cfn-kendra-datasource-confluencespaceconfiguration-spacefieldmappings): {{
    - ConfluenceSpaceToIndexFieldMapping}}
```

## Properties
<a name="aws-properties-kendra-datasource-confluencespaceconfiguration-properties"></a>

`CrawlArchivedSpaces`  <a name="cfn-kendra-datasource-confluencespaceconfiguration-crawlarchivedspaces"></a>
`TRUE` to index archived spaces.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrawlPersonalSpaces`  <a name="cfn-kendra-datasource-confluencespaceconfiguration-crawlpersonalspaces"></a>
`TRUE` to index personal spaces. You can add restrictions to items in personal spaces. If personal spaces are indexed, queries without user context information may return restricted items from a personal space in their results. For more information, see [Filtering on user context](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeSpaces`  <a name="cfn-kendra-datasource-confluencespaceconfiguration-excludespaces"></a>
A list of space keys of Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are not indexed. If a space is in both the `ExcludeSpaces` and the `IncludeSpaces` list, the space is excluded.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeSpaces`  <a name="cfn-kendra-datasource-confluencespaceconfiguration-includespaces"></a>
A list of space keys for Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are indexed. Spaces that aren't in the list aren't indexed. A space in the list must exist. Otherwise, Amazon Kendra logs an error when the data source is synchronized. If a space is in both the `IncludeSpaces` and the `ExcludeSpaces` list, the space is excluded.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceFieldMappings`  <a name="cfn-kendra-datasource-confluencespaceconfiguration-spacefieldmappings"></a>
Maps attributes or field names of Confluence spaces to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The Confluence data source field names must exist in your Confluence custom metadata.
If you specify the `SpaceFieldMappings` parameter, you must specify at least one field mapping.
*Required*: No
*Type*: Array of [ConfluenceSpaceToIndexFieldMapping](aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.md)
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
