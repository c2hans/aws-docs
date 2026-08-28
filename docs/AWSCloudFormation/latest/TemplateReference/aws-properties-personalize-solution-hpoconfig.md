---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-solution-hpoconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Solution HpoConfig
<a name="aws-properties-personalize-solution-hpoconfig"></a>

Describes the properties for hyperparameter optimization (HPO).

## Syntax
<a name="aws-properties-personalize-solution-hpoconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-solution-hpoconfig-syntax.json"></a>

```
{
  "[AlgorithmHyperParameterRanges](#cfn-personalize-solution-hpoconfig-algorithmhyperparameterranges)" : {{AlgorithmHyperParameterRanges}},
  "[HpoObjective](#cfn-personalize-solution-hpoconfig-hpoobjective)" : {{HpoObjective}},
  "[HpoResourceConfig](#cfn-personalize-solution-hpoconfig-hporesourceconfig)" : {{HpoResourceConfig}}
}
```

### YAML
<a name="aws-properties-personalize-solution-hpoconfig-syntax.yaml"></a>

```
  [AlgorithmHyperParameterRanges](#cfn-personalize-solution-hpoconfig-algorithmhyperparameterranges): {{
    AlgorithmHyperParameterRanges}}
  [HpoObjective](#cfn-personalize-solution-hpoconfig-hpoobjective): {{
    HpoObjective}}
  [HpoResourceConfig](#cfn-personalize-solution-hpoconfig-hporesourceconfig): {{
    HpoResourceConfig}}
```

## Properties
<a name="aws-properties-personalize-solution-hpoconfig-properties"></a>

`AlgorithmHyperParameterRanges`  <a name="cfn-personalize-solution-hpoconfig-algorithmhyperparameterranges"></a>
The hyperparameters and their allowable ranges.
*Required*: No
*Type*: [AlgorithmHyperParameterRanges](aws-properties-personalize-solution-algorithmhyperparameterranges.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HpoObjective`  <a name="cfn-personalize-solution-hpoconfig-hpoobjective"></a>
The metric to optimize during HPO.
Amazon Personalize doesn't support configuring the `hpoObjective` at this time.
*Required*: No
*Type*: [HpoObjective](aws-properties-personalize-solution-hpoobjective.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HpoResourceConfig`  <a name="cfn-personalize-solution-hpoconfig-hporesourceconfig"></a>
Describes the resource configuration for HPO.
*Required*: No
*Type*: [HpoResourceConfig](aws-properties-personalize-solution-hporesourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
