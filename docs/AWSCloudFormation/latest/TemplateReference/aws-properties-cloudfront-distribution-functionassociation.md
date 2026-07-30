---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-functionassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution FunctionAssociation
<a name="aws-properties-cloudfront-distribution-functionassociation"></a>

A CloudFront function that is associated with a cache behavior in a CloudFront distribution.

## Syntax
<a name="aws-properties-cloudfront-distribution-functionassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-functionassociation-syntax.json"></a>

```
{
  "[EventType](#cfn-cloudfront-distribution-functionassociation-eventtype)" : {{String}},
  "[FunctionARN](#cfn-cloudfront-distribution-functionassociation-functionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-functionassociation-syntax.yaml"></a>

```
  [EventType](#cfn-cloudfront-distribution-functionassociation-eventtype): {{String}}
  [FunctionARN](#cfn-cloudfront-distribution-functionassociation-functionarn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-functionassociation-properties"></a>

`EventType`  <a name="cfn-cloudfront-distribution-functionassociation-eventtype"></a>
The event type of the function, either `viewer-request` or `viewer-response`. You cannot use origin-facing event types (`origin-request` and `origin-response`) with a CloudFront function.
*Required*: No
*Type*: String
*Allowed values*: `viewer-request | viewer-response | origin-request | origin-response`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionARN`  <a name="cfn-cloudfront-distribution-functionassociation-functionarn"></a>
The Amazon Resource Name (ARN) of the function.
*Required*: No
*Type*: String
*Pattern*: `arn:aws:cloudfront::[0-9]{12}:function\/[a-zA-Z0-9-_]{1,64}`
*Minimum*: `0`
*Maximum*: `108`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
