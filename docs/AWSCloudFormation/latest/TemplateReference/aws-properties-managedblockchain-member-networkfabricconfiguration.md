---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-managedblockchain-member-networkfabricconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ManagedBlockchain::Member NetworkFabricConfiguration
<a name="aws-properties-managedblockchain-member-networkfabricconfiguration"></a>

Hyperledger Fabric configuration properties for the network.

## Syntax
<a name="aws-properties-managedblockchain-member-networkfabricconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-managedblockchain-member-networkfabricconfiguration-syntax.json"></a>

```
{
  "[Edition](#cfn-managedblockchain-member-networkfabricconfiguration-edition)" : {{String}}
}
```

### YAML
<a name="aws-properties-managedblockchain-member-networkfabricconfiguration-syntax.yaml"></a>

```
  [Edition](#cfn-managedblockchain-member-networkfabricconfiguration-edition): {{String}}
```

## Properties
<a name="aws-properties-managedblockchain-member-networkfabricconfiguration-properties"></a>

`Edition`  <a name="cfn-managedblockchain-member-networkfabricconfiguration-edition"></a>
The edition of Amazon Managed Blockchain that the network uses. Valid values are `standard` and `starter`. For more information, see [Amazon Managed Blockchain Pricing](https://aws.amazon.com/managed-blockchain/pricing/)
*Required*: Yes
*Type*: String
*Allowed values*: `STARTER | STANDARD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
