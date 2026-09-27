---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_SnsMessageAttributeValue.html
---

# SnsMessageAttributeValue
<a name="API_SnsMessageAttributeValue"></a>

A custom SNS message attribute (data type plus string or binary value).

## Contents
<a name="API_SnsMessageAttributeValue_Contents"></a>

 ** BinaryValue **   <a name="eventbridgev2-Type-SnsMessageAttributeValue-BinaryValue"></a>
Base64-encoded literal binary attribute value.
Type: String
Required: No

 ** DataType **   <a name="eventbridgev2-Type-SnsMessageAttributeValue-DataType"></a>
Attribute data type. Requiredness and the accepted vocabulary belong to SNS, which rejects an attribute without a data type on delivery.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** StringValue **   <a name="eventbridgev2-Type-SnsMessageAttributeValue-StringValue"></a>
String attribute value. A JSONata expression resolves once per delivered event.
Type: String
Required: No

## See Also
<a name="API_SnsMessageAttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/SnsMessageAttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/SnsMessageAttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/SnsMessageAttributeValue)
