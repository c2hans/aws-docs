---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-recommenderschema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::RecommenderSchema
<a name="aws-resource-customerprofiles-recommenderschema"></a>

<a name="aws-resource-customerprofiles-recommenderschema-description"></a>The `AWS::CustomerProfiles::RecommenderSchema` resource Property description not available. for CustomerProfiles.

## Syntax
<a name="aws-resource-customerprofiles-recommenderschema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-recommenderschema-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::RecommenderSchema",
  "Properties" : {
      "[DomainName](#cfn-customerprofiles-recommenderschema-domainname)" : {{String}},
      "[Fields](#cfn-customerprofiles-recommenderschema-fields)" : {{{{{Key}}: {{Value}}, ...}}},
      "[RecommenderSchemaName](#cfn-customerprofiles-recommenderschema-recommenderschemaname)" : {{String}},
      "[Tags](#cfn-customerprofiles-recommenderschema-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-recommenderschema-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::RecommenderSchema
Properties:
  [DomainName](#cfn-customerprofiles-recommenderschema-domainname): {{String}}
  [Fields](#cfn-customerprofiles-recommenderschema-fields): {{
    {{Key}}: {{Value}}}}
  [RecommenderSchemaName](#cfn-customerprofiles-recommenderschema-recommenderschemaname): {{String}}
  [Tags](#cfn-customerprofiles-recommenderschema-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-customerprofiles-recommenderschema-properties"></a>

`DomainName`  <a name="cfn-customerprofiles-recommenderschema-domainname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Fields`  <a name="cfn-customerprofiles-recommenderschema-fields"></a>
A map of dataset type to column definitions included in the schema.
*Required*: Yes
*Type*: Object of Array
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecommenderSchemaName`  <a name="cfn-customerprofiles-recommenderschema-recommenderschemaname"></a>
The name of the recommender schema.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-customerprofiles-recommenderschema-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-customerprofiles-recommenderschema-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-recommenderschema-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-recommenderschema-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-customerprofiles-recommenderschema-return-values-fn--getatt"></a>

####
<a name="aws-resource-customerprofiles-recommenderschema-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the recommender schema was created.

`Status`  <a name="Status-fn::getatt"></a>
The current operational status of the recommender schema.
