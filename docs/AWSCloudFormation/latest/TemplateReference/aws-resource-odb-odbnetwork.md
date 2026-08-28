---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-odb-odbnetwork.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork
<a name="aws-resource-odb-odbnetwork"></a>

The `AWS::ODB::OdbNetwork` resource creates an ODB network. An ODB network provides the networking foundation for Oracle Database resources.

## Syntax
<a name="aws-resource-odb-odbnetwork-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-odb-odbnetwork-syntax.json"></a>

```
{
  "Type" : "AWS::ODB::OdbNetwork",
  "Properties" : {
      "[AvailabilityZone](#cfn-odb-odbnetwork-availabilityzone)" : {{String}},
      "[AvailabilityZoneId](#cfn-odb-odbnetwork-availabilityzoneid)" : {{String}},
      "[BackupSubnetCidr](#cfn-odb-odbnetwork-backupsubnetcidr)" : {{String}},
      "[ClientSubnetCidr](#cfn-odb-odbnetwork-clientsubnetcidr)" : {{String}},
      "[CrossRegionS3RestoreSources](#cfn-odb-odbnetwork-crossregions3restoresources)" : {{[ String, ... ]}},
      "[CustomDomainName](#cfn-odb-odbnetwork-customdomainname)" : {{String}},
      "[DefaultDnsPrefix](#cfn-odb-odbnetwork-defaultdnsprefix)" : {{String}},
      "[DeleteAssociatedResources](#cfn-odb-odbnetwork-deleteassociatedresources)" : {{Boolean}},
      "[DisplayName](#cfn-odb-odbnetwork-displayname)" : {{String}},
      "[KmsAccess](#cfn-odb-odbnetwork-kmsaccess)" : {{String}},
      "[KmsPolicyDocument](#cfn-odb-odbnetwork-kmspolicydocument)" : {{String}},
      "[S3Access](#cfn-odb-odbnetwork-s3access)" : {{String}},
      "[S3PolicyDocument](#cfn-odb-odbnetwork-s3policydocument)" : {{String}},
      "[StsAccess](#cfn-odb-odbnetwork-stsaccess)" : {{String}},
      "[StsPolicyDocument](#cfn-odb-odbnetwork-stspolicydocument)" : {{String}},
      "[Tags](#cfn-odb-odbnetwork-tags)" : {{[ Tag, ... ]}},
      "[ZeroEtlAccess](#cfn-odb-odbnetwork-zeroetlaccess)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-odb-odbnetwork-syntax.yaml"></a>

```
Type: AWS::ODB::OdbNetwork
Properties:
  [AvailabilityZone](#cfn-odb-odbnetwork-availabilityzone): {{String}}
  [AvailabilityZoneId](#cfn-odb-odbnetwork-availabilityzoneid): {{String}}
  [BackupSubnetCidr](#cfn-odb-odbnetwork-backupsubnetcidr): {{String}}
  [ClientSubnetCidr](#cfn-odb-odbnetwork-clientsubnetcidr): {{String}}
  [CrossRegionS3RestoreSources](#cfn-odb-odbnetwork-crossregions3restoresources): {{
    - String}}
  [CustomDomainName](#cfn-odb-odbnetwork-customdomainname): {{String}}
  [DefaultDnsPrefix](#cfn-odb-odbnetwork-defaultdnsprefix): {{String}}
  [DeleteAssociatedResources](#cfn-odb-odbnetwork-deleteassociatedresources): {{Boolean}}
  [DisplayName](#cfn-odb-odbnetwork-displayname): {{String}}
  [KmsAccess](#cfn-odb-odbnetwork-kmsaccess): {{String}}
  [KmsPolicyDocument](#cfn-odb-odbnetwork-kmspolicydocument): {{String}}
  [S3Access](#cfn-odb-odbnetwork-s3access): {{String}}
  [S3PolicyDocument](#cfn-odb-odbnetwork-s3policydocument): {{String}}
  [StsAccess](#cfn-odb-odbnetwork-stsaccess): {{String}}
  [StsPolicyDocument](#cfn-odb-odbnetwork-stspolicydocument): {{String}}
  [Tags](#cfn-odb-odbnetwork-tags): {{
    - Tag}}
  [ZeroEtlAccess](#cfn-odb-odbnetwork-zeroetlaccess): {{String}}
```

## Properties
<a name="aws-resource-odb-odbnetwork-properties"></a>

`AvailabilityZone`  <a name="cfn-odb-odbnetwork-availabilityzone"></a>
The Availability Zone (AZ) where the ODB network is located.
Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZoneId`  <a name="cfn-odb-odbnetwork-availabilityzoneid"></a>
The AZ ID of the AZ where the ODB network is located.
Required when creating an ODB network. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the network.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BackupSubnetCidr`  <a name="cfn-odb-odbnetwork-backupsubnetcidr"></a>
The CIDR range of the backup subnet in the ODB network.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientSubnetCidr`  <a name="cfn-odb-odbnetwork-clientsubnetcidr"></a>
The CIDR range of the client subnet in the ODB network.
Required when creating an ODB network.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CrossRegionS3RestoreSources`  <a name="cfn-odb-odbnetwork-crossregions3restoresources"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDomainName`  <a name="cfn-odb-odbnetwork-customdomainname"></a>
The domain name for the resources in the ODB network.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultDnsPrefix`  <a name="cfn-odb-odbnetwork-defaultdnsprefix"></a>
The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeleteAssociatedResources`  <a name="cfn-odb-odbnetwork-deleteassociatedresources"></a>
Specifies whether to delete associated OCI networking resources along with the ODB network.
Required when creating an ODB network.
*Required*: Conditional
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-odb-odbnetwork-displayname"></a>
The user-friendly name of the ODB network.
Required when creating an ODB network.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsAccess`  <a name="cfn-odb-odbnetwork-kmsaccess"></a>
Configuration for AWS Key Management Service (KMS) access from the ODB network.
*Required*: No
*Type*: [String](aws-properties-odb-odbnetwork-kmsaccess.md)
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsPolicyDocument`  <a name="cfn-odb-odbnetwork-kmspolicydocument"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Access`  <a name="cfn-odb-odbnetwork-s3access"></a>
The configuration for Amazon S3 access from the ODB network.
*Required*: No
*Type*: [String](aws-properties-odb-odbnetwork-s3access.md)
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3PolicyDocument`  <a name="cfn-odb-odbnetwork-s3policydocument"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StsAccess`  <a name="cfn-odb-odbnetwork-stsaccess"></a>
Configuration for AWS Security Token Service (STS) access from the ODB network.
*Required*: No
*Type*: [String](aws-properties-odb-odbnetwork-stsaccess.md)
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StsPolicyDocument`  <a name="cfn-odb-odbnetwork-stspolicydocument"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-odb-odbnetwork-tags"></a>
Tags to assign to the Odb Network.
*Required*: No
*Type*: Array of [Tag](aws-properties-odb-odbnetwork-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZeroEtlAccess`  <a name="cfn-odb-odbnetwork-zeroetlaccess"></a>
The configuration for Zero-ETL access from the ODB network.
*Required*: No
*Type*: [String](aws-properties-odb-odbnetwork-zeroetlaccess.md)
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-odb-odbnetwork-return-values"></a>

### Ref
<a name="aws-resource-odb-odbnetwork-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the ODB network. For example:

 `{ "Ref": "myOdbNetwork" }`

For the ODB network `myOdbNetwork`, `Ref` returns the unique identifier of the ODB network.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-odb-odbnetwork-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-odb-odbnetwork-return-values-fn--getatt-fn--getatt"></a>

`Ec2PlacementGroupIds`  <a name="Ec2PlacementGroupIds-fn::getatt"></a>
The list of EC2 Placement Group IDs associated with your ODB network.

`OciNetworkAnchorId`  <a name="OciNetworkAnchorId-fn::getatt"></a>
The unique identifier of the OCI network anchor for the ODB network.

`OciResourceAnchorName`  <a name="OciResourceAnchorName-fn::getatt"></a>
The name of the OCI resource anchor that's associated with the ODB network.

`OciVcnUrl`  <a name="OciVcnUrl-fn::getatt"></a>
The URL for the VCN that's associated with the ODB network.

`OdbNetworkArn`  <a name="OdbNetworkArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the ODB network.

`OdbNetworkId`  <a name="OdbNetworkId-fn::getatt"></a>
The unique identifier of the ODB network.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
