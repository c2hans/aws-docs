---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformscorethreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormScoreThreshold
<a name="aws-properties-connect-evaluationform-evaluationformscorethreshold"></a>

Information about a score threshold for a performance category.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformscorethreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformscorethreshold-syntax.json"></a>

```
{
  "[MaxScorePercentage](#cfn-connect-evaluationform-evaluationformscorethreshold-maxscorepercentage)" : {{Number}},
  "[MinScorePercentage](#cfn-connect-evaluationform-evaluationformscorethreshold-minscorepercentage)" : {{Number}},
  "[PerformanceCategory](#cfn-connect-evaluationform-evaluationformscorethreshold-performancecategory)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformscorethreshold-syntax.yaml"></a>

```
  [MaxScorePercentage](#cfn-connect-evaluationform-evaluationformscorethreshold-maxscorepercentage): {{Number}}
  [MinScorePercentage](#cfn-connect-evaluationform-evaluationformscorethreshold-minscorepercentage): {{Number}}
  [PerformanceCategory](#cfn-connect-evaluationform-evaluationformscorethreshold-performancecategory): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformscorethreshold-properties"></a>

`MaxScorePercentage`  <a name="cfn-connect-evaluationform-evaluationformscorethreshold-maxscorepercentage"></a>
The maximum score percentage for the performance category.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinScorePercentage`  <a name="cfn-connect-evaluationform-evaluationformscorethreshold-minscorepercentage"></a>
The minimum score percentage for the performance category.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerformanceCategory`  <a name="cfn-connect-evaluationform-evaluationformscorethreshold-performancecategory"></a>
The performance category name.
*Required*: Yes
*Type*: String
*Allowed values*: `NEEDS_IMPROVEMENT | EXCEEDS_EXPECTATIONS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
