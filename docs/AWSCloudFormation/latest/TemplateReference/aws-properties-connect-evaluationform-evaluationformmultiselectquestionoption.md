---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormMultiSelectQuestionOption
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption"></a>

An option for a multi-select question in an evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption-syntax.json"></a>

```
{
  "[AutomaticFail](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-automaticfail)" : {{Boolean}},
  "[AutomaticFailConfiguration](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-automaticfailconfiguration)" : {{AutomaticFailConfiguration}},
  "[PointsConfiguration](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-pointsconfiguration)" : {{QuestionOptionPointsConfiguration}},
  "[RefId](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-refid)" : {{String}},
  "[Score](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-score)" : {{Integer}},
  "[Text](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption-syntax.yaml"></a>

```
  [AutomaticFail](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-automaticfail): {{Boolean}}
  [AutomaticFailConfiguration](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-automaticfailconfiguration): {{
    AutomaticFailConfiguration}}
  [PointsConfiguration](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-pointsconfiguration): {{
    QuestionOptionPointsConfiguration}}
  [RefId](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-refid): {{String}}
  [Score](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-score): {{Integer}}
  [Text](#cfn-connect-evaluationform-evaluationformmultiselectquestionoption-text): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformmultiselectquestionoption-properties"></a>

`AutomaticFail`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionoption-automaticfail"></a>
The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutomaticFailConfiguration`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionoption-automaticfailconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [AutomaticFailConfiguration](aws-properties-connect-evaluationform-automaticfailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PointsConfiguration`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionoption-pointsconfiguration"></a>
The points configuration for point-based scoring.
*Required*: No
*Type*: [QuestionOptionPointsConfiguration](aws-properties-connect-evaluationform-questionoptionpointsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefId`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionoption-refid"></a>
Reference identifier for this option.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Score`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionoption-score"></a>
The score assigned to the answer option.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-connect-evaluationform-evaluationformmultiselectquestionoption-text"></a>
Display text for this option.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
