---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-starttag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint StartTag
<a name="aws-properties-mediapackagev2-originendpoint-starttag"></a>

To insert an EXT-X-START tag in your HLS playlist, specify a StartTag configuration object with a valid TimeOffset. When you do, you can also optionally specify whether to include a PRECISE value in the EXT-X-START tag.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-starttag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-starttag-syntax.json"></a>

```
{
  "[Precise](#cfn-mediapackagev2-originendpoint-starttag-precise)" : {{Boolean}},
  "[TimeOffset](#cfn-mediapackagev2-originendpoint-starttag-timeoffset)" : {{Number}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-starttag-syntax.yaml"></a>

```
  [Precise](#cfn-mediapackagev2-originendpoint-starttag-precise): {{Boolean}}
  [TimeOffset](#cfn-mediapackagev2-originendpoint-starttag-timeoffset): {{Number}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-starttag-properties"></a>

`Precise`  <a name="cfn-mediapackagev2-originendpoint-starttag-precise"></a>
Specify the value for PRECISE within your EXT-X-START tag. Leave blank, or choose false, to use the default value NO. Choose yes to use the value YES.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeOffset`  <a name="cfn-mediapackagev2-originendpoint-starttag-timeoffset"></a>
Specify the value for TIME-OFFSET within your EXT-X-START tag. Enter a signed floating point value which, if positive, must be less than the configured manifest duration minus three times the configured segment target duration. If negative, the absolute value must be larger than three times the configured segment target duration, and the absolute value must be smaller than the configured manifest duration.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
