---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-supportauthz-supportpermit-resourceset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit ResourceSet
<a name="aws-properties-supportauthz-supportpermit-resourceset"></a>

The set of resources a support permit applies to. Specify exactly one of `AllResourcesInRegion` or `Resources`.

## Syntax
<a name="aws-properties-supportauthz-supportpermit-resourceset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-supportauthz-supportpermit-resourceset-syntax.json"></a>

```
{
  "[AllResourcesInRegion](#cfn-supportauthz-supportpermit-resourceset-allresourcesinregion)" : {{Json}},
  "[Resources](#cfn-supportauthz-supportpermit-resourceset-resources)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-supportauthz-supportpermit-resourceset-syntax.yaml"></a>

```
  [AllResourcesInRegion](#cfn-supportauthz-supportpermit-resourceset-allresourcesinregion): {{Json}}
  [Resources](#cfn-supportauthz-supportpermit-resourceset-resources): {{
    - String}}
```

## Properties
<a name="aws-properties-supportauthz-supportpermit-resourceset-properties"></a>

`AllResourcesInRegion`  <a name="cfn-supportauthz-supportpermit-resourceset-allresourcesinregion"></a>
Applies the permit to all resources in the current Region. Specify an empty object (`{}`) to include every resource in the Region. Don't specify this property together with `Resources`.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-supportauthz-supportpermit-resourceset-resources"></a>
An explicit list of resource ARNs the permit applies to. Don't specify this property together with `AllResourcesInRegion`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `512 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
