---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-lambdafunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType LambdaFunction
<a name="aws-properties-iottwinmaker-componenttype-lambdafunction"></a>

The Lambda function.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-lambdafunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-lambdafunction-syntax.json"></a>

```
{
  "[Arn](#cfn-iottwinmaker-componenttype-lambdafunction-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-lambdafunction-syntax.yaml"></a>

```
  [Arn](#cfn-iottwinmaker-componenttype-lambdafunction-arn): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-lambdafunction-properties"></a>

`Arn`  <a name="cfn-iottwinmaker-componenttype-lambdafunction-arn"></a>
The Lambda function ARN.
*Required*: Yes
*Type*: String
*Pattern*: `arn:((aws)|(aws-cn)|(aws-us-gov)):lambda:[a-z0-9-]+:[0-9]{12}:function:[\/a-zA-Z0-9_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
