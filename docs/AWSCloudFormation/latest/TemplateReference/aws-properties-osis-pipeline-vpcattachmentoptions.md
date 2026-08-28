---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-vpcattachmentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline VpcAttachmentOptions
<a name="aws-properties-osis-pipeline-vpcattachmentoptions"></a>

Options for attaching a VPC to pipeline.

## Syntax
<a name="aws-properties-osis-pipeline-vpcattachmentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-vpcattachmentoptions-syntax.json"></a>

```
{
  "[AttachToVpc](#cfn-osis-pipeline-vpcattachmentoptions-attachtovpc)" : {{Boolean}},
  "[CidrBlock](#cfn-osis-pipeline-vpcattachmentoptions-cidrblock)" : {{String}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-vpcattachmentoptions-syntax.yaml"></a>

```
  [AttachToVpc](#cfn-osis-pipeline-vpcattachmentoptions-attachtovpc): {{Boolean}}
  [CidrBlock](#cfn-osis-pipeline-vpcattachmentoptions-cidrblock): {{String}}
```

## Properties
<a name="aws-properties-osis-pipeline-vpcattachmentoptions-properties"></a>

`AttachToVpc`  <a name="cfn-osis-pipeline-vpcattachmentoptions-attachtovpc"></a>
Whether a VPC is attached to the pipeline.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CidrBlock`  <a name="cfn-osis-pipeline-vpcattachmentoptions-cidrblock"></a>
The CIDR block to be reserved for OpenSearch Ingestion to create elastic network interfaces (ENIs).
*Required*: Yes
*Type*: String
*Pattern*: `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/(3[0-2]|[12]?[0-9])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
