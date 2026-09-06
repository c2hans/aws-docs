---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-recency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment Recency
<a name="aws-properties-pinpoint-segment-recency"></a>

Specifies how recently segment members were active.

## Syntax
<a name="aws-properties-pinpoint-segment-recency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-recency-syntax.json"></a>

```
{
  "[Duration](#cfn-pinpoint-segment-recency-duration)" : {{String}},
  "[RecencyType](#cfn-pinpoint-segment-recency-recencytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-recency-syntax.yaml"></a>

```
  [Duration](#cfn-pinpoint-segment-recency-duration): {{String}}
  [RecencyType](#cfn-pinpoint-segment-recency-recencytype): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-segment-recency-properties"></a>

`Duration`  <a name="cfn-pinpoint-segment-recency-duration"></a>
The duration to use when determining which users have been active or inactive with your app.
Possible values: `HR_24` \| `DAY_7` \| `DAY_14` \| `DAY_30`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecencyType`  <a name="cfn-pinpoint-segment-recency-recencytype"></a>
The type of recency dimension to use for the segment. Valid values are: `ACTIVE` and `INACTIVE`. If the value is `ACTIVE`, the segment includes users who have used your app within the specified duration are included in the segment. If the value is `INACTIVE`, the segment includes users who haven't used your app within the specified duration are included in the segment.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
