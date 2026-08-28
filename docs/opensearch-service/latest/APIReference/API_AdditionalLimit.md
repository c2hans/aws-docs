---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AdditionalLimit.html
---

# AdditionalLimit
<a name="API_AdditionalLimit"></a>

 List of limits that are specific to a given instance type.

## Contents
<a name="API_AdditionalLimit_Contents"></a>

 ** LimitName **   <a name="opensearchservice-Type-AdditionalLimit-LimitName"></a>
+  `MaximumNumberOfDataNodesSupported` - This attribute only applies to master nodes and specifies the maximum number of data nodes of a given instance type a master node can support.
+  `MaximumNumberOfDataNodesWithoutMasterNode` - This attribute only applies to data nodes and specifies the maximum number of data nodes of a given instance type can exist without a master node governing them.
Type: String
Required: No

 ** LimitValues **   <a name="opensearchservice-Type-AdditionalLimit-LimitValues"></a>
 The values of the additional instance type limits.
Type: Array of strings
Required: No

## See Also
<a name="API_AdditionalLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AdditionalLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AdditionalLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AdditionalLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
