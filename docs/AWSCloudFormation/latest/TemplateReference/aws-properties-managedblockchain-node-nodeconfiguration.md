---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-managedblockchain-node-nodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ManagedBlockchain::Node NodeConfiguration
<a name="aws-properties-managedblockchain-node-nodeconfiguration"></a>

Configuration properties of a peer node within a membership.

## Syntax
<a name="aws-properties-managedblockchain-node-nodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-managedblockchain-node-nodeconfiguration-syntax.json"></a>

```
{
  "[AvailabilityZone](#cfn-managedblockchain-node-nodeconfiguration-availabilityzone)" : {{String}},
  "[InstanceType](#cfn-managedblockchain-node-nodeconfiguration-instancetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-managedblockchain-node-nodeconfiguration-syntax.yaml"></a>

```
  [AvailabilityZone](#cfn-managedblockchain-node-nodeconfiguration-availabilityzone): {{String}}
  [InstanceType](#cfn-managedblockchain-node-nodeconfiguration-instancetype): {{String}}
```

## Properties
<a name="aws-properties-managedblockchain-node-nodeconfiguration-properties"></a>

`AvailabilityZone`  <a name="cfn-managedblockchain-node-nodeconfiguration-availabilityzone"></a>
The Availability Zone in which the node exists. Required for Ethereum nodes.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-managedblockchain-node-nodeconfiguration-instancetype"></a>
The Amazon Managed Blockchain instance type for the node.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
