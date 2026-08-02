---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-usersettings-imagemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::UserSettings ImageMetadata
<a name="aws-properties-workspacesweb-usersettings-imagemetadata"></a>

Metadata information about an uploaded image file.

## Syntax
<a name="aws-properties-workspacesweb-usersettings-imagemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-usersettings-imagemetadata-syntax.json"></a>

```
{
  "[FileExtension](#cfn-workspacesweb-usersettings-imagemetadata-fileextension)" : {{String}},
  "[LastUploadTimestamp](#cfn-workspacesweb-usersettings-imagemetadata-lastuploadtimestamp)" : {{String}},
  "[MimeType](#cfn-workspacesweb-usersettings-imagemetadata-mimetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesweb-usersettings-imagemetadata-syntax.yaml"></a>

```
  [FileExtension](#cfn-workspacesweb-usersettings-imagemetadata-fileextension): {{String}}
  [LastUploadTimestamp](#cfn-workspacesweb-usersettings-imagemetadata-lastuploadtimestamp): {{String}}
  [MimeType](#cfn-workspacesweb-usersettings-imagemetadata-mimetype): {{String}}
```

## Properties
<a name="aws-properties-workspacesweb-usersettings-imagemetadata-properties"></a>

`FileExtension`  <a name="cfn-workspacesweb-usersettings-imagemetadata-fileextension"></a>
The file extension of the image.
*Required*: Yes
*Type*: String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUploadTimestamp`  <a name="cfn-workspacesweb-usersettings-imagemetadata-lastuploadtimestamp"></a>
The timestamp when the image was last uploaded.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MimeType`  <a name="cfn-workspacesweb-usersettings-imagemetadata-mimetype"></a>
The MIME type of the image.
*Required*: Yes
*Type*: String
*Allowed values*: `image/png | image/jpeg | image/x-icon`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
