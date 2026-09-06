---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_KafkaSchemaRegistryConfig.html
---

# KafkaSchemaRegistryConfig
<a name="API_KafkaSchemaRegistryConfig"></a>

Specific configuration settings for a Kafka schema registry.

## Contents
<a name="API_KafkaSchemaRegistryConfig_Contents"></a>

 ** AccessConfigs **   <a name="lambda-Type-KafkaSchemaRegistryConfig-AccessConfigs"></a>
An array of access configuration objects that tell Lambda how to authenticate with your schema registry.
Type: Array of [KafkaSchemaRegistryAccessConfig](API_KafkaSchemaRegistryAccessConfig.md) objects
Required: No

 ** EventRecordFormat **   <a name="lambda-Type-KafkaSchemaRegistryConfig-EventRecordFormat"></a>
The record format that Lambda delivers to your function after schema validation.
+ Choose `JSON` to have Lambda deliver the record to your function as a standard JSON object.
+ Choose `SOURCE` to have Lambda deliver the record to your function in its original source format. Lambda removes all schema metadata, such as the schema ID, before sending the record to your function.
Type: String
Valid Values: `JSON | SOURCE`
Required: No

 ** SchemaRegistryURI **   <a name="lambda-Type-KafkaSchemaRegistryConfig-SchemaRegistryURI"></a>
The URI for your schema registry. The correct URI format depends on the type of schema registry you're using.
+ For AWS Glue schema registries, use the ARN of the registry.
+ For Confluent schema registries, use the URL of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Pattern: `[a-zA-Z0-9-\/*:_+=.@-]*`
Required: No

 ** SchemaValidationConfigs **   <a name="lambda-Type-KafkaSchemaRegistryConfig-SchemaValidationConfigs"></a>
An array of schema validation configuration objects, which tell Lambda the message attributes you want to validate and filter using your schema registry.
Type: Array of [KafkaSchemaValidationConfig](API_KafkaSchemaValidationConfig.md) objects
Required: No

## See Also
<a name="API_KafkaSchemaRegistryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/KafkaSchemaRegistryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/KafkaSchemaRegistryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/KafkaSchemaRegistryConfig)
