---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-campaign.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Campaign
<a name="aws-resource-personalize-campaign"></a>

An object that describes the deployment of a solution version. For more information on campaigns, see [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html).

## Syntax
<a name="aws-resource-personalize-campaign-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-campaign-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::Campaign",
  "Properties" : {
      "[CampaignConfig](#cfn-personalize-campaign-campaignconfig)" : {{CampaignConfig}},
      "[MinProvisionedTPS](#cfn-personalize-campaign-minprovisionedtps)" : {{Integer}},
      "[Name](#cfn-personalize-campaign-name)" : {{String}},
      "[SolutionVersionArn](#cfn-personalize-campaign-solutionversionarn)" : {{String}},
      "[Tags](#cfn-personalize-campaign-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-personalize-campaign-syntax.yaml"></a>

```
Type: AWS::Personalize::Campaign
Properties:
  [CampaignConfig](#cfn-personalize-campaign-campaignconfig): {{
    CampaignConfig}}
  [MinProvisionedTPS](#cfn-personalize-campaign-minprovisionedtps): {{Integer}}
  [Name](#cfn-personalize-campaign-name): {{String}}
  [SolutionVersionArn](#cfn-personalize-campaign-solutionversionarn): {{String}}
  [Tags](#cfn-personalize-campaign-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-personalize-campaign-properties"></a>

`CampaignConfig`  <a name="cfn-personalize-campaign-campaignconfig"></a>
The configuration details of a campaign.
*Required*: No
*Type*: [CampaignConfig](aws-properties-personalize-campaign-campaignconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinProvisionedTPS`  <a name="cfn-personalize-campaign-minprovisionedtps"></a>
Specifies the requested minimum provisioned transactions (recommendations) per second. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-personalize-campaign-name"></a>
The name of the campaign.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SolutionVersionArn`  <a name="cfn-personalize-campaign-solutionversionarn"></a>
The Amazon Resource Name (ARN) of the solution version the campaign uses.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([a-z\d-]+):personalize:.*:.*:.+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-personalize-campaign-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-personalize-campaign-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-personalize-campaign-return-values"></a>

### Ref
<a name="aws-resource-personalize-campaign-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-campaign-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-campaign-return-values-fn--getatt-fn--getatt"></a>

`CampaignArn`  <a name="CampaignArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the campaign.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The date and time (in Unix format) that the campaign was created.

`LastUpdatedDateTime`  <a name="LastUpdatedDateTime-fn::getatt"></a>
The date and time (in Unix format) that the campaign was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the campaign.
A campaign can be in one of the following states:
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ DELETE PENDING > DELETE IN\_PROGRESS
