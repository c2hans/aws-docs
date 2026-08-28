---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImageRecipe SystemsManagerAgent
<a name="aws-properties-imagebuilder-imagerecipe-systemsmanageragent"></a>

Contains settings for the Systems Manager agent on your build instance.

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
Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. default value is false.
The default behavior of uninstallAfterBuild is to remove the SSM Agent if it was installed by EC2 Image Builder
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
