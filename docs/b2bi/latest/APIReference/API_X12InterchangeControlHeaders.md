---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12InterchangeControlHeaders.html
---

# X12InterchangeControlHeaders
<a name="API_X12InterchangeControlHeaders"></a>

In X12, the Interchange Control Header is the first segment of an EDI document and is part of the Interchange Envelope. It contains information about the sender and receiver, the date and time of transmission, and the X12 version being used. It also includes delivery information, such as the sender and receiver IDs.

## Contents
<a name="API_X12InterchangeControlHeaders_Contents"></a>

 ** acknowledgmentRequestedCode **   <a name="b2bi-Type-X12InterchangeControlHeaders-acknowledgmentRequestedCode"></a>
Located at position ISA-14 in the header. The value "1" indicates that the sender is requesting an interchange acknowledgment at receipt of the interchange. The value "0" is used otherwise.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** receiverId **   <a name="b2bi-Type-X12InterchangeControlHeaders-receiverId"></a>
Located at position ISA-08 in the header. This value (along with the `receiverIdQualifier`) identifies the intended recipient of the interchange.
Type: String
Length Constraints: Fixed length of 15.
Pattern: `[a-zA-Z0-9 ]*`
Required: No

 ** receiverIdQualifier **   <a name="b2bi-Type-X12InterchangeControlHeaders-receiverIdQualifier"></a>
Located at position ISA-07 in the header. Qualifier for the receiver ID. Together, the ID and qualifier uniquely identify the receiving trading partner.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** repetitionSeparator **   <a name="b2bi-Type-X12InterchangeControlHeaders-repetitionSeparator"></a>
Located at position ISA-11 in the header. This string makes it easier when you need to group similar adjacent element values together without using extra segments.
This parameter is only honored for version greater than 401 (`VERSION_4010` and higher).
For versions less than 401, this field is called [StandardsId](https://www.stedi.com/edi/x12-004010/segment/ISA#ISA-11), in which case our service sets the value to `U`.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** senderId **   <a name="b2bi-Type-X12InterchangeControlHeaders-senderId"></a>
Located at position ISA-06 in the header. This value (along with the `senderIdQualifier`) identifies the sender of the interchange.
Type: String
Length Constraints: Fixed length of 15.
Pattern: `[a-zA-Z0-9 ]*`
Required: No

 ** senderIdQualifier **   <a name="b2bi-Type-X12InterchangeControlHeaders-senderIdQualifier"></a>
Located at position ISA-05 in the header. Qualifier for the sender ID. Together, the ID and qualifier uniquely identify the sending trading partner.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** usageIndicatorCode **   <a name="b2bi-Type-X12InterchangeControlHeaders-usageIndicatorCode"></a>
Located at position ISA-15 in the header. Specifies how this interchange is being used:
+  `T` indicates this interchange is for testing.
+  `P` indicates this interchange is for production.
+  `I` indicates this interchange is informational.
Type: String
Length Constraints: Fixed length of 1.
Pattern: `[a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_X12InterchangeControlHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12InterchangeControlHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12InterchangeControlHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12InterchangeControlHeaders)
