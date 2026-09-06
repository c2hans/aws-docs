---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiodolbyedecode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioDolbyEDecode
<a name="aws-properties-medialive-channel-audiodolbyedecode"></a>

Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337.

The parent of this entity is AudioTrackSelection.

## Syntax
<a name="aws-properties-medialive-channel-audiodolbyedecode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiodolbyedecode-syntax.json"></a>

```
{
  "[ProgramSelection](#cfn-medialive-channel-audiodolbyedecode-programselection)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiodolbyedecode-syntax.yaml"></a>

```
  [ProgramSelection](#cfn-medialive-channel-audiodolbyedecode-programselection): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-audiodolbyedecode-properties"></a>

`ProgramSelection`  <a name="cfn-medialive-channel-audiodolbyedecode-programselection"></a>
Required. Applies only to Dolby E. Enter the program ID (according to the metadata in the audio) of the Dolby E program to extract from the specified track. One program extracted per audio selector. To select multiple programs, create multiple selectors with the same Track and different Program numbers. "All channels" means to ignore the program IDs and include all the channels in this selector; useful if metadata is known to be incorrect.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
