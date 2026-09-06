---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotResolutionSetting.html
---

# SlotResolutionSetting
<a name="API_SlotResolutionSetting"></a>

Contains information about whether assisted slot resolution is turned on for the slot or not.

## Contents
<a name="API_SlotResolutionSetting_Contents"></a>

 ** slotResolutionStrategy **   <a name="lexv2-Type-SlotResolutionSetting-slotResolutionStrategy"></a>
Specifies whether assisted slot resolution is turned on for the slot or not. If the value is `EnhancedFallback`, assisted slot resolution is activated when Amazon Lex defaults to the `AMAZON.FallbackIntent`. If the value is `Default`, assisted slot resolution is turned off.
Type: String
Valid Values: `EnhancedFallback | Default`
Required: Yes

## See Also
<a name="API_SlotResolutionSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/SlotResolutionSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/SlotResolutionSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/SlotResolutionSetting)
