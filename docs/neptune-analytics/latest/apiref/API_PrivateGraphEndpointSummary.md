---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_PrivateGraphEndpointSummary.html
---

# PrivateGraphEndpointSummary
<a name="API_PrivateGraphEndpointSummary"></a>

Details about a private graph endpoint.

## Contents
<a name="API_PrivateGraphEndpointSummary_Contents"></a>

 ** status **   <a name="neptunegraph-Type-PrivateGraphEndpointSummary-status"></a>
The status of the private graph endpoint.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | FAILED`
Required: Yes

 ** subnetIds **   <a name="neptunegraph-Type-PrivateGraphEndpointSummary-subnetIds"></a>
The subnet IDs associated with the private graph endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Pattern: `subnet-[a-z0-9]+`
Required: Yes

 ** vpcId **   <a name="neptunegraph-Type-PrivateGraphEndpointSummary-vpcId"></a>
The ID of the VPC in which the private graph endpoint is located.
Type: String
Pattern: `vpc-[a-z0-9]+`
Required: Yes

 ** vpcEndpointId **   <a name="neptunegraph-Type-PrivateGraphEndpointSummary-vpcEndpointId"></a>
The ID of the VPC endpoint.
Type: String
Pattern: `vpce-[0-9a-f]{17}`
Required: No

## See Also
<a name="API_PrivateGraphEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/PrivateGraphEndpointSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/PrivateGraphEndpointSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/PrivateGraphEndpointSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
