---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DataReference.html
---

# DataReference
<a name="API_amazon-q-connect_DataReference"></a>

Reference data.

## Contents
<a name="API_amazon-q-connect_DataReference_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** contentReference **   <a name="connect-Type-amazon-q-connect_DataReference-contentReference"></a>
Reference information about the content.
Type: [ContentReference](API_amazon-q-connect_ContentReference.md) object
Required: No

 ** generativeReference **   <a name="connect-Type-amazon-q-connect_DataReference-generativeReference"></a>
Reference information about the generative content.
Type: [GenerativeReference](API_amazon-q-connect_GenerativeReference.md) object
Required: No

 ** suggestedMessageReference **   <a name="connect-Type-amazon-q-connect_DataReference-suggestedMessageReference"></a>
Reference information for suggested messages.
Type: [SuggestedMessageReference](API_amazon-q-connect_SuggestedMessageReference.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_DataReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/DataReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/DataReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/DataReference)
