---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediapackagev2-harvestjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::HarvestJob
<a name="aws-resource-mediapackagev2-harvestjob"></a>

Creates a new harvest job to export content from a MediaPackage v2 channel to an S3 bucket.

## Syntax
<a name="aws-resource-mediapackagev2-harvestjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediapackagev2-harvestjob-syntax.json"></a>

```
{
  "Type" : "AWS::MediaPackageV2::HarvestJob",
  "Properties" : {
      "[ChannelGroupName](#cfn-mediapackagev2-harvestjob-channelgroupname)" : {{String}},
      "[ChannelName](#cfn-mediapackagev2-harvestjob-channelname)" : {{String}},
      "[Description](#cfn-mediapackagev2-harvestjob-description)" : {{String}},
      "[Destination](#cfn-mediapackagev2-harvestjob-destination)" : {{Destination}},
      "[HarvestedManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests)" : {{HarvestedManifests}},
      "[HarvestJobName](#cfn-mediapackagev2-harvestjob-harvestjobname)" : {{String}},
      "[OriginEndpointName](#cfn-mediapackagev2-harvestjob-originendpointname)" : {{String}},
      "[ScheduleConfiguration](#cfn-mediapackagev2-harvestjob-scheduleconfiguration)" : {{HarvesterScheduleConfiguration}},
      "[Tags](#cfn-mediapackagev2-harvestjob-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediapackagev2-harvestjob-syntax.yaml"></a>

```
Type: AWS::MediaPackageV2::HarvestJob
Properties:
  [ChannelGroupName](#cfn-mediapackagev2-harvestjob-channelgroupname): {{String}}
  [ChannelName](#cfn-mediapackagev2-harvestjob-channelname): {{String}}
  [Description](#cfn-mediapackagev2-harvestjob-description): {{String}}
  [Destination](#cfn-mediapackagev2-harvestjob-destination): {{
    Destination}}
  [HarvestedManifests](#cfn-mediapackagev2-harvestjob-harvestedmanifests): {{
    HarvestedManifests}}
  [HarvestJobName](#cfn-mediapackagev2-harvestjob-harvestjobname): {{String}}
  [OriginEndpointName](#cfn-mediapackagev2-harvestjob-originendpointname): {{String}}
  [ScheduleConfiguration](#cfn-mediapackagev2-harvestjob-scheduleconfiguration): {{
    HarvesterScheduleConfiguration}}
  [Tags](#cfn-mediapackagev2-harvestjob-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediapackagev2-harvestjob-properties"></a>

`ChannelGroupName`  <a name="cfn-mediapackagev2-harvestjob-channelgroupname"></a>
The name of the channel group containing the channel associated with the harvest job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ChannelName`  <a name="cfn-mediapackagev2-harvestjob-channelname"></a>
The name of the channel associated with the harvest job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-mediapackagev2-harvestjob-description"></a>
The description of the harvest job, if provided.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Destination`  <a name="cfn-mediapackagev2-harvestjob-destination"></a>
The S3 destination where the harvested content is being placed.
*Required*: Yes
*Type*: [Destination](aws-properties-mediapackagev2-harvestjob-destination.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HarvestedManifests`  <a name="cfn-mediapackagev2-harvestjob-harvestedmanifests"></a>
A list of manifests that are being or have been harvested.
*Required*: Yes
*Type*: [HarvestedManifests](aws-properties-mediapackagev2-harvestjob-harvestedmanifests.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HarvestJobName`  <a name="cfn-mediapackagev2-harvestjob-harvestjobname"></a>
The name of the harvest job.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OriginEndpointName`  <a name="cfn-mediapackagev2-harvestjob-originendpointname"></a>
The name of the origin endpoint associated with the harvest job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScheduleConfiguration`  <a name="cfn-mediapackagev2-harvestjob-scheduleconfiguration"></a>
The configuration for when the harvest job is scheduled to run, including start and end times.
*Required*: Yes
*Type*: [HarvesterScheduleConfiguration](aws-properties-mediapackagev2-harvestjob-harvesterscheduleconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-mediapackagev2-harvestjob-tags"></a>
A collection of tags associated with the harvest job.
*Required*: No
*Type*: Array of [Tag](aws-properties-mediapackagev2-harvestjob-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-mediapackagev2-harvestjob-return-values"></a>

### Ref
<a name="aws-resource-mediapackagev2-harvestjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediapackagev2-harvestjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediapackagev2-harvestjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the harvest job.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the harvest job was created.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
The date and time when the harvest job was last modified.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the harvest job (e.g., QUEUED, IN\_PROGRESS, CANCELLED, COMPLETED, FAILED).
