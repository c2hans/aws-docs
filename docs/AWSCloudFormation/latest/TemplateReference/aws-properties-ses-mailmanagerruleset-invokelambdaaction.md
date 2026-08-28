---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-invokelambdaaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet InvokeLambdaAction
<a name="aws-properties-ses-mailmanagerruleset-invokelambdaaction"></a>

The action to invoke an AWS Lambda function for processing the email.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-invokelambdaaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-invokelambdaaction-syntax.json"></a>

```
{
  "[ActionFailurePolicy](#cfn-ses-mailmanagerruleset-invokelambdaaction-actionfailurepolicy)" : {{String}},
  "[FunctionArn](#cfn-ses-mailmanagerruleset-invokelambdaaction-functionarn)" : {{String}},
  "[InvocationType](#cfn-ses-mailmanagerruleset-invokelambdaaction-invocationtype)" : {{String}},
  "[RetryTimeMinutes](#cfn-ses-mailmanagerruleset-invokelambdaaction-retrytimeminutes)" : {{Integer}},
  "[RoleArn](#cfn-ses-mailmanagerruleset-invokelambdaaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-invokelambdaaction-syntax.yaml"></a>

```
  [ActionFailurePolicy](#cfn-ses-mailmanagerruleset-invokelambdaaction-actionfailurepolicy): {{String}}
  [FunctionArn](#cfn-ses-mailmanagerruleset-invokelambdaaction-functionarn): {{String}}
  [InvocationType](#cfn-ses-mailmanagerruleset-invokelambdaaction-invocationtype): {{String}}
  [RetryTimeMinutes](#cfn-ses-mailmanagerruleset-invokelambdaaction-retrytimeminutes): {{Integer}}
  [RoleArn](#cfn-ses-mailmanagerruleset-invokelambdaaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-invokelambdaaction-properties"></a>

`ActionFailurePolicy`  <a name="cfn-ses-mailmanagerruleset-invokelambdaaction-actionfailurepolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the AWS Lambda function no longer exists.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | DROP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionArn`  <a name="cfn-ses-mailmanagerruleset-invokelambdaaction-functionarn"></a>
The Amazon Resource Name (ARN) of the Lambda function to invoke.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationType`  <a name="cfn-ses-mailmanagerruleset-invokelambdaaction-invocationtype"></a>
The invocation type of the Lambda function. Use EVENT for asynchronous invocation or REQUEST\_RESPONSE for synchronous invocation.
*Required*: Yes
*Type*: String
*Allowed values*: `EVENT | REQUEST_RESPONSE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryTimeMinutes`  <a name="cfn-ses-mailmanagerruleset-invokelambdaaction-retrytimeminutes"></a>
The maximum time in minutes that the email processing can be retried if the Lambda invocation fails. The maximum value is 2160 minutes (36 hours).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2160`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ses-mailmanagerruleset-invokelambdaaction-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to use to invoke the Lambda function.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
