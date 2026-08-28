---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-microvmimagehooks.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage MicrovmImageHooks
<a name="aws-properties-lambda-microvmimage-microvmimagehooks"></a>

Configuration for hooks invoked during MicroVM image build events such as ready and validate.

## Syntax
<a name="aws-properties-lambda-microvmimage-microvmimagehooks-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-microvmimagehooks-syntax.json"></a>

```
{
  "[Ready](#cfn-lambda-microvmimage-microvmimagehooks-ready)" : {{String}},
  "[ReadyTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-readytimeoutinseconds)" : {{Integer}},
  "[Validate](#cfn-lambda-microvmimage-microvmimagehooks-validate)" : {{String}},
  "[ValidateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-validatetimeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-microvmimagehooks-syntax.yaml"></a>

```
  [Ready](#cfn-lambda-microvmimage-microvmimagehooks-ready): {{String}}
  [ReadyTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-readytimeoutinseconds): {{Integer}}
  [Validate](#cfn-lambda-microvmimage-microvmimagehooks-validate): {{String}}
  [ValidateTimeoutInSeconds](#cfn-lambda-microvmimage-microvmimagehooks-validatetimeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-microvmimagehooks-properties"></a>

`Ready`  <a name="cfn-lambda-microvmimage-microvmimagehooks-ready"></a>
The path of the hook invoked when the MicroVM image build is ready.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadyTimeoutInSeconds`  <a name="cfn-lambda-microvmimage-microvmimagehooks-readytimeoutinseconds"></a>
The maximum time in seconds for the ready hook to complete.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Validate`  <a name="cfn-lambda-microvmimage-microvmimagehooks-validate"></a>
The path of the hook invoked to validate the MicroVM image build.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidateTimeoutInSeconds`  <a name="cfn-lambda-microvmimage-microvmimagehooks-validatetimeoutinseconds"></a>
The maximum time in seconds for the validate hook to complete.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
