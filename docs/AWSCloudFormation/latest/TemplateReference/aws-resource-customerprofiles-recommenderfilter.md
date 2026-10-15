---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-recommenderfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::RecommenderFilter
<a name="aws-resource-customerprofiles-recommenderfilter"></a>

<a name="aws-resource-customerprofiles-recommenderfilter-description"></a>The `AWS::CustomerProfiles::RecommenderFilter` resource Property description not available. for CustomerProfiles.

## Syntax
<a name="aws-resource-customerprofiles-recommenderfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-recommenderfilter-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::RecommenderFilter",
  "Properties" : {
      "[Description](#cfn-customerprofiles-recommenderfilter-description)" : {{String}},
      "[DomainName](#cfn-customerprofiles-recommenderfilter-domainname)" : {{String}},
      "[RecommenderFilterExpression](#cfn-customerprofiles-recommenderfilter-recommenderfilterexpression)" : {{String}},
      "[RecommenderFilterName](#cfn-customerprofiles-recommenderfilter-recommenderfiltername)" : {{String}},
      "[RecommenderSchemaName](#cfn-customerprofiles-recommenderfilter-recommenderschemaname)" : {{String}},
      "[Tags](#cfn-customerprofiles-recommenderfilter-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-recommenderfilter-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::RecommenderFilter
Properties:
  [Description](#cfn-customerprofiles-recommenderfilter-description): {{String}}
  [DomainName](#cfn-customerprofiles-recommenderfilter-domainname): {{String}}
  [RecommenderFilterExpression](#cfn-customerprofiles-recommenderfilter-recommenderfilterexpression): {{String}}
  [RecommenderFilterName](#cfn-customerprofiles-recommenderfilter-recommenderfiltername): {{String}}
  [RecommenderSchemaName](#cfn-customerprofiles-recommenderfilter-recommenderschemaname): {{String}}
  [Tags](#cfn-customerprofiles-recommenderfilter-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-customerprofiles-recommenderfilter-properties"></a>

`Description`  <a name="cfn-customerprofiles-recommenderfilter-description"></a>
A description of the recommender filter's purpose and characteristics.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainName`  <a name="cfn-customerprofiles-recommenderfilter-domainname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderFilterExpression`  <a name="cfn-customerprofiles-recommenderfilter-recommenderfilterexpression"></a>
The filter expression that defines which items to include or exclude from recommendations.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderFilterName`  <a name="cfn-customerprofiles-recommenderfilter-recommenderfiltername"></a>
The name of the recommender filter.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderSchemaName`  <a name="cfn-customerprofiles-recommenderfilter-recommenderschemaname"></a>
The name of the recommender schema associated with this recommender filter.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-customerprofiles-recommenderfilter-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-customerprofiles-recommenderfilter-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-recommenderfilter-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-recommenderfilter-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-recommenderfilter-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-recommenderfilter-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the recommender filter was created.

`RecommenderFilterArn`  <a name="RecommenderFilterArn-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The current operational status of the recommender filter.
