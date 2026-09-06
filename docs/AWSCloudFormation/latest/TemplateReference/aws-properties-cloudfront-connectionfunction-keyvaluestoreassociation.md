---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ConnectionFunction KeyValueStoreAssociation
<a name="aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation"></a>

The key value store association.

## Syntax
<a name="aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation-syntax.json"></a>

```
{
  "[KeyValueStoreARN](#cfn-cloudfront-connectionfunction-keyvaluestoreassociation-keyvaluestorearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation-syntax.yaml"></a>

```
  [KeyValueStoreARN](#cfn-cloudfront-connectionfunction-keyvaluestoreassociation-keyvaluestorearn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation-properties"></a>

`KeyValueStoreARN`  <a name="cfn-cloudfront-connectionfunction-keyvaluestoreassociation-keyvaluestorearn"></a>
The Amazon Resource Name (ARN) of the key value store association.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:cloudfront::[0-9]{12}:key-value-store\/[0-9a-fA-F-]{36}`
*Minimum*: `0`
*Maximum*: `85`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
