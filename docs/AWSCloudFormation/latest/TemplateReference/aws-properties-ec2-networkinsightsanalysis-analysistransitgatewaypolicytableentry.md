---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAnalysis AnalysisTransitGatewayPolicyTableEntry
<a name="aws-properties-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry"></a>

Describes an entry in a transit gateway policy table.

## Syntax
<a name="aws-properties-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-syntax.json"></a>

```
{
  "[DestinationCidr](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-destinationcidr)" : {{String}},
  "[DestinationPortRange](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-destinationportrange)" : {{PortRange}},
  "[Protocol](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-protocol)" : {{String}},
  "[RuleNumber](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-rulenumber)" : {{Integer}},
  "[SourceCidr](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-sourcecidr)" : {{String}},
  "[SourcePortRange](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-sourceportrange)" : {{PortRange}},
  "[TargetRouteTableId](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-targetroutetableid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-syntax.yaml"></a>

```
  [DestinationCidr](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-destinationcidr): {{String}}
  [DestinationPortRange](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-destinationportrange): {{
    PortRange}}
  [Protocol](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-protocol): {{String}}
  [RuleNumber](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-rulenumber): {{Integer}}
  [SourceCidr](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-sourcecidr): {{String}}
  [SourcePortRange](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-sourceportrange): {{
    PortRange}}
  [TargetRouteTableId](#cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-targetroutetableid): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-properties"></a>

`DestinationCidr`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-destinationcidr"></a>
The destination CIDR block. If this value is not present, the entry matches any destination address.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPortRange`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-destinationportrange"></a>
The destination port range. If this value is not present, the entry matches any destination port.
*Required*: No
*Type*: [PortRange](aws-properties-ec2-networkinsightsanalysis-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-protocol"></a>
The protocol number. A value of `-1` means that the entry matches all protocols.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleNumber`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-rulenumber"></a>
The rule number for the policy table entry. Entries are evaluated in ascending order of rule number.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceCidr`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-sourcecidr"></a>
The source CIDR block. If this value is not present, the entry matches any source address.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePortRange`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-sourceportrange"></a>
The source port range. If this value is not present, the entry matches any source port.
*Required*: No
*Type*: [PortRange](aws-properties-ec2-networkinsightsanalysis-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetRouteTableId`  <a name="cfn-ec2-networkinsightsanalysis-analysistransitgatewaypolicytableentry-targetroutetableid"></a>
The ID of the transit gateway route table to which the entry routes matching traffic.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
