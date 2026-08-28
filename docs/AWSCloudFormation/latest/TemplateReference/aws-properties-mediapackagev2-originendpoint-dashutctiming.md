---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashutctiming.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashUtcTiming
<a name="aws-properties-mediapackagev2-originendpoint-dashutctiming"></a>

Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashutctiming-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashutctiming-syntax.json"></a>

```
{
  "[TimingMode](#cfn-mediapackagev2-originendpoint-dashutctiming-timingmode)" : {{String}},
  "[TimingSource](#cfn-mediapackagev2-originendpoint-dashutctiming-timingsource)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashutctiming-syntax.yaml"></a>

```
  [TimingMode](#cfn-mediapackagev2-originendpoint-dashutctiming-timingmode): {{String}}
  [TimingSource](#cfn-mediapackagev2-originendpoint-dashutctiming-timingsource): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashutctiming-properties"></a>

`TimingMode`  <a name="cfn-mediapackagev2-originendpoint-dashutctiming-timingmode"></a>
The UTC timing mode.
*Required*: No
*Type*: String
*Allowed values*: `HTTP_HEAD | HTTP_ISO | HTTP_XSDATE | UTC_DIRECT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimingSource`  <a name="cfn-mediapackagev2-originendpoint-dashutctiming-timingsource"></a>
The the method that the player uses to synchronize to coordinated universal time (UTC) wall clock time.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
