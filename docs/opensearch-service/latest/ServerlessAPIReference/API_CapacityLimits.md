---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CapacityLimits.html
---

# CapacityLimits
<a name="API_CapacityLimits"></a>

The maximum capacity limits for all OpenSearch Serverless collections, in OpenSearch Compute Units (OCUs). These limits are used to scale your collections based on the current workload. For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html).

## Contents
<a name="API_CapacityLimits_Contents"></a>

 ** maxIndexingCapacityInOCU **   <a name="opensearchserverless-Type-CapacityLimits-maxIndexingCapacityInOCU"></a>
The maximum indexing capacity for collections.
Type: Integer
Valid Range: Minimum value of 2.
Required: No

 ** maxSearchCapacityInOCU **   <a name="opensearchserverless-Type-CapacityLimits-maxSearchCapacityInOCU"></a>
The maximum search capacity for collections.
Type: Integer
Valid Range: Minimum value of 2.
Required: No

## See Also
<a name="API_CapacityLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CapacityLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CapacityLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CapacityLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
