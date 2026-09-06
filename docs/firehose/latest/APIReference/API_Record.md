---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_Record.html
---

# Record
<a name="API_Record"></a>

The unit of data in a Firehose stream.

## Contents
<a name="API_Record_Contents"></a>

 ** Data **   <a name="Firehose-Type-Record-Data"></a>
The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 0. Maximum length of 1024000.
Required: Yes

## See Also
<a name="API_Record_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/Record)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/Record)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/Record)
