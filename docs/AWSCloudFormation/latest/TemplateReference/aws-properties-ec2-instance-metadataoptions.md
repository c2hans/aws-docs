---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-metadataoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance MetadataOptions
<a name="aws-properties-ec2-instance-metadataoptions"></a>

Specifies the metadata options for the instance.

## Syntax
<a name="aws-properties-ec2-instance-metadataoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-metadataoptions-syntax.json"></a>

```
{
  "[HttpEndpoint](#cfn-ec2-instance-metadataoptions-httpendpoint)" : {{String}},
  "[HttpProtocolIpv6](#cfn-ec2-instance-metadataoptions-httpprotocolipv6)" : {{String}},
  "[HttpPutResponseHopLimit](#cfn-ec2-instance-metadataoptions-httpputresponsehoplimit)" : {{Integer}},
  "[HttpTokens](#cfn-ec2-instance-metadataoptions-httptokens)" : {{String}},
  "[InstanceMetadataTags](#cfn-ec2-instance-metadataoptions-instancemetadatatags)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-metadataoptions-syntax.yaml"></a>

```
  [HttpEndpoint](#cfn-ec2-instance-metadataoptions-httpendpoint): {{String}}
  [HttpProtocolIpv6](#cfn-ec2-instance-metadataoptions-httpprotocolipv6): {{String}}
  [HttpPutResponseHopLimit](#cfn-ec2-instance-metadataoptions-httpputresponsehoplimit): {{Integer}}
  [HttpTokens](#cfn-ec2-instance-metadataoptions-httptokens): {{String}}
  [InstanceMetadataTags](#cfn-ec2-instance-metadataoptions-instancemetadatatags): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-metadataoptions-properties"></a>

`HttpEndpoint`  <a name="cfn-ec2-instance-metadataoptions-httpendpoint"></a>
Enables or disables the HTTP metadata endpoint on your instances.
If you specify a value of `disabled`, you cannot access your instance metadata.
Default: `enabled`
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpProtocolIpv6`  <a name="cfn-ec2-instance-metadataoptions-httpprotocolipv6"></a>
Enables or disables the IPv6 endpoint for the instance metadata service.
Default: `disabled`
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpPutResponseHopLimit`  <a name="cfn-ec2-instance-metadataoptions-httpputresponsehoplimit"></a>
The maximum number of hops that the metadata token can travel.
Possible values: Integers from 1 to 64
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpTokens`  <a name="cfn-ec2-instance-metadataoptions-httptokens"></a>
Indicates whether IMDSv2 is required.
+ `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
+ `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.
Default:
+ If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0` and the account level default is set to `no-preference`, the default is `required`.
+ If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0`, but the account level default is set to `V1 or V2`, the default is `optional`.
The default value can also be affected by other combinations of parameters. For more information, see [Order of precedence for instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `optional | required`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceMetadataTags`  <a name="cfn-ec2-instance-metadataoptions-instancemetadatatags"></a>
Set to `enabled` to allow access to instance tags from the instance metadata. Set to `disabled` to turn off access to instance tags from the instance metadata. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html).
Default: `disabled`
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
