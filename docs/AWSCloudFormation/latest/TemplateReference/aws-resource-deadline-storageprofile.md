---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-deadline-storageprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::StorageProfile
<a name="aws-resource-deadline-storageprofile"></a>

Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.

## Syntax
<a name="aws-resource-deadline-storageprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-deadline-storageprofile-syntax.json"></a>

```
{
  "Type" : "AWS::Deadline::StorageProfile",
  "Properties" : {
      "[DisplayName](#cfn-deadline-storageprofile-displayname)" : {{String}},
      "[FarmId](#cfn-deadline-storageprofile-farmid)" : {{String}},
      "[FileSystemLocations](#cfn-deadline-storageprofile-filesystemlocations)" : {{[ FileSystemLocation, ... ]}},
      "[OsFamily](#cfn-deadline-storageprofile-osfamily)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-deadline-storageprofile-syntax.yaml"></a>

```
Type: AWS::Deadline::StorageProfile
Properties:
  [DisplayName](#cfn-deadline-storageprofile-displayname): {{String}}
  [FarmId](#cfn-deadline-storageprofile-farmid): {{String}}
  [FileSystemLocations](#cfn-deadline-storageprofile-filesystemlocations): {{
    - FileSystemLocation}}
  [OsFamily](#cfn-deadline-storageprofile-osfamily): {{String}}
```

## Properties
<a name="aws-resource-deadline-storageprofile-properties"></a>

`DisplayName`  <a name="cfn-deadline-storageprofile-displayname"></a>
The display name of the storage profile summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FarmId`  <a name="cfn-deadline-storageprofile-farmid"></a>
The unique identifier of the farm that contains the storage profile.
*Required*: Yes
*Type*: String
*Pattern*: `^farm-[0-9a-f]{32}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemLocations`  <a name="cfn-deadline-storageprofile-filesystemlocations"></a>
Operating system specific file system path to the storage location.
*Required*: No
*Type*: Array of [FileSystemLocation](aws-properties-deadline-storageprofile-filesystemlocation.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OsFamily`  <a name="cfn-deadline-storageprofile-osfamily"></a>
The operating system (OS) family.
*Required*: Yes
*Type*: String
*Allowed values*: `WINDOWS | LINUX | MACOS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-deadline-storageprofile-return-values"></a>

### Ref
<a name="aws-resource-deadline-storageprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the storage profile.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-deadline-storageprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-deadline-storageprofile-return-values-fn--getatt-fn--getatt"></a>

`StorageProfileId`  <a name="StorageProfileId-fn::getatt"></a>
The storage profile ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
