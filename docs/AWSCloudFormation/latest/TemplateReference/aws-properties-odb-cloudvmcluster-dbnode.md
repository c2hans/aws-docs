---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-cloudvmcluster-dbnode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::CloudVmCluster DbNode
<a name="aws-properties-odb-cloudvmcluster-dbnode"></a>

Information about a DB node.

## Syntax
<a name="aws-properties-odb-cloudvmcluster-dbnode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-cloudvmcluster-dbnode-syntax.json"></a>

```
{
  "[BackupIpId](#cfn-odb-cloudvmcluster-dbnode-backupipid)" : {{String}},
  "[BackupVnic2Id](#cfn-odb-cloudvmcluster-dbnode-backupvnic2id)" : {{String}},
  "[CpuCoreCount](#cfn-odb-cloudvmcluster-dbnode-cpucorecount)" : {{Integer}},
  "[DbNodeArn](#cfn-odb-cloudvmcluster-dbnode-dbnodearn)" : {{String}},
  "[DbNodeId](#cfn-odb-cloudvmcluster-dbnode-dbnodeid)" : {{String}},
  "[DbNodeStorageSizeInGBs](#cfn-odb-cloudvmcluster-dbnode-dbnodestoragesizeingbs)" : {{Integer}},
  "[DbServerId](#cfn-odb-cloudvmcluster-dbnode-dbserverid)" : {{String}},
  "[DbSystemId](#cfn-odb-cloudvmcluster-dbnode-dbsystemid)" : {{String}},
  "[HostIpId](#cfn-odb-cloudvmcluster-dbnode-hostipid)" : {{String}},
  "[Hostname](#cfn-odb-cloudvmcluster-dbnode-hostname)" : {{String}},
  "[MemorySizeInGBs](#cfn-odb-cloudvmcluster-dbnode-memorysizeingbs)" : {{Integer}},
  "[Ocid](#cfn-odb-cloudvmcluster-dbnode-ocid)" : {{String}},
  "[Status](#cfn-odb-cloudvmcluster-dbnode-status)" : {{String}},
  "[Tags](#cfn-odb-cloudvmcluster-dbnode-tags)" : {{[ Tag, ... ]}},
  "[Vnic2Id](#cfn-odb-cloudvmcluster-dbnode-vnic2id)" : {{String}},
  "[VnicId](#cfn-odb-cloudvmcluster-dbnode-vnicid)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-cloudvmcluster-dbnode-syntax.yaml"></a>

```
  [BackupIpId](#cfn-odb-cloudvmcluster-dbnode-backupipid): {{String}}
  [BackupVnic2Id](#cfn-odb-cloudvmcluster-dbnode-backupvnic2id): {{String}}
  [CpuCoreCount](#cfn-odb-cloudvmcluster-dbnode-cpucorecount): {{Integer}}
  [DbNodeArn](#cfn-odb-cloudvmcluster-dbnode-dbnodearn): {{String}}
  [DbNodeId](#cfn-odb-cloudvmcluster-dbnode-dbnodeid): {{String}}
  [DbNodeStorageSizeInGBs](#cfn-odb-cloudvmcluster-dbnode-dbnodestoragesizeingbs): {{Integer}}
  [DbServerId](#cfn-odb-cloudvmcluster-dbnode-dbserverid): {{String}}
  [DbSystemId](#cfn-odb-cloudvmcluster-dbnode-dbsystemid): {{String}}
  [HostIpId](#cfn-odb-cloudvmcluster-dbnode-hostipid): {{String}}
  [Hostname](#cfn-odb-cloudvmcluster-dbnode-hostname): {{String}}
  [MemorySizeInGBs](#cfn-odb-cloudvmcluster-dbnode-memorysizeingbs): {{Integer}}
  [Ocid](#cfn-odb-cloudvmcluster-dbnode-ocid): {{String}}
  [Status](#cfn-odb-cloudvmcluster-dbnode-status): {{String}}
  [Tags](#cfn-odb-cloudvmcluster-dbnode-tags): {{
    - Tag}}
  [Vnic2Id](#cfn-odb-cloudvmcluster-dbnode-vnic2id): {{String}}
  [VnicId](#cfn-odb-cloudvmcluster-dbnode-vnicid): {{String}}
```

## Properties
<a name="aws-properties-odb-cloudvmcluster-dbnode-properties"></a>

`BackupIpId`  <a name="cfn-odb-cloudvmcluster-dbnode-backupipid"></a>
The Oracle Cloud ID (OCID) of the backup IP address that's associated with the DB node.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`BackupVnic2Id`  <a name="cfn-odb-cloudvmcluster-dbnode-backupvnic2id"></a>
The OCID of the second backup VNIC.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`CpuCoreCount`  <a name="cfn-odb-cloudvmcluster-dbnode-cpucorecount"></a>
Number of CPU cores enabled on the DB node.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DbNodeArn`  <a name="cfn-odb-cloudvmcluster-dbnode-dbnodearn"></a>
The Amazon Resource Name (ARN) of the DB node.
*Required*: No
*Type*: String
*Pattern*: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DbNodeId`  <a name="cfn-odb-cloudvmcluster-dbnode-dbnodeid"></a>
The unique identifier of the DB node.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_~.-]+`
*Minimum*: `6`
*Maximum*: `64`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DbNodeStorageSizeInGBs`  <a name="cfn-odb-cloudvmcluster-dbnode-dbnodestoragesizeingbs"></a>
The amount of local node storage, in gigabytes (GB), that's allocated on the DB node.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DbServerId`  <a name="cfn-odb-cloudvmcluster-dbnode-dbserverid"></a>
The unique identifier of the Db server that is associated with the DB node.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9_~.-]+`
*Minimum*: `6`
*Maximum*: `64`

`DbSystemId`  <a name="cfn-odb-cloudvmcluster-dbnode-dbsystemid"></a>
The OCID of the DB system.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`HostIpId`  <a name="cfn-odb-cloudvmcluster-dbnode-hostipid"></a>
The OCID of the host IP address that's associated with the DB node.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Hostname`  <a name="cfn-odb-cloudvmcluster-dbnode-hostname"></a>
The host name for the DB node.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`MemorySizeInGBs`  <a name="cfn-odb-cloudvmcluster-dbnode-memorysizeingbs"></a>
The allocated memory in GBs on the DB node.
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Ocid`  <a name="cfn-odb-cloudvmcluster-dbnode-ocid"></a>
The OCID of the DB node.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Status`  <a name="cfn-odb-cloudvmcluster-dbnode-status"></a>
The current status of the DB node.
*Required*: No
*Type*: String
*Allowed values*: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | STOPPING | STOPPED | STARTING`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Tags`  <a name="cfn-odb-cloudvmcluster-dbnode-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-odb-cloudvmcluster-tag.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Vnic2Id`  <a name="cfn-odb-cloudvmcluster-dbnode-vnic2id"></a>
The OCID of the second VNIC.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`VnicId`  <a name="cfn-odb-cloudvmcluster-dbnode-vnicid"></a>
The OCID of the VNIC.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
