---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InsightField.html
---

# InsightField
<a name="API_InsightField"></a>

Represents a field in the detailed view of an insight, returned by the `DescribeInsightDetails` operation.

## Contents
<a name="API_InsightField_Contents"></a>

 ** Name **   <a name="opensearchservice-Type-InsightField-Name"></a>
The name of the insight field.
Type: String
Required: Yes

 ** Type **   <a name="opensearchservice-Type-InsightField-Type"></a>
The type of the insight field. Possible values are `text` and `metric`.
Type: String
Valid Values: `text | metric`
Required: Yes

 ** Value **   <a name="opensearchservice-Type-InsightField-Value"></a>
The value of the insight field.
Type: String
Required: Yes

## See Also
<a name="API_InsightField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/InsightField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/InsightField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/InsightField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
