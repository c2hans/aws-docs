---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-scte.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint Scte
<a name="aws-properties-mediapackagev2-originendpoint-scte"></a>

The SCTE-35 configuration associated with the origin endpoint.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-scte-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-scte-syntax.json"></a>

```
{
  "[CustomAdTypes](#cfn-mediapackagev2-originendpoint-scte-customadtypes)" : {{[ String, ... ]}},
  "[ScteFilter](#cfn-mediapackagev2-originendpoint-scte-sctefilter)" : {{[ String, ... ]}},
  "[ScteInSegments](#cfn-mediapackagev2-originendpoint-scte-scteinsegments)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-scte-syntax.yaml"></a>

```
  [CustomAdTypes](#cfn-mediapackagev2-originendpoint-scte-customadtypes): {{
    - String}}
  [ScteFilter](#cfn-mediapackagev2-originendpoint-scte-sctefilter): {{
    - String}}
  [ScteInSegments](#cfn-mediapackagev2-originendpoint-scte-scteinsegments): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-scte-properties"></a>

`CustomAdTypes`  <a name="cfn-mediapackagev2-originendpoint-scte-customadtypes"></a>
A list of additional non-Ad SCTE-35 event types to treat as advertisements. When configured, events matching these types produce ad markers (such as `SCTE35-OUT` and `SCTE35-IN` in HLS DATERANGE tags) in manifests.
Valid values: `PROGRAM` \| `CHAPTER` \| `UNSCHEDULED_EVENT` \| `ALTERNATE_CONTENT_OPPORTUNITY` \| `NETWORK`
If you don't specify any values, the default is empty (only default ad types are used).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteFilter`  <a name="cfn-mediapackagev2-originendpoint-scte-sctefilter"></a>
The filter associated with the SCTE-35 configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScteInSegments`  <a name="cfn-mediapackagev2-originendpoint-scte-scteinsegments"></a>
Controls whether SCTE-35 messages are included in segment files.
+ None – SCTE-35 messages are not included in segments (default)
+ All – SCTE-35 messages are embedded in segment data
+ MatchesFilter – SCTE-35 messages which match the ScteFilter are embedded in segment data
 For DASH manifests, when set to `All` or `MatchesFilter`, an `InbandEventStream` tag signals that SCTE messages are present in segments. This setting works independently of manifest ad markers.
*Required*: No
*Type*: String
*Allowed values*: `NONE | ALL | MATCHES_FILTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
