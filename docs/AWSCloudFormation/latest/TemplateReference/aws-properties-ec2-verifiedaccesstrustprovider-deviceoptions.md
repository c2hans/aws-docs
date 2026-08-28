---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessTrustProvider DeviceOptions
<a name="aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions"></a>

Describes the options for an AWS Verified Access device-identity based trust provider.

## Syntax
<a name="aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions-syntax.json"></a>

```
{
  "[PublicSigningKeyUrl](#cfn-ec2-verifiedaccesstrustprovider-deviceoptions-publicsigningkeyurl)" : {{String}},
  "[TenantId](#cfn-ec2-verifiedaccesstrustprovider-deviceoptions-tenantid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions-syntax.yaml"></a>

```
  [PublicSigningKeyUrl](#cfn-ec2-verifiedaccesstrustprovider-deviceoptions-publicsigningkeyurl): {{String}}
  [TenantId](#cfn-ec2-verifiedaccesstrustprovider-deviceoptions-tenantid): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccesstrustprovider-deviceoptions-properties"></a>

`PublicSigningKeyUrl`  <a name="cfn-ec2-verifiedaccesstrustprovider-deviceoptions-publicsigningkeyurl"></a>
 The URL AWS Verified Access will use to verify the authenticity of the device tokens.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TenantId`  <a name="cfn-ec2-verifiedaccesstrustprovider-deviceoptions-tenantid"></a>
The ID of the tenant application with the device-identity provider.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
