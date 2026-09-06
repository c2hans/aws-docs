---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12AcknowledgmentOptions.html
---

# X12AcknowledgmentOptions
<a name="API_X12AcknowledgmentOptions"></a>

Contains options for configuring X12 acknowledgments. These options control how functional and technical acknowledgments are handled.

## Contents
<a name="API_X12AcknowledgmentOptions_Contents"></a>

 ** functionalAcknowledgment **   <a name="b2bi-Type-X12AcknowledgmentOptions-functionalAcknowledgment"></a>
Specifies whether functional acknowledgments (997/999) should be generated for incoming X12 transactions. Valid values are `DO_NOT_GENERATE`, `GENERATE_ALL_SEGMENTS` and `GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP`.
If you choose `GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP`, AWS B2B Data Interchange skips the AK2\_Loop when generating an acknowledgment document.
Type: String
Valid Values: `DO_NOT_GENERATE | GENERATE_ALL_SEGMENTS | GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP`
Required: Yes

 ** technicalAcknowledgment **   <a name="b2bi-Type-X12AcknowledgmentOptions-technicalAcknowledgment"></a>
Specifies whether technical acknowledgments (TA1) should be generated for incoming X12 interchanges. Valid values are `DO_NOT_GENERATE` and `GENERATE_ALL_SEGMENTS` and.
Type: String
Valid Values: `DO_NOT_GENERATE | GENERATE_ALL_SEGMENTS`
Required: Yes

## See Also
<a name="API_X12AcknowledgmentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12AcknowledgmentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12AcknowledgmentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12AcknowledgmentOptions)
