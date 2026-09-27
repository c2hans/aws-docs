---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_SchemaRegistryConfiguration.html
---

# SchemaRegistryConfiguration
<a name="API_SchemaRegistryConfiguration"></a>

Schema registry settings used to encode open-format (Avro/Protobuf) events.

## Contents
<a name="API_SchemaRegistryConfiguration_Contents"></a>

 ** RegistryUri **   <a name="eventbridgev2-Type-SchemaRegistryConfiguration-RegistryUri"></a>
Glue Schema Registry ARN, or Confluent Cloud HTTPS URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:[a-z0-9-]+:glue:[a-z0-9-]+:[0-9]{12}:registry/[-_$#A-Za-z0-9]{1,255}|https://((([A-Za-z0-9]+-)*[A-Za-z0-9]+)\.)*([A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)(:[0-9]{1,5})?)(?![\s\S]).*`
Required: Yes

 ** ConfluentPublicRegistryConfiguration **   <a name="eventbridgev2-Type-SchemaRegistryConfiguration-ConfluentPublicRegistryConfiguration"></a>
Required when RegistryUri is an HTTPS URL. Provides Connection-based auth for Confluent Cloud.
Type: [ConfluentPublicRegistryConfiguration](API_ConfluentPublicRegistryConfiguration.md) object
Required: No

## See Also
<a name="API_SchemaRegistryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/SchemaRegistryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/SchemaRegistryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/SchemaRegistryConfiguration)
