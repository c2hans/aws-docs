---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable IntermediateTableAnalysisRuleCustom
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom"></a>

Contains the custom analysis rule configuration for an intermediate table.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-syntax.json"></a>

```
{
  "[AdditionalAnalyses](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-additionalanalyses)" : {{String}},
  "[AllowedAnalyses](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedanalyses)" : {{[ String, ... ]}},
  "[AllowedAnalysisProviders](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedanalysisproviders)" : {{[ String, ... ]}},
  "[AllowedResultReceivers](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedresultreceivers)" : {{[ String, ... ]}},
  "[DifferentialPrivacy](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-differentialprivacy)" : {{DifferentialPrivacy}},
  "[DisallowedOutputColumns](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-disallowedoutputcolumns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-syntax.yaml"></a>

```
  [AdditionalAnalyses](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-additionalanalyses): {{String}}
  [AllowedAnalyses](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedanalyses): {{
    - String}}
  [AllowedAnalysisProviders](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedanalysisproviders): {{
    - String}}
  [AllowedResultReceivers](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedresultreceivers): {{
    - String}}
  [DifferentialPrivacy](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-differentialprivacy): {{
    DifferentialPrivacy}}
  [DisallowedOutputColumns](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-disallowedoutputcolumns): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-properties"></a>

`AdditionalAnalyses`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-additionalanalyses"></a>
The setting that controls whether additional analyses are allowed on the intermediate table.
*Required*: No
*Type*: String
*Allowed values*: `ALLOWED | REQUIRED | NOT_ALLOWED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedAnalyses`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedanalyses"></a>
The list of allowed analyses that can be performed on the intermediate table.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedAnalysisProviders`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedanalysisproviders"></a>
The list of AWS account IDs for the allowed analysis providers.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedResultReceivers`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-allowedresultreceivers"></a>
The list of AWS account IDs that are allowed to receive results from queries run on the intermediate table.
*Required*: No
*Type*: Array of String
*Maximum*: `12`
*Minimum*: `12 | 0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DifferentialPrivacy`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-differentialprivacy"></a>
Property description not available.
*Required*: No
*Type*: [DifferentialPrivacy](aws-properties-cleanrooms-intermediatetable-differentialprivacy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisallowedOutputColumns`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom-disallowedoutputcolumns"></a>
The list of columns that are not allowed in the query output.
*Required*: No
*Type*: Array of String
*Maximum*: `127`
*Minimum*: `1 | 0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
