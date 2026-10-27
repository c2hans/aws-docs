---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-recommender-recommenderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Recommender RecommenderConfig
<a name="aws-properties-personalize-recommender-recommenderconfig"></a>

The configuration details of the recommender.

## Syntax
<a name="aws-properties-personalize-recommender-recommenderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-recommender-recommenderconfig-syntax.json"></a>

```
{
  "[EnableMetadataWithRecommendations](#cfn-personalize-recommender-recommenderconfig-enablemetadatawithrecommendations)" : {{Boolean}},
  "[ItemExplorationConfig](#cfn-personalize-recommender-recommenderconfig-itemexplorationconfig)" : {{{{{Key}}: {{Value}}, ...}}},
  "[MinRecommendationRequestsPerSecond](#cfn-personalize-recommender-recommenderconfig-minrecommendationrequestspersecond)" : {{Integer}},
  "[TrainingDataConfig](#cfn-personalize-recommender-recommenderconfig-trainingdataconfig)" : {{TrainingDataConfig}}
}
```

### YAML
<a name="aws-properties-personalize-recommender-recommenderconfig-syntax.yaml"></a>

```
  [EnableMetadataWithRecommendations](#cfn-personalize-recommender-recommenderconfig-enablemetadatawithrecommendations): {{Boolean}}
  [ItemExplorationConfig](#cfn-personalize-recommender-recommenderconfig-itemexplorationconfig): {{
    {{Key}}: {{Value}}}}
  [MinRecommendationRequestsPerSecond](#cfn-personalize-recommender-recommenderconfig-minrecommendationrequestspersecond): {{Integer}}
  [TrainingDataConfig](#cfn-personalize-recommender-recommenderconfig-trainingdataconfig): {{
    TrainingDataConfig}}
```

## Properties
<a name="aws-properties-personalize-recommender-recommenderconfig-properties"></a>

`EnableMetadataWithRecommendations`  <a name="cfn-personalize-recommender-recommenderconfig-enablemetadatawithrecommendations"></a>
Whether metadata with recommendations is enabled for the recommender. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a recommender, see [Enabling metadata in recommendations for a recommender](https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html#create-recommender-return-metadata).
 If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ItemExplorationConfig`  <a name="cfn-personalize-recommender-recommenderconfig-itemexplorationconfig"></a>
Specifies the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff`, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide `itemExplorationConfig` data only if your recommenders generate personalized recommendations for a user (not popular items or similar items).
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinRecommendationRequestsPerSecond`  <a name="cfn-personalize-recommender-recommenderconfig-minrecommendationrequestspersecond"></a>
Specifies the requested minimum provisioned recommendation requests per second that Amazon Personalize will support. A high `minRecommendationRequestsPerSecond` will increase your bill. We recommend starting with 1 for `minRecommendationRequestsPerSecond` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minRecommendationRequestsPerSecond` as necessary.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrainingDataConfig`  <a name="cfn-personalize-recommender-recommenderconfig-trainingdataconfig"></a>
 Specifies the training data configuration to use when creating a domain recommender.
*Required*: No
*Type*: [TrainingDataConfig](aws-properties-personalize-recommender-trainingdataconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
