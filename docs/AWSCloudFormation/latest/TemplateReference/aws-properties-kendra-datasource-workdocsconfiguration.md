---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-workdocsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource WorkDocsConfiguration
<a name="aws-properties-kendra-datasource-workdocsconfiguration"></a>

Provides the configuration information to connect to WorkDocs as your data source.

WorkDocs connector is available in Oregon, North Virginia, Sydney, Singapore and Ireland regions.

## Syntax
<a name="aws-properties-kendra-datasource-workdocsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-workdocsconfiguration-syntax.json"></a>

```
{
  "[CrawlComments](#cfn-kendra-datasource-workdocsconfiguration-crawlcomments)" : {{Boolean}},
  "[ExclusionPatterns](#cfn-kendra-datasource-workdocsconfiguration-exclusionpatterns)" : {{[ String, ... ]}},
  "[FieldMappings](#cfn-kendra-datasource-workdocsconfiguration-fieldmappings)" : {{[ DataSourceToIndexFieldMapping, ... ]}},
  "[InclusionPatterns](#cfn-kendra-datasource-workdocsconfiguration-inclusionpatterns)" : {{[ String, ... ]}},
  "[OrganizationId](#cfn-kendra-datasource-workdocsconfiguration-organizationid)" : {{String}},
  "[UseChangeLog](#cfn-kendra-datasource-workdocsconfiguration-usechangelog)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-workdocsconfiguration-syntax.yaml"></a>

```
  [CrawlComments](#cfn-kendra-datasource-workdocsconfiguration-crawlcomments): {{Boolean}}
  [ExclusionPatterns](#cfn-kendra-datasource-workdocsconfiguration-exclusionpatterns): {{
    - String}}
  [FieldMappings](#cfn-kendra-datasource-workdocsconfiguration-fieldmappings): {{
    - DataSourceToIndexFieldMapping}}
  [InclusionPatterns](#cfn-kendra-datasource-workdocsconfiguration-inclusionpatterns): {{
    - String}}
  [OrganizationId](#cfn-kendra-datasource-workdocsconfiguration-organizationid): {{String}}
  [UseChangeLog](#cfn-kendra-datasource-workdocsconfiguration-usechangelog): {{Boolean}}
```

## Properties
<a name="aws-properties-kendra-datasource-workdocsconfiguration-properties"></a>

`CrawlComments`  <a name="cfn-kendra-datasource-workdocsconfiguration-crawlcomments"></a>
`TRUE` to include comments on documents in your index. Including comments in your index means each comment is a document that can be searched on.
The default is set to `FALSE`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExclusionPatterns`  <a name="cfn-kendra-datasource-workdocsconfiguration-exclusionpatterns"></a>
A list of regular expression patterns to exclude certain files in your WorkDocs site repository. Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldMappings`  <a name="cfn-kendra-datasource-workdocsconfiguration-fieldmappings"></a>
A list of `DataSourceToIndexFieldMapping` objects that map WorkDocs data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to WorkDocs fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html). The WorkDocs data source field names must exist in your WorkDocs custom metadata.
*Required*: No
*Type*: Array of [DataSourceToIndexFieldMapping](aws-properties-kendra-datasource-datasourcetoindexfieldmapping.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InclusionPatterns`  <a name="cfn-kendra-datasource-workdocsconfiguration-inclusionpatterns"></a>
A list of regular expression patterns to include certain files in your WorkDocs site repository. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationId`  <a name="cfn-kendra-datasource-workdocsconfiguration-organizationid"></a>
The identifier of the directory corresponding to your WorkDocs site repository.
You can find the organization ID in the [Directory Service](https://console.aws.amazon.com/directoryservicev2/) by going to **Active Directory**, then **Directories**. Your WorkDocs site directory has an ID, which is the organization ID. You can also set up a new WorkDocs directory in the Directory Service console and enable a WorkDocs site for the directory in the WorkDocs console.
*Required*: Yes
*Type*: String
*Pattern*: `d-[0-9a-fA-F]{10}`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UseChangeLog`  <a name="cfn-kendra-datasource-workdocsconfiguration-usechangelog"></a>
`TRUE` to use the WorkDocs change log to determine which documents require updating in the index. Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in WorkDocs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
