---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_NeptuneImportOptions.html
---

# NeptuneImportOptions
<a name="API_NeptuneImportOptions"></a>

Options for how to import Neptune data.

## Contents
<a name="API_NeptuneImportOptions_Contents"></a>

 ** s3ExportKmsKeyId **   <a name="neptunegraph-Type-NeptuneImportOptions-s3ExportKmsKeyId"></a>
The KMS key to use to encrypt data in the S3 bucket where the graph data is exported
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** s3ExportPath **   <a name="neptunegraph-Type-NeptuneImportOptions-s3ExportPath"></a>
The path to an S3 bucket from which to import data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** preserveDefaultVertexLabels **   <a name="neptunegraph-Type-NeptuneImportOptions-preserveDefaultVertexLabels"></a>
Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided. Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting *preserveDefaultVertexLabels* to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when preserveDefaultVertexLabels is set to false.
Type: Boolean
Required: No

 ** preserveEdgeIds **   <a name="neptunegraph-Type-NeptuneImportOptions-preserveEdgeIds"></a>
Neptune Analytics currently does not support user defined edge ids. The edge ids are not imported by default. They are imported if *preserveEdgeIds* is set to true, and ids are stored as properties on the relationships with the property name *neptuneEdgeId*.
Type: Boolean
Required: No

## See Also
<a name="API_NeptuneImportOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/NeptuneImportOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/NeptuneImportOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/NeptuneImportOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
