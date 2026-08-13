---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob GraphQLRenderConfig
<a name="aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig"></a>

Describes the GraphQL configuration for an API for a code generation job.

## Syntax
<a name="aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig-syntax.json"></a>

```
{
  "[FragmentsFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-fragmentsfilepath)" : {{String}},
  "[MutationsFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-mutationsfilepath)" : {{String}},
  "[QueriesFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-queriesfilepath)" : {{String}},
  "[SubscriptionsFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-subscriptionsfilepath)" : {{String}},
  "[TypesFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-typesfilepath)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig-syntax.yaml"></a>

```
  [FragmentsFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-fragmentsfilepath): {{String}}
  [MutationsFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-mutationsfilepath): {{String}}
  [QueriesFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-queriesfilepath): {{String}}
  [SubscriptionsFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-subscriptionsfilepath): {{String}}
  [TypesFilePath](#cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-typesfilepath): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig-properties"></a>

`FragmentsFilePath`  <a name="cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-fragmentsfilepath"></a>
The path to the GraphQL fragments file, relative to the component output directory.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MutationsFilePath`  <a name="cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-mutationsfilepath"></a>
The path to the GraphQL mutations file, relative to the component output directory.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueriesFilePath`  <a name="cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-queriesfilepath"></a>
The path to the GraphQL queries file, relative to the component output directory.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubscriptionsFilePath`  <a name="cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-subscriptionsfilepath"></a>
The path to the GraphQL subscriptions file, relative to the component output directory.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TypesFilePath`  <a name="cfn-amplifyuibuilder-codegenjob-graphqlrenderconfig-typesfilepath"></a>
The path to the GraphQL types file, relative to the component output directory.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
