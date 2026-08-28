---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AIMLOptionsInput.html
---

# AIMLOptionsInput
<a name="API_AIMLOptionsInput"></a>

Container for parameters required to enable all machine learning features.

## Contents
<a name="API_AIMLOptionsInput_Contents"></a>

 ** NaturalLanguageQueryGenerationOptions **   <a name="opensearchservice-Type-AIMLOptionsInput-NaturalLanguageQueryGenerationOptions"></a>
Container for parameters required for natural language query generation on the specified domain.
Type: [NaturalLanguageQueryGenerationOptionsInput](API_NaturalLanguageQueryGenerationOptionsInput.md) object
Required: No

 ** S3VectorsEngine **   <a name="opensearchservice-Type-AIMLOptionsInput-S3VectorsEngine"></a>
Container for parameters required to enable S3 vectors engine features on the specified domain.
Type: [S3VectorsEngine](API_S3VectorsEngine.md) object
Required: No

 ** ServerlessVectorAcceleration **   <a name="opensearchservice-Type-AIMLOptionsInput-ServerlessVectorAcceleration"></a>
Specifies whether to enable serverless vector acceleration for the domain. When enabled, provides [GPU-accelerated](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gpu-acceleration-vector-index.html) vector search capabilities for improved performance on vector workloads.
Type: [ServerlessVectorAcceleration](API_ServerlessVectorAcceleration.md) object
Required: No

## See Also
<a name="API_AIMLOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AIMLOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AIMLOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AIMLOptionsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
