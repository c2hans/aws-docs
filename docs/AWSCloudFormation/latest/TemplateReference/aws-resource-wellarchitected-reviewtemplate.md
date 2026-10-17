---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-reviewtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::ReviewTemplate
<a name="aws-resource-wellarchitected-reviewtemplate"></a>

A review template.

## Syntax
<a name="aws-resource-wellarchitected-reviewtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-reviewtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::ReviewTemplate",
  "Properties" : {
      "[Description](#cfn-wellarchitected-reviewtemplate-description)" : {{String}},
      "[Lenses](#cfn-wellarchitected-reviewtemplate-lenses)" : {{[ String, ... ]}},
      "[Notes](#cfn-wellarchitected-reviewtemplate-notes)" : {{String}},
      "[Tags](#cfn-wellarchitected-reviewtemplate-tags)" : {{[ TagsItems, ... ]}},
      "[TemplateName](#cfn-wellarchitected-reviewtemplate-templatename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-reviewtemplate-syntax.yaml"></a>

```
Type: AWS::WellArchitected::ReviewTemplate
Properties:
  [Description](#cfn-wellarchitected-reviewtemplate-description): {{String}}
  [Lenses](#cfn-wellarchitected-reviewtemplate-lenses): {{
    - String}}
  [Notes](#cfn-wellarchitected-reviewtemplate-notes): {{String}}
  [Tags](#cfn-wellarchitected-reviewtemplate-tags): {{
    - TagsItems}}
  [TemplateName](#cfn-wellarchitected-reviewtemplate-templatename): {{String}}
```

## Properties
<a name="aws-resource-wellarchitected-reviewtemplate-properties"></a>

`Description`  <a name="cfn-wellarchitected-reviewtemplate-description"></a>
The review template description.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9-_.,:/()@!&?#+''\s]+$`
*Minimum*: `3`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lenses`  <a name="cfn-wellarchitected-reviewtemplate-lenses"></a>
The lenses applied to the review template.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Notes`  <a name="cfn-wellarchitected-reviewtemplate-notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2084`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wellarchitected-reviewtemplate-tags"></a>
The tags assigned to the review template.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-wellarchitected-reviewtemplate-tagsitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateName`  <a name="cfn-wellarchitected-reviewtemplate-templatename"></a>
The name of the review template.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9-_.,:/()@!&?#+''\s]+$`
*Minimum*: `3`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-reviewtemplate-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-reviewtemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the review template ARN.

### Fn::GetAtt
<a name="aws-resource-wellarchitected-reviewtemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-reviewtemplate-return-values-fn--getatt-fn--getatt"></a>

`Owner`  <a name="Owner-fn::getatt"></a>
The owner of the review template.

`TemplateArn`  <a name="TemplateArn-fn::getatt"></a>
The review template ARN.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the review template was last updated.

`UpdateStatus`  <a name="UpdateStatus-fn::getatt"></a>
The latest status of a review template.
