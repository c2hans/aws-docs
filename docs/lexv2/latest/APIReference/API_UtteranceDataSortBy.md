---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UtteranceDataSortBy.html
---

# UtteranceDataSortBy
<a name="API_UtteranceDataSortBy"></a>

An object specifying the measure and method by which to sort the utterance data.

## Contents
<a name="API_UtteranceDataSortBy_Contents"></a>

 ** name **   <a name="lexv2-Type-UtteranceDataSortBy-name"></a>
The measure by which to sort the utterance analytics data.
+  `Count` – The number of utterances.
+  `UtteranceTimestamp` – The date and time of the utterance.
Type: String
Valid Values: `UtteranceTimestamp`
Required: Yes

 ** order **   <a name="lexv2-Type-UtteranceDataSortBy-order"></a>
Specifies whether to sort the results in ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: Yes

## See Also
<a name="API_UtteranceDataSortBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UtteranceDataSortBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UtteranceDataSortBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UtteranceDataSortBy)
