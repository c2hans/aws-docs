---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportFilterElement.html
---

# ExportFilterElement
<a name="API_ExportFilterElement"></a>

Specifies whihc properties of that label should be included in the export.

## Contents
<a name="API_ExportFilterElement_Contents"></a>

 ** properties **   <a name="neptunegraph-Type-ExportFilterElement-properties"></a>
Each property is defined by a key-value pair, where the key is the desired output property name (e.g. "name"), and the value is an object.
Type: String to [ExportFilterPropertyAttributes](API_ExportFilterPropertyAttributes.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_]+`
Required: No

## See Also
<a name="API_ExportFilterElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ExportFilterElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ExportFilterElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ExportFilterElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
