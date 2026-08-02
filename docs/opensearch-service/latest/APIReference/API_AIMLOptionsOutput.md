---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AIMLOptionsOutput.html
---

# AIMLOptionsOutput
<a name="API_AIMLOptionsOutput"></a>

Container for parameters representing the state of machine learning features on the specified domain.

## Contents
<a name="API_AIMLOptionsOutput_Contents"></a>

 ** NaturalLanguageQueryGenerationOptions **   <a name="opensearchservice-Type-AIMLOptionsOutput-NaturalLanguageQueryGenerationOptions"></a>
Container for parameters required for natural language query generation on the specified domain.
Type: [NaturalLanguageQueryGenerationOptionsOutput](API_NaturalLanguageQueryGenerationOptionsOutput.md) object
Required: No

 ** S3VectorsEngine **   <a name="opensearchservice-Type-AIMLOptionsOutput-S3VectorsEngine"></a>
Container for parameters representing the state of S3 vectors engine features on the specified domain.
Type: [S3VectorsEngine](API_S3VectorsEngine.md) object
Required: No

 ** ServerlessVectorAcceleration **   <a name="opensearchservice-Type-AIMLOptionsOutput-ServerlessVectorAcceleration"></a>
The current serverless vector acceleration configuration for the domain.
Type: [ServerlessVectorAcceleration](API_ServerlessVectorAcceleration.md) object
Required: No

## See Also
<a name="API_AIMLOptionsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AIMLOptionsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AIMLOptionsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AIMLOptionsOutput)
