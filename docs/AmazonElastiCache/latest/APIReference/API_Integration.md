---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Integration.html
---

# Integration

An integration configured on the serverless cache, and its current status. ElastiCache supports DynamoDB integration.

## Contents
<a name="API_Integration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IntegrationType **
The integration type. ElastiCache supports `dynamodb`.
Type: String
Valid Values: `dynamodb`
Required: No

 ** Status **
The current status of the integration. Valid values are:
+  `enabled` – The integration is enabled.
+  `disabled` – The integration is disabled.
Type: String
Valid Values: `enabled | disabled | enabling | disabling | failed`
Required: No

## See Also
<a name="API_Integration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Integration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Integration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Integration)
