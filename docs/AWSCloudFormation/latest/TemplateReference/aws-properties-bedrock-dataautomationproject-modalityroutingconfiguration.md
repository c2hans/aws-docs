---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject ModalityRoutingConfiguration
<a name="aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration"></a>

This element allows you to set up where JPEG, PNG, MOV, and MP4 files get routed to for processing. JPEG routing applies to both "JPEG" and "JPG" file extensions.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration-syntax.json"></a>

```
{
  "[jpeg](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-jpeg)" : {{String}},
  "[mov](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-mov)" : {{String}},
  "[mp4](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-mp4)" : {{String}},
  "[png](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-png)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration-syntax.yaml"></a>

```
  [jpeg](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-jpeg): {{String}}
  [mov](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-mov): {{String}}
  [mp4](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-mp4): {{String}}
  [png](#cfn-bedrock-dataautomationproject-modalityroutingconfiguration-png): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-modalityroutingconfiguration-properties"></a>

`jpeg`  <a name="cfn-bedrock-dataautomationproject-modalityroutingconfiguration-jpeg"></a>
Sets whether JPEG files are routed to document or image processing.
*Required*: No
*Type*: String
*Allowed values*: `DOCUMENT | IMAGE | VIDEO | AUDIO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`mov`  <a name="cfn-bedrock-dataautomationproject-modalityroutingconfiguration-mov"></a>
Sets whether MOV files are routed to audio or video processing.
*Required*: No
*Type*: String
*Allowed values*: `DOCUMENT | IMAGE | VIDEO | AUDIO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`mp4`  <a name="cfn-bedrock-dataautomationproject-modalityroutingconfiguration-mp4"></a>
Sets whether MP4 files are routed to audio or video processing.
*Required*: No
*Type*: String
*Allowed values*: `DOCUMENT | IMAGE | VIDEO | AUDIO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`png`  <a name="cfn-bedrock-dataautomationproject-modalityroutingconfiguration-png"></a>
Sets whether PNG files are routed to document or image processing.
*Required*: No
*Type*: String
*Allowed values*: `DOCUMENT | IMAGE | VIDEO | AUDIO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
