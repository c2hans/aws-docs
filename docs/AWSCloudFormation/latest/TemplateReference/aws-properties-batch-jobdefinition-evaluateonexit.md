---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-evaluateonexit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EvaluateOnExit
<a name="aws-properties-batch-jobdefinition-evaluateonexit"></a>

Specifies an array of up to 5 conditions to be met, and an action to take (`RETRY` or `EXIT`) if all conditions are met. If none of the `EvaluateOnExit` conditions in a `RetryStrategy` match, then the job is retried.

## Syntax
<a name="aws-properties-batch-jobdefinition-evaluateonexit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-evaluateonexit-syntax.json"></a>

```
{
  "[Action](#cfn-batch-jobdefinition-evaluateonexit-action)" : {{String}},
  "[OnExitCode](#cfn-batch-jobdefinition-evaluateonexit-onexitcode)" : {{String}},
  "[OnReason](#cfn-batch-jobdefinition-evaluateonexit-onreason)" : {{String}},
  "[OnStatusReason](#cfn-batch-jobdefinition-evaluateonexit-onstatusreason)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-evaluateonexit-syntax.yaml"></a>

```
  [Action](#cfn-batch-jobdefinition-evaluateonexit-action): {{String}}
  [OnExitCode](#cfn-batch-jobdefinition-evaluateonexit-onexitcode): {{String}}
  [OnReason](#cfn-batch-jobdefinition-evaluateonexit-onreason): {{String}}
  [OnStatusReason](#cfn-batch-jobdefinition-evaluateonexit-onstatusreason): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-evaluateonexit-properties"></a>

`Action`  <a name="cfn-batch-jobdefinition-evaluateonexit-action"></a>
Specifies the action to take if all of the specified conditions (`onStatusReason`, `onReason`, and `onExitCode`) are met. The values aren't case sensitive.
*Required*: Yes
*Type*: String
*Allowed values*: `RETRY | EXIT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnExitCode`  <a name="cfn-batch-jobdefinition-evaluateonexit-onexitcode"></a>
Contains a glob pattern to match against the decimal representation of the `ExitCode` returned for a job. The pattern can be up to 512 characters long. It can contain only numbers, and can end with an asterisk (\*) so that only the start of the string needs to be an exact match.
The string can contain up to 512 characters.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnReason`  <a name="cfn-batch-jobdefinition-evaluateonexit-onreason"></a>
Contains a glob pattern to match against the `Reason` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (\*) so that only the start of the string needs to be an exact match.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnStatusReason`  <a name="cfn-batch-jobdefinition-evaluateonexit-onstatusreason"></a>
Contains a glob pattern to match against the `StatusReason` returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white spaces (including spaces or tabs). It can optionally end with an asterisk (\*) so that only the start of the string needs to be an exact match.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
