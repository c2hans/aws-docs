---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-manageds3backupaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork ManagedS3BackupAccess
<a name="aws-properties-odb-odbnetwork-manageds3backupaccess"></a>

The configuration for managed Amazon S3 backup access from the ODB network.

## Syntax
<a name="aws-properties-odb-odbnetwork-manageds3backupaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-manageds3backupaccess-syntax.json"></a>

```
{
  "[Ipv4Addresses](#cfn-odb-odbnetwork-manageds3backupaccess-ipv4addresses)" : {{[ String, ... ]}},
  "[Status](#cfn-odb-odbnetwork-manageds3backupaccess-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-manageds3backupaccess-syntax.yaml"></a>

```
  [Ipv4Addresses](#cfn-odb-odbnetwork-manageds3backupaccess-ipv4addresses): {{
    - String}}
  [Status](#cfn-odb-odbnetwork-manageds3backupaccess-status): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-manageds3backupaccess-properties"></a>

`Ipv4Addresses`  <a name="cfn-odb-odbnetwork-manageds3backupaccess-ipv4addresses"></a>
The IPv4 addresses for the managed Amazon S3 backup access.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-odb-odbnetwork-manageds3backupaccess-status"></a>
The status of the managed Amazon S3 backup access.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENABLING | DISABLED | DISABLING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
