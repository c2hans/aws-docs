---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_RDFGraphSummaryValueMap.html
---

# RDFGraphSummaryValueMap
<a name="API_RDFGraphSummaryValueMap"></a>

Payload for an RDF graph summary response.

## Contents
<a name="API_RDFGraphSummaryValueMap_Contents"></a>

 ** graphSummary **   <a name="neptunedata-Type-RDFGraphSummaryValueMap-graphSummary"></a>
The graph summary of an RDF graph. See [Graph summary response for an RDF graph](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-graph-summary.html#neptune-graph-summary-rdf-response).
Type: [RDFGraphSummary](API_RDFGraphSummary.md) object
Required: No

 ** lastStatisticsComputationTime **   <a name="neptunedata-Type-RDFGraphSummaryValueMap-lastStatisticsComputationTime"></a>
The timestamp, in ISO 8601 format, of the time at which Neptune last computed statistics.
Type: Timestamp
Required: No

 ** version **   <a name="neptunedata-Type-RDFGraphSummaryValueMap-version"></a>
The version of this graph summary response.
Type: String
Required: No

## See Also
<a name="API_RDFGraphSummaryValueMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/RDFGraphSummaryValueMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/RDFGraphSummaryValueMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/RDFGraphSummaryValueMap)
