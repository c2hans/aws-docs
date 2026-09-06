---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTableAssociation ConfiguredTableAssociationAnalysisRuleAggregation
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation"></a>

 The configured table association analysis rule applied to a configured table with the aggregation analysis rule.

## Syntax
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-syntax.json"></a>

```
{
  "[AllowedAdditionalAnalyses](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedadditionalanalyses)" : {{[ String, ... ]}},
  "[AllowedResultReceivers](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedresultreceivers)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-syntax.yaml"></a>

```
  [AllowedAdditionalAnalyses](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedadditionalanalyses): {{
    - String}}
  [AllowedResultReceivers](#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedresultreceivers): {{
    - String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-properties"></a>

`AllowedAdditionalAnalyses`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedadditionalanalyses"></a>
 The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.
The `allowedAdditionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList`) and the custom analysis rule (`AnalysisRuleCustom`).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedResultReceivers`  <a name="cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedresultreceivers"></a>
 The list of collaboration members who are allowed to receive results of queries run with this configured table.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
