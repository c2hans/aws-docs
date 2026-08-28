---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-recommender.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Recommender
<a name="aws-resource-customerprofiles-recommender"></a>

<a name="aws-resource-customerprofiles-recommender-description"></a>The `AWS::CustomerProfiles::Recommender` resource Property description not available. for CustomerProfiles.

## Syntax
<a name="aws-resource-customerprofiles-recommender-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-recommender-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::Recommender",
  "Properties" : {
      "[Description](#cfn-customerprofiles-recommender-description)" : {{String}},
      "[DomainName](#cfn-customerprofiles-recommender-domainname)" : {{String}},
      "[RecommenderConfig](#cfn-customerprofiles-recommender-recommenderconfig)" : {{RecommenderConfig}},
      "[RecommenderName](#cfn-customerprofiles-recommender-recommendername)" : {{String}},
      "[RecommenderRecipeName](#cfn-customerprofiles-recommender-recommenderrecipename)" : {{String}},
      "[Tags](#cfn-customerprofiles-recommender-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-recommender-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::Recommender
Properties:
  [Description](#cfn-customerprofiles-recommender-description): {{String}}
  [DomainName](#cfn-customerprofiles-recommender-domainname): {{String}}
  [RecommenderConfig](#cfn-customerprofiles-recommender-recommenderconfig): {{
    RecommenderConfig}}
  [RecommenderName](#cfn-customerprofiles-recommender-recommendername): {{String}}
  [RecommenderRecipeName](#cfn-customerprofiles-recommender-recommenderrecipename): {{String}}
  [Tags](#cfn-customerprofiles-recommender-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-customerprofiles-recommender-properties"></a>

`Description`  <a name="cfn-customerprofiles-recommender-description"></a>
A description of the recommender's purpose and characteristics.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-customerprofiles-recommender-domainname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderConfig`  <a name="cfn-customerprofiles-recommender-recommenderconfig"></a>
The configuration settings applied to this recommender.
*Required*: No
*Type*: [RecommenderConfig](aws-properties-customerprofiles-recommender-recommenderconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecommenderName`  <a name="cfn-customerprofiles-recommender-recommendername"></a>
The name of the recommender.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderRecipeName`  <a name="cfn-customerprofiles-recommender-recommenderrecipename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-customerprofiles-recommender-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-recommender-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-recommender-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-recommender-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-recommender-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-recommender-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the recommender was created.

`FailureReason`  <a name="FailureReason-fn::getatt"></a>
If the recommender is in a failed state, provides the reason for the failure.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the recommender was edited.

`RecommenderArn`  <a name="RecommenderArn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The current operational status of the recommender.

`TrainingMetrics`  <a name="TrainingMetrics-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
