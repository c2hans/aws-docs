---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-codegenjob-apiconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob ApiConfiguration
<a name="aws-properties-amplifyuibuilder-codegenjob-apiconfiguration"></a>

Describes the API configuration for a code generation job.

## Syntax
<a name="aws-properties-amplifyuibuilder-codegenjob-apiconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-codegenjob-apiconfiguration-syntax.json"></a>

```
{
  "[DataStoreConfig](#cfn-amplifyuibuilder-codegenjob-apiconfiguration-datastoreconfig)" : {{Json}},
  "[GraphQLConfig](#cfn-amplifyuibuilder-codegenjob-apiconfiguration-graphqlconfig)" : {{GraphQLRenderConfig}},
  "[NoApiConfig](#cfn-amplifyuibuilder-codegenjob-apiconfiguration-noapiconfig)" : {{Json}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-codegenjob-apiconfiguration-syntax.yaml"></a>

```
  [DataStoreConfig](#cfn-amplifyuibuilder-codegenjob-apiconfiguration-datastoreconfig): {{Json}}
  [GraphQLConfig](#cfn-amplifyuibuilder-codegenjob-apiconfiguration-graphqlconfig): {{
    GraphQLRenderConfig}}
  [NoApiConfig](#cfn-amplifyuibuilder-codegenjob-apiconfiguration-noapiconfig): {{Json}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-codegenjob-apiconfiguration-properties"></a>

`DataStoreConfig`  <a name="cfn-amplifyuibuilder-codegenjob-apiconfiguration-datastoreconfig"></a>
The configuration for an application using DataStore APIs.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GraphQLConfig`  <a name="cfn-amplifyuibuilder-codegenjob-apiconfiguration-graphqlconfig"></a>
The configuration for an application using GraphQL APIs.
*Required*: No
*Type*: [GraphQLRenderConfig](aws-properties-amplifyuibuilder-codegenjob-graphqlrenderconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NoApiConfig`  <a name="cfn-amplifyuibuilder-codegenjob-apiconfiguration-noapiconfig"></a>
The configuration for an application with no API being used.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
