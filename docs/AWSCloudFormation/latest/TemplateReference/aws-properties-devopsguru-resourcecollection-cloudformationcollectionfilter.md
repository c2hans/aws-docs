---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsGuru::ResourceCollection CloudFormationCollectionFilter
<a name="aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter"></a>

 Information about AWS CloudFormation stacks. You can use up to 1000 stacks to specify which AWS resources in your account to analyze. For more information, see [Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the *AWS CloudFormation User Guide*.

## Syntax
<a name="aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter-syntax.json"></a>

```
{
  "[StackNames](#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter-syntax.yaml"></a>

```
  [StackNames](#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames): {{
    - String}}
```

## Properties
<a name="aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter-properties"></a>

`StackNames`  <a name="cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames"></a>
 An array of CloudFormation stack names.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `128 | 1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
