---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-recommender-recommenderupdate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Recommender RecommenderUpdate
<a name="aws-properties-customerprofiles-recommender-recommenderupdate"></a>

<a name="aws-properties-customerprofiles-recommender-recommenderupdate-description"></a>The `RecommenderUpdate` property type specifies Property description not available. for an [AWS::CustomerProfiles::Recommender](aws-resource-customerprofiles-recommender.md).

## Syntax
<a name="aws-properties-customerprofiles-recommender-recommenderupdate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-recommender-recommenderupdate-syntax.json"></a>

```
{
  "[CreationDateTime](#cfn-customerprofiles-recommender-recommenderupdate-creationdatetime)" : {{String}},
  "[FailureReason](#cfn-customerprofiles-recommender-recommenderupdate-failurereason)" : {{String}},
  "[LastUpdatedDateTime](#cfn-customerprofiles-recommender-recommenderupdate-lastupdateddatetime)" : {{String}},
  "[RecommenderConfig](#cfn-customerprofiles-recommender-recommenderupdate-recommenderconfig)" : {{RecommenderConfig}},
  "[Status](#cfn-customerprofiles-recommender-recommenderupdate-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-recommender-recommenderupdate-syntax.yaml"></a>

```
  [CreationDateTime](#cfn-customerprofiles-recommender-recommenderupdate-creationdatetime): {{String}}
  [FailureReason](#cfn-customerprofiles-recommender-recommenderupdate-failurereason): {{String}}
  [LastUpdatedDateTime](#cfn-customerprofiles-recommender-recommenderupdate-lastupdateddatetime): {{String}}
  [RecommenderConfig](#cfn-customerprofiles-recommender-recommenderupdate-recommenderconfig): {{
    RecommenderConfig}}
  [Status](#cfn-customerprofiles-recommender-recommenderupdate-status): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-recommender-recommenderupdate-properties"></a>

`CreationDateTime`  <a name="cfn-customerprofiles-recommender-recommenderupdate-creationdatetime"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureReason`  <a name="cfn-customerprofiles-recommender-recommenderupdate-failurereason"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUpdatedDateTime`  <a name="cfn-customerprofiles-recommender-recommenderupdate-lastupdateddatetime"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecommenderConfig`  <a name="cfn-customerprofiles-recommender-recommenderupdate-recommenderconfig"></a>
Property description not available.
*Required*: No
*Type*: [RecommenderConfig](aws-properties-customerprofiles-recommender-recommenderconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-customerprofiles-recommender-recommenderupdate-status"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PENDING | IN_PROGRESS | STOPPING | STARTING | ACTIVE | INACTIVE | FAILED | DELETING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
