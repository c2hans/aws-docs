---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-privateendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime PrivateEndpoint
<a name="aws-properties-bedrockagentcore-runtime-privateendpoint"></a>

The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-privateendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-privateendpoint-syntax.json"></a>

```
{
  "[ManagedVpcResource](#cfn-bedrockagentcore-runtime-privateendpoint-managedvpcresource)" : {{ManagedVpcResource}},
  "[SelfManagedLatticeResource](#cfn-bedrockagentcore-runtime-privateendpoint-selfmanagedlatticeresource)" : {{SelfManagedLatticeResource}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-privateendpoint-syntax.yaml"></a>

```
  [ManagedVpcResource](#cfn-bedrockagentcore-runtime-privateendpoint-managedvpcresource): {{
    ManagedVpcResource}}
  [SelfManagedLatticeResource](#cfn-bedrockagentcore-runtime-privateendpoint-selfmanagedlatticeresource): {{
    SelfManagedLatticeResource}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-privateendpoint-properties"></a>

`ManagedVpcResource`  <a name="cfn-bedrockagentcore-runtime-privateendpoint-managedvpcresource"></a>
Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
*Required*: No
*Type*: [ManagedVpcResource](aws-properties-bedrockagentcore-runtime-managedvpcresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfManagedLatticeResource`  <a name="cfn-bedrockagentcore-runtime-privateendpoint-selfmanagedlatticeresource"></a>
Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
*Required*: No
*Type*: [SelfManagedLatticeResource](aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
