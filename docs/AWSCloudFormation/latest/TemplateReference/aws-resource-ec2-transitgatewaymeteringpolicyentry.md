---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaymeteringpolicyentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayMeteringPolicyEntry
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry"></a>

Creates an entry in a transit gateway metering policy to define traffic measurement rules.

## Syntax
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayMeteringPolicyEntry",
  "Properties" : {
      "[DestinationCidrBlock](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationcidrblock)" : {{String}},
      "[DestinationPortRange](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationportrange)" : {{String}},
      "[DestinationTransitGatewayAttachmentId](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationtransitgatewayattachmentid)" : {{String}},
      "[DestinationTransitGatewayAttachmentType](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationtransitgatewayattachmenttype)" : {{String}},
      "[MeteredAccount](#cfn-ec2-transitgatewaymeteringpolicyentry-meteredaccount)" : {{String}},
      "[PolicyRuleNumber](#cfn-ec2-transitgatewaymeteringpolicyentry-policyrulenumber)" : {{Integer}},
      "[Protocol](#cfn-ec2-transitgatewaymeteringpolicyentry-protocol)" : {{String}},
      "[SourceCidrBlock](#cfn-ec2-transitgatewaymeteringpolicyentry-sourcecidrblock)" : {{String}},
      "[SourcePortRange](#cfn-ec2-transitgatewaymeteringpolicyentry-sourceportrange)" : {{String}},
      "[SourceTransitGatewayAttachmentId](#cfn-ec2-transitgatewaymeteringpolicyentry-sourcetransitgatewayattachmentid)" : {{String}},
      "[SourceTransitGatewayAttachmentType](#cfn-ec2-transitgatewaymeteringpolicyentry-sourcetransitgatewayattachmenttype)" : {{String}},
      "[TransitGatewayMeteringPolicyId](#cfn-ec2-transitgatewaymeteringpolicyentry-transitgatewaymeteringpolicyid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayMeteringPolicyEntry
Properties:
  [DestinationCidrBlock](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationcidrblock): {{String}}
  [DestinationPortRange](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationportrange): {{String}}
  [DestinationTransitGatewayAttachmentId](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationtransitgatewayattachmentid): {{String}}
  [DestinationTransitGatewayAttachmentType](#cfn-ec2-transitgatewaymeteringpolicyentry-destinationtransitgatewayattachmenttype): {{String}}
  [MeteredAccount](#cfn-ec2-transitgatewaymeteringpolicyentry-meteredaccount): {{String}}
  [PolicyRuleNumber](#cfn-ec2-transitgatewaymeteringpolicyentry-policyrulenumber): {{Integer}}
  [Protocol](#cfn-ec2-transitgatewaymeteringpolicyentry-protocol): {{String}}
  [SourceCidrBlock](#cfn-ec2-transitgatewaymeteringpolicyentry-sourcecidrblock): {{String}}
  [SourcePortRange](#cfn-ec2-transitgatewaymeteringpolicyentry-sourceportrange): {{String}}
  [SourceTransitGatewayAttachmentId](#cfn-ec2-transitgatewaymeteringpolicyentry-sourcetransitgatewayattachmentid): {{String}}
  [SourceTransitGatewayAttachmentType](#cfn-ec2-transitgatewaymeteringpolicyentry-sourcetransitgatewayattachmenttype): {{String}}
  [TransitGatewayMeteringPolicyId](#cfn-ec2-transitgatewaymeteringpolicyentry-transitgatewaymeteringpolicyid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-properties"></a>

`DestinationCidrBlock`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-destinationcidrblock"></a>
Describes an IPv4 CIDR block.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationPortRange`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-destinationportrange"></a>
Describes a range of ports.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationTransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-destinationtransitgatewayattachmentid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DestinationTransitGatewayAttachmentType`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-destinationtransitgatewayattachmenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `vpc | vpn | direct-connect-gateway | peering | network-function | vpn-concentrator | client-vpn`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MeteredAccount`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-meteredaccount"></a>
The AWS account ID to which the metered traffic is attributed.
*Required*: Yes
*Type*: String
*Allowed values*: `source-attachment-owner | destination-attachment-owner | transit-gateway-owner`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyRuleNumber`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-policyrulenumber"></a>
The rule number of the metering policy entry.
*Required*: Yes
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-protocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceCidrBlock`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-sourcecidrblock"></a>
Describes an IPv4 CIDR block.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourcePortRange`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-sourceportrange"></a>
Describes a range of ports.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceTransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-sourcetransitgatewayattachmentid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceTransitGatewayAttachmentType`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-sourcetransitgatewayattachmenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `vpc | vpn | direct-connect-gateway | peering | network-function | vpn-concentrator | client-vpn`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayMeteringPolicyId`  <a name="cfn-ec2-transitgatewaymeteringpolicyentry-transitgatewaymeteringpolicyid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewaymeteringpolicyentry-return-values-fn--getatt-fn--getatt"></a>

`State`  <a name="State-fn::getatt"></a>
The state of the metering policy entry.

`UpdateEffectiveAt`  <a name="UpdateEffectiveAt-fn::getatt"></a>
The date and time when the metering policy entry update becomes effective.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
