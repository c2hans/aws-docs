---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-storageprofile-filesystemlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::StorageProfile FileSystemLocation
<a name="aws-properties-deadline-storageprofile-filesystemlocation"></a>

The details of the file system location for the resource.

## Syntax
<a name="aws-properties-deadline-storageprofile-filesystemlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-storageprofile-filesystemlocation-syntax.json"></a>

```
{
  "[Name](#cfn-deadline-storageprofile-filesystemlocation-name)" : {{String}},
  "[Path](#cfn-deadline-storageprofile-filesystemlocation-path)" : {{String}},
  "[Type](#cfn-deadline-storageprofile-filesystemlocation-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-storageprofile-filesystemlocation-syntax.yaml"></a>

```
  [Name](#cfn-deadline-storageprofile-filesystemlocation-name): {{String}}
  [Path](#cfn-deadline-storageprofile-filesystemlocation-path): {{String}}
  [Type](#cfn-deadline-storageprofile-filesystemlocation-type): {{String}}
```

## Properties
<a name="aws-properties-deadline-storageprofile-filesystemlocation-properties"></a>

`Name`  <a name="cfn-deadline-storageprofile-filesystemlocation-name"></a>
The location name.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z ]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-deadline-storageprofile-filesystemlocation-path"></a>
The file path.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-deadline-storageprofile-filesystemlocation-type"></a>
The type of file.
*Required*: Yes
*Type*: String
*Allowed values*: `SHARED | LOCAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
