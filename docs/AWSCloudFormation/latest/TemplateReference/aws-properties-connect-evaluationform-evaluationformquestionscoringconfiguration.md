---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormQuestionScoringConfiguration
<a name="aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration"></a>

Scoring configuration for a question in an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration-syntax.json"></a>

```
{
  "[IsExcludedFromScoring](#cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-isexcludedfromscoring)" : {{Boolean}},
  "[PointsConfiguration](#cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-pointsconfiguration)" : {{QuestionPointsConfiguration}},
  "[ScoreThresholds](#cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-scorethresholds)" : {{[ EvaluationFormScoreThreshold, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration-syntax.yaml"></a>

```
  [IsExcludedFromScoring](#cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-isexcludedfromscoring): {{Boolean}}
  [PointsConfiguration](#cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-pointsconfiguration): {{
    QuestionPointsConfiguration}}
  [ScoreThresholds](#cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-scorethresholds): {{
    - EvaluationFormScoreThreshold}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration-properties"></a>

`IsExcludedFromScoring`  <a name="cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-isexcludedfromscoring"></a>
The flag to exclude the question from scoring.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointsConfiguration`  <a name="cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-pointsconfiguration"></a>
The points configuration for point-based scoring.
*Required*: No
*Type*: [QuestionPointsConfiguration](aws-properties-connect-evaluationform-questionpointsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScoreThresholds`  <a name="cfn-connect-evaluationform-evaluationformquestionscoringconfiguration-scorethresholds"></a>
The score thresholds for performance categories.
*Required*: No
*Type*: Array of [EvaluationFormScoreThreshold](aws-properties-connect-evaluationform-evaluationformscorethreshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
