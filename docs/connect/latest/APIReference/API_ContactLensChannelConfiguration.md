---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactLensChannelConfiguration.html
---

# ContactLensChannelConfiguration

The per-channel conversational analytics configuration for a contact.

## Contents
<a name="API_ContactLensChannelConfiguration_Contents"></a>

 ** AnalyticsModes **   <a name="connect-Type-ContactLensChannelConfiguration-AnalyticsModes"></a>
The conversational analytics modes enabled for the channel. Valid values:
+  `RealTime` – Real-time analysis is enabled during the contact. Voice channel only.
+  `PostContact` – Post-contact analysis is enabled after the contact ends. Voice channel only.
+  `ContactLens` – Conversational analytics is enabled for the contact. Chat channel only.
Type: Array of strings
Required: No

## See Also
<a name="API_ContactLensChannelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactLensChannelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactLensChannelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactLensChannelConfiguration)
