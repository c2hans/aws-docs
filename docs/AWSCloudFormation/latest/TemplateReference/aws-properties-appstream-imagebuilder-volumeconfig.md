---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-imagebuilder-volumeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::ImageBuilder VolumeConfig
<a name="aws-properties-appstream-imagebuilder-volumeconfig"></a>

Configuration for the root volume of fleet instances and image builders. This allows you to customize the storage capacity beyond the default 200 GB.

## Syntax
<a name="aws-properties-appstream-imagebuilder-volumeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-imagebuilder-volumeconfig-syntax.json"></a>

```
{
  "[VolumeSizeInGb](#cfn-appstream-imagebuilder-volumeconfig-volumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appstream-imagebuilder-volumeconfig-syntax.yaml"></a>

```
  [VolumeSizeInGb](#cfn-appstream-imagebuilder-volumeconfig-volumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-appstream-imagebuilder-volumeconfig-properties"></a>

`VolumeSizeInGb`  <a name="cfn-appstream-imagebuilder-volumeconfig-volumesizeingb"></a>
The size of the root volume in GB. Valid range is 200-500 GB. The default is 200 GB, which is included in the hourly instance rate. Additional storage beyond 200 GB incurs extra charges and applies to instances regardless of their running state.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
