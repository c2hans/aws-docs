---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-corenetwork-corenetworknetworkfunctiongroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::CoreNetwork CoreNetworkNetworkFunctionGroup
<a name="aws-properties-networkmanager-corenetwork-corenetworknetworkfunctiongroup"></a>

Describes a network function group.

## Syntax
<a name="aws-properties-networkmanager-corenetwork-corenetworknetworkfunctiongroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-corenetwork-corenetworknetworkfunctiongroup-syntax.json"></a>

```
{
  "[EdgeLocations](#cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-edgelocations)" : {{[ String, ... ]}},
  "[Name](#cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-name)" : {{String}},
  "[Segments](#cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-segments)" : {{Segments}}
}
```

### YAML
<a name="aws-properties-networkmanager-corenetwork-corenetworknetworkfunctiongroup-syntax.yaml"></a>

```
  [EdgeLocations](#cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-edgelocations): {{
    - String}}
  [Name](#cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-name): {{String}}
  [Segments](#cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-segments): {{
    Segments}}
```

## Properties
<a name="aws-properties-networkmanager-corenetwork-corenetworknetworkfunctiongroup-properties"></a>

`EdgeLocations`  <a name="cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-edgelocations"></a>
The core network edge locations.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-name"></a>
The name of the network function group.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Segments`  <a name="cfn-networkmanager-corenetwork-corenetworknetworkfunctiongroup-segments"></a>
The segments associated with the network function group.
*Required*: No
*Type*: [Segments](aws-properties-networkmanager-corenetwork-segments.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
