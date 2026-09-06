---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashprograminformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashProgramInformation
<a name="aws-properties-mediapackagev2-originendpoint-dashprograminformation"></a>

Details about the content that you want MediaPackage to pass through in the manifest to the playback device.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashprograminformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashprograminformation-syntax.json"></a>

```
{
  "[Copyright](#cfn-mediapackagev2-originendpoint-dashprograminformation-copyright)" : {{String}},
  "[LanguageCode](#cfn-mediapackagev2-originendpoint-dashprograminformation-languagecode)" : {{String}},
  "[MoreInformationUrl](#cfn-mediapackagev2-originendpoint-dashprograminformation-moreinformationurl)" : {{String}},
  "[Source](#cfn-mediapackagev2-originendpoint-dashprograminformation-source)" : {{String}},
  "[Title](#cfn-mediapackagev2-originendpoint-dashprograminformation-title)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashprograminformation-syntax.yaml"></a>

```
  [Copyright](#cfn-mediapackagev2-originendpoint-dashprograminformation-copyright): {{String}}
  [LanguageCode](#cfn-mediapackagev2-originendpoint-dashprograminformation-languagecode): {{String}}
  [MoreInformationUrl](#cfn-mediapackagev2-originendpoint-dashprograminformation-moreinformationurl): {{String}}
  [Source](#cfn-mediapackagev2-originendpoint-dashprograminformation-source): {{String}}
  [Title](#cfn-mediapackagev2-originendpoint-dashprograminformation-title): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashprograminformation-properties"></a>

`Copyright`  <a name="cfn-mediapackagev2-originendpoint-dashprograminformation-copyright"></a>
A copyright statement about the content.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LanguageCode`  <a name="cfn-mediapackagev2-originendpoint-dashprograminformation-languagecode"></a>
The language code for this manifest.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$`
*Minimum*: `2`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MoreInformationUrl`  <a name="cfn-mediapackagev2-originendpoint-dashprograminformation-moreinformationurl"></a>
An absolute URL that contains more information about this content.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-mediapackagev2-originendpoint-dashprograminformation-source"></a>
Information about the content provider.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-mediapackagev2-originendpoint-dashprograminformation-title"></a>
The title for the manifest.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
