---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_ApacheKafkaClusterDescription.html
---

# ApacheKafkaClusterDescription
<a name="API_ApacheKafkaClusterDescription"></a>

The description of the Apache Kafka cluster to which the connector is connected.

## Contents
<a name="API_ApacheKafkaClusterDescription_Contents"></a>

 ** bootstrapServers **   <a name="MSKC-Type-ApacheKafkaClusterDescription-bootstrapServers"></a>
The bootstrap servers of the cluster.
Type: String
Required: No

 ** vpc **   <a name="MSKC-Type-ApacheKafkaClusterDescription-vpc"></a>
Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.
Type: [VpcDescription](API_VpcDescription.md) object
Required: No

## See Also
<a name="API_ApacheKafkaClusterDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ApacheKafkaClusterDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ApacheKafkaClusterDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ApacheKafkaClusterDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
