---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_AmazonManagedKafkaEventSourceConfig.html
---

# AmazonManagedKafkaEventSourceConfig
<a name="API_AmazonManagedKafkaEventSourceConfig"></a>

Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.

## Contents
<a name="API_AmazonManagedKafkaEventSourceConfig_Contents"></a>

 ** ConsumerGroupId **   <a name="lambda-Type-AmazonManagedKafkaEventSourceConfig-ConsumerGroupId"></a>
The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see [Customizable consumer group ID](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-consumer-group-id).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-\/*:_+=.@-]*`
Required: No

 ** SchemaRegistryConfig **   <a name="lambda-Type-AmazonManagedKafkaEventSourceConfig-SchemaRegistryConfig"></a>
Specific configuration settings for a Kafka schema registry.
Type: [KafkaSchemaRegistryConfig](API_KafkaSchemaRegistryConfig.md) object
Required: No

## See Also
<a name="API_AmazonManagedKafkaEventSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/AmazonManagedKafkaEventSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/AmazonManagedKafkaEventSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/AmazonManagedKafkaEventSourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
