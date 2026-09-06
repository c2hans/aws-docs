---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-ipamexternalresourceverificationtoken.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IpamExternalResourceVerificationToken
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken"></a>

A verification token is an AWS-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification token to validate that you control a public IP address range when you bring an IP address range to AWS (BYOIP).

## Syntax
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::IpamExternalResourceVerificationToken",
  "Properties" : {
      "[IpamId](#cfn-ec2-ipamexternalresourceverificationtoken-ipamid)" : {{String}},
      "[Tags](#cfn-ec2-ipamexternalresourceverificationtoken-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-syntax.yaml"></a>

```
Type: AWS::EC2::IpamExternalResourceVerificationToken
Properties:
  [IpamId](#cfn-ec2-ipamexternalresourceverificationtoken-ipamid): {{String}}
  [Tags](#cfn-ec2-ipamexternalresourceverificationtoken-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-properties"></a>

`IpamId`  <a name="cfn-ec2-ipamexternalresourceverificationtoken-ipamid"></a>
The ID of the IPAM that created the token.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-ipamexternalresourceverificationtoken-tags"></a>
Token tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-ipamexternalresourceverificationtoken-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-return-values"></a>

### Ref
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-ipamexternalresourceverificationtoken-return-values-fn--getatt-fn--getatt"></a>

`IpamArn`  <a name="IpamArn-fn::getatt"></a>
ARN of the IPAM that created the token.

`IpamExternalResourceVerificationTokenArn`  <a name="IpamExternalResourceVerificationTokenArn-fn::getatt"></a>
Token ARN.

`IpamExternalResourceVerificationTokenId`  <a name="IpamExternalResourceVerificationTokenId-fn::getatt"></a>
The ID of the token.

`IpamRegion`  <a name="IpamRegion-fn::getatt"></a>
Region of the IPAM that created the token.

`NotAfter`  <a name="NotAfter-fn::getatt"></a>
Token expiration.

`State`  <a name="State-fn::getatt"></a>
Token state.

`Status`  <a name="Status-fn::getatt"></a>
Token status.

`TokenName`  <a name="TokenName-fn::getatt"></a>
Token name.

`TokenValue`  <a name="TokenValue-fn::getatt"></a>
Token value.
