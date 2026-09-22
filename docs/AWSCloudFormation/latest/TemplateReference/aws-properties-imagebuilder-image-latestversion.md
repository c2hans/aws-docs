---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-latestversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image LatestVersion
<a name="aws-properties-imagebuilder-image-latestversion"></a>

A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.

## Syntax
<a name="aws-properties-imagebuilder-image-latestversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-latestversion-syntax.json"></a>

```
{
  "[Arn](#cfn-imagebuilder-image-latestversion-arn)" : {{String}},
  "[Major](#cfn-imagebuilder-image-latestversion-major)" : {{String}},
  "[Minor](#cfn-imagebuilder-image-latestversion-minor)" : {{String}},
  "[Patch](#cfn-imagebuilder-image-latestversion-patch)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-latestversion-syntax.yaml"></a>

```
  [Arn](#cfn-imagebuilder-image-latestversion-arn): {{String}}
  [Major](#cfn-imagebuilder-image-latestversion-major): {{String}}
  [Minor](#cfn-imagebuilder-image-latestversion-minor): {{String}}
  [Patch](#cfn-imagebuilder-image-latestversion-patch): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-image-latestversion-properties"></a>

`Arn`  <a name="cfn-imagebuilder-image-latestversion-arn"></a>
The latest version Amazon Resource Name (ARN) of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Major`  <a name="cfn-imagebuilder-image-latestversion-major"></a>
The latest version Amazon Resource Name (ARN) with the same `major` version of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minor`  <a name="cfn-imagebuilder-image-latestversion-minor"></a>
The latest version Amazon Resource Name (ARN) with the same `minor` version of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Patch`  <a name="cfn-imagebuilder-image-latestversion-patch"></a>
The latest version Amazon Resource Name (ARN) with the same `patch` version of the Image Builder resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
