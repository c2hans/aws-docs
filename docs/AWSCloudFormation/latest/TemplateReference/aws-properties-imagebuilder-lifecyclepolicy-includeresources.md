---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy IncludeResources
<a name="aws-properties-imagebuilder-lifecyclepolicy-includeresources"></a>

Specifies how the lifecycle policy should apply actions to selected resources.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-includeresources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-includeresources-syntax.json"></a>

```
{
  "[Amis](#cfn-imagebuilder-lifecyclepolicy-includeresources-amis)" : {{Boolean}},
  "[Containers](#cfn-imagebuilder-lifecyclepolicy-includeresources-containers)" : {{Boolean}},
  "[Snapshots](#cfn-imagebuilder-lifecyclepolicy-includeresources-snapshots)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-includeresources-syntax.yaml"></a>

```
  [Amis](#cfn-imagebuilder-lifecyclepolicy-includeresources-amis): {{Boolean}}
  [Containers](#cfn-imagebuilder-lifecyclepolicy-includeresources-containers): {{Boolean}}
  [Snapshots](#cfn-imagebuilder-lifecyclepolicy-includeresources-snapshots): {{Boolean}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-includeresources-properties"></a>

`Amis`  <a name="cfn-imagebuilder-lifecyclepolicy-includeresources-amis"></a>
Specifies whether the lifecycle action should apply to distributed AMIs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Containers`  <a name="cfn-imagebuilder-lifecyclepolicy-includeresources-containers"></a>
Specifies whether the lifecycle action should apply to distributed containers.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Snapshots`  <a name="cfn-imagebuilder-lifecyclepolicy-includeresources-snapshots"></a>
Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
