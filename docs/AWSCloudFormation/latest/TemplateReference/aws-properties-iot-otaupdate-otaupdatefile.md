---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-otaupdatefile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate OTAUpdateFile
<a name="aws-properties-iot-otaupdate-otaupdatefile"></a>

Describes a file to be associated with an OTA update.

## Syntax
<a name="aws-properties-iot-otaupdate-otaupdatefile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-otaupdatefile-syntax.json"></a>

```
{
  "[Attributes](#cfn-iot-otaupdate-otaupdatefile-attributes)" : {{{{{Key}}: {{Value}}, ...}}},
  "[CodeSigning](#cfn-iot-otaupdate-otaupdatefile-codesigning)" : {{CodeSigning}},
  "[FileLocation](#cfn-iot-otaupdate-otaupdatefile-filelocation)" : {{FileLocation}},
  "[FileName](#cfn-iot-otaupdate-otaupdatefile-filename)" : {{String}},
  "[FileType](#cfn-iot-otaupdate-otaupdatefile-filetype)" : {{Integer}},
  "[FileVersion](#cfn-iot-otaupdate-otaupdatefile-fileversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-otaupdatefile-syntax.yaml"></a>

```
  [Attributes](#cfn-iot-otaupdate-otaupdatefile-attributes): {{
    {{Key}}: {{Value}}}}
  [CodeSigning](#cfn-iot-otaupdate-otaupdatefile-codesigning): {{
    CodeSigning}}
  [FileLocation](#cfn-iot-otaupdate-otaupdatefile-filelocation): {{
    FileLocation}}
  [FileName](#cfn-iot-otaupdate-otaupdatefile-filename): {{String}}
  [FileType](#cfn-iot-otaupdate-otaupdatefile-filetype): {{Integer}}
  [FileVersion](#cfn-iot-otaupdate-otaupdatefile-fileversion): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-otaupdatefile-properties"></a>

`Attributes`  <a name="cfn-iot-otaupdate-otaupdatefile-attributes"></a>
A list of name-attribute pairs. They won't be sent to devices as a part of the Job document.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CodeSigning`  <a name="cfn-iot-otaupdate-otaupdatefile-codesigning"></a>
The code signing method of the file.
*Required*: No
*Type*: [CodeSigning](aws-properties-iot-otaupdate-codesigning.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileLocation`  <a name="cfn-iot-otaupdate-otaupdatefile-filelocation"></a>
The location of the updated firmware.
*Required*: No
*Type*: [FileLocation](aws-properties-iot-otaupdate-filelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileName`  <a name="cfn-iot-otaupdate-otaupdatefile-filename"></a>
The name of the file.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileType`  <a name="cfn-iot-otaupdate-otaupdatefile-filetype"></a>
An integer value you can include in the job document to allow your devices to identify the type of file received from the cloud.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileVersion`  <a name="cfn-iot-otaupdate-otaupdatefile-fileversion"></a>
The file version.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
