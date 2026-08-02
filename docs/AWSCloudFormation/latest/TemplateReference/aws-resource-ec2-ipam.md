---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-ipam.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAM
<a name="aws-resource-ec2-ipam"></a>

IPAM is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across AWS Regions and accounts throughout your AWS Organization. For more information, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.

There are AWS Identity and Access Management (IAM) permissions required to fully manage an IPAM in CloudFormation. For more information, see [Example policy](https://docs.aws.amazon.com/vpc/latest/ipam/iam-ipam-policy-examples.html) in the *Amazon VPC IPAM User Guide*.

## Syntax
<a name="aws-resource-ec2-ipam-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-ipam-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::IPAM",
  "Properties" : {
      "[DefaultResourceDiscoveryOrganizationalUnitExclusions](#cfn-ec2-ipam-defaultresourcediscoveryorganizationalunitexclusions)" : {{[ IpamOrganizationalUnitExclusion, ... ]}},
      "[Description](#cfn-ec2-ipam-description)" : {{String}},
      "[EnablePrivateGua](#cfn-ec2-ipam-enableprivategua)" : {{Boolean}},
      "[MeteredAccount](#cfn-ec2-ipam-meteredaccount)" : {{String}},
      "[OperatingRegions](#cfn-ec2-ipam-operatingregions)" : {{[ IpamOperatingRegion, ... ]}},
      "[Tags](#cfn-ec2-ipam-tags)" : {{[ Tag, ... ]}},
      "[Tier](#cfn-ec2-ipam-tier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-ipam-syntax.yaml"></a>

```
Type: AWS::EC2::IPAM
Properties:
  [DefaultResourceDiscoveryOrganizationalUnitExclusions](#cfn-ec2-ipam-defaultresourcediscoveryorganizationalunitexclusions): {{
    - IpamOrganizationalUnitExclusion}}
  [Description](#cfn-ec2-ipam-description): {{String}}
  [EnablePrivateGua](#cfn-ec2-ipam-enableprivategua): {{Boolean}}
  [MeteredAccount](#cfn-ec2-ipam-meteredaccount): {{String}}
  [OperatingRegions](#cfn-ec2-ipam-operatingregions): {{
    - IpamOperatingRegion}}
  [Tags](#cfn-ec2-ipam-tags): {{
    - Tag}}
  [Tier](#cfn-ec2-ipam-tier): {{String}}
```

## Properties
<a name="aws-resource-ec2-ipam-properties"></a>

`DefaultResourceDiscoveryOrganizationalUnitExclusions`  <a name="cfn-ec2-ipam-defaultresourcediscoveryorganizationalunitexclusions"></a>
If your IPAM is integrated with AWS Organizations, you can exclude an [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) from being managed by IPAM. When you exclude an OU, IPAM will not manage the IP addresses in accounts in that OU. For more information, see [Exclude organizational units from IPAM ](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html) in the *Amazon Virtual Private Cloud IP Address Manager User Guide*.
*Required*: No
*Type*: Array of [IpamOrganizationalUnitExclusion](aws-properties-ec2-ipam-ipamorganizationalunitexclusion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ec2-ipam-description"></a>
The description for the IPAM.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnablePrivateGua`  <a name="cfn-ec2-ipam-enableprivategua"></a>
Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MeteredAccount`  <a name="cfn-ec2-ipam-meteredaccount"></a>
A metered account is an AWS account that is charged for active IP addresses managed in IPAM. For more information, see [Enable cost distribution](https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html) in the *Amazon VPC IPAM User Guide*.
Possible values:
+ `ipam-owner` (default): The AWS account which owns the IPAM is charged for all active IP addresses managed in IPAM.
+ `resource-owner`: The AWS account that owns the IP address is charged for the active IP address.
*Required*: No
*Type*: String
*Allowed values*: `ipam-owner | resource-owner`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatingRegions`  <a name="cfn-ec2-ipam-operatingregions"></a>
The operating Regions for an IPAM. Operating Regions are AWS Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the AWS Regions you select as operating Regions.
For more information about operating Regions, see [Create an IPAM](https://docs.aws.amazon.com//vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IPAM User Guide*.
*Required*: No
*Type*: Array of [IpamOperatingRegion](aws-properties-ec2-ipam-ipamoperatingregion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-ipam-tags"></a>
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-ipam-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-ec2-ipam-tier"></a>
IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see the [VPC IPAM product pricing page](https://aws.amazon.com/vpc/pricing/).
*Required*: No
*Type*: String
*Allowed values*: `free | advanced`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-ipam-return-values"></a>

### Ref
<a name="aws-resource-ec2-ipam-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the IPAM ID.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-ipam-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-ipam-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the IPAM.

`DefaultResourceDiscoveryAssociationId`  <a name="DefaultResourceDiscoveryAssociationId-fn::getatt"></a>
The ID of the default resource discovery association.

`DefaultResourceDiscoveryId`  <a name="DefaultResourceDiscoveryId-fn::getatt"></a>
The ID of the default resource discovery.

`IpamId`  <a name="IpamId-fn::getatt"></a>
The ID of the IPAM.

`PrivateDefaultScopeId`  <a name="PrivateDefaultScopeId-fn::getatt"></a>
The ID of the default private scope.

`PublicDefaultScopeId`  <a name="PublicDefaultScopeId-fn::getatt"></a>
The ID of the default public scope.

`ResourceDiscoveryAssociationCount`  <a name="ResourceDiscoveryAssociationCount-fn::getatt"></a>
The number of resource discovery associations.

`ScopeCount`  <a name="ScopeCount-fn::getatt"></a>
The number of scopes.
