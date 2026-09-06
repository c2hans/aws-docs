---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMGuiConnect::Preferences ConnectionRecordingPreferences
<a name="aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences"></a>

The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region. This includes details such as which S3 bucket recordings are stored in.

## Syntax
<a name="aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences-syntax.json"></a>

```
{
  "[KMSKeyArn](#cfn-ssmguiconnect-preferences-connectionrecordingpreferences-kmskeyarn)" : {{String}},
  "[RecordingDestinations](#cfn-ssmguiconnect-preferences-connectionrecordingpreferences-recordingdestinations)" : {{RecordingDestinations}}
}
```

### YAML
<a name="aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences-syntax.yaml"></a>

```
  [KMSKeyArn](#cfn-ssmguiconnect-preferences-connectionrecordingpreferences-kmskeyarn): {{String}}
  [RecordingDestinations](#cfn-ssmguiconnect-preferences-connectionrecordingpreferences-recordingdestinations): {{
    RecordingDestinations}}
```

## Properties
<a name="aws-properties-ssmguiconnect-preferences-connectionrecordingpreferences-properties"></a>

`KMSKeyArn`  <a name="cfn-ssmguiconnect-preferences-connectionrecordingpreferences-kmskeyarn"></a>
The ARN of a AWS KMS key that is used to encrypt data while it is being processed by the service. This key must exist in the same AWS Region as the node you start an RDP connection to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordingDestinations`  <a name="cfn-ssmguiconnect-preferences-connectionrecordingpreferences-recordingdestinations"></a>
Determines where recordings of RDP connections are stored.
*Required*: Yes
*Type*: [RecordingDestinations](aws-properties-ssmguiconnect-preferences-recordingdestinations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
