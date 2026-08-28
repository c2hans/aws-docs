---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-durableconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function DurableConfig
<a name="aws-properties-lambda-function-durableconfig"></a>

Configuration settings for [durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including execution timeout, retention period for execution history, and an optional ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.

## Syntax
<a name="aws-properties-lambda-function-durableconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-durableconfig-syntax.json"></a>

```
{
  "[ExecutionTimeout](#cfn-lambda-function-durableconfig-executiontimeout)" : {{Integer}},
  "[KMSKeyArn](#cfn-lambda-function-durableconfig-kmskeyarn)" : {{String}},
  "[RetentionPeriodInDays](#cfn-lambda-function-durableconfig-retentionperiodindays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-function-durableconfig-syntax.yaml"></a>

```
  [ExecutionTimeout](#cfn-lambda-function-durableconfig-executiontimeout): {{Integer}}
  [KMSKeyArn](#cfn-lambda-function-durableconfig-kmskeyarn): {{String}}
  [RetentionPeriodInDays](#cfn-lambda-function-durableconfig-retentionperiodindays): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-function-durableconfig-properties"></a>

`ExecutionTimeout`  <a name="cfn-lambda-function-durableconfig-executiontimeout"></a>
The maximum time (in seconds) that a durable execution can run before timing out. This timeout applies to the entire durable execution, not individual function invocations.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `31622400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KMSKeyArn`  <a name="cfn-lambda-function-durableconfig-kmskeyarn"></a>
The ARN of the AWS Key Management Service (AWS KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetentionPeriodInDays`  <a name="cfn-lambda-function-durableconfig-retentionperiodindays"></a>
The number of days to retain execution history after a durable execution completes. After this period, execution history is no longer available through the GetDurableExecutionHistory API.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `90`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
