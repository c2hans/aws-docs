---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-recommender.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Recommender
<a name="aws-resource-personalize-recommender"></a>

Describes a recommendation generator for a Domain dataset group. You create a recommender in a Domain dataset group for a specific domain use case (domain recipe), and specify the recommender in a [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html) request.

## Syntax
<a name="aws-resource-personalize-recommender-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-recommender-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::Recommender",
  "Properties" : {
      "[DatasetGroupArn](#cfn-personalize-recommender-datasetgrouparn)" : {{String}},
      "[Name](#cfn-personalize-recommender-name)" : {{String}},
      "[RecipeArn](#cfn-personalize-recommender-recipearn)" : {{String}},
      "[RecommenderConfig](#cfn-personalize-recommender-recommenderconfig)" : {{RecommenderConfig}},
      "[Tags](#cfn-personalize-recommender-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-personalize-recommender-syntax.yaml"></a>

```
Type: AWS::Personalize::Recommender
Properties:
  [DatasetGroupArn](#cfn-personalize-recommender-datasetgrouparn): {{String}}
  [Name](#cfn-personalize-recommender-name): {{String}}
  [RecipeArn](#cfn-personalize-recommender-recipearn): {{String}}
  [RecommenderConfig](#cfn-personalize-recommender-recommenderconfig): {{
    RecommenderConfig}}
  [Tags](#cfn-personalize-recommender-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-personalize-recommender-properties"></a>

`DatasetGroupArn`  <a name="cfn-personalize-recommender-datasetgrouparn"></a>
The Amazon Resource Name (ARN) of the Domain dataset group that contains the recommender.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([a-z\d-]+):personalize:.*:.*:.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-personalize-recommender-name"></a>
The name of the recommender.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecipeArn`  <a name="cfn-personalize-recommender-recipearn"></a>
The Amazon Resource Name (ARN) of the recipe (Domain dataset group use case) that the recommender was created for.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([a-z\d-]+):personalize:.*:.*:.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderConfig`  <a name="cfn-personalize-recommender-recommenderconfig"></a>
The configuration details of the recommender.
*Required*: No
*Type*: [RecommenderConfig](aws-properties-personalize-recommender-recommenderconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-personalize-recommender-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-personalize-recommender-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-personalize-recommender-return-values"></a>

### Ref
<a name="aws-resource-personalize-recommender-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-recommender-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-recommender-return-values-fn--getatt-fn--getatt"></a>

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The date and time (in Unix format) that the recommender was created.

`LastUpdatedDateTime`  <a name="LastUpdatedDateTime-fn::getatt"></a>
The date and time (in Unix format) that the recommender was last updated.

`RecommenderArn`  <a name="RecommenderArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the recommender.

`Status`  <a name="Status-fn::getatt"></a>
The status of the recommender.
A recommender can be in one of the following states:
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ STOP PENDING > STOP IN\_PROGRESS > INACTIVE > START PENDING > START IN\_PROGRESS > ACTIVE
+ DELETE PENDING > DELETE IN\_PROGRESS
