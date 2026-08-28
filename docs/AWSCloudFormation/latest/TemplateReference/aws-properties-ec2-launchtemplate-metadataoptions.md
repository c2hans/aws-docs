---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-metadataoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate MetadataOptions
<a name="aws-properties-ec2-launchtemplate-metadataoptions"></a>

The metadata options for the instance. For more information, see [Instance metadata and user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.

`MetadataOptions` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-metadataoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-metadataoptions-syntax.json"></a>

```
{
  "[HttpEndpoint](#cfn-ec2-launchtemplate-metadataoptions-httpendpoint)" : {{String}},
  "[HttpProtocolIpv6](#cfn-ec2-launchtemplate-metadataoptions-httpprotocolipv6)" : {{String}},
  "[HttpPutResponseHopLimit](#cfn-ec2-launchtemplate-metadataoptions-httpputresponsehoplimit)" : {{Integer}},
  "[HttpTokens](#cfn-ec2-launchtemplate-metadataoptions-httptokens)" : {{String}},
  "[InstanceMetadataTags](#cfn-ec2-launchtemplate-metadataoptions-instancemetadatatags)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-metadataoptions-syntax.yaml"></a>

```
  [HttpEndpoint](#cfn-ec2-launchtemplate-metadataoptions-httpendpoint): {{String}}
  [HttpProtocolIpv6](#cfn-ec2-launchtemplate-metadataoptions-httpprotocolipv6): {{String}}
  [HttpPutResponseHopLimit](#cfn-ec2-launchtemplate-metadataoptions-httpputresponsehoplimit): {{Integer}}
  [HttpTokens](#cfn-ec2-launchtemplate-metadataoptions-httptokens): {{String}}
  [InstanceMetadataTags](#cfn-ec2-launchtemplate-metadataoptions-instancemetadatatags): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-metadataoptions-properties"></a>

`HttpEndpoint`  <a name="cfn-ec2-launchtemplate-metadataoptions-httpendpoint"></a>
Enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is `enabled`.
If you specify a value of `disabled`, you will not be able to access your instance metadata.
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpProtocolIpv6`  <a name="cfn-ec2-launchtemplate-metadataoptions-httpprotocolipv6"></a>
Enables or disables the IPv6 endpoint for the instance metadata service.
Default: `disabled`
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpPutResponseHopLimit`  <a name="cfn-ec2-launchtemplate-metadataoptions-httpputresponsehoplimit"></a>
The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.
Default: `1`
Possible values: Integers from 1 to 64
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpTokens`  <a name="cfn-ec2-launchtemplate-metadataoptions-httptokens"></a>
Indicates whether IMDSv2 is required.
+ `optional` - IMDSv2 is optional. You can choose whether to send a session token in your instance metadata retrieval requests. If you retrieve IAM role credentials without a session token, you receive the IMDSv1 role credentials. If you retrieve IAM role credentials using a valid session token, you receive the IMDSv2 role credentials.
+ `required` - IMDSv2 is required. You must send a session token in your instance metadata retrieval requests. With this option, retrieving the IAM role credentials always returns IMDSv2 credentials; IMDSv1 credentials are not available.
Default: If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0`, the default is `required`.
*Required*: No
*Type*: String
*Allowed values*: `optional | required`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceMetadataTags`  <a name="cfn-ec2-launchtemplate-metadataoptions-instancemetadatatags"></a>
Set to `enabled` to allow access to instance tags from the instance metadata. Set to `disabled` to turn off access to instance tags from the instance metadata. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html).
Default: `disabled`
*Required*: No
*Type*: String
*Allowed values*: `disabled | enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
