---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbinstance-additionalstoragevolume.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBInstance AdditionalStorageVolume
<a name="aws-properties-rds-dbinstance-additionalstoragevolume"></a>

Contains details about an additional storage volume for a DB instance. RDS support additional storage volumes for RDS for Oracle and RDS for SQL Server.

## Syntax
<a name="aws-properties-rds-dbinstance-additionalstoragevolume-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbinstance-additionalstoragevolume-syntax.json"></a>

```
{
  "[AllocatedStorage](#cfn-rds-dbinstance-additionalstoragevolume-allocatedstorage)" : {{String}},
  "[Iops](#cfn-rds-dbinstance-additionalstoragevolume-iops)" : {{Integer}},
  "[MaxAllocatedStorage](#cfn-rds-dbinstance-additionalstoragevolume-maxallocatedstorage)" : {{Integer}},
  "[StorageThroughput](#cfn-rds-dbinstance-additionalstoragevolume-storagethroughput)" : {{Integer}},
  "[StorageType](#cfn-rds-dbinstance-additionalstoragevolume-storagetype)" : {{String}},
  "[VolumeName](#cfn-rds-dbinstance-additionalstoragevolume-volumename)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-dbinstance-additionalstoragevolume-syntax.yaml"></a>

```
  [AllocatedStorage](#cfn-rds-dbinstance-additionalstoragevolume-allocatedstorage): {{String}}
  [Iops](#cfn-rds-dbinstance-additionalstoragevolume-iops): {{Integer}}
  [MaxAllocatedStorage](#cfn-rds-dbinstance-additionalstoragevolume-maxallocatedstorage): {{Integer}}
  [StorageThroughput](#cfn-rds-dbinstance-additionalstoragevolume-storagethroughput): {{Integer}}
  [StorageType](#cfn-rds-dbinstance-additionalstoragevolume-storagetype): {{String}}
  [VolumeName](#cfn-rds-dbinstance-additionalstoragevolume-volumename): {{String}}
```

## Properties
<a name="aws-properties-rds-dbinstance-additionalstoragevolume-properties"></a>

`AllocatedStorage`  <a name="cfn-rds-dbinstance-additionalstoragevolume-allocatedstorage"></a>
The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).
*Required*: No
*Type*: String
*Pattern*: `^[0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Iops`  <a name="cfn-rds-dbinstance-additionalstoragevolume-iops"></a>
The number of I/O operations per second (IOPS) provisioned for the additional storage volume.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxAllocatedStorage`  <a name="cfn-rds-dbinstance-additionalstoragevolume-maxallocatedstorage"></a>
The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageThroughput`  <a name="cfn-rds-dbinstance-additionalstoragevolume-storagethroughput"></a>
The storage throughput value for the additional storage volume, in mebibytes per second (MiBps). This setting applies only to the General Purpose SSD (`gp3`) storage type.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageType`  <a name="cfn-rds-dbinstance-additionalstoragevolume-storagetype"></a>
The storage type for the additional storage volume.
Valid Values: `GP3 | IO2`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeName`  <a name="cfn-rds-dbinstance-additionalstoragevolume-volumename"></a>
The name of the additional storage volume.
Valid Values: `RDSDBDATA2 | RDSDBDATA3 | RDSDBDATA4`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
