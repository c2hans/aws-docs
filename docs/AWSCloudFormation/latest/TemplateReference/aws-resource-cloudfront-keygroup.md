---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-keygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::KeyGroup
<a name="aws-resource-cloudfront-keygroup"></a>

A key group.

A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).

## Syntax
<a name="aws-resource-cloudfront-keygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-keygroup-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::KeyGroup",
  "Properties" : {
      "[KeyGroupConfig](#cfn-cloudfront-keygroup-keygroupconfig)" : {{KeyGroupConfig}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-keygroup-syntax.yaml"></a>

```
Type: AWS::CloudFront::KeyGroup
Properties:
  [KeyGroupConfig](#cfn-cloudfront-keygroup-keygroupconfig): {{
    KeyGroupConfig}}
```

## Properties
<a name="aws-resource-cloudfront-keygroup-properties"></a>

`KeyGroupConfig`  <a name="cfn-cloudfront-keygroup-keygroupconfig"></a>
The key group configuration.
*Required*: Yes
*Type*: [KeyGroupConfig](aws-properties-cloudfront-keygroup-keygroupconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-keygroup-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-keygroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the key group. For example: `e9fcd3cf-f3f4-4b61-bd85-9ba9e091b309`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudfront-keygroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudfront-keygroup-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The identifier for the key group.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time when the key group was last modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
