---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormSingleSelectQuestionOption
<a name="aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption"></a>

Information about the automation configuration in single select questions.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption-syntax.json"></a>

```
{
  "[AutomaticFail](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfail)" : {{Boolean}},
  "[AutomaticFailConfiguration](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfailconfiguration)" : {{AutomaticFailConfiguration}},
  "[PointsConfiguration](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-pointsconfiguration)" : {{QuestionOptionPointsConfiguration}},
  "[RefId](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-refid)" : {{String}},
  "[Score](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-score)" : {{Integer}},
  "[Text](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption-syntax.yaml"></a>

```
  [AutomaticFail](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfail): {{Boolean}}
  [AutomaticFailConfiguration](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfailconfiguration): {{
    AutomaticFailConfiguration}}
  [PointsConfiguration](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-pointsconfiguration): {{
    QuestionOptionPointsConfiguration}}
  [RefId](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-refid): {{String}}
  [Score](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-score): {{Integer}}
  [Text](#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-text): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption-properties"></a>

`AutomaticFail`  <a name="cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfail"></a>
The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticFailConfiguration`  <a name="cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfailconfiguration"></a>
Whether automatic fail is configured on a single select question.
*Required*: No
*Type*: [AutomaticFailConfiguration](aws-properties-connect-evaluationform-automaticfailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointsConfiguration`  <a name="cfn-connect-evaluationform-evaluationformsingleselectquestionoption-pointsconfiguration"></a>
The points configuration for point-based scoring.
*Required*: No
*Type*: [QuestionOptionPointsConfiguration](aws-properties-connect-evaluationform-questionoptionpointsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefId`  <a name="cfn-connect-evaluationform-evaluationformsingleselectquestionoption-refid"></a>
The identifier of the answer option. An identifier must be unique within the question.
*Length Constraints*: Minimum length of 1. Maximum length of 40.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Score`  <a name="cfn-connect-evaluationform-evaluationformsingleselectquestionoption-score"></a>
The score assigned to the answer option.
*Minimum*: 0
*Maximum*: 10
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-connect-evaluationform-evaluationformsingleselectquestionoption-text"></a>
The title of the answer option.
*Length Constraints*: Minimum length of 1. Maximum length of 128.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
