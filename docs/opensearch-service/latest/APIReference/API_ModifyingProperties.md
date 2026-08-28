---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ModifyingProperties.html
---

# ModifyingProperties
<a name="API_ModifyingProperties"></a>

Information about the domain properties that are currently being modified.

## Contents
<a name="API_ModifyingProperties_Contents"></a>

 ** ActiveValue **   <a name="opensearchservice-Type-ModifyingProperties-ActiveValue"></a>
The current value of the domain property that is being modified.
Type: String
Required: No

 ** Name **   <a name="opensearchservice-Type-ModifyingProperties-Name"></a>
The name of the property that is currently being modified.
Type: String
Required: No

 ** PendingValue **   <a name="opensearchservice-Type-ModifyingProperties-PendingValue"></a>
The value that the property that is currently being modified will eventually have.
Type: String
Required: No

 ** ValueType **   <a name="opensearchservice-Type-ModifyingProperties-ValueType"></a>
The type of value that is currently being modified. Properties can have two types:
+  `PLAIN_TEXT`: Contain direct values such as "1", "True", or "c5.large.search".
+  `STRINGIFIED_JSON`: Contain content in JSON format, such as {"Enabled":"True"}".
Type: String
Valid Values: `PLAIN_TEXT | STRINGIFIED_JSON`
Required: No

## See Also
<a name="API_ModifyingProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ModifyingProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ModifyingProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ModifyingProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
