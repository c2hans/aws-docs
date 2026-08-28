---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-managedblockchain-member-networkframeworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ManagedBlockchain::Member NetworkFrameworkConfiguration
<a name="aws-properties-managedblockchain-member-networkframeworkconfiguration"></a>

 Configuration properties relevant to the network for the blockchain framework that the network uses.

## Syntax
<a name="aws-properties-managedblockchain-member-networkframeworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-managedblockchain-member-networkframeworkconfiguration-syntax.json"></a>

```
{
  "[NetworkFabricConfiguration](#cfn-managedblockchain-member-networkframeworkconfiguration-networkfabricconfiguration)" : {{NetworkFabricConfiguration}}
}
```

### YAML
<a name="aws-properties-managedblockchain-member-networkframeworkconfiguration-syntax.yaml"></a>

```
  [NetworkFabricConfiguration](#cfn-managedblockchain-member-networkframeworkconfiguration-networkfabricconfiguration): {{
    NetworkFabricConfiguration}}
```

## Properties
<a name="aws-properties-managedblockchain-member-networkframeworkconfiguration-properties"></a>

`NetworkFabricConfiguration`  <a name="cfn-managedblockchain-member-networkframeworkconfiguration-networkfabricconfiguration"></a>
Configuration properties for Hyperledger Fabric for a member in a Managed Blockchain network that is using the Hyperledger Fabric framework.
*Required*: No
*Type*: [NetworkFabricConfiguration](aws-properties-managedblockchain-member-networkfabricconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
