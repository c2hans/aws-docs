---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-function-keyvaluestoreassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Function KeyValueStoreAssociation
<a name="aws-properties-cloudfront-function-keyvaluestoreassociation"></a>

The key value store association.

## Syntax
<a name="aws-properties-cloudfront-function-keyvaluestoreassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-function-keyvaluestoreassociation-syntax.json"></a>

```
{
  "[KeyValueStoreARN](#cfn-cloudfront-function-keyvaluestoreassociation-keyvaluestorearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-function-keyvaluestoreassociation-syntax.yaml"></a>

```
  [KeyValueStoreARN](#cfn-cloudfront-function-keyvaluestoreassociation-keyvaluestorearn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-function-keyvaluestoreassociation-properties"></a>

`KeyValueStoreARN`  <a name="cfn-cloudfront-function-keyvaluestoreassociation-keyvaluestorearn"></a>
The Amazon Resource Name (ARN) of the key value store association.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:cloudfront::[0-9]{12}:key-value-store\/[0-9a-fA-F-]{36}`
*Minimum*: `0`
*Maximum*: `85`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
