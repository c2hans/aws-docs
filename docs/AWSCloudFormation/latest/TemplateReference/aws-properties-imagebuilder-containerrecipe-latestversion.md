---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-containerrecipe-latestversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ContainerRecipe LatestVersion
<a name="aws-properties-imagebuilder-containerrecipe-latestversion"></a>

The resource ARNs with different wildcard variations of semantic versioning.

## Syntax
<a name="aws-properties-imagebuilder-containerrecipe-latestversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-containerrecipe-latestversion-syntax.json"></a>

```
{
  "[Arn](#cfn-imagebuilder-containerrecipe-latestversion-arn)" : {{String}},
  "[Major](#cfn-imagebuilder-containerrecipe-latestversion-major)" : {{String}},
  "[Minor](#cfn-imagebuilder-containerrecipe-latestversion-minor)" : {{String}},
  "[Patch](#cfn-imagebuilder-containerrecipe-latestversion-patch)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-containerrecipe-latestversion-syntax.yaml"></a>

```
  [Arn](#cfn-imagebuilder-containerrecipe-latestversion-arn): {{String}}
  [Major](#cfn-imagebuilder-containerrecipe-latestversion-major): {{String}}
  [Minor](#cfn-imagebuilder-containerrecipe-latestversion-minor): {{String}}
  [Patch](#cfn-imagebuilder-containerrecipe-latestversion-patch): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-containerrecipe-latestversion-properties"></a>

`Arn`  <a name="cfn-imagebuilder-containerrecipe-latestversion-arn"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Major`  <a name="cfn-imagebuilder-containerrecipe-latestversion-major"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minor`  <a name="cfn-imagebuilder-containerrecipe-latestversion-minor"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Patch`  <a name="cfn-imagebuilder-containerrecipe-latestversion-patch"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
