---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImageRecipe SystemsManagerAgent
<a name="aws-properties-imagebuilder-imagerecipe-systemsmanageragent"></a>

Contains settings for the Systems Manager agent on your build instance. This setting applies to Linux and macOS build instances only. Requests that set it for a recipe with a Windows base image are rejected.

## Syntax
<a name="aws-properties-imagebuilder-imagerecipe-systemsmanageragent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagerecipe-systemsmanageragent-syntax.json"></a>

```
{
  "[UninstallAfterBuild](#cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagerecipe-systemsmanageragent-syntax.yaml"></a>

```
  [UninstallAfterBuild](#cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild): {{Boolean}}
```

## Properties
<a name="aws-properties-imagebuilder-imagerecipe-systemsmanageragent-properties"></a>

`UninstallAfterBuild`  <a name="cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild"></a>
Specifies whether the Systems Manager agent is removed from your final build image before Image Builder creates the new AMI. If `true`, the agent is removed. If `false`, the agent is kept, so that it's included in the AMI. If you don't set this property, Image Builder removes the agent only if Image Builder installed the agent during the build. An agent that was pre-installed on the base image is kept.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
