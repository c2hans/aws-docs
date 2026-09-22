---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration InstanceMetadataOptions
<a name="aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions"></a>

The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches. These settings control how software on those instances retrieves instance metadata and IAM role credentials.

## Syntax
<a name="aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions-syntax.json"></a>

```
{
  "[HttpPutResponseHopLimit](#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httpputresponsehoplimit)" : {{Integer}},
  "[HttpTokens](#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httptokens)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions-syntax.yaml"></a>

```
  [HttpPutResponseHopLimit](#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httpputresponsehoplimit): {{Integer}}
  [HttpTokens](#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httptokens): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions-properties"></a>

`HttpPutResponseHopLimit`  <a name="cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httpputresponsehoplimit"></a>
Limit the number of hops that an instance metadata request can traverse to reach its destination. If you don't set a value, the EC2 launch default for the instance applies. If HTTP tokens are required, container image builds need a minimum of two hops.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpTokens`  <a name="cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httptokens"></a>
Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows:
+ **required** – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.
+ **optional** – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.
If you don't set a value, the EC2 launch default applies to the build and test instances. That default depends on the base AMI and any account-level instance metadata defaults. For more information, see [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 User Guide* *.
*Required*: No
*Type*: String
*Allowed values*: `required | optional`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
