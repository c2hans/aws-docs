---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-eventtrigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign EventTrigger
<a name="aws-properties-connectcampaignsv2-campaign-eventtrigger"></a>

The event trigger of the campaign.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-eventtrigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-eventtrigger-syntax.json"></a>

```
{
  "[CustomerProfilesDomainArn](#cfn-connectcampaignsv2-campaign-eventtrigger-customerprofilesdomainarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-eventtrigger-syntax.yaml"></a>

```
  [CustomerProfilesDomainArn](#cfn-connectcampaignsv2-campaign-eventtrigger-customerprofilesdomainarn): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-eventtrigger-properties"></a>

`CustomerProfilesDomainArn`  <a name="cfn-connectcampaignsv2-campaign-eventtrigger-customerprofilesdomainarn"></a>
The Amazon Resource Name (ARN) of the Customer Profiles domain.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
