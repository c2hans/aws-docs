---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-scalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping ScalingConfig
<a name="aws-properties-lambda-eventsourcemapping-scalingconfig"></a>

(Amazon SQS only) The scaling configuration for the event source. To remove the configuration, pass an empty value.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-scalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-scalingconfig-syntax.json"></a>

```
{
  "[MaximumConcurrency](#cfn-lambda-eventsourcemapping-scalingconfig-maximumconcurrency)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-scalingconfig-syntax.yaml"></a>

```
  [MaximumConcurrency](#cfn-lambda-eventsourcemapping-scalingconfig-maximumconcurrency): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-scalingconfig-properties"></a>

`MaximumConcurrency`  <a name="cfn-lambda-eventsourcemapping-scalingconfig-maximumconcurrency"></a>
Limits the number of concurrent instances that the Amazon SQS event source can invoke.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
