---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-function-functionmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Function FunctionMetadata
<a name="aws-properties-cloudfront-function-functionmetadata"></a>

Contains metadata about a CloudFront function.

## Syntax
<a name="aws-properties-cloudfront-function-functionmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-function-functionmetadata-syntax.json"></a>

```
{
  "[FunctionARN](#cfn-cloudfront-function-functionmetadata-functionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-function-functionmetadata-syntax.yaml"></a>

```
  [FunctionARN](#cfn-cloudfront-function-functionmetadata-functionarn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-function-functionmetadata-properties"></a>

`FunctionARN`  <a name="cfn-cloudfront-function-functionmetadata-functionarn"></a>
The Amazon Resource Name (ARN) of the function. The ARN uniquely identifies the function.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
