---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SpliceInsertMessage.html
---

# SpliceInsertMessage
<a name="API_SpliceInsertMessage"></a>

Splice insert message configuration.

## Contents
<a name="API_SpliceInsertMessage_Contents"></a>

 ** AvailNum **   <a name="mediatailor-Type-SpliceInsertMessage-AvailNum"></a>
This is written to `splice_insert.avail_num`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0`. Values must be between `0` and `256`, inclusive.
Type: Integer
Required: No

 ** AvailsExpected **   <a name="mediatailor-Type-SpliceInsertMessage-AvailsExpected"></a>
This is written to `splice_insert.avails_expected`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0`. Values must be between `0` and `256`, inclusive.
Type: Integer
Required: No

 ** SpliceEventId **   <a name="mediatailor-Type-SpliceInsertMessage-SpliceEventId"></a>
This is written to `splice_insert.splice_event_id`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `1`.
Type: Integer
Required: No

 ** UniqueProgramId **   <a name="mediatailor-Type-SpliceInsertMessage-UniqueProgramId"></a>
This is written to `splice_insert.unique_program_id`, as defined in section 9.7.3.1 of the SCTE-35 specification. The default value is `0`. Values must be between `0` and `256`, inclusive.
Type: Integer
Required: No

## See Also
<a name="API_SpliceInsertMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/SpliceInsertMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/SpliceInsertMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/SpliceInsertMessage)
