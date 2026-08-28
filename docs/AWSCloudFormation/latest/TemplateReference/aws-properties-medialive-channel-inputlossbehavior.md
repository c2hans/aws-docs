---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-inputlossbehavior.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel InputLossBehavior
<a name="aws-properties-medialive-channel-inputlossbehavior"></a>

The configuration of channel behavior when the input is lost.

The parent of this entity is GlobalConfiguration.

## Syntax
<a name="aws-properties-medialive-channel-inputlossbehavior-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-inputlossbehavior-syntax.json"></a>

```
{
  "[BlackFrameMsec](#cfn-medialive-channel-inputlossbehavior-blackframemsec)" : {{Integer}},
  "[InputLossImageColor](#cfn-medialive-channel-inputlossbehavior-inputlossimagecolor)" : {{String}},
  "[InputLossImageSlate](#cfn-medialive-channel-inputlossbehavior-inputlossimageslate)" : {{InputLocation}},
  "[InputLossImageType](#cfn-medialive-channel-inputlossbehavior-inputlossimagetype)" : {{String}},
  "[RepeatFrameMsec](#cfn-medialive-channel-inputlossbehavior-repeatframemsec)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-inputlossbehavior-syntax.yaml"></a>

```
  [BlackFrameMsec](#cfn-medialive-channel-inputlossbehavior-blackframemsec): {{Integer}}
  [InputLossImageColor](#cfn-medialive-channel-inputlossbehavior-inputlossimagecolor): {{String}}
  [InputLossImageSlate](#cfn-medialive-channel-inputlossbehavior-inputlossimageslate): {{
    InputLocation}}
  [InputLossImageType](#cfn-medialive-channel-inputlossbehavior-inputlossimagetype): {{String}}
  [RepeatFrameMsec](#cfn-medialive-channel-inputlossbehavior-repeatframemsec): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-inputlossbehavior-properties"></a>

`BlackFrameMsec`  <a name="cfn-medialive-channel-inputlossbehavior-blackframemsec"></a>
On input loss, the number of milliseconds to substitute black into the output before switching to the frame specified by inputLossImageType. A value x, where 0 <= x <= 1,000,000 and a value of 1,000,000, is interpreted as infinite.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputLossImageColor`  <a name="cfn-medialive-channel-inputlossbehavior-inputlossimagecolor"></a>
When the input loss image type is "color," this field specifies the color to use. Value: 6 hex characters that represent the values of RGB.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputLossImageSlate`  <a name="cfn-medialive-channel-inputlossbehavior-inputlossimageslate"></a>
When the input loss image type is "slate," these fields specify the parameters for accessing the slate.
*Required*: No
*Type*: [InputLocation](aws-properties-medialive-channel-inputlocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputLossImageType`  <a name="cfn-medialive-channel-inputlossbehavior-inputlossimagetype"></a>
Indicates whether to substitute a solid color or a slate into the output after the input loss exceeds blackFrameMsec.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepeatFrameMsec`  <a name="cfn-medialive-channel-inputlossbehavior-repeatframemsec"></a>
On input loss, the number of milliseconds to repeat the previous picture before substituting black into the output. A value x, where 0 <= x <= 1,000,000 and a value of 1,000,000, is interpreted as infinite.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
