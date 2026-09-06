---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-plugin-custompluginconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Plugin CustomPluginConfiguration
<a name="aws-properties-qbusiness-plugin-custompluginconfiguration"></a>

 Configuration information required to create a custom plugin.

## Syntax
<a name="aws-properties-qbusiness-plugin-custompluginconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-plugin-custompluginconfiguration-syntax.json"></a>

```
{
  "[ApiSchema](#cfn-qbusiness-plugin-custompluginconfiguration-apischema)" : {{APISchema}},
  "[ApiSchemaType](#cfn-qbusiness-plugin-custompluginconfiguration-apischematype)" : {{String}},
  "[Description](#cfn-qbusiness-plugin-custompluginconfiguration-description)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-plugin-custompluginconfiguration-syntax.yaml"></a>

```
  [ApiSchema](#cfn-qbusiness-plugin-custompluginconfiguration-apischema): {{
    APISchema}}
  [ApiSchemaType](#cfn-qbusiness-plugin-custompluginconfiguration-apischematype): {{String}}
  [Description](#cfn-qbusiness-plugin-custompluginconfiguration-description): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-plugin-custompluginconfiguration-properties"></a>

`ApiSchema`  <a name="cfn-qbusiness-plugin-custompluginconfiguration-apischema"></a>
Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema.
*Required*: Yes
*Type*: [APISchema](aws-properties-qbusiness-plugin-apischema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiSchemaType`  <a name="cfn-qbusiness-plugin-custompluginconfiguration-apischematype"></a>
The type of OpenAPI schema to use.
*Required*: Yes
*Type*: String
*Allowed values*: `OPEN_API_V3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-qbusiness-plugin-custompluginconfiguration-description"></a>
A description for your custom plugin configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
