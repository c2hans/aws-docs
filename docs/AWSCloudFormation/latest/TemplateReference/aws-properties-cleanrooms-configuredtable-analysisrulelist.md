---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-analysisrulelist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable AnalysisRuleList
<a name="aws-properties-cleanrooms-configuredtable-analysisrulelist"></a>

A type of analysis rule that enables row-level analysis.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-analysisrulelist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-analysisrulelist-syntax.json"></a>

```
{
  "[AdditionalAnalyses](#cfn-cleanrooms-configuredtable-analysisrulelist-additionalanalyses)" : {{String}},
  "[AllowedJoinOperators](#cfn-cleanrooms-configuredtable-analysisrulelist-allowedjoinoperators)" : {{[ String, ... ]}},
  "[JoinColumns](#cfn-cleanrooms-configuredtable-analysisrulelist-joincolumns)" : {{[ String, ... ]}},
  "[ListColumns](#cfn-cleanrooms-configuredtable-analysisrulelist-listcolumns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-analysisrulelist-syntax.yaml"></a>

```
  [AdditionalAnalyses](#cfn-cleanrooms-configuredtable-analysisrulelist-additionalanalyses): {{String}}
  [AllowedJoinOperators](#cfn-cleanrooms-configuredtable-analysisrulelist-allowedjoinoperators): {{
    - String}}
  [JoinColumns](#cfn-cleanrooms-configuredtable-analysisrulelist-joincolumns): {{
    - String}}
  [ListColumns](#cfn-cleanrooms-configuredtable-analysisrulelist-listcolumns): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-analysisrulelist-properties"></a>

`AdditionalAnalyses`  <a name="cfn-cleanrooms-configuredtable-analysisrulelist-additionalanalyses"></a>
 An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
*Required*: No
*Type*: String
*Allowed values*: `ALLOWED | REQUIRED | NOT_ALLOWED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedJoinOperators`  <a name="cfn-cleanrooms-configuredtable-analysisrulelist-allowedjoinoperators"></a>
The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is `AND`.
*Required*: No
*Type*: Array of String
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JoinColumns`  <a name="cfn-cleanrooms-configuredtable-analysisrulelist-joincolumns"></a>
Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListColumns`  <a name="cfn-cleanrooms-configuredtable-analysisrulelist-listcolumns"></a>
Columns that can be listed in the output.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
