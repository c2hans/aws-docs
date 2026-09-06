---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-connectiongroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ConnectionGroup
<a name="aws-resource-cloudfront-connectiongroup"></a>

The connection group for your distribution tenants. When you first create a distribution tenant and you don't specify a connection group, CloudFront will automatically create a default connection group for you. When you create a new distribution tenant and don't specify a connection group, the default one will be associated with your distribution tenant.

## Syntax
<a name="aws-resource-cloudfront-connectiongroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudfront-connectiongroup-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFront::ConnectionGroup",
  "Properties" : {
      "[AnycastIpListId](#cfn-cloudfront-connectiongroup-anycastiplistid)" : {{String}},
      "[Enabled](#cfn-cloudfront-connectiongroup-enabled)" : {{Boolean}},
      "[Ipv6Enabled](#cfn-cloudfront-connectiongroup-ipv6enabled)" : {{Boolean}},
      "[Name](#cfn-cloudfront-connectiongroup-name)" : {{String}},
      "[Tags](#cfn-cloudfront-connectiongroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudfront-connectiongroup-syntax.yaml"></a>

```
Type: AWS::CloudFront::ConnectionGroup
Properties:
  [AnycastIpListId](#cfn-cloudfront-connectiongroup-anycastiplistid): {{String}}
  [Enabled](#cfn-cloudfront-connectiongroup-enabled): {{Boolean}}
  [Ipv6Enabled](#cfn-cloudfront-connectiongroup-ipv6enabled): {{Boolean}}
  [Name](#cfn-cloudfront-connectiongroup-name): {{String}}
  [Tags](#cfn-cloudfront-connectiongroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudfront-connectiongroup-properties"></a>

`AnycastIpListId`  <a name="cfn-cloudfront-connectiongroup-anycastiplistid"></a>
The ID of the Anycast static IP list.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-cloudfront-connectiongroup-enabled"></a>
Whether the connection group is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ipv6Enabled`  <a name="cfn-cloudfront-connectiongroup-ipv6enabled"></a>
IPv6 is enabled for the connection group.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-connectiongroup-name"></a>
The name of the connection group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudfront-connectiongroup-tags"></a>
A complex type that contains zero or more `Tag` elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudfront-connectiongroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudfront-connectiongroup-return-values"></a>

### Ref
<a name="aws-resource-cloudfront-connectiongroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudfront-connectiongroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudfront-connectiongroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connection group.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The date and time when the connection group was created.

`ETag`  <a name="ETag-fn::getatt"></a>
The current version of the connection group.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the connection group.

`IsDefault`  <a name="IsDefault-fn::getatt"></a>
Whether the connection group is the default connection group for the distribution tenants.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The date and time when the connection group was updated.

`RoutingEndpoint`  <a name="RoutingEndpoint-fn::getatt"></a>
The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.

`Status`  <a name="Status-fn::getatt"></a>
The status of the connection group.
