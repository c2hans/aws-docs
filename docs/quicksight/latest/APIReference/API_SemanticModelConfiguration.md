---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SemanticModelConfiguration.html
---

# SemanticModelConfiguration
<a name="API_SemanticModelConfiguration"></a>

Configuration for the semantic model that defines how prepared data is structured for analysis and reporting.

## Contents
<a name="API_SemanticModelConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SemanticMetadata **   <a name="QS-Type-SemanticModelConfiguration-SemanticMetadata"></a>
The dataset-level semantic metadata, including a description and custom instructions.
Type: Array of [DataSetSemanticMetadata](API_DataSetSemanticMetadata.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** TableMap **   <a name="QS-Type-SemanticModelConfiguration-TableMap"></a>
A map of semantic tables that define the analytical structure.
Type: String to [SemanticTable](API_SemanticTable.md) object map
Map Entries: Maximum number of 1 item.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[0-9a-zA-Z-]*`
Required: No

## See Also
<a name="API_SemanticModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SemanticModelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SemanticModelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SemanticModelConfiguration)
