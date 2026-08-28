---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_QueryComputeResponse.html
---

# QueryComputeResponse
<a name="API_query_QueryComputeResponse"></a>

The response to a request to retrieve or update the compute capacity settings for querying data. QueryCompute is available only in the Asia Pacific (Mumbai) region.

## Contents
<a name="API_query_QueryComputeResponse_Contents"></a>

 ** ComputeMode **   <a name="timestream-Type-query_QueryComputeResponse-ComputeMode"></a>
The mode in which Timestream Compute Units (TCUs) are allocated and utilized within an account. Note that in the Asia Pacific (Mumbai) region, the API operation only recognizes the value `PROVISIONED`. QueryCompute is available only in the Asia Pacific (Mumbai) region.
Type: String
Valid Values: `ON_DEMAND | PROVISIONED`
Required: No

 ** ProvisionedCapacity **   <a name="timestream-Type-query_QueryComputeResponse-ProvisionedCapacity"></a>
Configuration object that contains settings for provisioned Timestream Compute Units (TCUs) in your account. QueryCompute is available only in the Asia Pacific (Mumbai) region.
Type: [ProvisionedCapacityResponse](API_query_ProvisionedCapacityResponse.md) object
Required: No

## See Also
<a name="API_query_QueryComputeResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/QueryComputeResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/QueryComputeResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/QueryComputeResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
