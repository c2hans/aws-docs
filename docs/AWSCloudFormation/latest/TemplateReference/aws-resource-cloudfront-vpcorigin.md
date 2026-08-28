---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-vpcorigin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::VpcOrigin
<a name="aws-resource-cloudfront-vpcorigin"></a>

An Amazon CloudFront VPC origin.

## Syntax
<a name="aws-resource-cloudfront-vpcorigin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-vpcorigin-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::VpcOrigin",
  "Properties" : {
      "[Tags](#cfn-cloudfront-vpcorigin-tags)" : {{[ Tag, ... ]}},
      "[VpcOriginEndpointConfig](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig)" : {{VpcOriginEndpointConfig}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-vpcorigin-syntax.yaml"></a>

```
Type: AWS::CloudFront::VpcOrigin
Properties:
  [Tags](#cfn-cloudfront-vpcorigin-tags): {{
    - Tag}}
  [VpcOriginEndpointConfig](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig): {{
    VpcOriginEndpointConfig}}
```

## Properties
<a name="aws-resource-cloudfront-vpcorigin-properties"></a>

`Tags`  <a name="cfn-cloudfront-vpcorigin-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-vpcorigin-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcOriginEndpointConfig`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig"></a>
The VPC origin endpoint configuration.
*Required*: Yes
*Type*: [VpcOriginEndpointConfig](aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-vpcorigin-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-vpcorigin-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-vpcorigin-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-vpcorigin-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The account ID of the AWS account that owns the VPC origin.

`Arn`  <a name="Arn-fn::getatt"></a>
The VPC origin ARN.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The VPC origin created time.

`Id`  <a name="Id-fn::getatt"></a>
The VPC origin ID.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The VPC origin last modified time.

`Status`  <a name="Status-fn::getatt"></a>
The VPC origin status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
