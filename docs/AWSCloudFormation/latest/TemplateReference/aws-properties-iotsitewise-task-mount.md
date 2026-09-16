---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-task-mount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Task Mount
<a name="aws-properties-iotsitewise-task-mount"></a>

<a name="aws-properties-iotsitewise-task-mount-description"></a>The `Mount` property type specifies Property description not available. for an [AWS::IoTSiteWise::Task](aws-resource-iotsitewise-task.md).

## Syntax
<a name="aws-properties-iotsitewise-task-mount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-task-mount-syntax.json"></a>

```
{
  "[Name](#cfn-iotsitewise-task-mount-name)" : {{String}},
  "[RelativePath](#cfn-iotsitewise-task-mount-relativepath)" : {{String}},
  "[Source](#cfn-iotsitewise-task-mount-source)" : {{MountSource}},
  "[StorageType](#cfn-iotsitewise-task-mount-storagetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-task-mount-syntax.yaml"></a>

```
  [Name](#cfn-iotsitewise-task-mount-name): {{String}}
  [RelativePath](#cfn-iotsitewise-task-mount-relativepath): {{String}}
  [Source](#cfn-iotsitewise-task-mount-source): {{
    MountSource}}
  [StorageType](#cfn-iotsitewise-task-mount-storagetype): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-task-mount-properties"></a>

`Name`  <a name="cfn-iotsitewise-task-mount-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelativePath`  <a name="cfn-iotsitewise-task-mount-relativepath"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^((?!.*(^|/)\.\.?(/|$))(?!.*//)[a-zA-Z0-9._-][a-zA-Z0-9._/-]*[a-zA-Z0-9._-]|[a-zA-Z0-9_-])$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-iotsitewise-task-mount-source"></a>
Property description not available.
*Required*: Yes
*Type*: [MountSource](aws-properties-iotsitewise-task-mountsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageType`  <a name="cfn-iotsitewise-task-mount-storagetype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `SHARED_STORAGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
