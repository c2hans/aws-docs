---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryInputData.html
---

# QueryInputData
<a name="API_amazon-q-connect_QueryInputData"></a>

Input information for the query.

## Contents
<a name="API_amazon-q-connect_QueryInputData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** caseSummarizationInputData **   <a name="connect-Type-amazon-q-connect_QueryInputData-caseSummarizationInputData"></a>
Input data for case summarization queries.
Type: [CaseSummarizationInputData](API_amazon-q-connect_CaseSummarizationInputData.md) object
Required: No

 ** intentInputData **   <a name="connect-Type-amazon-q-connect_QueryInputData-intentInputData"></a>
Input information for the intent.
Type: [IntentInputData](API_amazon-q-connect_IntentInputData.md) object
Required: No

 ** queryTextInputData **   <a name="connect-Type-amazon-q-connect_QueryInputData-queryTextInputData"></a>
Input information for the query.
Type: [QueryTextInputData](API_amazon-q-connect_QueryTextInputData.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_QueryInputData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QueryInputData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QueryInputData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QueryInputData)
