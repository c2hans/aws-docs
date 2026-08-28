---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-odb-cloudautonomousvmcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudAutonomousVmCluster
<a name="aws-resource-odb-cloudautonomousvmcluster"></a>

The `AWS::ODB::CloudAutonomousVmCluster` resource creates an Autonomous VM cluster. An Autonomous VM cluster provides the infrastructure for running Autonomous Databases.

## Syntax
<a name="aws-resource-odb-cloudautonomousvmcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-odb-cloudautonomousvmcluster-syntax.json"></a>

```
{
  "Type" : "AWS::ODB::CloudAutonomousVmCluster",
  "Properties" : {
      "[AutonomousDataStorageSizeInTBs](#cfn-odb-cloudautonomousvmcluster-autonomousdatastoragesizeintbs)" : {{Number}},
      "[CloudExadataInfrastructureId](#cfn-odb-cloudautonomousvmcluster-cloudexadatainfrastructureid)" : {{String}},
      "[CpuCoreCountPerNode](#cfn-odb-cloudautonomousvmcluster-cpucorecountpernode)" : {{Integer}},
      "[DbServers](#cfn-odb-cloudautonomousvmcluster-dbservers)" : {{[ String, ... ]}},
      "[Description](#cfn-odb-cloudautonomousvmcluster-description)" : {{String}},
      "[DisplayName](#cfn-odb-cloudautonomousvmcluster-displayname)" : {{String}},
      "[IamRoles](#cfn-odb-cloudautonomousvmcluster-iamroles)" : {{[ IamRole, ... ]}},
      "[IsMtlsEnabledVmCluster](#cfn-odb-cloudautonomousvmcluster-ismtlsenabledvmcluster)" : {{Boolean}},
      "[LicenseModel](#cfn-odb-cloudautonomousvmcluster-licensemodel)" : {{String}},
      "[MaintenanceWindow](#cfn-odb-cloudautonomousvmcluster-maintenancewindow)" : {{MaintenanceWindow}},
      "[MemoryPerOracleComputeUnitInGBs](#cfn-odb-cloudautonomousvmcluster-memoryperoraclecomputeunitingbs)" : {{Integer}},
      "[OdbNetworkId](#cfn-odb-cloudautonomousvmcluster-odbnetworkid)" : {{String}},
      "[ScanListenerPortNonTls](#cfn-odb-cloudautonomousvmcluster-scanlistenerportnontls)" : {{Integer}},
      "[ScanListenerPortTls](#cfn-odb-cloudautonomousvmcluster-scanlistenerporttls)" : {{Integer}},
      "[Tags](#cfn-odb-cloudautonomousvmcluster-tags)" : {{[ Tag, ... ]}},
      "[TimeZone](#cfn-odb-cloudautonomousvmcluster-timezone)" : {{String}},
      "[TotalContainerDatabases](#cfn-odb-cloudautonomousvmcluster-totalcontainerdatabases)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-odb-cloudautonomousvmcluster-syntax.yaml"></a>

```
Type: AWS::ODB::CloudAutonomousVmCluster
Properties:
  [AutonomousDataStorageSizeInTBs](#cfn-odb-cloudautonomousvmcluster-autonomousdatastoragesizeintbs): {{Number}}
  [CloudExadataInfrastructureId](#cfn-odb-cloudautonomousvmcluster-cloudexadatainfrastructureid): {{String}}
  [CpuCoreCountPerNode](#cfn-odb-cloudautonomousvmcluster-cpucorecountpernode): {{Integer}}
  [DbServers](#cfn-odb-cloudautonomousvmcluster-dbservers): {{
    - String}}
  [Description](#cfn-odb-cloudautonomousvmcluster-description): {{String}}
  [DisplayName](#cfn-odb-cloudautonomousvmcluster-displayname): {{String}}
  [IamRoles](#cfn-odb-cloudautonomousvmcluster-iamroles): {{
    - IamRole}}
  [IsMtlsEnabledVmCluster](#cfn-odb-cloudautonomousvmcluster-ismtlsenabledvmcluster): {{Boolean}}
  [LicenseModel](#cfn-odb-cloudautonomousvmcluster-licensemodel): {{String}}
  [MaintenanceWindow](#cfn-odb-cloudautonomousvmcluster-maintenancewindow): {{
    MaintenanceWindow}}
  [MemoryPerOracleComputeUnitInGBs](#cfn-odb-cloudautonomousvmcluster-memoryperoraclecomputeunitingbs): {{Integer}}
  [OdbNetworkId](#cfn-odb-cloudautonomousvmcluster-odbnetworkid): {{String}}
  [ScanListenerPortNonTls](#cfn-odb-cloudautonomousvmcluster-scanlistenerportnontls): {{Integer}}
  [ScanListenerPortTls](#cfn-odb-cloudautonomousvmcluster-scanlistenerporttls): {{Integer}}
  [Tags](#cfn-odb-cloudautonomousvmcluster-tags): {{
    - Tag}}
  [TimeZone](#cfn-odb-cloudautonomousvmcluster-timezone): {{String}}
  [TotalContainerDatabases](#cfn-odb-cloudautonomousvmcluster-totalcontainerdatabases): {{Integer}}
```

## Properties
<a name="aws-resource-odb-cloudautonomousvmcluster-properties"></a>

`AutonomousDataStorageSizeInTBs`  <a name="cfn-odb-cloudautonomousvmcluster-autonomousdatastoragesizeintbs"></a>
The data storage size allocated for Autonomous Databases in the Autonomous VM cluster, in TB.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CloudExadataInfrastructureId`  <a name="cfn-odb-cloudautonomousvmcluster-cloudexadatainfrastructureid"></a>
The unique identifier of the Cloud Exadata Infrastructure containing this Autonomous VM cluster.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: String
*Pattern*: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
*Minimum*: `6`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CpuCoreCountPerNode`  <a name="cfn-odb-cloudautonomousvmcluster-cpucorecountpernode"></a>
The number of CPU cores enabled per node in the Autonomous VM cluster.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DbServers`  <a name="cfn-odb-cloudautonomousvmcluster-dbservers"></a>
The list of database servers associated with the Autonomous VM cluster.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-odb-cloudautonomousvmcluster-description"></a>
The user-provided description of the Autonomous VM cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisplayName`  <a name="cfn-odb-cloudautonomousvmcluster-displayname"></a>
The display name of the Autonomous VM cluster.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IamRoles`  <a name="cfn-odb-cloudautonomousvmcluster-iamroles"></a>
The AWS Identity and Access Management (IAM) service roles associated with the Autonomous VM cluster.
*Required*: No
*Type*: Array of [IamRole](aws-properties-odb-cloudautonomousvmcluster-iamrole.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsMtlsEnabledVmCluster`  <a name="cfn-odb-cloudautonomousvmcluster-ismtlsenabledvmcluster"></a>
Specifies whether mutual TLS (mTLS) authentication is enabled for the Autonomous VM cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseModel`  <a name="cfn-odb-cloudautonomousvmcluster-licensemodel"></a>
The Oracle license model that applies to the Autonomous VM cluster. Valid values are `LICENSE_INCLUDED` or `BRING_YOUR_OWN_LICENSE`.
*Required*: No
*Type*: String
*Allowed values*: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceWindow`  <a name="cfn-odb-cloudautonomousvmcluster-maintenancewindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
*Required*: No
*Type*: [MaintenanceWindow](aws-properties-odb-cloudautonomousvmcluster-maintenancewindow.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MemoryPerOracleComputeUnitInGBs`  <a name="cfn-odb-cloudautonomousvmcluster-memoryperoraclecomputeunitingbs"></a>
The amount of memory allocated per Oracle Compute Unit, in GB.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OdbNetworkId`  <a name="cfn-odb-cloudautonomousvmcluster-odbnetworkid"></a>
The unique identifier of the ODB network associated with this Autonomous VM cluster.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: String
*Pattern*: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
*Minimum*: `6`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScanListenerPortNonTls`  <a name="cfn-odb-cloudautonomousvmcluster-scanlistenerportnontls"></a>
The SCAN listener port for non-TLS (TCP) protocol. The default is 1521.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `8999`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScanListenerPortTls`  <a name="cfn-odb-cloudautonomousvmcluster-scanlistenerporttls"></a>
The SCAN listener port for TLS (TCP) protocol. The default is 2484.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `8999`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-odb-cloudautonomousvmcluster-tags"></a>
Tags to assign to the Autonomous Vm Cluster.
*Required*: No
*Type*: Array of [Tag](aws-properties-odb-cloudautonomousvmcluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeZone`  <a name="cfn-odb-cloudautonomousvmcluster-timezone"></a>
The time zone of the Autonomous VM cluster.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TotalContainerDatabases`  <a name="cfn-odb-cloudautonomousvmcluster-totalcontainerdatabases"></a>
The total number of Autonomous Container Databases that can be created with the allocated local storage.
Required when creating an Autonomous VM cluster.
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-odb-cloudautonomousvmcluster-return-values"></a>

### Ref
<a name="aws-resource-odb-cloudautonomousvmcluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the Autonomous VM cluster. For example:

 `{ "Ref": "myAutonomousVmCluster" }`

For the Autonomous VM cluster `myAutonomousVmCluster`, `Ref` returns the unique identifier of the Autonomous VM cluster.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-odb-cloudautonomousvmcluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-odb-cloudautonomousvmcluster-return-values-fn--getatt-fn--getatt"></a>

`AutonomousDataStoragePercentage`  <a name="AutonomousDataStoragePercentage-fn::getatt"></a>
The percentage of data storage currently in use for Autonomous Databases in the Autonomous VM cluster.

`AvailableAutonomousDataStorageSizeInTBs`  <a name="AvailableAutonomousDataStorageSizeInTBs-fn::getatt"></a>
The available data storage space for Autonomous Databases in the Autonomous VM cluster, in TB.

`AvailableContainerDatabases`  <a name="AvailableContainerDatabases-fn::getatt"></a>
The number of Autonomous CDBs that you can create with the currently available storage.

`AvailableCpus`  <a name="AvailableCpus-fn::getatt"></a>
The number of CPU cores available for allocation to Autonomous Databases.

`CloudAutonomousVmClusterArn`  <a name="CloudAutonomousVmClusterArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the Autonomous VM cluster.

`CloudAutonomousVmClusterId`  <a name="CloudAutonomousVmClusterId-fn::getatt"></a>
The unique identifier of the Autonomous VM cluster.

`ComputeModel`  <a name="ComputeModel-fn::getatt"></a>
The compute model of the Autonomous VM cluster: ECPU or OCPU.

`CpuCoreCount`  <a name="CpuCoreCount-fn::getatt"></a>
The total number of CPU cores in the Autonomous VM cluster.

`CpuPercentage`  <a name="CpuPercentage-fn::getatt"></a>
The percentage of total CPU cores currently in use in the Autonomous VM cluster.

`DataStorageSizeInGBs`  <a name="DataStorageSizeInGBs-fn::getatt"></a>
The total data storage allocated to the Autonomous VM cluster, in GB.

`DataStorageSizeInTBs`  <a name="DataStorageSizeInTBs-fn::getatt"></a>
The total data storage allocated to the Autonomous VM cluster, in TB.

`DbNodeStorageSizeInGBs`  <a name="DbNodeStorageSizeInGBs-fn::getatt"></a>
The local node storage allocated to the Autonomous VM cluster, in gigabytes (GB).

`Domain`  <a name="Domain-fn::getatt"></a>
The domain name for the Autonomous VM cluster.

`ExadataStorageInTBsLowestScaledValue`  <a name="ExadataStorageInTBsLowestScaledValue-fn::getatt"></a>
The minimum value to which you can scale down the Exadata storage, in TB.

`Hostname`  <a name="Hostname-fn::getatt"></a>
The hostname for the Autonomous VM cluster.

`MaxAcdsLowestScaledValue`  <a name="MaxAcdsLowestScaledValue-fn::getatt"></a>
The minimum value to which you can scale down the maximum number of Autonomous CDBs.

`MemorySizeInGBs`  <a name="MemorySizeInGBs-fn::getatt"></a>
The total amount of memory allocated to the Autonomous VM cluster, in gigabytes (GB).

`NodeCount`  <a name="NodeCount-fn::getatt"></a>
The number of database server nodes in the Autonomous VM cluster.

`NonProvisionableAutonomousContainerDatabases`  <a name="NonProvisionableAutonomousContainerDatabases-fn::getatt"></a>
The number of Autonomous CDBs that can't be provisioned because of resource constraints.

`Ocid`  <a name="Ocid-fn::getatt"></a>
The Oracle Cloud Identifier (OCID) of the Autonomous VM cluster.

`OciResourceAnchorName`  <a name="OciResourceAnchorName-fn::getatt"></a>
The name of the OCI resource anchor associated with this Autonomous VM cluster.

`OciUrl`  <a name="OciUrl-fn::getatt"></a>
The URL for accessing the OCI console page for this Autonomous VM cluster.

`ProvisionableAutonomousContainerDatabases`  <a name="ProvisionableAutonomousContainerDatabases-fn::getatt"></a>
The number of Autonomous CDBs that can be provisioned in the Autonomous VM cluster.

`ProvisionedAutonomousContainerDatabases`  <a name="ProvisionedAutonomousContainerDatabases-fn::getatt"></a>
The number of Autonomous CDBs currently provisioned in the Autonomous VM cluster.

`ProvisionedCpus`  <a name="ProvisionedCpus-fn::getatt"></a>
The number of CPU cores currently provisioned in the Autonomous VM cluster.

`ReclaimableCpus`  <a name="ReclaimableCpus-fn::getatt"></a>
The number of CPU cores that can be reclaimed from terminated or scaled-down Autonomous Databases.

`ReservedCpus`  <a name="ReservedCpus-fn::getatt"></a>
The number of CPU cores reserved for system operations and redundancy.

`Shape`  <a name="Shape-fn::getatt"></a>
The shape of the Exadata infrastructure for the Autonomous VM cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
