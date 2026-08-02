---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportFilter.html
---

# ExportFilter
<a name="API_ExportFilter"></a>

This is the top-level field for specifying vertex or edge filters. If the ExportFilter is not provided, then all properties for all labels will be exported. If the ExportFilter is provided but is an empty object, then no data will be exported.

## Contents
<a name="API_ExportFilter_Contents"></a>

 ** edgeFilter **   <a name="neptunegraph-Type-ExportFilter-edgeFilter"></a>
Used to specify filters on a per-label basis for edges. This allows you to control which edge labels and properties are included in the export.
Type: String to [ExportFilterElement](API_ExportFilterElement.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** vertexFilter **   <a name="neptunegraph-Type-ExportFilter-vertexFilter"></a>
Used to specify filters on a per-label basis for vertices. This allows you to control which vertex labels and properties are included in the export.
Type: String to [ExportFilterElement](API_ExportFilterElement.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ExportFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ExportFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ExportFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ExportFilter)
