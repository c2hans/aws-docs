---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy Action
<a name="aws-properties-imagebuilder-lifecyclepolicy-action"></a>

Contains the action configuration for a lifecycle policy rule: the action to take, and which underlying resources the action extends to.

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
Specifies which underlying resources the action extends to beyond the Image Builder image resource itself: distributed AMIs, their snapshots, or distributed container images. `DELETE` rules can include all three, `DEPRECATE` and `DISABLE` rules can include AMIs only, and you can only include snapshots together with AMIs.
*Required*: No
*Type*: [IncludeResources](aws-properties-imagebuilder-lifecyclepolicy-includeresources.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-imagebuilder-lifecyclepolicy-action-type"></a>
Specifies the lifecycle action to take. `DELETE` deletes the image resource and, with `includeResources`, also removes distributed AMIs, snapshots, or container images. `DEPRECATE` and `DISABLE` set the corresponding status on the image resource and, if `includeResources.amis` is set, on its distributed AMIs.
*Required*: Yes
*Type*: String
*Allowed values*: `DELETE | DEPRECATE | DISABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
