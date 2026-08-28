---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-managedblockchain-member-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ManagedBlockchain::Member NetworkConfiguration
<a name="aws-properties-managedblockchain-member-networkconfiguration"></a>

Configuration properties of the network to which the member belongs.

## Syntax
<a name="aws-properties-managedblockchain-member-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-managedblockchain-member-networkconfiguration-syntax.json"></a>

```
{
  "[Description](#cfn-managedblockchain-member-networkconfiguration-description)" : {{String}},
  "[Framework](#cfn-managedblockchain-member-networkconfiguration-framework)" : {{String}},
  "[FrameworkVersion](#cfn-managedblockchain-member-networkconfiguration-frameworkversion)" : {{String}},
  "[Name](#cfn-managedblockchain-member-networkconfiguration-name)" : {{String}},
  "[NetworkFrameworkConfiguration](#cfn-managedblockchain-member-networkconfiguration-networkframeworkconfiguration)" : {{NetworkFrameworkConfiguration}},
  "[VotingPolicy](#cfn-managedblockchain-member-networkconfiguration-votingpolicy)" : {{VotingPolicy}}
}
```

### YAML
<a name="aws-properties-managedblockchain-member-networkconfiguration-syntax.yaml"></a>

```
  [Description](#cfn-managedblockchain-member-networkconfiguration-description): {{String}}
  [Framework](#cfn-managedblockchain-member-networkconfiguration-framework): {{String}}
  [FrameworkVersion](#cfn-managedblockchain-member-networkconfiguration-frameworkversion): {{String}}
  [Name](#cfn-managedblockchain-member-networkconfiguration-name): {{String}}
  [NetworkFrameworkConfiguration](#cfn-managedblockchain-member-networkconfiguration-networkframeworkconfiguration): {{
    NetworkFrameworkConfiguration}}
  [VotingPolicy](#cfn-managedblockchain-member-networkconfiguration-votingpolicy): {{
    VotingPolicy}}
```

## Properties
<a name="aws-properties-managedblockchain-member-networkconfiguration-properties"></a>

`Description`  <a name="cfn-managedblockchain-member-networkconfiguration-description"></a>
Attributes of the blockchain framework for the network.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Framework`  <a name="cfn-managedblockchain-member-networkconfiguration-framework"></a>
The blockchain framework that the network uses.
*Required*: Yes
*Type*: String
*Allowed values*: `HYPERLEDGER_FABRIC | ETHEREUM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrameworkVersion`  <a name="cfn-managedblockchain-member-networkconfiguration-frameworkversion"></a>
The version of the blockchain framework that the network uses.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-managedblockchain-member-networkconfiguration-name"></a>
The name of the network.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkFrameworkConfiguration`  <a name="cfn-managedblockchain-member-networkconfiguration-networkframeworkconfiguration"></a>
Configuration properties relevant to the network for the blockchain framework that the network uses.
*Required*: No
*Type*: [NetworkFrameworkConfiguration](aws-properties-managedblockchain-member-networkframeworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VotingPolicy`  <a name="cfn-managedblockchain-member-networkconfiguration-votingpolicy"></a>
The voting rules that the network uses to decide if a proposal is accepted.
*Required*: Yes
*Type*: [VotingPolicy](aws-properties-managedblockchain-member-votingpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
