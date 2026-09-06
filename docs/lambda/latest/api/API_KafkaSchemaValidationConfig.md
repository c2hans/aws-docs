---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_KafkaSchemaValidationConfig.html
---

# KafkaSchemaValidationConfig
<a name="API_KafkaSchemaValidationConfig"></a>

Specific schema validation configuration settings that tell Lambda the message attributes you want to validate and filter using your schema registry.

## Contents
<a name="API_KafkaSchemaValidationConfig_Contents"></a>

 ** Attribute **   <a name="lambda-Type-KafkaSchemaValidationConfig-Attribute"></a>
 The attributes you want your schema registry to validate and filter for. If you selected `JSON` as the `EventRecordFormat`, Lambda also deserializes the selected message attributes.
Type: String
Valid Values: `KEY | VALUE`
Required: No

## See Also
<a name="API_KafkaSchemaValidationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/KafkaSchemaValidationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/KafkaSchemaValidationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/KafkaSchemaValidationConfig)
