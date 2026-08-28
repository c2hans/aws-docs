---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GraphSummary.html
---

# GraphSummary
<a name="API_GraphSummary"></a>

Summary details about a graph.

## Contents
<a name="API_GraphSummary_Contents"></a>

 ** arn **   <a name="neptunegraph-Type-GraphSummary-arn"></a>
The ARN associated with the graph.
Type: String
Required: Yes

 ** id **   <a name="neptunegraph-Type-GraphSummary-id"></a>
The unique identifier of the graph.
Type: String
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** name **   <a name="neptunegraph-Type-GraphSummary-name"></a>
The name of the graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: Yes

 ** deletionProtection **   <a name="neptunegraph-Type-GraphSummary-deletionProtection"></a>
If `true`, deletion protection is enabled for the graph.
Type: Boolean
Required: No

 ** endpoint **   <a name="neptunegraph-Type-GraphSummary-endpoint"></a>
The graph endpoint.
Type: String
Required: No

 ** kmsKeyIdentifier **   <a name="neptunegraph-Type-GraphSummary-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt graph data.
Type: String
Required: No

 ** provisionedMemory **   <a name="neptunegraph-Type-GraphSummary-provisionedMemory"></a>
The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.
Required: No

 ** publicConnectivity **   <a name="neptunegraph-Type-GraphSummary-publicConnectivity"></a>
If `true`, the graph has a public endpoint, otherwise not.
Type: Boolean
Required: No

 ** replicaCount **   <a name="neptunegraph-Type-GraphSummary-replicaCount"></a>
The number of replicas for the graph.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** status **   <a name="neptunegraph-Type-GraphSummary-status"></a>
The status of the graph.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | RESETTING | UPDATING | SNAPSHOTTING | FAILED | IMPORTING | STARTING | STOPPING | STOPPED`
Required: No

## See Also
<a name="API_GraphSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GraphSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GraphSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GraphSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
