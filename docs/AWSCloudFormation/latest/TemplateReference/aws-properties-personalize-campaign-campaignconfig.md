---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-campaign-campaignconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Campaign CampaignConfig
<a name="aws-properties-personalize-campaign-campaignconfig"></a>

The configuration details of a campaign.

## Syntax
<a name="aws-properties-personalize-campaign-campaignconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-campaign-campaignconfig-syntax.json"></a>

```
{
  "[EnableMetadataWithRecommendations](#cfn-personalize-campaign-campaignconfig-enablemetadatawithrecommendations)" : {{Boolean}},
  "[ItemExplorationConfig](#cfn-personalize-campaign-campaignconfig-itemexplorationconfig)" : {{{{{Key}}: {{Value}}, ...}}},
  "[RankingInfluence](#cfn-personalize-campaign-campaignconfig-rankinginfluence)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SyncWithLatestSolutionVersion](#cfn-personalize-campaign-campaignconfig-syncwithlatestsolutionversion)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-personalize-campaign-campaignconfig-syntax.yaml"></a>

```
  [EnableMetadataWithRecommendations](#cfn-personalize-campaign-campaignconfig-enablemetadatawithrecommendations): {{Boolean}}
  [ItemExplorationConfig](#cfn-personalize-campaign-campaignconfig-itemexplorationconfig): {{
    {{Key}}: {{Value}}}}
  [RankingInfluence](#cfn-personalize-campaign-campaignconfig-rankinginfluence): {{
    {{Key}}: {{Value}}}}
  [SyncWithLatestSolutionVersion](#cfn-personalize-campaign-campaignconfig-syncwithlatestsolutionversion): {{Boolean}}
```

## Properties
<a name="aws-properties-personalize-campaign-campaignconfig-properties"></a>

`EnableMetadataWithRecommendations`  <a name="cfn-personalize-campaign-campaignconfig-enablemetadatawithrecommendations"></a>
Whether metadata with recommendations is enabled for the campaign. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata).
 If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ItemExplorationConfig`  <a name="cfn-personalize-campaign-campaignconfig-itemexplorationconfig"></a>
Specifies the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide `itemExplorationConfig` data only if your solution uses the [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) recipe.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9]+$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RankingInfluence`  <a name="cfn-personalize-campaign-campaignconfig-rankinginfluence"></a>
A map of ranking influence values for POPULARITY and FRESHNESS. For each key, specify a numerical value between 0.0 and 1.0 that determines how much influence that ranking factor has on the final recommendations. A value closer to 1.0 gives more weight to the factor, while a value closer to 0.0 reduces its influence. If not specified, both default to 0.0.
*Required*: No
*Type*: Object of Number
*Pattern*: `^(POPULARITY|FRESHNESS)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SyncWithLatestSolutionVersion`  <a name="cfn-personalize-campaign-campaignconfig-syncwithlatestsolutionversion"></a>
Whether the campaign automatically updates to use the latest solution version (trained model) of a solution. If you specify `True`, you must specify the ARN of your *solution* for the `SolutionVersionArn` parameter. It must be in `SolutionArn/$LATEST` format. The default is `False` and you must manually update the campaign to deploy the latest solution version.
 For more information about automatic campaign updates, see [Enabling automatic campaign updates](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
