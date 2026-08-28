---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-vpcoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline VpcOptions
<a name="aws-properties-osis-pipeline-vpcoptions"></a>

Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.

## Syntax
<a name="aws-properties-osis-pipeline-vpcoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-vpcoptions-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-osis-pipeline-vpcoptions-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-osis-pipeline-vpcoptions-subnetids)" : {{[ String, ... ]}},
  "[VpcAttachmentOptions](#cfn-osis-pipeline-vpcoptions-vpcattachmentoptions)" : {{VpcAttachmentOptions}},
  "[VpcEndpointManagement](#cfn-osis-pipeline-vpcoptions-vpcendpointmanagement)" : {{String}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-vpcoptions-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-osis-pipeline-vpcoptions-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-osis-pipeline-vpcoptions-subnetids): {{
    - String}}
  [VpcAttachmentOptions](#cfn-osis-pipeline-vpcoptions-vpcattachmentoptions): {{
    VpcAttachmentOptions}}
  [VpcEndpointManagement](#cfn-osis-pipeline-vpcoptions-vpcendpointmanagement): {{String}}
```

## Properties
<a name="aws-properties-osis-pipeline-vpcoptions-properties"></a>

`SecurityGroupIds`  <a name="cfn-osis-pipeline-vpcoptions-securitygroupids"></a>
A list of security groups associated with the VPC endpoint.
*Required*: No
*Type*: Array of String
*Minimum*: `11`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-osis-pipeline-vpcoptions-subnetids"></a>
A list of subnet IDs associated with the VPC endpoint.
*Required*: Yes
*Type*: Array of String
*Minimum*: `15`
*Maximum*: `24`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcAttachmentOptions`  <a name="cfn-osis-pipeline-vpcoptions-vpcattachmentoptions"></a>
Options for attaching a VPC to a pipeline.
*Required*: No
*Type*: [VpcAttachmentOptions](aws-properties-osis-pipeline-vpcattachmentoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointManagement`  <a name="cfn-osis-pipeline-vpcoptions-vpcendpointmanagement"></a>
Defines whether you or Amazon OpenSearch Ingestion service create and manage the VPC endpoint configured for the pipeline.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOMER | SERVICE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
