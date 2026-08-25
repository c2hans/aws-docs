---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaypolicytableentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPolicyTableEntry
<a name="aws-resource-ec2-transitgatewaypolicytableentry"></a>

Creates an entry in a transit gateway policy table to route matching traffic to a specified route table.

## Syntax
<a name="aws-resource-ec2-transitgatewaypolicytableentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaypolicytableentry-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayPolicyTableEntry",
  "Properties" : {
      "[PolicyRule](#cfn-ec2-transitgatewaypolicytableentry-policyrule)" : {{TransitGatewayPolicyRule}},
      "[PolicyRuleNumber](#cfn-ec2-transitgatewaypolicytableentry-policyrulenumber)" : {{String}},
      "[TargetRouteTableId](#cfn-ec2-transitgatewaypolicytableentry-targetroutetableid)" : {{String}},
      "[TransitGatewayPolicyTableId](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicytableid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaypolicytableentry-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayPolicyTableEntry
Properties:
  [PolicyRule](#cfn-ec2-transitgatewaypolicytableentry-policyrule): {{
    TransitGatewayPolicyRule}}
  [PolicyRuleNumber](#cfn-ec2-transitgatewaypolicytableentry-policyrulenumber): {{String}}
  [TargetRouteTableId](#cfn-ec2-transitgatewaypolicytableentry-targetroutetableid): {{String}}
  [TransitGatewayPolicyTableId](#cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicytableid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaypolicytableentry-properties"></a>

`PolicyRule`  <a name="cfn-ec2-transitgatewaypolicytableentry-policyrule"></a>
The policy rule associated with the transit gateway policy table.
*Required*: Yes
*Type*: [TransitGatewayPolicyRule](aws-properties-ec2-transitgatewaypolicytableentry-transitgatewaypolicyrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyRuleNumber`  <a name="cfn-ec2-transitgatewaypolicytableentry-policyrulenumber"></a>
The rule number for the transit gateway policy table entry.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetRouteTableId`  <a name="cfn-ec2-transitgatewaypolicytableentry-targetroutetableid"></a>
The ID of the target route table.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitGatewayPolicyTableId`  <a name="cfn-ec2-transitgatewaypolicytableentry-transitgatewaypolicytableid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaypolicytableentry-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaypolicytableentry-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaypolicytableentry-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewaypolicytableentry-return-values-fn--getatt-fn--getatt"></a>

`State`  <a name="State-fn::getatt"></a>
The state of the transit gateway policy table entry.
