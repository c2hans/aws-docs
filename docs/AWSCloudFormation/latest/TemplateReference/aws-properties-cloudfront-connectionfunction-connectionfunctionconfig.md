---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-connectionfunction-connectionfunctionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ConnectionFunction ConnectionFunctionConfig
<a name="aws-properties-cloudfront-connectionfunction-connectionfunctionconfig"></a>

Contains configuration information about a CloudFront function.

## Syntax
<a name="aws-properties-cloudfront-connectionfunction-connectionfunctionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-connectionfunction-connectionfunctionconfig-syntax.json"></a>

```
{
  "[Comment](#cfn-cloudfront-connectionfunction-connectionfunctionconfig-comment)" : {{String}},
  "[KeyValueStoreAssociations](#cfn-cloudfront-connectionfunction-connectionfunctionconfig-keyvaluestoreassociations)" : {{[ KeyValueStoreAssociation, ... ]}},
  "[Runtime](#cfn-cloudfront-connectionfunction-connectionfunctionconfig-runtime)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-connectionfunction-connectionfunctionconfig-syntax.yaml"></a>

```
  [Comment](#cfn-cloudfront-connectionfunction-connectionfunctionconfig-comment): {{String}}
  [KeyValueStoreAssociations](#cfn-cloudfront-connectionfunction-connectionfunctionconfig-keyvaluestoreassociations): {{
    - KeyValueStoreAssociation}}
  [Runtime](#cfn-cloudfront-connectionfunction-connectionfunctionconfig-runtime): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-connectionfunction-connectionfunctionconfig-properties"></a>

`Comment`  <a name="cfn-cloudfront-connectionfunction-connectionfunctionconfig-comment"></a>
A comment to describe the function. The comment cannot be longer than 128 characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyValueStoreAssociations`  <a name="cfn-cloudfront-connectionfunction-connectionfunctionconfig-keyvaluestoreassociations"></a>
The configuration for the key value store associations.
*Required*: No
*Type*: Array of [KeyValueStoreAssociation](aws-properties-cloudfront-connectionfunction-keyvaluestoreassociation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Runtime`  <a name="cfn-cloudfront-connectionfunction-connectionfunctionconfig-runtime"></a>
The function's runtime environment version.
*Required*: Yes
*Type*: String
*Allowed values*: `cloudfront-js-2.0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
