---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-privateendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway PrivateEndpoint
<a name="aws-properties-bedrockagentcore-gateway-privateendpoint"></a>

The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-privateendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-privateendpoint-syntax.json"></a>

```
{
  "[ManagedVpcResource](#cfn-bedrockagentcore-gateway-privateendpoint-managedvpcresource)" : {{ManagedVpcResource}},
  "[SelfManagedLatticeResource](#cfn-bedrockagentcore-gateway-privateendpoint-selfmanagedlatticeresource)" : {{SelfManagedLatticeResource}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-privateendpoint-syntax.yaml"></a>

```
  [ManagedVpcResource](#cfn-bedrockagentcore-gateway-privateendpoint-managedvpcresource): {{
    ManagedVpcResource}}
  [SelfManagedLatticeResource](#cfn-bedrockagentcore-gateway-privateendpoint-selfmanagedlatticeresource): {{
    SelfManagedLatticeResource}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-privateendpoint-properties"></a>

`ManagedVpcResource`  <a name="cfn-bedrockagentcore-gateway-privateendpoint-managedvpcresource"></a>
Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
*Required*: No
*Type*: [ManagedVpcResource](aws-properties-bedrockagentcore-gateway-managedvpcresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedLatticeResource`  <a name="cfn-bedrockagentcore-gateway-privateendpoint-selfmanagedlatticeresource"></a>
Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
*Required*: No
*Type*: [SelfManagedLatticeResource](aws-properties-bedrockagentcore-gateway-selfmanagedlatticeresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
