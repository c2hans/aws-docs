---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-vpcendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline VpcEndpoint
<a name="aws-properties-osis-pipeline-vpcendpoint"></a>

An OpenSearch Ingestion-managed VPC endpoint that will access one or more pipelines.

## Syntax
<a name="aws-properties-osis-pipeline-vpcendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-vpcendpoint-syntax.json"></a>

```
{
  "[VpcEndpointId](#cfn-osis-pipeline-vpcendpoint-vpcendpointid)" : {{String}},
  "[VpcId](#cfn-osis-pipeline-vpcendpoint-vpcid)" : {{String}},
  "[VpcOptions](#cfn-osis-pipeline-vpcendpoint-vpcoptions)" : {{VpcOptions}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-vpcendpoint-syntax.yaml"></a>

```
  [VpcEndpointId](#cfn-osis-pipeline-vpcendpoint-vpcendpointid): {{String}}
  [VpcId](#cfn-osis-pipeline-vpcendpoint-vpcid): {{String}}
  [VpcOptions](#cfn-osis-pipeline-vpcendpoint-vpcoptions): {{
    VpcOptions}}
```

## Properties
<a name="aws-properties-osis-pipeline-vpcendpoint-properties"></a>

`VpcEndpointId`  <a name="cfn-osis-pipeline-vpcendpoint-vpcendpointid"></a>
The unique identifier of the endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-osis-pipeline-vpcendpoint-vpcid"></a>
The ID for your VPC. AWS PrivateLink generates this value when you create a VPC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcOptions`  <a name="cfn-osis-pipeline-vpcendpoint-vpcoptions"></a>
Information about the VPC, including associated subnets and security groups.
*Required*: No
*Type*: [VpcOptions](aws-properties-osis-pipeline-vpcoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
