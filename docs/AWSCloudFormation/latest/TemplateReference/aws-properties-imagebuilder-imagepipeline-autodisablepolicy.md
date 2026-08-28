---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-autodisablepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline AutoDisablePolicy
<a name="aws-properties-imagebuilder-imagepipeline-autodisablepolicy"></a>

Defines the rules by which an image pipeline is automatically disabled when it fails.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-autodisablepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-autodisablepolicy-syntax.json"></a>

```
{
  "[FailureCount](#cfn-imagebuilder-imagepipeline-autodisablepolicy-failurecount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-autodisablepolicy-syntax.yaml"></a>

```
  [FailureCount](#cfn-imagebuilder-imagepipeline-autodisablepolicy-failurecount): {{Integer}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-autodisablepolicy-properties"></a>

`FailureCount`  <a name="cfn-imagebuilder-imagepipeline-autodisablepolicy-failurecount"></a>
The number of consecutive scheduled image pipeline executions that must fail before Image Builder automatically disables the pipeline.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
