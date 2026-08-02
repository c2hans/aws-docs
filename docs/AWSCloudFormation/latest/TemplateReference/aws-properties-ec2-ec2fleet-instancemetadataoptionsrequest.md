---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-instancemetadataoptionsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet InstanceMetadataOptionsRequest
<a name="aws-properties-ec2-ec2fleet-instancemetadataoptionsrequest"></a>

The metadata options for the instance.

## Syntax
<a name="aws-properties-ec2-ec2fleet-instancemetadataoptionsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-instancemetadataoptionsrequest-syntax.json"></a>

```
{
  "[HttpEndpoint](#cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httpendpoint)" : {{String}},
  "[HttpPutResponseHopLimit](#cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httpputresponsehoplimit)" : {{Integer}},
  "[HttpTokens](#cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httptokens)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-instancemetadataoptionsrequest-syntax.yaml"></a>

```
  [HttpEndpoint](#cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httpendpoint): {{String}}
  [HttpPutResponseHopLimit](#cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httpputresponsehoplimit): {{Integer}}
  [HttpTokens](#cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httptokens): {{String}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-instancemetadataoptionsrequest-properties"></a>

`HttpEndpoint`  <a name="cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httpendpoint"></a>
Enables or disables the HTTP metadata endpoint on your instances.
If you specify a value of `disabled`, you cannot access your instance metadata.
Default: `enabled`
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HttpPutResponseHopLimit`  <a name="cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httpputresponsehoplimit"></a>
The maximum number of hops that the metadata token can travel.
Possible values: Integers from 1 to 64
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HttpTokens`  <a name="cfn-ec2-ec2fleet-instancemetadataoptionsrequest-httptokens"></a>
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
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
