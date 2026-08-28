---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment S3AccessPointVpcConfiguration
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration"></a>

If included, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).

## Syntax
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-syntax.json"></a>

```
{
  "[VpcId](#cfn-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-syntax.yaml"></a>

```
  [VpcId](#cfn-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-properties"></a>

`VpcId`  <a name="cfn-fsx-s3accesspointattachment-s3accesspointvpcconfiguration-vpcid"></a>
Specifies the virtual private cloud (VPC) for the S3 access point VPC configuration, if one exists.
*Required*: Yes
*Type*: String
*Pattern*: `^(vpc-[0-9a-f]{8,})$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
