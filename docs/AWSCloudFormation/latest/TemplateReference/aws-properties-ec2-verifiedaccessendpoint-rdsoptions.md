---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-rdsoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint RdsOptions
<a name="aws-properties-ec2-verifiedaccessendpoint-rdsoptions"></a>

Describes the RDS options for a Verified Access endpoint.

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-rdsoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-rdsoptions-syntax.json"></a>

```
{
  "[Port](#cfn-ec2-verifiedaccessendpoint-rdsoptions-port)" : {{Integer}},
  "[Protocol](#cfn-ec2-verifiedaccessendpoint-rdsoptions-protocol)" : {{String}},
  "[RdsDbClusterArn](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbclusterarn)" : {{String}},
  "[RdsDbInstanceArn](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbinstancearn)" : {{String}},
  "[RdsDbProxyArn](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbproxyarn)" : {{String}},
  "[RdsEndpoint](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsendpoint)" : {{String}},
  "[SubnetIds](#cfn-ec2-verifiedaccessendpoint-rdsoptions-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-rdsoptions-syntax.yaml"></a>

```
  [Port](#cfn-ec2-verifiedaccessendpoint-rdsoptions-port): {{Integer}}
  [Protocol](#cfn-ec2-verifiedaccessendpoint-rdsoptions-protocol): {{String}}
  [RdsDbClusterArn](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbclusterarn): {{String}}
  [RdsDbInstanceArn](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbinstancearn): {{String}}
  [RdsDbProxyArn](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbproxyarn): {{String}}
  [RdsEndpoint](#cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsendpoint): {{String}}
  [SubnetIds](#cfn-ec2-verifiedaccessendpoint-rdsoptions-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-rdsoptions-properties"></a>

`Port`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-port"></a>
The port.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-protocol"></a>
The protocol.
*Required*: No
*Type*: String
*Allowed values*: `http | https | tcp`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RdsDbClusterArn`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbclusterarn"></a>
The ARN of the DB cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RdsDbInstanceArn`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbinstancearn"></a>
The ARN of the RDS instance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RdsDbProxyArn`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsdbproxyarn"></a>
The ARN of the RDS proxy.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RdsEndpoint`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-rdsendpoint"></a>
The RDS endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-ec2-verifiedaccessendpoint-rdsoptions-subnetids"></a>
The IDs of the subnets. You can specify only one subnet per Availability Zone.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
