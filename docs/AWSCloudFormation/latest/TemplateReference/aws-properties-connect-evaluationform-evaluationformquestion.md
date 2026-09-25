---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformquestion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormQuestion
<a name="aws-properties-connect-evaluationform-evaluationformquestion"></a>

Information about a question from an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformquestion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformquestion-syntax.json"></a>

```
{
  "[Enablement](#cfn-connect-evaluationform-evaluationformquestion-enablement)" : {{EvaluationFormItemEnablementConfiguration}},
  "[Instructions](#cfn-connect-evaluationform-evaluationformquestion-instructions)" : {{String}},
  "[MetricConfiguration](#cfn-connect-evaluationform-evaluationformquestion-metricconfiguration)" : {{EvaluationFormMetricConfiguration}},
  "[NotApplicableEnabled](#cfn-connect-evaluationform-evaluationformquestion-notapplicableenabled)" : {{Boolean}},
  "[QuestionType](#cfn-connect-evaluationform-evaluationformquestion-questiontype)" : {{String}},
  "[QuestionTypeProperties](#cfn-connect-evaluationform-evaluationformquestion-questiontypeproperties)" : {{EvaluationFormQuestionTypeProperties}},
  "[RefId](#cfn-connect-evaluationform-evaluationformquestion-refid)" : {{String}},
  "[ScoringConfiguration](#cfn-connect-evaluationform-evaluationformquestion-scoringconfiguration)" : {{EvaluationFormQuestionScoringConfiguration}},
  "[Title](#cfn-connect-evaluationform-evaluationformquestion-title)" : {{String}},
  "[Weight](#cfn-connect-evaluationform-evaluationformquestion-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformquestion-syntax.yaml"></a>

```
  [Enablement](#cfn-connect-evaluationform-evaluationformquestion-enablement): {{
    EvaluationFormItemEnablementConfiguration}}
  [Instructions](#cfn-connect-evaluationform-evaluationformquestion-instructions): {{String}}
  [MetricConfiguration](#cfn-connect-evaluationform-evaluationformquestion-metricconfiguration): {{
    EvaluationFormMetricConfiguration}}
  [NotApplicableEnabled](#cfn-connect-evaluationform-evaluationformquestion-notapplicableenabled): {{Boolean}}
  [QuestionType](#cfn-connect-evaluationform-evaluationformquestion-questiontype): {{String}}
  [QuestionTypeProperties](#cfn-connect-evaluationform-evaluationformquestion-questiontypeproperties): {{
    EvaluationFormQuestionTypeProperties}}
  [RefId](#cfn-connect-evaluationform-evaluationformquestion-refid): {{String}}
  [ScoringConfiguration](#cfn-connect-evaluationform-evaluationformquestion-scoringconfiguration): {{
    EvaluationFormQuestionScoringConfiguration}}
  [Title](#cfn-connect-evaluationform-evaluationformquestion-title): {{String}}
  [Weight](#cfn-connect-evaluationform-evaluationformquestion-weight): {{Number}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformquestion-properties"></a>

`Enablement`  <a name="cfn-connect-evaluationform-evaluationformquestion-enablement"></a>
A question conditional enablement.
*Required*: No
*Type*: [EvaluationFormItemEnablementConfiguration](aws-properties-connect-evaluationform-evaluationformitemenablementconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Instructions`  <a name="cfn-connect-evaluationform-evaluationformquestion-instructions"></a>
The instructions of the section.
*Length Constraints*: Minimum length of 0. Maximum length of 1024.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricConfiguration`  <a name="cfn-connect-evaluationform-evaluationformquestion-metricconfiguration"></a>
The metric configuration for the question. Use this to associate a business outcome metric with the question.
*Required*: No
*Type*: [EvaluationFormMetricConfiguration](aws-properties-connect-evaluationform-evaluationformmetricconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotApplicableEnabled`  <a name="cfn-connect-evaluationform-evaluationformquestion-notapplicableenabled"></a>
The flag to enable not applicable answers to the question.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuestionType`  <a name="cfn-connect-evaluationform-evaluationformquestion-questiontype"></a>
The type of the question.
*Allowed values*: `NUMERIC` \| `SINGLESELECT` \| `TEXT`
*Required*: Yes
*Type*: String
*Allowed values*: `NUMERIC | SINGLESELECT | TEXT | MULTISELECT | DATETIME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QuestionTypeProperties`  <a name="cfn-connect-evaluationform-evaluationformquestion-questiontypeproperties"></a>
The properties of the type of question. Text questions do not have to define question type properties.
*Required*: No
*Type*: [EvaluationFormQuestionTypeProperties](aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefId`  <a name="cfn-connect-evaluationform-evaluationformquestion-refid"></a>
The identifier of the question. An identifier must be unique within the evaluation form.
*Length Constraints*: Minimum length of 1. Maximum length of 40.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScoringConfiguration`  <a name="cfn-connect-evaluationform-evaluationformquestion-scoringconfiguration"></a>
The scoring configuration of the question.
*Required*: No
*Type*: [EvaluationFormQuestionScoringConfiguration](aws-properties-connect-evaluationform-evaluationformquestionscoringconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-connect-evaluationform-evaluationformquestion-title"></a>
The title of the question.
*Length Constraints*: Minimum length of 1. Maximum length of 350.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `350`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-connect-evaluationform-evaluationformquestion-weight"></a>
The scoring weight of the section.
*Minimum*: 0
*Maximum*: 100
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
