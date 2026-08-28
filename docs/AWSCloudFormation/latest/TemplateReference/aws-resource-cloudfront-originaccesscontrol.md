---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-originaccesscontrol.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::OriginAccessControl
<a name="aws-resource-cloudfront-originaccesscontrol"></a>

Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.

This makes it possible to block public access to the origin, allowing viewers (users) to access the origin's content only through CloudFront.

For more information about using a CloudFront origin access control, see [Restricting access to an AWS origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-resource-cloudfront-originaccesscontrol-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-originaccesscontrol-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::OriginAccessControl",
  "Properties" : {
      "[OriginAccessControlConfig](#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig)" : {{OriginAccessControlConfig}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-originaccesscontrol-syntax.yaml"></a>

```
Type: AWS::CloudFront::OriginAccessControl
Properties:
  [OriginAccessControlConfig](#cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig): {{
    OriginAccessControlConfig}}
```

## Properties
<a name="aws-resource-cloudfront-originaccesscontrol-properties"></a>

`OriginAccessControlConfig`  <a name="cfn-cloudfront-originaccesscontrol-originaccesscontrolconfig"></a>
The origin access control.
*Required*: Yes
*Type*: [OriginAccessControlConfig](aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-originaccesscontrol-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-originaccesscontrol-return-values-ref"></a>

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudfront-originaccesscontrol-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudfront-originaccesscontrol-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The unique identifier of the origin access control.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
