---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_MskHeader.html
---

# MskHeader

A single Kafka record header. Both Key and Value accept a literal or a JSONata expression (for example, "{% $events.metadata.source %}") resolved once per delivered event.

## Contents
<a name="API_MskHeader_Contents"></a>

 ** Key **   <a name="eventbridgev2-Type-MskHeader-Key"></a>
The header key. Accepts a literal or a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: Yes

 ** Value **   <a name="eventbridgev2-Type-MskHeader-Value"></a>
The header value. Accepts a literal or a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_MskHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/MskHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/MskHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/MskHeader)
