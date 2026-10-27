---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-recommender-trainingdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Recommender TrainingDataConfig
<a name="aws-properties-personalize-recommender-trainingdataconfig"></a>

The training data configuration to use when creating a domain recommender or custom solution version (trained model).

## Syntax
<a name="aws-properties-personalize-recommender-trainingdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-recommender-trainingdataconfig-syntax.json"></a>

```
{
  "[ExcludedDatasetColumns](#cfn-personalize-recommender-trainingdataconfig-excludeddatasetcolumns)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-personalize-recommender-trainingdataconfig-syntax.yaml"></a>

```
  [ExcludedDatasetColumns](#cfn-personalize-recommender-trainingdataconfig-excludeddatasetcolumns): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-personalize-recommender-trainingdataconfig-properties"></a>

`ExcludedDatasetColumns`  <a name="cfn-personalize-recommender-trainingdataconfig-excludeddatasetcolumns"></a>
Specifies the columns to exclude from training. Each key is a dataset type, and each value is a list of columns. Exclude columns to control what data Amazon Personalize uses to generate recommendations.
 For example, you might have a column that you want to use only to filter recommendations. You can exclude this column from training and Amazon Personalize considers it only when filtering.
*Required*: No
*Type*: Object of Array
*Pattern*: `^[A-Za-z_]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
