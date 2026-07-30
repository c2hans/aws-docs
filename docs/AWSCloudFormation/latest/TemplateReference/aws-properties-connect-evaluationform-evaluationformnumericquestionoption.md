---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormNumericQuestionOption
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionoption"></a>

Information about the option range used for scoring in numeric questions.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionoption-syntax.json"></a>

```
{
  "[AutomaticFail](#cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfail)" : {{Boolean}},
  "[AutomaticFailConfiguration](#cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfailconfiguration)" : {{AutomaticFailConfiguration}},
  "[MaxValue](#cfn-connect-evaluationform-evaluationformnumericquestionoption-maxvalue)" : {{Integer}},
  "[MinValue](#cfn-connect-evaluationform-evaluationformnumericquestionoption-minvalue)" : {{Integer}},
  "[PointsConfiguration](#cfn-connect-evaluationform-evaluationformnumericquestionoption-pointsconfiguration)" : {{QuestionOptionPointsConfiguration}},
  "[Score](#cfn-connect-evaluationform-evaluationformnumericquestionoption-score)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionoption-syntax.yaml"></a>

```
  [AutomaticFail](#cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfail): {{Boolean}}
  [AutomaticFailConfiguration](#cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfailconfiguration): {{
    AutomaticFailConfiguration}}
  [MaxValue](#cfn-connect-evaluationform-evaluationformnumericquestionoption-maxvalue): {{Integer}}
  [MinValue](#cfn-connect-evaluationform-evaluationformnumericquestionoption-minvalue): {{Integer}}
  [PointsConfiguration](#cfn-connect-evaluationform-evaluationformnumericquestionoption-pointsconfiguration): {{
    QuestionOptionPointsConfiguration}}
  [Score](#cfn-connect-evaluationform-evaluationformnumericquestionoption-score): {{Integer}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformnumericquestionoption-properties"></a>

`AutomaticFail`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfail"></a>
The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticFailConfiguration`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfailconfiguration"></a>
A configuration for automatic fail.
*Required*: No
*Type*: [AutomaticFailConfiguration](aws-properties-connect-evaluationform-automaticfailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxValue`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionoption-maxvalue"></a>
The maximum answer value of the range option.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValue`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionoption-minvalue"></a>
The minimum answer value of the range option.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointsConfiguration`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionoption-pointsconfiguration"></a>
The points configuration for point-based scoring.
*Required*: No
*Type*: [QuestionOptionPointsConfiguration](aws-properties-connect-evaluationform-questionoptionpointsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Score`  <a name="cfn-connect-evaluationform-evaluationformnumericquestionoption-score"></a>
The score assigned to answer values within the range option.
*Minimum*: 0
*Maximum*: 10
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
