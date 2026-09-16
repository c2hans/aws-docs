---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-task-ephemeralstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Task EphemeralStorageConfiguration
<a name="aws-properties-iotsitewise-task-ephemeralstorageconfiguration"></a>

<a name="aws-properties-iotsitewise-task-ephemeralstorageconfiguration-description"></a>The `EphemeralStorageConfiguration` property type specifies Property description not available. for an [AWS::IoTSiteWise::Task](aws-resource-iotsitewise-task.md).

## Syntax
<a name="aws-properties-iotsitewise-task-ephemeralstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-task-ephemeralstorageconfiguration-syntax.json"></a>

```
{
  "[StorageClass](#cfn-iotsitewise-task-ephemeralstorageconfiguration-storageclass)" : {{String}},
  "[StorageSizeInGiB](#cfn-iotsitewise-task-ephemeralstorageconfiguration-storagesizeingib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iotsitewise-task-ephemeralstorageconfiguration-syntax.yaml"></a>

```
  [StorageClass](#cfn-iotsitewise-task-ephemeralstorageconfiguration-storageclass): {{String}}
  [StorageSizeInGiB](#cfn-iotsitewise-task-ephemeralstorageconfiguration-storagesizeingib): {{Integer}}
```

## Properties
<a name="aws-properties-iotsitewise-task-ephemeralstorageconfiguration-properties"></a>

`StorageClass`  <a name="cfn-iotsitewise-task-ephemeralstorageconfiguration-storageclass"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `STANDARD_1 | STANDARD_2 | THROUGHPUT_1 | THROUGHPUT_2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageSizeInGiB`  <a name="cfn-iotsitewise-task-ephemeralstorageconfiguration-storagesizeingib"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
