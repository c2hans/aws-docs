---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy Action
<a name="aws-properties-imagebuilder-lifecyclepolicy-action"></a>

Contains selection criteria for the lifecycle policy.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-action-syntax.json"></a>

```
{
  "[IncludeResources](#cfn-imagebuilder-lifecyclepolicy-action-includeresources)" : {{IncludeResources}},
  "[Type](#cfn-imagebuilder-lifecyclepolicy-action-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-action-syntax.yaml"></a>

```
  [IncludeResources](#cfn-imagebuilder-lifecyclepolicy-action-includeresources): {{
    IncludeResources}}
  [Type](#cfn-imagebuilder-lifecyclepolicy-action-type): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-action-properties"></a>

`IncludeResources`  <a name="cfn-imagebuilder-lifecyclepolicy-action-includeresources"></a>
Specifies the resources that the lifecycle policy applies to.
*Required*: No
*Type*: [IncludeResources](aws-properties-imagebuilder-lifecyclepolicy-includeresources.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-imagebuilder-lifecyclepolicy-action-type"></a>
Specifies the lifecycle action to take.
*Required*: Yes
*Type*: String
*Allowed values*: `DELETE | DEPRECATE | DISABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
