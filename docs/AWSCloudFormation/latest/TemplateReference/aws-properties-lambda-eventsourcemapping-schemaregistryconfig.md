---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-schemaregistryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::EventSourceMapping SchemaRegistryConfig
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryconfig"></a>

Specific configuration settings for a Kafka schema registry.

## Syntax
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryconfig-syntax.json"></a>

```
{
  "[AccessConfigs](#cfn-lambda-eventsourcemapping-schemaregistryconfig-accessconfigs)" : {{[ SchemaRegistryAccessConfig, ... ]}},
  "[EventRecordFormat](#cfn-lambda-eventsourcemapping-schemaregistryconfig-eventrecordformat)" : {{String}},
  "[SchemaRegistryURI](#cfn-lambda-eventsourcemapping-schemaregistryconfig-schemaregistryuri)" : {{String}},
  "[SchemaValidationConfigs](#cfn-lambda-eventsourcemapping-schemaregistryconfig-schemavalidationconfigs)" : {{[ SchemaValidationConfig, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryconfig-syntax.yaml"></a>

```
  [AccessConfigs](#cfn-lambda-eventsourcemapping-schemaregistryconfig-accessconfigs): {{
    - SchemaRegistryAccessConfig}}
  [EventRecordFormat](#cfn-lambda-eventsourcemapping-schemaregistryconfig-eventrecordformat): {{String}}
  [SchemaRegistryURI](#cfn-lambda-eventsourcemapping-schemaregistryconfig-schemaregistryuri): {{String}}
  [SchemaValidationConfigs](#cfn-lambda-eventsourcemapping-schemaregistryconfig-schemavalidationconfigs): {{
    - SchemaValidationConfig}}
```

## Properties
<a name="aws-properties-lambda-eventsourcemapping-schemaregistryconfig-properties"></a>

`AccessConfigs`  <a name="cfn-lambda-eventsourcemapping-schemaregistryconfig-accessconfigs"></a>
An array of access configuration objects that tell Lambda how to authenticate with your schema registry.
*Required*: No
*Type*: Array of [SchemaRegistryAccessConfig](aws-properties-lambda-eventsourcemapping-schemaregistryaccessconfig.md)
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventRecordFormat`  <a name="cfn-lambda-eventsourcemapping-schemaregistryconfig-eventrecordformat"></a>
The record format that Lambda delivers to your function after schema validation.
+ Choose `JSON` to have Lambda deliver the record to your function as a standard JSON object.
+ Choose `SOURCE` to have Lambda deliver the record to your function in its original source format. Lambda removes all schema metadata, such as the schema ID, before sending the record to your function.
*Required*: No
*Type*: String
*Allowed values*: `JSON | SOURCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaRegistryURI`  <a name="cfn-lambda-eventsourcemapping-schemaregistryconfig-schemaregistryuri"></a>
The URI for your schema registry. The correct URI format depends on the type of schema registry you're using.
+ For AWS Glue schema registries, use the ARN of the registry.
+ For Confluent schema registries, use the URL of the registry.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9-/*:_+=.@-]*`
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaValidationConfigs`  <a name="cfn-lambda-eventsourcemapping-schemaregistryconfig-schemavalidationconfigs"></a>
An array of schema validation configuration objects, which tell Lambda the message attributes you want to validate and filter using your schema registry.
*Required*: No
*Type*: Array of [SchemaValidationConfig](aws-properties-lambda-eventsourcemapping-schemavalidationconfig.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
