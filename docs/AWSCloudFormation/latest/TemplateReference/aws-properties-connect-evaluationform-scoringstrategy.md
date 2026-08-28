---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-scoringstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm ScoringStrategy
<a name="aws-properties-connect-evaluationform-scoringstrategy"></a>

A scoring strategy of the evaluation form.

## Syntax
<a name="aws-properties-connect-evaluationform-scoringstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-scoringstrategy-syntax.json"></a>

```
{
  "[Mode](#cfn-connect-evaluationform-scoringstrategy-mode)" : {{String}},
  "[ScoreThresholds](#cfn-connect-evaluationform-scoringstrategy-scorethresholds)" : {{[ EvaluationFormScoreThreshold, ... ]}},
  "[Status](#cfn-connect-evaluationform-scoringstrategy-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-scoringstrategy-syntax.yaml"></a>

```
  [Mode](#cfn-connect-evaluationform-scoringstrategy-mode): {{String}}
  [ScoreThresholds](#cfn-connect-evaluationform-scoringstrategy-scorethresholds): {{
    - EvaluationFormScoreThreshold}}
  [Status](#cfn-connect-evaluationform-scoringstrategy-status): {{String}}
```

## Properties
<a name="aws-properties-connect-evaluationform-scoringstrategy-properties"></a>

`Mode`  <a name="cfn-connect-evaluationform-scoringstrategy-mode"></a>
The scoring mode of the evaluation form.
*Allowed values*: `QUESTION_ONLY` \| `SECTION_ONLY`
*Required*: Yes
*Type*: String
*Allowed values*: `QUESTION_ONLY | SECTION_ONLY | POINTS_BASED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScoreThresholds`  <a name="cfn-connect-evaluationform-scoringstrategy-scorethresholds"></a>
Property description not available.
*Required*: No
*Type*: Array of [EvaluationFormScoreThreshold](aws-properties-connect-evaluationform-evaluationformscorethreshold.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-connect-evaluationform-scoringstrategy-status"></a>
The scoring status of the evaluation form.
*Allowed values*: `ENABLED` \| `DISABLED`
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
