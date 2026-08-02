---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-resourcegateway.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ResourceGateway
<a name="aws-resource-vpclattice-resourcegateway"></a>

A resource gateway is a point of ingress into the VPC where a resource resides. It spans multiple Availability Zones. For your resource to be accessible from all Availability Zones, you should create your resource gateways to span as many Availability Zones as possible. A VPC can have multiple resource gateways.

## Syntax
<a name="aws-resource-vpclattice-resourcegateway-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-resourcegateway-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::ResourceGateway",
  "Properties" : {
      "[IpAddressType](#cfn-vpclattice-resourcegateway-ipaddresstype)" : {{String}},
      "[Ipv4AddressesPerEni](#cfn-vpclattice-resourcegateway-ipv4addressespereni)" : {{Integer}},
      "[Name](#cfn-vpclattice-resourcegateway-name)" : {{String}},
      "[ResourceConfigDnsResolution](#cfn-vpclattice-resourcegateway-resourceconfigdnsresolution)" : {{String}},
      "[SecurityGroupIds](#cfn-vpclattice-resourcegateway-securitygroupids)" : {{[ String, ... ]}},
      "[SubnetIds](#cfn-vpclattice-resourcegateway-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-vpclattice-resourcegateway-tags)" : {{[ Tag, ... ]}},
      "[VpcIdentifier](#cfn-vpclattice-resourcegateway-vpcidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-resourcegateway-syntax.yaml"></a>

```
Type: AWS::VpcLattice::ResourceGateway
Properties:
  [IpAddressType](#cfn-vpclattice-resourcegateway-ipaddresstype): {{String}}
  [Ipv4AddressesPerEni](#cfn-vpclattice-resourcegateway-ipv4addressespereni): {{Integer}}
  [Name](#cfn-vpclattice-resourcegateway-name): {{String}}
  [ResourceConfigDnsResolution](#cfn-vpclattice-resourcegateway-resourceconfigdnsresolution): {{String}}
  [SecurityGroupIds](#cfn-vpclattice-resourcegateway-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-vpclattice-resourcegateway-subnetids): {{
    - String}}
  [Tags](#cfn-vpclattice-resourcegateway-tags): {{
    - Tag}}
  [VpcIdentifier](#cfn-vpclattice-resourcegateway-vpcidentifier): {{String}}
```

## Properties
<a name="aws-resource-vpclattice-resourcegateway-properties"></a>

`IpAddressType`  <a name="cfn-vpclattice-resourcegateway-ipaddresstype"></a>
The type of IP address used by the resource gateway.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | IPV6 | DUALSTACK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ipv4AddressesPerEni`  <a name="cfn-vpclattice-resourcegateway-ipv4addressespereni"></a>
The number of IPv4 addresses in each ENI for the resource gateway.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-vpclattice-resourcegateway-name"></a>
The name of the resource gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfigDnsResolution`  <a name="cfn-vpclattice-resourcegateway-resourceconfigdnsresolution"></a>
Indicates how DNS is resolved for resource configurations associated with this resource gateway. ResourceConfigDnsResolution is set at creation time and updates require replacement. The default is `PUBLIC`
+ `IN_VPC` - DNS resolution occurs privately within the resource gateway's VPC. DNS queries for resources behind this resource gateway resolve using the DNS resolvers defined in the VPC's DHCP option sets. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC.
+ `PUBLIC` - DNS resolution occurs against public DNS resolvers. DNS queries for resources behind this resource gateway resolve using standard public DNS. Use this when your resource domain names are publicly resolvable.
*Required*: No
*Type*: String
*Allowed values*: `IN_VPC | PUBLIC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-vpclattice-resourcegateway-securitygroupids"></a>
The IDs of the security groups applied to the resource gateway.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-vpclattice-resourcegateway-subnetids"></a>
The IDs of the VPC subnets for the resource gateway.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-vpclattice-resourcegateway-tags"></a>
The tags for the resource gateway.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-resourcegateway-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcIdentifier`  <a name="cfn-vpclattice-resourcegateway-vpcidentifier"></a>
The ID of the VPC for the resource gateway.
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-vpclattice-resourcegateway-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-resourcegateway-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the resource gateway.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-resourcegateway-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-resourcegateway-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource gateway.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the resource gateway.
