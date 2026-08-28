---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-workflow-customstepdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Workflow CustomStepDetails
<a name="aws-properties-transfer-workflow-customstepdetails"></a>

Details for a step that invokes an AWS Lambda function.

Consists of the Lambda function's name, target, and timeout (in seconds).

## Syntax
<a name="aws-properties-transfer-workflow-customstepdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-workflow-customstepdetails-syntax.json"></a>

```
{
  "[Name](#cfn-transfer-workflow-customstepdetails-name)" : {{String}},
  "[SourceFileLocation](#cfn-transfer-workflow-customstepdetails-sourcefilelocation)" : {{String}},
  "[Target](#cfn-transfer-workflow-customstepdetails-target)" : {{String}},
  "[TimeoutSeconds](#cfn-transfer-workflow-customstepdetails-timeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-transfer-workflow-customstepdetails-syntax.yaml"></a>

```
  [Name](#cfn-transfer-workflow-customstepdetails-name): {{String}}
  [SourceFileLocation](#cfn-transfer-workflow-customstepdetails-sourcefilelocation): {{String}}
  [Target](#cfn-transfer-workflow-customstepdetails-target): {{String}}
  [TimeoutSeconds](#cfn-transfer-workflow-customstepdetails-timeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-transfer-workflow-customstepdetails-properties"></a>

`Name`  <a name="cfn-transfer-workflow-customstepdetails-name"></a>
The name of the step, used as an identifier.
*Required*: No
*Type*: String
*Pattern*: `^[\w-]*$`
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceFileLocation`  <a name="cfn-transfer-workflow-customstepdetails-sourcefilelocation"></a>
Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.
+ To use the previous file as the input, enter `${previous.file}`. In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
+ To use the originally uploaded file location as input for this step, enter `${original.file}`.
*Required*: No
*Type*: String
*Pattern*: `^\$\{(\w+.)+\w+\}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Target`  <a name="cfn-transfer-workflow-customstepdetails-target"></a>
The ARN for the Lambda function that is being called.
*Required*: No
*Type*: String
*Pattern*: `arn:[a-z-]+:lambda:.*$`
*Minimum*: `0`
*Maximum*: `170`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutSeconds`  <a name="cfn-transfer-workflow-customstepdetails-timeoutseconds"></a>
Timeout, in seconds, for the step.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1800`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
