---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformsection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormSection
<a name="aws-properties-connect-evaluationform-evaluationformsection"></a>

Information about a section from an evaluation form. A section can contain sections and/or questions. Evaluation forms can only contain sections and subsections (two level nesting).

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformsection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformsection-syntax.json"></a>

```
{
  "[Instructions](#cfn-connect-evaluationform-evaluationformsection-instructions)" : {{String}},
  "[IsExcludedFromScoring](#cfn-connect-evaluationform-evaluationformsection-isexcludedfromscoring)" : {{Boolean}},
  "[Items](#cfn-connect-evaluationform-evaluationformsection-items)" : {{[ EvaluationFormItem, ... ]}},
  "[RefId](#cfn-connect-evaluationform-evaluationformsection-refid)" : {{String}},
  "[ScoreThresholds](#cfn-connect-evaluationform-evaluationformsection-scorethresholds)" : {{[ EvaluationFormScoreThreshold, ... ]}},
  "[Title](#cfn-connect-evaluationform-evaluationformsection-title)" : {{String}},
  "[Weight](#cfn-connect-evaluationform-evaluationformsection-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformsection-syntax.yaml"></a>

```
  [Instructions](#cfn-connect-evaluationform-evaluationformsection-instructions): {{String}}
  [IsExcludedFromScoring](#cfn-connect-evaluationform-evaluationformsection-isexcludedfromscoring): {{Boolean}}
  [Items](#cfn-connect-evaluationform-evaluationformsection-items): {{
    - EvaluationFormItem}}
  [RefId](#cfn-connect-evaluationform-evaluationformsection-refid): {{String}}
  [ScoreThresholds](#cfn-connect-evaluationform-evaluationformsection-scorethresholds): {{
    - EvaluationFormScoreThreshold}}
  [Title](#cfn-connect-evaluationform-evaluationformsection-title): {{String}}
  [Weight](#cfn-connect-evaluationform-evaluationformsection-weight): {{Number}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformsection-properties"></a>

`Instructions`  <a name="cfn-connect-evaluationform-evaluationformsection-instructions"></a>
The instructions of the section.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsExcludedFromScoring`  <a name="cfn-connect-evaluationform-evaluationformsection-isexcludedfromscoring"></a>
The flag to exclude the section from scoring.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Items`  <a name="cfn-connect-evaluationform-evaluationformsection-items"></a>
The items of the section.
*Minimum*: 1
*Required*: No
*Type*: Array of [EvaluationFormItem](aws-properties-connect-evaluationform-evaluationformitem.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefId`  <a name="cfn-connect-evaluationform-evaluationformsection-refid"></a>
The identifier of the section. An identifier must be unique within the evaluation form.
*Length Constraints*: Minimum length of 1. Maximum length of 40.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]{1,40}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScoreThresholds`  <a name="cfn-connect-evaluationform-evaluationformsection-scorethresholds"></a>
The score thresholds for performance categories.
*Required*: No
*Type*: Array of [EvaluationFormScoreThreshold](aws-properties-connect-evaluationform-evaluationformscorethreshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-connect-evaluationform-evaluationformsection-title"></a>
The title of the section.
*Length Constraints*: Minimum length of 1. Maximum length of 128.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-connect-evaluationform-evaluationformsection-weight"></a>
The scoring weight of the section.
*Minimum*: 0
*Maximum*: 100
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
