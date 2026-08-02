---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-odb-cloudexadatainfrastructure.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudExadataInfrastructure
<a name="aws-resource-odb-cloudexadatainfrastructure"></a>

The `AWS::ODB::CloudExadataInfrastructure` resource creates an Exadata infrastructure. An Exadata infrastructure provides the underlying compute and storage resources for Oracle Database workloads.

## Syntax
<a name="aws-resource-odb-cloudexadatainfrastructure-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-odb-cloudexadatainfrastructure-syntax.json"></a>

```
{
  "Type" : "AWS::ODB::CloudExadataInfrastructure",
  "Properties" : {
      "[AvailabilityZone](#cfn-odb-cloudexadatainfrastructure-availabilityzone)" : {{String}},
      "[AvailabilityZoneId](#cfn-odb-cloudexadatainfrastructure-availabilityzoneid)" : {{String}},
      "[ComputeCount](#cfn-odb-cloudexadatainfrastructure-computecount)" : {{Integer}},
      "[CustomerContactsToSendToOCI](#cfn-odb-cloudexadatainfrastructure-customercontactstosendtooci)" : {{[ CustomerContact, ... ]}},
      "[DatabaseServerType](#cfn-odb-cloudexadatainfrastructure-databaseservertype)" : {{String}},
      "[DisplayName](#cfn-odb-cloudexadatainfrastructure-displayname)" : {{String}},
      "[MaintenanceWindow](#cfn-odb-cloudexadatainfrastructure-maintenancewindow)" : {{MaintenanceWindow}},
      "[Shape](#cfn-odb-cloudexadatainfrastructure-shape)" : {{String}},
      "[StorageCount](#cfn-odb-cloudexadatainfrastructure-storagecount)" : {{Integer}},
      "[StorageServerType](#cfn-odb-cloudexadatainfrastructure-storageservertype)" : {{String}},
      "[Tags](#cfn-odb-cloudexadatainfrastructure-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-odb-cloudexadatainfrastructure-syntax.yaml"></a>

```
Type: AWS::ODB::CloudExadataInfrastructure
Properties:
  [AvailabilityZone](#cfn-odb-cloudexadatainfrastructure-availabilityzone): {{String}}
  [AvailabilityZoneId](#cfn-odb-cloudexadatainfrastructure-availabilityzoneid): {{String}}
  [ComputeCount](#cfn-odb-cloudexadatainfrastructure-computecount): {{Integer}}
  [CustomerContactsToSendToOCI](#cfn-odb-cloudexadatainfrastructure-customercontactstosendtooci): {{
    - CustomerContact}}
  [DatabaseServerType](#cfn-odb-cloudexadatainfrastructure-databaseservertype): {{String}}
  [DisplayName](#cfn-odb-cloudexadatainfrastructure-displayname): {{String}}
  [MaintenanceWindow](#cfn-odb-cloudexadatainfrastructure-maintenancewindow): {{
    MaintenanceWindow}}
  [Shape](#cfn-odb-cloudexadatainfrastructure-shape): {{String}}
  [StorageCount](#cfn-odb-cloudexadatainfrastructure-storagecount): {{Integer}}
  [StorageServerType](#cfn-odb-cloudexadatainfrastructure-storageservertype): {{String}}
  [Tags](#cfn-odb-cloudexadatainfrastructure-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-odb-cloudexadatainfrastructure-properties"></a>

`AvailabilityZone`  <a name="cfn-odb-cloudexadatainfrastructure-availabilityzone"></a>
The name of the Availability Zone (AZ) where the Exadata infrastructure is located.
Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZoneId`  <a name="cfn-odb-cloudexadatainfrastructure-availabilityzoneid"></a>
The AZ ID of the AZ where the Exadata infrastructure is located.
Required when creating an Exadata infrastructure. Specify either AvailabilityZone or AvailabilityZoneId to define the location of the infrastructure.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ComputeCount`  <a name="cfn-odb-cloudexadatainfrastructure-computecount"></a>
The number of database servers for the Exadata infrastructure.
Required when creating an Exadata infrastructure.
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CustomerContactsToSendToOCI`  <a name="cfn-odb-cloudexadatainfrastructure-customercontactstosendtooci"></a>
The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.
*Required*: No
*Type*: Array of [CustomerContact](aws-properties-odb-cloudexadatainfrastructure-customercontact.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseServerType`  <a name="cfn-odb-cloudexadatainfrastructure-databaseservertype"></a>
The database server model type of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\/.=-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DisplayName`  <a name="cfn-odb-cloudexadatainfrastructure-displayname"></a>
The user-friendly name for the Exadata infrastructure.
Required when creating an Exadata infrastructure.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceWindow`  <a name="cfn-odb-cloudexadatainfrastructure-maintenancewindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
*Required*: No
*Type*: [MaintenanceWindow](aws-properties-odb-cloudexadatainfrastructure-maintenancewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Shape`  <a name="cfn-odb-cloudexadatainfrastructure-shape"></a>
The model name of the Exadata infrastructure.
Required when creating an Exadata infrastructure.
*Required*: Conditional
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\/.=-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageCount`  <a name="cfn-odb-cloudexadatainfrastructure-storagecount"></a>
The number of storage servers that are activated for the Exadata infrastructure.
Required when creating an Exadata infrastructure.
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageServerType`  <a name="cfn-odb-cloudexadatainfrastructure-storageservertype"></a>
The storage server model type of the Exadata infrastructure. For the list of valid model names, use the `ListDbSystemShapes` operation.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\/.=-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-odb-cloudexadatainfrastructure-tags"></a>
Tags to assign to the Exadata Infrastructure.
*Required*: No
*Type*: Array of [Tag](aws-properties-odb-cloudexadatainfrastructure-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-odb-cloudexadatainfrastructure-return-values"></a>

### Ref
<a name="aws-resource-odb-cloudexadatainfrastructure-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the unique identifier of the Exadata infrastructure. For example:

 `{ "Ref": "myExadataInfrastructure" }`

For the Exadata infrastructure `myExadataInfrastructure`, `Ref` returns the unique identifier of the Exadata infrastructure.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-odb-cloudexadatainfrastructure-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-odb-cloudexadatainfrastructure-return-values-fn--getatt-fn--getatt"></a>

`ActivatedStorageCount`  <a name="ActivatedStorageCount-fn::getatt"></a>
The number of storage servers requested for the Exadata infrastructure.

`AdditionalStorageCount`  <a name="AdditionalStorageCount-fn::getatt"></a>
The number of storage servers requested for the Exadata infrastructure.

`AvailableStorageSizeInGBs`  <a name="AvailableStorageSizeInGBs-fn::getatt"></a>
The amount of available storage, in gigabytes (GB), for the Exadata infrastructure.

`CloudExadataInfrastructureArn`  <a name="CloudExadataInfrastructureArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the Exadata infrastructure.

`CloudExadataInfrastructureId`  <a name="CloudExadataInfrastructureId-fn::getatt"></a>
The unique identifier for the Exadata infrastructure.

`ComputeModel`  <a name="ComputeModel-fn::getatt"></a>
The OCI model compute model used when you create or clone an instance: ECPU or OCPU. An ECPU is an abstracted measure of compute resources. ECPUs are based on the number of cores elastically allocated from a pool of compute and storage servers. An OCPU is a legacy physical measure of compute resources. OCPUs are based on the physical core of a processor with hyper-threading enabled.

`CpuCount`  <a name="CpuCount-fn::getatt"></a>
The total number of CPU cores that are allocated to the Exadata infrastructure.

`DataStorageSizeInTBs`  <a name="DataStorageSizeInTBs-fn::getatt"></a>
The size of the Exadata infrastructure's data disk group, in terabytes (TB).

`DbNodeStorageSizeInGBs`  <a name="DbNodeStorageSizeInGBs-fn::getatt"></a>
The size of the Exadata infrastructure's local node storage, in gigabytes (GB).

`DbServerIds`  <a name="DbServerIds-fn::getatt"></a>
The list of database server identifiers for the Exadata infrastructure.

`DbServerVersion`  <a name="DbServerVersion-fn::getatt"></a>
The software version of the database servers (dom0) in the Exadata infrastructure.

`MaxCpuCount`  <a name="MaxCpuCount-fn::getatt"></a>
The total number of CPU cores available on the Exadata infrastructure.

`MaxDataStorageInTBs`  <a name="MaxDataStorageInTBs-fn::getatt"></a>
The total amount of data disk group storage, in terabytes (TB), that's available on the Exadata infrastructure.

`MaxDbNodeStorageSizeInGBs`  <a name="MaxDbNodeStorageSizeInGBs-fn::getatt"></a>
The total amount of local node storage, in gigabytes (GB), that's available on the Exadata infrastructure.

`MaxMemoryInGBs`  <a name="MaxMemoryInGBs-fn::getatt"></a>
The total amount of memory, in gigabytes (GB), that's available on the Exadata infrastructure.

`MemorySizeInGBs`  <a name="MemorySizeInGBs-fn::getatt"></a>
The amount of memory, in gigabytes (GB), that's allocated on the Exadata infrastructure.

`Ocid`  <a name="Ocid-fn::getatt"></a>
The OCID of the Exadata infrastructure.

`OciResourceAnchorName`  <a name="OciResourceAnchorName-fn::getatt"></a>
The name of the OCI resource anchor for the Exadata infrastructure.

`OciUrl`  <a name="OciUrl-fn::getatt"></a>
The HTTPS link to the Exadata infrastructure in OCI.

`StorageServerVersion`  <a name="StorageServerVersion-fn::getatt"></a>
The software version of the storage servers on the Exadata infrastructure.

`TotalStorageSizeInGBs`  <a name="TotalStorageSizeInGBs-fn::getatt"></a>
The total amount of storage, in gigabytes (GB), on the the Exadata infrastructure.
