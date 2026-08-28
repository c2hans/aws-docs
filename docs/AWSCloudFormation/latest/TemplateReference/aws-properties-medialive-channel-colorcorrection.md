---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-colorcorrection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ColorCorrection
<a name="aws-properties-medialive-channel-colorcorrection"></a>

Identifies one 3D LUT file and specifies the input/output color space combination that the file will be used for.

The parent of this entity is ColorCorrectionSettings.

## Syntax
<a name="aws-properties-medialive-channel-colorcorrection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-colorcorrection-syntax.json"></a>

```
{
  "[InputColorSpace](#cfn-medialive-channel-colorcorrection-inputcolorspace)" : {{String}},
  "[OutputColorSpace](#cfn-medialive-channel-colorcorrection-outputcolorspace)" : {{String}},
  "[Uri](#cfn-medialive-channel-colorcorrection-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-colorcorrection-syntax.yaml"></a>

```
  [InputColorSpace](#cfn-medialive-channel-colorcorrection-inputcolorspace): {{String}}
  [OutputColorSpace](#cfn-medialive-channel-colorcorrection-outputcolorspace): {{String}}
  [Uri](#cfn-medialive-channel-colorcorrection-uri): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-colorcorrection-properties"></a>

`InputColorSpace`  <a name="cfn-medialive-channel-colorcorrection-inputcolorspace"></a>
Required. The color space of the input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputColorSpace`  <a name="cfn-medialive-channel-colorcorrection-outputcolorspace"></a>
Required. The color space of the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Uri`  <a name="cfn-medialive-channel-colorcorrection-uri"></a>
Required. The URI of the 3D LUT file. The protocol must be 's3:' or 's3ssl:'.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
