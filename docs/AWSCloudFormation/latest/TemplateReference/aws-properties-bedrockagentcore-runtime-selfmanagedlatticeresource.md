---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime SelfManagedLatticeResource
<a name="aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource"></a>

Configuration for a self-managed VPC Lattice resource. You create and manage the VPC Lattice resource gateway and resource configuration, then provide the resource configuration identifier.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource-syntax.json"></a>

```
{
  "[ResourceConfigurationIdentifier](#cfn-bedrockagentcore-runtime-selfmanagedlatticeresource-resourceconfigurationidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource-syntax.yaml"></a>

```
  [ResourceConfigurationIdentifier](#cfn-bedrockagentcore-runtime-selfmanagedlatticeresource-resourceconfigurationidentifier): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-selfmanagedlatticeresource-properties"></a>

`ResourceConfigurationIdentifier`  <a name="cfn-bedrockagentcore-runtime-selfmanagedlatticeresource-resourceconfigurationidentifier"></a>
The ARN or ID of the VPC Lattice resource configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
