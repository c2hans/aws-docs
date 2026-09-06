---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-graphqlapi-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::GraphQLApi Tag
<a name="aws-properties-appsync-graphqlapi-tag"></a>

An arbitrary set of tags (key-value pairs) for this GraphQL API.

## Syntax
<a name="aws-properties-appsync-graphqlapi-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-graphqlapi-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appsync-graphqlapi-tag-key)" : {{String}},
  "[Value](#cfn-appsync-graphqlapi-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-graphqlapi-tag-syntax.yaml"></a>

```
  [Key](#cfn-appsync-graphqlapi-tag-key): {{String}}
  [Value](#cfn-appsync-graphqlapi-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appsync-graphqlapi-tag-properties"></a>

`Key`  <a name="cfn-appsync-graphqlapi-tag-key"></a>
Describes the key of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appsync-graphqlapi-tag-value"></a>
Describes the value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
