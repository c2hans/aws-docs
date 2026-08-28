---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-branch-backend.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Branch Backend
<a name="aws-properties-amplify-branch-backend"></a>

Describes the backend associated with an Amplify `Branch`.

This property is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.

## Syntax
<a name="aws-properties-amplify-branch-backend-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-branch-backend-syntax.json"></a>

```
{
  "[StackArn](#cfn-amplify-branch-backend-stackarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-branch-backend-syntax.yaml"></a>

```
  [StackArn](#cfn-amplify-branch-backend-stackarn): {{String}}
```

## Properties
<a name="aws-properties-amplify-branch-backend-properties"></a>

`StackArn`  <a name="cfn-amplify-branch-backend-stackarn"></a>
The Amazon Resource Name (ARN) for the CloudFormation stack.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
