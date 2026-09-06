---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_RDFGraphSummary.html
---

# RDFGraphSummary
<a name="API_RDFGraphSummary"></a>

The RDF graph summary API returns a read-only list of classes and predicate keys, along with counts of quads, subjects, and predicates.

## Contents
<a name="API_RDFGraphSummary_Contents"></a>

 ** classes **   <a name="neptunedata-Type-RDFGraphSummary-classes"></a>
A list of the classes in the graph.
Type: Array of strings
Required: No

 ** numClasses **   <a name="neptunedata-Type-RDFGraphSummary-numClasses"></a>
The number of classes in the graph.
Type: Long
Required: No

 ** numDistinctPredicates **   <a name="neptunedata-Type-RDFGraphSummary-numDistinctPredicates"></a>
The number of distinct predicates in the graph.
Type: Long
Required: No

 ** numDistinctSubjects **   <a name="neptunedata-Type-RDFGraphSummary-numDistinctSubjects"></a>
The number of distinct subjects in the graph.
Type: Long
Required: No

 ** numQuads **   <a name="neptunedata-Type-RDFGraphSummary-numQuads"></a>
The number of quads in the graph.
Type: Long
Required: No

 ** predicates **   <a name="neptunedata-Type-RDFGraphSummary-predicates"></a>
"A list of predicates in the graph, along with the predicate counts.
Type: Array of string to long maps
Required: No

 ** subjectStructures **   <a name="neptunedata-Type-RDFGraphSummary-subjectStructures"></a>
This field is only present when the request mode is `DETAILED`. It contains a list of subject structures.
Type: Array of [SubjectStructure](API_SubjectStructure.md) objects
Required: No

## See Also
<a name="API_RDFGraphSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/RDFGraphSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/RDFGraphSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/RDFGraphSummary)
