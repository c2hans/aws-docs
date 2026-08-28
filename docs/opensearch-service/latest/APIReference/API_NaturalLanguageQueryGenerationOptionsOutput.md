---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_NaturalLanguageQueryGenerationOptionsOutput.html
---

# NaturalLanguageQueryGenerationOptionsOutput
<a name="API_NaturalLanguageQueryGenerationOptionsOutput"></a>

Container for parameters representing the state of the natural language query generation feature on the specified domain.

## Contents
<a name="API_NaturalLanguageQueryGenerationOptionsOutput_Contents"></a>

 ** CurrentState **   <a name="opensearchservice-Type-NaturalLanguageQueryGenerationOptionsOutput-CurrentState"></a>
The current state of the natural language query generation feature, indicating completion, in progress, or failure.
Type: String
Valid Values: `NOT_ENABLED | ENABLE_COMPLETE | ENABLE_IN_PROGRESS | ENABLE_FAILED | DISABLE_COMPLETE | DISABLE_IN_PROGRESS | DISABLE_FAILED`
Required: No

 ** DesiredState **   <a name="opensearchservice-Type-NaturalLanguageQueryGenerationOptionsOutput-DesiredState"></a>
The desired state of the natural language query generation feature. Valid values are ENABLED and DISABLED.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_NaturalLanguageQueryGenerationOptionsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/NaturalLanguageQueryGenerationOptionsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/NaturalLanguageQueryGenerationOptionsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/NaturalLanguageQueryGenerationOptionsOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
