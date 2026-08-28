---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CapacityDetails.html
---

# CapacityDetails
<a name="API_CapacityDetails"></a>

Capacity details for an OpenSearch Serverless collection group, including the current capacity and autoscaling status.

## Contents
<a name="API_CapacityDetails_Contents"></a>

 ** autoscalingStatus **   <a name="opensearchserverless-Type-CapacityDetails-autoscalingStatus"></a>
The current autoscaling status for the collection group.
Type: String
Valid Values: `ACTION_SCALING_UP | ACTION_SCALING_DOWN | NO_ACTION`
Required: No

 ** capacityInOcu **   <a name="opensearchserverless-Type-CapacityDetails-capacityInOcu"></a>
The current capacity in OpenSearch Compute Units (OCUs).
Type: Float
Required: No

## See Also
<a name="API_CapacityDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CapacityDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CapacityDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CapacityDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
