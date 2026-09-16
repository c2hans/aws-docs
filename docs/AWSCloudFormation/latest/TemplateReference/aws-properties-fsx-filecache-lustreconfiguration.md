---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filecache-lustreconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileCache LustreConfiguration
<a name="aws-properties-fsx-filecache-lustreconfiguration"></a>

<a name="aws-properties-fsx-filecache-lustreconfiguration-description"></a>The `LustreConfiguration` property type specifies Property description not available. for an [AWS::FSx::FileCache](aws-resource-fsx-filecache.md).

## Syntax
<a name="aws-properties-fsx-filecache-lustreconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filecache-lustreconfiguration-syntax.json"></a>

```
{
  "[DeploymentType](#cfn-fsx-filecache-lustreconfiguration-deploymenttype)" : {{String}},
  "[LogConfiguration](#cfn-fsx-filecache-lustreconfiguration-logconfiguration)" : {{LogConfiguration}},
  "[MetadataConfiguration](#cfn-fsx-filecache-lustreconfiguration-metadataconfiguration)" : {{MetadataConfiguration}},
  "[MountName](#cfn-fsx-filecache-lustreconfiguration-mountname)" : {{String}},
  "[PerUnitStorageThroughput](#cfn-fsx-filecache-lustreconfiguration-perunitstoragethroughput)" : {{Integer}},
  "[WeeklyMaintenanceStartTime](#cfn-fsx-filecache-lustreconfiguration-weeklymaintenancestarttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filecache-lustreconfiguration-syntax.yaml"></a>

```
  [DeploymentType](#cfn-fsx-filecache-lustreconfiguration-deploymenttype): {{String}}
  [LogConfiguration](#cfn-fsx-filecache-lustreconfiguration-logconfiguration): {{
    LogConfiguration}}
  [MetadataConfiguration](#cfn-fsx-filecache-lustreconfiguration-metadataconfiguration): {{
    MetadataConfiguration}}
  [MountName](#cfn-fsx-filecache-lustreconfiguration-mountname): {{String}}
  [PerUnitStorageThroughput](#cfn-fsx-filecache-lustreconfiguration-perunitstoragethroughput): {{Integer}}
  [WeeklyMaintenanceStartTime](#cfn-fsx-filecache-lustreconfiguration-weeklymaintenancestarttime): {{String}}
```

## Properties
<a name="aws-properties-fsx-filecache-lustreconfiguration-properties"></a>

`DeploymentType`  <a name="cfn-fsx-filecache-lustreconfiguration-deploymenttype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `CACHE_1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogConfiguration`  <a name="cfn-fsx-filecache-lustreconfiguration-logconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [LogConfiguration](aws-properties-fsx-filecache-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataConfiguration`  <a name="cfn-fsx-filecache-lustreconfiguration-metadataconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [MetadataConfiguration](aws-properties-fsx-filecache-metadataconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MountName`  <a name="cfn-fsx-filecache-lustreconfiguration-mountname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^([A-Za-z0-9_-]{1,8})$`
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PerUnitStorageThroughput`  <a name="cfn-fsx-filecache-lustreconfiguration-perunitstoragethroughput"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `12`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WeeklyMaintenanceStartTime`  <a name="cfn-fsx-filecache-lustreconfiguration-weeklymaintenancestarttime"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`
*Minimum*: `7`
*Maximum*: `7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
