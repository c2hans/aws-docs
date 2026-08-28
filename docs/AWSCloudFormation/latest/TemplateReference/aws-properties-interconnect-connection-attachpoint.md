---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-interconnect-connection-attachpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Interconnect::Connection AttachPoint
<a name="aws-properties-interconnect-connection-attachpoint"></a>

The logical attachment point in your AWS network where the managed connection is connected. Currently, the only supported type of attach point is a AWS Direct Connect gateway.

## Syntax
<a name="aws-properties-interconnect-connection-attachpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-interconnect-connection-attachpoint-syntax.json"></a>

```
{
  "[Arn](#cfn-interconnect-connection-attachpoint-arn)" : {{String}},
  "[DirectConnectGateway](#cfn-interconnect-connection-attachpoint-directconnectgateway)" : {{String}}
}
```

### YAML
<a name="aws-properties-interconnect-connection-attachpoint-syntax.yaml"></a>

```
  [Arn](#cfn-interconnect-connection-attachpoint-arn): {{String}}
  [DirectConnectGateway](#cfn-interconnect-connection-attachpoint-directconnectgateway): {{String}}
```

## Properties
<a name="aws-properties-interconnect-connection-attachpoint-properties"></a>

`Arn`  <a name="cfn-interconnect-connection-attachpoint-arn"></a>
The Amazon Resource Name (ARN) of the resource to attach to.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectConnectGateway`  <a name="cfn-interconnect-connection-attachpoint-directconnectgateway"></a>
The ID of the AWS Direct Connect gateway to attach to.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
