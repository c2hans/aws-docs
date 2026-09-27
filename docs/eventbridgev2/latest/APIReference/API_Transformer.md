---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_Transformer.html
---

# Transformer
<a name="API_Transformer"></a>

Transformer configuration for a subscriber.

## Contents
<a name="API_Transformer_Contents"></a>

 ** JsonataConfiguration **   <a name="eventbridgev2-Type-Transformer-JsonataConfiguration"></a>
JSONata expression configuration. Required when Type is JSONATA.
Type: [JsonataConfiguration](API_JsonataConfiguration.md) object
Required: No

 ** Type **   <a name="eventbridgev2-Type-Transformer-Type"></a>
Transform type.
Type: String
Valid Values: `RAW | WITH_METADATA | JSONATA`
Required: No

## See Also
<a name="API_Transformer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/Transformer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/Transformer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/Transformer)
