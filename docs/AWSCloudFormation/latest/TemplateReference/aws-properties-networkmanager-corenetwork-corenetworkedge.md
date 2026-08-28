---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-corenetwork-corenetworkedge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::CoreNetwork CoreNetworkEdge
<a name="aws-properties-networkmanager-corenetwork-corenetworkedge"></a>

Describes a core network edge.

## Syntax
<a name="aws-properties-networkmanager-corenetwork-corenetworkedge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-corenetwork-corenetworkedge-syntax.json"></a>

```
{
  "[Asn](#cfn-networkmanager-corenetwork-corenetworkedge-asn)" : {{Number}},
  "[EdgeLocation](#cfn-networkmanager-corenetwork-corenetworkedge-edgelocation)" : {{String}},
  "[InsideCidrBlocks](#cfn-networkmanager-corenetwork-corenetworkedge-insidecidrblocks)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-corenetwork-corenetworkedge-syntax.yaml"></a>

```
  [Asn](#cfn-networkmanager-corenetwork-corenetworkedge-asn): {{Number}}
  [EdgeLocation](#cfn-networkmanager-corenetwork-corenetworkedge-edgelocation): {{String}}
  [InsideCidrBlocks](#cfn-networkmanager-corenetwork-corenetworkedge-insidecidrblocks): {{
    - String}}
```

## Properties
<a name="aws-properties-networkmanager-corenetwork-corenetworkedge-properties"></a>

`Asn`  <a name="cfn-networkmanager-corenetwork-corenetworkedge-asn"></a>
The ASN of a core network edge.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EdgeLocation`  <a name="cfn-networkmanager-corenetwork-corenetworkedge-edgelocation"></a>
The Region where a core network edge is located.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InsideCidrBlocks`  <a name="cfn-networkmanager-corenetwork-corenetworkedge-insidecidrblocks"></a>
The inside IP addresses used for core network edges.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
