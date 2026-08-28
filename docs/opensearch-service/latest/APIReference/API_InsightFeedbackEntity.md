---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InsightFeedbackEntity.html
---

# InsightFeedbackEntity
<a name="API_InsightFeedbackEntity"></a>

Specifies the entity for which to submit insight feedback. An entity represents an Amazon OpenSearch Service domain.

## Contents
<a name="API_InsightFeedbackEntity_Contents"></a>

 ** Type **   <a name="opensearchservice-Type-InsightFeedbackEntity-Type"></a>
The type of the entity. Possible values are `DomainName`.
Type: String
Valid Values: `DomainName`
Required: Yes

 ** Value **   <a name="opensearchservice-Type-InsightFeedbackEntity-Value"></a>
The value of the entity, such as a domain name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `([a-z][a-z0-9\-]+|\d{12})`
Required: Yes

## See Also
<a name="API_InsightFeedbackEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/InsightFeedbackEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/InsightFeedbackEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/InsightFeedbackEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
