---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-analysistemplate-columnclassificationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::AnalysisTemplate ColumnClassificationDetails
<a name="aws-properties-cleanrooms-analysistemplate-columnclassificationdetails"></a>

Contains classification information for data columns, including mappings that specify how columns should be handled during synthetic data generation and privacy analysis.

## Syntax
<a name="aws-properties-cleanrooms-analysistemplate-columnclassificationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-analysistemplate-columnclassificationdetails-syntax.json"></a>

```
{
  "[ColumnMapping](#cfn-cleanrooms-analysistemplate-columnclassificationdetails-columnmapping)" : {{[ SyntheticDataColumnProperties, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-analysistemplate-columnclassificationdetails-syntax.yaml"></a>

```
  [ColumnMapping](#cfn-cleanrooms-analysistemplate-columnclassificationdetails-columnmapping): {{
    - SyntheticDataColumnProperties}}
```

## Properties
<a name="aws-properties-cleanrooms-analysistemplate-columnclassificationdetails-properties"></a>

`ColumnMapping`  <a name="cfn-cleanrooms-analysistemplate-columnclassificationdetails-columnmapping"></a>
A mapping that defines the classification of data columns for synthetic data generation and specifies how each column should be handled during the privacy-preserving data synthesis process.
*Required*: Yes
*Type*: Array of [SyntheticDataColumnProperties](aws-properties-cleanrooms-analysistemplate-syntheticdatacolumnproperties.md)
*Minimum*: `5`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
