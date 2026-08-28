---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-patternobjectfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource PatternObjectFilter
<a name="aws-properties-bedrock-datasource-patternobjectfilter"></a>

The specific filters applied to your data source content. You can filter out or include certain content.

## Syntax
<a name="aws-properties-bedrock-datasource-patternobjectfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-patternobjectfilter-syntax.json"></a>

```
{
  "[ExclusionFilters](#cfn-bedrock-datasource-patternobjectfilter-exclusionfilters)" : {{[ String, ... ]}},
  "[InclusionFilters](#cfn-bedrock-datasource-patternobjectfilter-inclusionfilters)" : {{[ String, ... ]}},
  "[ObjectType](#cfn-bedrock-datasource-patternobjectfilter-objecttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-patternobjectfilter-syntax.yaml"></a>

```
  [ExclusionFilters](#cfn-bedrock-datasource-patternobjectfilter-exclusionfilters): {{
    - String}}
  [InclusionFilters](#cfn-bedrock-datasource-patternobjectfilter-inclusionfilters): {{
    - String}}
  [ObjectType](#cfn-bedrock-datasource-patternobjectfilter-objecttype): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-patternobjectfilter-properties"></a>

`ExclusionFilters`  <a name="cfn-bedrock-datasource-patternobjectfilter-exclusionfilters"></a>
A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000 | 25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InclusionFilters`  <a name="cfn-bedrock-datasource-patternobjectfilter-inclusionfilters"></a>
A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000 | 25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectType`  <a name="cfn-bedrock-datasource-patternobjectfilter-objecttype"></a>
The supported object type or content type of the data source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
