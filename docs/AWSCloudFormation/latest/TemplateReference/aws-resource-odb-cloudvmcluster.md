---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-odb-cloudvmcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudVmCluster
<a name="aws-resource-odb-cloudvmcluster"></a>

The `AWS::ODB::CloudVmCluster` resource creates a VM cluster on the specified Exadata infrastructure in the Oracle Database. A VM cluster provides the compute resources for Oracle Database workloads.

## Syntax
<a name="aws-resource-odb-cloudvmcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-odb-cloudvmcluster-syntax.json"></a>

```
{
  "Type" : "AWS::ODB::CloudVmCluster",
  "Properties" : {
      "[CloudExadataInfrastructureId](#cfn-odb-cloudvmcluster-cloudexadatainfrastructureid)" : {{String}},
      "[ClusterName](#cfn-odb-cloudvmcluster-clustername)" : {{String}},
      "[CpuCoreCount](#cfn-odb-cloudvmcluster-cpucorecount)" : {{Integer}},
      "[DataCollectionOptions](#cfn-odb-cloudvmcluster-datacollectionoptions)" : {{DataCollectionOptions}},
      "[DataStorageSizeInTBs](#cfn-odb-cloudvmcluster-datastoragesizeintbs)" : {{Number}},
      "[DbNodes](#cfn-odb-cloudvmcluster-dbnodes)" : {{[ DbNode, ... ]}},
      "[DbNodeStorageSizeInGBs](#cfn-odb-cloudvmcluster-dbnodestoragesizeingbs)" : {{Integer}},
      "[DbServers](#cfn-odb-cloudvmcluster-dbservers)" : {{[ String, ... ]}},
      "[DisplayName](#cfn-odb-cloudvmcluster-displayname)" : {{String}},
      "[GiVersion](#cfn-odb-cloudvmcluster-giversion)" : {{String}},
      "[Hostname](#cfn-odb-cloudvmcluster-hostname)" : {{String}},
      "[IamRoles](#cfn-odb-cloudvmcluster-iamroles)" : {{[ IamRole, ... ]}},
      "[IsLocalBackupEnabled](#cfn-odb-cloudvmcluster-islocalbackupenabled)" : {{Boolean}},
      "[IsSparseDiskgroupEnabled](#cfn-odb-cloudvmcluster-issparsediskgroupenabled)" : {{Boolean}},
      "[LicenseModel](#cfn-odb-cloudvmcluster-licensemodel)" : {{String}},
      "[MemorySizeInGBs](#cfn-odb-cloudvmcluster-memorysizeingbs)" : {{Integer}},
      "[OdbNetworkId](#cfn-odb-cloudvmcluster-odbnetworkid)" : {{String}},
      "[ScanListenerPortTcp](#cfn-odb-cloudvmcluster-scanlistenerporttcp)" : {{Integer}},
      "[SshPublicKeys](#cfn-odb-cloudvmcluster-sshpublickeys)" : {{[ String, ... ]}},
      "[SystemVersion](#cfn-odb-cloudvmcluster-systemversion)" : {{String}},
      "[Tags](#cfn-odb-cloudvmcluster-tags)" : {{[ Tag, ... ]}},
      "[TimeZone](#cfn-odb-cloudvmcluster-timezone)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-odb-cloudvmcluster-syntax.yaml"></a>

```
Type: AWS::ODB::CloudVmCluster
Properties:
  [CloudExadataInfrastructureId](#cfn-odb-cloudvmcluster-cloudexadatainfrastructureid): {{String}}
  [ClusterName](#cfn-odb-cloudvmcluster-clustername): {{String}}
  [CpuCoreCount](#cfn-odb-cloudvmcluster-cpucorecount): {{Integer}}
  [DataCollectionOptions](#cfn-odb-cloudvmcluster-datacollectionoptions): {{
    DataCollectionOptions}}
  [DataStorageSizeInTBs](#cfn-odb-cloudvmcluster-datastoragesizeintbs): {{Number}}
  [DbNodes](#cfn-odb-cloudvmcluster-dbnodes): {{
    - DbNode}}
  [DbNodeStorageSizeInGBs](#cfn-odb-cloudvmcluster-dbnodestoragesizeingbs): {{Integer}}
  [DbServers](#cfn-odb-cloudvmcluster-dbservers): {{
    - String}}
  [DisplayName](#cfn-odb-cloudvmcluster-displayname): {{String}}
  [GiVersion](#cfn-odb-cloudvmcluster-giversion): {{String}}
  [Hostname](#cfn-odb-cloudvmcluster-hostname): {{String}}
  [IamRoles](#cfn-odb-cloudvmcluster-iamroles): {{
    - IamRole}}
  [IsLocalBackupEnabled](#cfn-odb-cloudvmcluster-islocalbackupenabled): {{Boolean}}
  [IsSparseDiskgroupEnabled](#cfn-odb-cloudvmcluster-issparsediskgroupenabled): {{Boolean}}
  [LicenseModel](#cfn-odb-cloudvmcluster-licensemodel): {{String}}
  [MemorySizeInGBs](#cfn-odb-cloudvmcluster-memorysizeingbs): {{Integer}}
  [OdbNetworkId](#cfn-odb-cloudvmcluster-odbnetworkid): {{String}}
  [ScanListenerPortTcp](#cfn-odb-cloudvmcluster-scanlistenerporttcp): {{Integer}}
  [SshPublicKeys](#cfn-odb-cloudvmcluster-sshpublickeys): {{
    - String}}
  [SystemVersion](#cfn-odb-cloudvmcluster-systemversion): {{String}}
  [Tags](#cfn-odb-cloudvmcluster-tags): {{
    - Tag}}
  [TimeZone](#cfn-odb-cloudvmcluster-timezone): {{String}}
```

## Properties
<a name="aws-resource-odb-cloudvmcluster-properties"></a>

`CloudExadataInfrastructureId`  <a name="cfn-odb-cloudvmcluster-cloudexadatainfrastructureid"></a>
The unique identifier of the Exadata infrastructure that this VM cluster belongs to.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterName`  <a name="cfn-odb-cloudvmcluster-clustername"></a>
The name of the Grid Infrastructure (GI) cluster.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9-]*$`
*Minimum*: `1`
*Maximum*: `11`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CpuCoreCount`  <a name="cfn-odb-cloudvmcluster-cpucorecount"></a>
The number of CPU cores enabled on the VM cluster.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: Integer
*Minimum*: `0`
*Maximum*: `368`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataCollectionOptions`  <a name="cfn-odb-cloudvmcluster-datacollectionoptions"></a>
The set of diagnostic collection options enabled for the VM cluster.
*Required*: No
*Type*: [DataCollectionOptions](aws-properties-odb-cloudvmcluster-datacollectionoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataStorageSizeInTBs`  <a name="cfn-odb-cloudvmcluster-datastoragesizeintbs"></a>
The size of the data disk group, in terabytes (TB), that's allocated for the VM cluster.
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DbNodes`  <a name="cfn-odb-cloudvmcluster-dbnodes"></a>
Property description not available.
*Required*: No
*Type*: Array of [DbNode](aws-properties-odb-cloudvmcluster-dbnode.md)
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DbNodeStorageSizeInGBs`  <a name="cfn-odb-cloudvmcluster-dbnodestoragesizeingbs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated for the VM cluster.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DbServers`  <a name="cfn-odb-cloudvmcluster-dbservers"></a>
The list of database servers for the VM cluster.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisplayName`  <a name="cfn-odb-cloudvmcluster-displayname"></a>
The user-friendly name for the VM cluster.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GiVersion`  <a name="cfn-odb-cloudvmcluster-giversion"></a>
The software version of the Oracle Grid Infrastructure (GI) for the VM cluster.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Hostname`  <a name="cfn-odb-cloudvmcluster-hostname"></a>
The host name for the VM cluster.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9-]*[a-zA-Z0-9]$`
*Minimum*: `1`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IamRoles`  <a name="cfn-odb-cloudvmcluster-iamroles"></a>
The AWS Identity and Access Management (IAM) service roles associated with the VM cluster.
*Required*: No
*Type*: Array of [IamRole](aws-properties-odb-cloudvmcluster-iamrole.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsLocalBackupEnabled`  <a name="cfn-odb-cloudvmcluster-islocalbackupenabled"></a>
Specifies whether database backups to local Exadata storage are enabled for the VM cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IsSparseDiskgroupEnabled`  <a name="cfn-odb-cloudvmcluster-issparsediskgroupenabled"></a>
Specifies whether the VM cluster is configured with a sparse disk group.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseModel`  <a name="cfn-odb-cloudvmcluster-licensemodel"></a>
The Oracle license model applied to the VM cluster.
*Required*: No
*Type*: String
*Allowed values*: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemorySizeInGBs`  <a name="cfn-odb-cloudvmcluster-memorysizeingbs"></a>
The amount of memory, in gigabytes (GB), that's allocated for the VM cluster.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OdbNetworkId`  <a name="cfn-odb-cloudvmcluster-odbnetworkid"></a>
The unique identifier of the ODB network for the VM cluster.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: String
*Pattern*: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
*Minimum*: `6`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScanListenerPortTcp`  <a name="cfn-odb-cloudvmcluster-scanlistenerporttcp"></a>
The port number for TCP connections to the single client access name (SCAN) listener.
Valid values: `1024–8999` with the following exceptions: `2484`, `6100`, `6200`, `7060`, `7070`, `7085`, and `7879`
Default: `1521`
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `8999`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SshPublicKeys`  <a name="cfn-odb-cloudvmcluster-sshpublickeys"></a>
The public key portion of one or more key pairs used for SSH access to the VM cluster.
Required when creating a VM cluster.
*Required*: Conditional
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SystemVersion`  <a name="cfn-odb-cloudvmcluster-systemversion"></a>
The operating system version of the image chosen for the VM cluster.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-odb-cloudvmcluster-tags"></a>
Tags to assign to the Vm Cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-odb-cloudvmcluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-odb-cloudvmcluster-timezone"></a>
The time zone of the VM cluster.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-odb-cloudvmcluster-return-values"></a>

### Ref
<a name="aws-resource-odb-cloudvmcluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the VM cluster. For example:

 `{ "Ref": "myVmCluster" }`

For the VM cluster `myVmCluster`, `Ref` returns the unique identifier of the VM cluster.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-odb-cloudvmcluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-odb-cloudvmcluster-return-values-fn--getatt-fn--getatt"></a>

`CloudVmClusterArn`  <a name="CloudVmClusterArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the VM cluster.

`CloudVmClusterId`  <a name="CloudVmClusterId-fn::getatt"></a>
The unique identifier of the VM cluster.

`ComputeModel`  <a name="ComputeModel-fn::getatt"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.

`DiskRedundancy`  <a name="DiskRedundancy-fn::getatt"></a>
The type of redundancy configured for the VM cluster. `NORMAL` is 2-way redundancy. `HIGH` is 3-way redundancy.

`Domain`  <a name="Domain-fn::getatt"></a>
The domain of the VM cluster.

`ListenerPort`  <a name="ListenerPort-fn::getatt"></a>
The port number configured for the listener on the VM cluster.

`NodeCount`  <a name="NodeCount-fn::getatt"></a>
The number of nodes in the VM cluster.

`Ocid`  <a name="Ocid-fn::getatt"></a>
The OCID of the VM cluster.

`OciResourceAnchorName`  <a name="OciResourceAnchorName-fn::getatt"></a>
The name of the OCI resource anchor for the VM cluster.

`OciUrl`  <a name="OciUrl-fn::getatt"></a>
The HTTPS link to the VM cluster in OCI.

`ScanDnsName`  <a name="ScanDnsName-fn::getatt"></a>
The FQDN of the DNS record for the Single Client Access Name (SCAN) IP addresses that are associated with the VM cluster.

`ScanIpIds`  <a name="ScanIpIds-fn::getatt"></a>
The OCID of the SCAN IP addresses that are associated with the VM cluster.

`Shape`  <a name="Shape-fn::getatt"></a>
The hardware model name of the Exadata infrastructure that's running the VM cluster.

`StorageSizeInGBs`  <a name="StorageSizeInGBs-fn::getatt"></a>
The amount of local node storage, in gigabytes (GB), that's allocated to the VM cluster.

`VipIds`  <a name="VipIds-fn::getatt"></a>
The virtual IP (VIP) addresses that are associated with the VM cluster. Oracle's Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the VM cluster to enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.
