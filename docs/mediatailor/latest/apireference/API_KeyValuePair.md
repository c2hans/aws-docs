---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_KeyValuePair.html
---

# KeyValuePair
<a name="API_KeyValuePair"></a>

For `SCTE35_ENHANCED` output, defines a key and corresponding value. MediaTailor generates these pairs within the `EXT-X-ASSET`tag.

## Contents
<a name="API_KeyValuePair_Contents"></a>

 ** Key **   <a name="mediatailor-Type-KeyValuePair-Key"></a>
For `SCTE35_ENHANCED` output, defines a key. MediaTailor takes this key, and its associated value, and generates the key/value pair within the `EXT-X-ASSET`tag. If you specify a key, you must also specify a corresponding value.
Type: String
Required: Yes

 ** Value **   <a name="mediatailor-Type-KeyValuePair-Value"></a>
For `SCTE35_ENHANCED` output, defines a value. MediaTailor; takes this value, and its associated key, and generates the key/value pair within the `EXT-X-ASSET`tag. If you specify a value, you must also specify a corresponding key.
Type: String
Required: Yes

## See Also
<a name="API_KeyValuePair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/KeyValuePair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/KeyValuePair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/KeyValuePair)
