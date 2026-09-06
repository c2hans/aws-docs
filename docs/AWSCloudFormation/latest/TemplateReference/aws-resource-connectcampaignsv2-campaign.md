---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connectcampaignsv2-campaign.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign
<a name="aws-resource-connectcampaignsv2-campaign"></a>

 Creates an outbound campaign.

**Note**
For users to be able to view or edit a campaign at a later date by using the Amazon Connect user interface, you must add the instance ID as a tag. For example, `{ "tags": {"owner": "arn:aws:connect:{REGION}:{AWS_ACCOUNT_ID}:instance/{CONNECT_INSTANCE_ID}"}}`.
After a campaign is created, you can't add/remove source.

## Syntax
<a name="aws-resource-connectcampaignsv2-campaign-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connectcampaignsv2-campaign-syntax.json"></a>

```
{
  "Type" : "AWS::ConnectCampaignsV2::Campaign",
  "Properties" : {
      "[ChannelSubtypeConfig](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig)" : {{ChannelSubtypeConfig}},
      "[CommunicationLimitsOverride](#cfn-connectcampaignsv2-campaign-communicationlimitsoverride)" : {{CommunicationLimitsConfig}},
      "[CommunicationTimeConfig](#cfn-connectcampaignsv2-campaign-communicationtimeconfig)" : {{CommunicationTimeConfig}},
      "[ConnectCampaignFlowArn](#cfn-connectcampaignsv2-campaign-connectcampaignflowarn)" : {{String}},
      "[ConnectInstanceId](#cfn-connectcampaignsv2-campaign-connectinstanceid)" : {{String}},
      "[EntryLimitsConfig](#cfn-connectcampaignsv2-campaign-entrylimitsconfig)" : {{EntryLimitsConfig}},
      "[Name](#cfn-connectcampaignsv2-campaign-name)" : {{String}},
      "[Schedule](#cfn-connectcampaignsv2-campaign-schedule)" : {{Schedule}},
      "[Source](#cfn-connectcampaignsv2-campaign-source)" : {{Source}},
      "[Tags](#cfn-connectcampaignsv2-campaign-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-connectcampaignsv2-campaign-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connectcampaignsv2-campaign-syntax.yaml"></a>

```
Type: AWS::ConnectCampaignsV2::Campaign
Properties:
  [ChannelSubtypeConfig](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig): {{
    ChannelSubtypeConfig}}
  [CommunicationLimitsOverride](#cfn-connectcampaignsv2-campaign-communicationlimitsoverride): {{
    CommunicationLimitsConfig}}
  [CommunicationTimeConfig](#cfn-connectcampaignsv2-campaign-communicationtimeconfig): {{
    CommunicationTimeConfig}}
  [ConnectCampaignFlowArn](#cfn-connectcampaignsv2-campaign-connectcampaignflowarn): {{String}}
  [ConnectInstanceId](#cfn-connectcampaignsv2-campaign-connectinstanceid): {{String}}
  [EntryLimitsConfig](#cfn-connectcampaignsv2-campaign-entrylimitsconfig): {{
    EntryLimitsConfig}}
  [Name](#cfn-connectcampaignsv2-campaign-name): {{String}}
  [Schedule](#cfn-connectcampaignsv2-campaign-schedule): {{
    Schedule}}
  [Source](#cfn-connectcampaignsv2-campaign-source): {{
    Source}}
  [Tags](#cfn-connectcampaignsv2-campaign-tags): {{
    - Tag}}
  [Type](#cfn-connectcampaignsv2-campaign-type): {{String}}
```

## Properties
<a name="aws-resource-connectcampaignsv2-campaign-properties"></a>

`ChannelSubtypeConfig`  <a name="cfn-connectcampaignsv2-campaign-channelsubtypeconfig"></a>
Contains channel subtype configuration for an outbound campaign.
*Required*: No
*Type*: [ChannelSubtypeConfig](aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CommunicationLimitsOverride`  <a name="cfn-connectcampaignsv2-campaign-communicationlimitsoverride"></a>
Communication limits configuration for an outbound campaign.
*Required*: No
*Type*: [CommunicationLimitsConfig](aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CommunicationTimeConfig`  <a name="cfn-connectcampaignsv2-campaign-communicationtimeconfig"></a>
Contains communication time configuration for an outbound campaign.
*Required*: No
*Type*: [CommunicationTimeConfig](aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectCampaignFlowArn`  <a name="cfn-connectcampaignsv2-campaign-connectcampaignflowarn"></a>
The Amazon Resource Name (ARN) of the Amazon Connect campaign flow associated with the outbound campaign.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectInstanceId`  <a name="cfn-connectcampaignsv2-campaign-connectinstanceid"></a>
The identifier of the Connect Customer instance. You can find the `instanceId` in the ARN of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-.]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntryLimitsConfig`  <a name="cfn-connectcampaignsv2-campaign-entrylimitsconfig"></a>
Contains entry limits configuration for an outbound campaign.
*Required*: No
*Type*: [EntryLimitsConfig](aws-properties-connectcampaignsv2-campaign-entrylimitsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connectcampaignsv2-campaign-name"></a>
The name of the outbound campaign.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-connectcampaignsv2-campaign-schedule"></a>
Contains the schedule configuration.
*Required*: No
*Type*: [Schedule](aws-properties-connectcampaignsv2-campaign-schedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-connectcampaignsv2-campaign-source"></a>
Contains source configuration.
*Required*: No
*Type*: [Source](aws-properties-connectcampaignsv2-campaign-source.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connectcampaignsv2-campaign-tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "tags": {"key1":"value1", "key2":"value2"} }`.
*Required*: No
*Type*: Array of [Tag](aws-properties-connectcampaignsv2-campaign-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connectcampaignsv2-campaign-type"></a>
The type of campaign.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | JOURNEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connectcampaignsv2-campaign-return-values"></a>

### Ref
<a name="aws-resource-connectcampaignsv2-campaign-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connectcampaignsv2-campaign-return-values-fn--getatt"></a>

####
<a name="aws-resource-connectcampaignsv2-campaign-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN).
