---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-hporesourceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution HpoResourceConfig
<a name="aws-properties-personalize-solution-hporesourceconfig"></a>

Describes the resource configuration for hyperparameter optimization (HPO).

## Syntax
<a name="aws-properties-personalize-solution-hporesourceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-hporesourceconfig-syntax.json"></a>

```
{
  "[MaxNumberOfTrainingJobs](#cfn-personalize-solution-hporesourceconfig-maxnumberoftrainingjobs)" : {{String}},
  "[MaxParallelTrainingJobs](#cfn-personalize-solution-hporesourceconfig-maxparalleltrainingjobs)" : {{String}}
}
```

### YAML
<a name="aws-properties-personalize-solution-hporesourceconfig-syntax.yaml"></a>

```
  [MaxNumberOfTrainingJobs](#cfn-personalize-solution-hporesourceconfig-maxnumberoftrainingjobs): {{String}}
  [MaxParallelTrainingJobs](#cfn-personalize-solution-hporesourceconfig-maxparalleltrainingjobs): {{String}}
```

## Properties
<a name="aws-properties-personalize-solution-hporesourceconfig-properties"></a>

`MaxNumberOfTrainingJobs`  <a name="cfn-personalize-solution-hporesourceconfig-maxnumberoftrainingjobs"></a>
The maximum number of training jobs when you create a solution version. The maximum value for `maxNumberOfTrainingJobs` is `40`.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxParallelTrainingJobs`  <a name="cfn-personalize-solution-hporesourceconfig-maxparalleltrainingjobs"></a>
The maximum number of parallel training jobs when you create a solution version. The maximum value for `maxParallelTrainingJobs` is `10`.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
