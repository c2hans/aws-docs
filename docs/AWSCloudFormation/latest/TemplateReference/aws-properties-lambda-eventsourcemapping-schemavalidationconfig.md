---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-schemavalidationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping SchemaValidationConfig
<a name="aws-properties-lambda-eventsourcemapping-schemavalidationconfig"></a>

Specific schema validation configuration settings that tell Lambda the message attributes you want to validate and filter using your schema registry.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-schemavalidationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-schemavalidationconfig-syntax.json"></a>

```
{
  "[Attribute](#cfn-lambda-eventsourcemapping-schemavalidationconfig-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-schemavalidationconfig-syntax.yaml"></a>

```
  [Attribute](#cfn-lambda-eventsourcemapping-schemavalidationconfig-attribute): {{String}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-schemavalidationconfig-properties"></a>

`Attribute`  <a name="cfn-lambda-eventsourcemapping-schemavalidationconfig-attribute"></a>
 The attributes you want your schema registry to validate and filter for. If you selected `JSON` as the `EventRecordFormat`, Lambda also deserializes the selected message attributes.
*Required*: No
*Type*: String
*Allowed values*: `KEY | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
