---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage Resources
<a name="aws-properties-lambda-microvmimage-resources"></a>

Resource requirements for a MicroVM.

## Syntax
<a name="aws-properties-lambda-microvmimage-resources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-resources-syntax.json"></a>

```
{
  "[MinimumMemoryInMiB](#cfn-lambda-microvmimage-resources-minimummemoryinmib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-resources-syntax.yaml"></a>

```
  [MinimumMemoryInMiB](#cfn-lambda-microvmimage-resources-minimummemoryinmib): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-resources-properties"></a>

`MinimumMemoryInMiB`  <a name="cfn-lambda-microvmimage-resources-minimummemoryinmib"></a>
The minimum amount of memory in MiB to allocate to the MicroVM.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
