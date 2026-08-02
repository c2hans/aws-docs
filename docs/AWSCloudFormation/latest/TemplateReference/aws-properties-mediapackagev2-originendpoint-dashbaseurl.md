---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-dashbaseurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint DashBaseUrl
<a name="aws-properties-mediapackagev2-originendpoint-dashbaseurl"></a>

The base URLs to use for retrieving segments. You can specify multiple locations and indicate the priority and weight for when each should be used, for use in mutli-CDN workflows.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-dashbaseurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-dashbaseurl-syntax.json"></a>

```
{
  "[DvbPriority](#cfn-mediapackagev2-originendpoint-dashbaseurl-dvbpriority)" : {{Integer}},
  "[DvbWeight](#cfn-mediapackagev2-originendpoint-dashbaseurl-dvbweight)" : {{Integer}},
  "[ServiceLocation](#cfn-mediapackagev2-originendpoint-dashbaseurl-servicelocation)" : {{String}},
  "[Url](#cfn-mediapackagev2-originendpoint-dashbaseurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-dashbaseurl-syntax.yaml"></a>

```
  [DvbPriority](#cfn-mediapackagev2-originendpoint-dashbaseurl-dvbpriority): {{Integer}}
  [DvbWeight](#cfn-mediapackagev2-originendpoint-dashbaseurl-dvbweight): {{Integer}}
  [ServiceLocation](#cfn-mediapackagev2-originendpoint-dashbaseurl-servicelocation): {{String}}
  [Url](#cfn-mediapackagev2-originendpoint-dashbaseurl-url): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-dashbaseurl-properties"></a>

`DvbPriority`  <a name="cfn-mediapackagev2-originendpoint-dashbaseurl-dvbpriority"></a>
For use with DVB-DASH profiles only. The priority of this location for servings segments. The lower the number, the higher the priority.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DvbWeight`  <a name="cfn-mediapackagev2-originendpoint-dashbaseurl-dvbweight"></a>
For use with DVB-DASH profiles only. The weighting for source locations that have the same priority.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceLocation`  <a name="cfn-mediapackagev2-originendpoint-dashbaseurl-servicelocation"></a>
The name of the source location.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediapackagev2-originendpoint-dashbaseurl-url"></a>
A source location for segments.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
