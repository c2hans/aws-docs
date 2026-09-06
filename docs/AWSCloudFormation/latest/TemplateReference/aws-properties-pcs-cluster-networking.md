---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-networking.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster Networking
<a name="aws-properties-pcs-cluster-networking"></a>

The networking configuration for the cluster's control plane.

## Syntax
<a name="aws-properties-pcs-cluster-networking-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-networking-syntax.json"></a>

```
{
  "[NetworkType](#cfn-pcs-cluster-networking-networktype)" : {{String}},
  "[SecurityGroupIds](#cfn-pcs-cluster-networking-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-pcs-cluster-networking-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-networking-syntax.yaml"></a>

```
  [NetworkType](#cfn-pcs-cluster-networking-networktype): {{String}}
  [SecurityGroupIds](#cfn-pcs-cluster-networking-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-pcs-cluster-networking-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-pcs-cluster-networking-properties"></a>

`NetworkType`  <a name="cfn-pcs-cluster-networking-networktype"></a>
The IP address version the cluster uses. The default is `IPV4`.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-pcs-cluster-networking-securitygroupids"></a>
The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.
The following rules are required:
+ Inbound rule 1
  + Protocol: All
  + Ports: All
  + Source: Self
+ Outbound rule 1
  + Protocol: All
  + Ports: All
  + Destination: 0.0.0.0/0 (IPv4) or ::/0 (IPv6)
+ Outbound rule 2
  + Protocol: All
  + Ports: All
  + Destination: Self
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-pcs-cluster-networking-subnetids"></a>
The ID of the subnet where AWS PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and AWS PCS resources. The subnet must have an available IP address, cannot reside in AWS Outposts, AWS Wavelength, or an AWS Local Zone.
 Example: `subnet-abcd1234`
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
