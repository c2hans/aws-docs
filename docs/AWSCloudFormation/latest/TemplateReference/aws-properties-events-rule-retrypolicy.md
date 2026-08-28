---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-retrypolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule RetryPolicy
<a name="aws-properties-events-rule-retrypolicy"></a>

A `RetryPolicy` object that includes information about the retry policy settings.

## Syntax
<a name="aws-properties-events-rule-retrypolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-retrypolicy-syntax.json"></a>

```
{
  "[MaximumEventAgeInSeconds](#cfn-events-rule-retrypolicy-maximumeventageinseconds)" : {{Integer}},
  "[MaximumRetryAttempts](#cfn-events-rule-retrypolicy-maximumretryattempts)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-events-rule-retrypolicy-syntax.yaml"></a>

```
  [MaximumEventAgeInSeconds](#cfn-events-rule-retrypolicy-maximumeventageinseconds): {{Integer}}
  [MaximumRetryAttempts](#cfn-events-rule-retrypolicy-maximumretryattempts): {{Integer}}
```

## Properties
<a name="aws-properties-events-rule-retrypolicy-properties"></a>

`MaximumEventAgeInSeconds`  <a name="cfn-events-rule-retrypolicy-maximumeventageinseconds"></a>
The maximum amount of time, in seconds, to continue to make retry attempts.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRetryAttempts`  <a name="cfn-events-rule-retrypolicy-maximumretryattempts"></a>
The maximum number of retry attempts to make before the request fails. Retry attempts continue until either the maximum number of attempts is made or until the duration of the `MaximumEventAgeInSeconds` is met.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `185`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
