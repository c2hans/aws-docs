---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_KafkaExporterConfiguration.html
---

# KafkaExporterConfiguration
<a name="API_KafkaExporterConfiguration"></a>

The configuration for collecting broker, topic, and consumer-group metrics from an Amazon MSK cluster through a managed Kafka exporter. The cluster must be active, have IAM authentication enabled, and be in the same account and Region as the scraper. Provisioned clusters with Standard brokers are supported. MSK Serverless clusters are not supported.

Use a VPC source that can connect to the cluster's IAM bootstrap brokers. The exporter authenticates with the scraper's service-linked role. Metrics can be sent to an Amazon Managed Service for Prometheus workspace or a CloudWatch dataset.

You must have an Amazon MSK cluster policy that grants the scraper's service-linked role access to the cluster. Without this policy, the scraper collects no Kafka metrics. For the required actions and example policies, see [Grant the scraper access to the cluster](https://docs.aws.amazon.com/prometheus/latest/userguide/prom-msk-kafka-exporter.html#prom-msk-kafka-exporter-access) in the *Amazon Managed Service for Prometheus User Guide*.

## Contents
<a name="API_KafkaExporterConfiguration_Contents"></a>

 ** clusterArn **   <a name="prometheus-Type-KafkaExporterConfiguration-clusterArn"></a>
The Amazon Resource Name (ARN) of the Amazon MSK cluster.
Type: String
Pattern: `arn:aws[-a-z]*:kafka:[-a-z0-9]+:[0-9]{12}:cluster\/.+`
Required: Yes

 ** consumerGroupFilter **   <a name="prometheus-Type-KafkaExporterConfiguration-consumerGroupFilter"></a>
An anchored RE2 regular expression that selects the Kafka consumer groups to monitor. The expression must start with `^` and end with `$`. If omitted, the default is `^.*$`, which selects all consumer groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** topicFilter **   <a name="prometheus-Type-KafkaExporterConfiguration-topicFilter"></a>
An anchored RE2 regular expression that selects the Kafka topics to monitor. The expression must start with `^` and end with `$`. If omitted, the default is `^.*$`, which selects all topics.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_KafkaExporterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/KafkaExporterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/KafkaExporterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/KafkaExporterConfiguration)
