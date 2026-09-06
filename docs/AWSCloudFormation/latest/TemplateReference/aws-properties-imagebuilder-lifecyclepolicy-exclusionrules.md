---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy ExclusionRules
<a name="aws-properties-imagebuilder-lifecyclepolicy-exclusionrules"></a>

Specifies resources that lifecycle policy actions should not apply to.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-exclusionrules-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-exclusionrules-syntax.json"></a>

```
{
  "[Amis](#cfn-imagebuilder-lifecyclepolicy-exclusionrules-amis)" : {{AmiExclusionRules}},
  "[TagMap](#cfn-imagebuilder-lifecyclepolicy-exclusionrules-tagmap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-exclusionrules-syntax.yaml"></a>

```
  [Amis](#cfn-imagebuilder-lifecyclepolicy-exclusionrules-amis): {{
    AmiExclusionRules}}
  [TagMap](#cfn-imagebuilder-lifecyclepolicy-exclusionrules-tagmap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-exclusionrules-properties"></a>

`Amis`  <a name="cfn-imagebuilder-lifecyclepolicy-exclusionrules-amis"></a>
Lists configuration values that apply to AMIs that Image Builder should exclude from the lifecycle action.
*Required*: No
*Type*: [AmiExclusionRules](aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagMap`  <a name="cfn-imagebuilder-lifecyclepolicy-exclusionrules-tagmap"></a>
Contains a list of tags that Image Builder uses to skip lifecycle actions for Image Builder image resources that have them.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
