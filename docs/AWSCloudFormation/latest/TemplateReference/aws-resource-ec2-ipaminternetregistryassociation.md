---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-ipaminternetregistryassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IpamInternetRegistryAssociation
<a name="aws-resource-ec2-ipaminternetregistryassociation"></a>

Contains information about an association between an IPAM and a Regional Internet Registry (RIR) for delegated RPKI management.

## Syntax
<a name="aws-resource-ec2-ipaminternetregistryassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-ipaminternetregistryassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::IpamInternetRegistryAssociation",
  "Properties" : {
      "[Description](#cfn-ec2-ipaminternetregistryassociation-description)" : {{String}},
      "[IpamId](#cfn-ec2-ipaminternetregistryassociation-ipamid)" : {{String}},
      "[OrganizationHandle](#cfn-ec2-ipaminternetregistryassociation-organizationhandle)" : {{String}},
      "[Rir](#cfn-ec2-ipaminternetregistryassociation-rir)" : {{String}},
      "[Tags](#cfn-ec2-ipaminternetregistryassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-ipaminternetregistryassociation-syntax.yaml"></a>

```
Type: AWS::EC2::IpamInternetRegistryAssociation
Properties:
  [Description](#cfn-ec2-ipaminternetregistryassociation-description): {{String}}
  [IpamId](#cfn-ec2-ipaminternetregistryassociation-ipamid): {{String}}
  [OrganizationHandle](#cfn-ec2-ipaminternetregistryassociation-organizationhandle): {{String}}
  [Rir](#cfn-ec2-ipaminternetregistryassociation-rir): {{String}}
  [Tags](#cfn-ec2-ipaminternetregistryassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-ipaminternetregistryassociation-properties"></a>

`Description`  <a name="cfn-ec2-ipaminternetregistryassociation-description"></a>
The description of the internet registry association.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpamId`  <a name="cfn-ec2-ipaminternetregistryassociation-ipamid"></a>
The ID of the associated IPAM.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OrganizationHandle`  <a name="cfn-ec2-ipaminternetregistryassociation-organizationhandle"></a>
The organization handle at the internet registry.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Rir`  <a name="cfn-ec2-ipaminternetregistryassociation-rir"></a>
The Regional Internet Registry. Possible values:
+ `ripe` - RIPE NCC (Europe, the Middle East, and Central Asia).
+ `apnic` - APNIC (Asia Pacific).
+ `arin` - ARIN (North America).
+ `lacnic` - LACNIC (Latin America and the Caribbean).
*Required*: Yes
*Type*: String
*Allowed values*: `RIPE | APNIC | ARIN | LACNIC`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-ipaminternetregistryassociation-tags"></a>
The tags assigned to the internet registry association.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-ipaminternetregistryassociation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-ipaminternetregistryassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-ipaminternetregistryassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-ipaminternetregistryassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-ipaminternetregistryassociation-return-values-fn--getatt-fn--getatt"></a>

`ChildRequestXml`  <a name="ChildRequestXml-fn::getatt"></a>
The XML content for the child request to be submitted to the internet registry to complete the BPKI setup.

`IpamInternetRegistryAssociationArn`  <a name="IpamInternetRegistryAssociationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the internet registry association.

`IpamInternetRegistryAssociationId`  <a name="IpamInternetRegistryAssociationId-fn::getatt"></a>
The ID of the internet registry association.

`IpamRegion`  <a name="IpamRegion-fn::getatt"></a>
The AWS Region of the IPAM.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the internet registry association.

`State`  <a name="State-fn::getatt"></a>
The state of the internet registry association. Valid values: `pending-activation` \| `pending-enable` \| `create-in-progress` \| `create-failed` \| `enable-in-progress` \| `enable-complete` \| `enable-failed` \| `delete-in-progress` \| `delete-complete` \| `delete-failed`.
