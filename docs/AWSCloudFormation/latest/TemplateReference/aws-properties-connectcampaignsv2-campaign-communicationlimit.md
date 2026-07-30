---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-communicationlimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign CommunicationLimit
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimit"></a>

Contains information about a communication limit.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimit-syntax.json"></a>

```
{
  "[Frequency](#cfn-connectcampaignsv2-campaign-communicationlimit-frequency)" : {{Integer}},
  "[MaxCountPerRecipient](#cfn-connectcampaignsv2-campaign-communicationlimit-maxcountperrecipient)" : {{Integer}},
  "[Unit](#cfn-connectcampaignsv2-campaign-communicationlimit-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimit-syntax.yaml"></a>

```
  [Frequency](#cfn-connectcampaignsv2-campaign-communicationlimit-frequency): {{Integer}}
  [MaxCountPerRecipient](#cfn-connectcampaignsv2-campaign-communicationlimit-maxcountperrecipient): {{Integer}}
  [Unit](#cfn-connectcampaignsv2-campaign-communicationlimit-unit): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimit-properties"></a>

`Frequency`  <a name="cfn-connectcampaignsv2-campaign-communicationlimit-frequency"></a>
The frequency of communication limit evaluation.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCountPerRecipient`  <a name="cfn-connectcampaignsv2-campaign-communicationlimit-maxcountperrecipient"></a>
The maximum outreaching count for each recipient.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-connectcampaignsv2-campaign-communicationlimit-unit"></a>
The unit of communication limit evaluation.
*Required*: Yes
*Type*: String
*Allowed values*: `DAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
