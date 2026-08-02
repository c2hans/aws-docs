---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12FunctionalGroupHeaders.html
---

# X12FunctionalGroupHeaders
<a name="API_X12FunctionalGroupHeaders"></a>

Part of the X12 message structure. These are the functional group headers for the X12 EDI object.

## Contents
<a name="API_X12FunctionalGroupHeaders_Contents"></a>

 ** applicationReceiverCode **   <a name="b2bi-Type-X12FunctionalGroupHeaders-applicationReceiverCode"></a>
A value representing the code used to identify the party receiving a message, at position GS-03.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 15.
Pattern: `[a-zA-Z0-9 ]*`
Required: No

 ** applicationSenderCode **   <a name="b2bi-Type-X12FunctionalGroupHeaders-applicationSenderCode"></a>
A value representing the code used to identify the party transmitting a message, at position GS-02.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 15.
Pattern: `[a-zA-Z0-9 ]*`
Required: No

 ** responsibleAgencyCode **   <a name="b2bi-Type-X12FunctionalGroupHeaders-responsibleAgencyCode"></a>
A code that identifies the issuer of the standard, at position GS-07.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2.
Pattern: `[a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_X12FunctionalGroupHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12FunctionalGroupHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12FunctionalGroupHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12FunctionalGroupHeaders)
