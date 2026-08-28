---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-managedblockchain-member-memberconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ManagedBlockchain::Member MemberConfiguration
<a name="aws-properties-managedblockchain-member-memberconfiguration"></a>

Configuration properties of the member.

Applies only to Hyperledger Fabric.

## Syntax
<a name="aws-properties-managedblockchain-member-memberconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-managedblockchain-member-memberconfiguration-syntax.json"></a>

```
{
  "[Description](#cfn-managedblockchain-member-memberconfiguration-description)" : {{String}},
  "[MemberFrameworkConfiguration](#cfn-managedblockchain-member-memberconfiguration-memberframeworkconfiguration)" : {{MemberFrameworkConfiguration}},
  "[Name](#cfn-managedblockchain-member-memberconfiguration-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-managedblockchain-member-memberconfiguration-syntax.yaml"></a>

```
  [Description](#cfn-managedblockchain-member-memberconfiguration-description): {{String}}
  [MemberFrameworkConfiguration](#cfn-managedblockchain-member-memberconfiguration-memberframeworkconfiguration): {{
    MemberFrameworkConfiguration}}
  [Name](#cfn-managedblockchain-member-memberconfiguration-name): {{String}}
```

## Properties
<a name="aws-properties-managedblockchain-member-memberconfiguration-properties"></a>

`Description`  <a name="cfn-managedblockchain-member-memberconfiguration-description"></a>
An optional description of the member.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemberFrameworkConfiguration`  <a name="cfn-managedblockchain-member-memberconfiguration-memberframeworkconfiguration"></a>
Configuration properties of the blockchain framework relevant to the member.
*Required*: No
*Type*: [MemberFrameworkConfiguration](aws-properties-managedblockchain-member-memberframeworkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-managedblockchain-member-memberconfiguration-name"></a>
The name of the member.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!-|[0-9])(?!.*-$)(?!.*?--)[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
