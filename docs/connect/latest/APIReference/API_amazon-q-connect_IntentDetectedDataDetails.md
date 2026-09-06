---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_IntentDetectedDataDetails.html
---

# IntentDetectedDataDetails
<a name="API_amazon-q-connect_IntentDetectedDataDetails"></a>

Details about the detected intent.

## Contents
<a name="API_amazon-q-connect_IntentDetectedDataDetails_Contents"></a>

 ** intent **   <a name="connect-Type-amazon-q-connect_IntentDetectedDataDetails-intent"></a>
The detected intent.
Type: String
Required: Yes

 ** intentId **   <a name="connect-Type-amazon-q-connect_IntentDetectedDataDetails-intentId"></a>
The identifier of the detected intent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** relevanceLevel **   <a name="connect-Type-amazon-q-connect_IntentDetectedDataDetails-relevanceLevel"></a>
The relevance level of the detected intent.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

## See Also
<a name="API_amazon-q-connect_IntentDetectedDataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/IntentDetectedDataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/IntentDetectedDataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/IntentDetectedDataDetails)
