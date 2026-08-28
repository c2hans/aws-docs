---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CrossClusterSearchConnectionProperties.html
---

# CrossClusterSearchConnectionProperties
<a name="API_CrossClusterSearchConnectionProperties"></a>

Cross-cluster search specific connection properties.

## Contents
<a name="API_CrossClusterSearchConnectionProperties_Contents"></a>

 ** SkipUnavailable **   <a name="opensearchservice-Type-CrossClusterSearchConnectionProperties-SkipUnavailable"></a>
The status of the `SkipUnavailable` setting for the outbound connection. This feature allows you to specify some clusters as optional and ensure that your cross-cluster queries return partial results despite failures on one or more remote clusters.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_CrossClusterSearchConnectionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CrossClusterSearchConnectionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CrossClusterSearchConnectionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CrossClusterSearchConnectionProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
