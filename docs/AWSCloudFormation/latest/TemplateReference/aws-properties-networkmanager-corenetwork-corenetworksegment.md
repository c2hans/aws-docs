---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-corenetwork-corenetworksegment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::CoreNetwork CoreNetworkSegment
<a name="aws-properties-networkmanager-corenetwork-corenetworksegment"></a>

Describes a core network segment, which are dedicated routes. Only attachments within this segment can communicate with each other.

## Syntax
<a name="aws-properties-networkmanager-corenetwork-corenetworksegment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-corenetwork-corenetworksegment-syntax.json"></a>

```
{
  "[EdgeLocations](#cfn-networkmanager-corenetwork-corenetworksegment-edgelocations)" : {{[ String, ... ]}},
  "[Name](#cfn-networkmanager-corenetwork-corenetworksegment-name)" : {{String}},
  "[SharedSegments](#cfn-networkmanager-corenetwork-corenetworksegment-sharedsegments)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-networkmanager-corenetwork-corenetworksegment-syntax.yaml"></a>

```
  [EdgeLocations](#cfn-networkmanager-corenetwork-corenetworksegment-edgelocations): {{
    - String}}
  [Name](#cfn-networkmanager-corenetwork-corenetworksegment-name): {{String}}
  [SharedSegments](#cfn-networkmanager-corenetwork-corenetworksegment-sharedsegments): {{
    - String}}
```

## Properties
<a name="aws-properties-networkmanager-corenetwork-corenetworksegment-properties"></a>

`EdgeLocations`  <a name="cfn-networkmanager-corenetwork-corenetworksegment-edgelocations"></a>
The Regions where the edges are located.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-networkmanager-corenetwork-corenetworksegment-name"></a>
The name of a core network segment.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharedSegments`  <a name="cfn-networkmanager-corenetwork-corenetworksegment-sharedsegments"></a>
The shared segments of a core network.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
