---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AfterContactWorkConfig.html
---

# AfterContactWorkConfig
<a name="API_AfterContactWorkConfig"></a>

Configuration settings for after contact work (ACW) timeout.

## Contents
<a name="API_AfterContactWorkConfig_Contents"></a>

 ** AfterContactWorkTimeLimit **   <a name="connect-Type-AfterContactWorkConfig-AfterContactWorkTimeLimit"></a>
The after contact work (ACW) timeout duration in seconds. Minimum: 1 second. Maximum: 2,000,000 seconds (24 days). For the CHAT channel, the maximum for a specific duration is 5,400 seconds (90 minutes); higher values end ACW after 90 minutes. For all channels, including chat, you can enter 0 for an indefinite amount of time, meaning agents must manually choose to end ACW.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_AfterContactWorkConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AfterContactWorkConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AfterContactWorkConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AfterContactWorkConfig)
