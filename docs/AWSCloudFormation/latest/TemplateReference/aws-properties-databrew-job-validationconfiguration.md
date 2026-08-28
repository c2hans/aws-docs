---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-validationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job ValidationConfiguration
<a name="aws-properties-databrew-job-validationconfiguration"></a>

Configuration for data quality validation. Used to select the Rulesets and Validation Mode to be used in the profile job. When ValidationConfiguration is null, the profile job will run without data quality validation.

## Syntax
<a name="aws-properties-databrew-job-validationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-validationconfiguration-syntax.json"></a>

```
{
  "[RulesetArn](#cfn-databrew-job-validationconfiguration-rulesetarn)" : {{String}},
  "[ValidationMode](#cfn-databrew-job-validationconfiguration-validationmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-job-validationconfiguration-syntax.yaml"></a>

```
  [RulesetArn](#cfn-databrew-job-validationconfiguration-rulesetarn): {{String}}
  [ValidationMode](#cfn-databrew-job-validationconfiguration-validationmode): {{String}}
```

## Properties
<a name="aws-properties-databrew-job-validationconfiguration-properties"></a>

`RulesetArn`  <a name="cfn-databrew-job-validationconfiguration-rulesetarn"></a>
The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job. The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationMode`  <a name="cfn-databrew-job-validationconfiguration-validationmode"></a>
Mode of data quality validation. Default mode is “CHECK\_ALL” which verifies all rules defined in the selected ruleset.
*Required*: No
*Type*: String
*Allowed values*: `CHECK_ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
