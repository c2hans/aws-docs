---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ResultData.html
---

# ResultData
<a name="API_amazon-q-connect_ResultData"></a>

Information about the result.

## Contents
<a name="API_amazon-q-connect_ResultData_Contents"></a>

 ** resultId **   <a name="connect-Type-amazon-q-connect_ResultData-resultId"></a>
The identifier of the result data.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** data **   <a name="connect-Type-amazon-q-connect_ResultData-data"></a>
 Summary of the recommended content.
Type: [DataSummary](API_amazon-q-connect_DataSummary.md) object
Required: No

 ** document **   <a name="connect-Type-amazon-q-connect_ResultData-document"></a>
The document.
Type: [Document](API_amazon-q-connect_Document.md) object
Required: No

 ** relevanceScore **   <a name="connect-Type-amazon-q-connect_ResultData-relevanceScore"></a>
The relevance score of the results.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** type **   <a name="connect-Type-amazon-q-connect_ResultData-type"></a>
The type of the query result.
Type: String
Valid Values: `KNOWLEDGE_CONTENT | INTENT_ANSWER | GENERATIVE_ANSWER | GENERATIVE_ANSWER_CHUNK | BLOCKED_GENERATIVE_ANSWER_CHUNK | INTENT_ANSWER_CHUNK | BLOCKED_INTENT_ANSWER_CHUNK | EMAIL_RESPONSE_CHUNK | EMAIL_OVERVIEW_CHUNK | EMAIL_GENERATIVE_ANSWER_CHUNK | CASE_SUMMARIZATION_CHUNK | BLOCKED_CASE_SUMMARIZATION_CHUNK | NOTES | NOTES_CHUNK | BLOCKED_NOTES_CHUNK`
Required: No

## See Also
<a name="API_amazon-q-connect_ResultData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ResultData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ResultData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ResultData)
