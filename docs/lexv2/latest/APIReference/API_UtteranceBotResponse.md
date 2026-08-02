---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UtteranceBotResponse.html
---

# UtteranceBotResponse
<a name="API_UtteranceBotResponse"></a>

An object that contains a response to the utterance from the bot.

## Contents
<a name="API_UtteranceBotResponse_Contents"></a>

 ** content **   <a name="lexv2-Type-UtteranceBotResponse-content"></a>
The text of the response to the utterance from the bot.
Type: String
Required: No

 ** contentType **   <a name="lexv2-Type-UtteranceBotResponse-contentType"></a>
The type of the response. The following values are possible:
+  `PlainText` – A plain text string.
+  `CustomPayload` – A response string that you can customize to include data or metadata for your application.
+  `SSML` – A string that includes Speech Synthesis Markup Language to customize the audio response.
+  `ImageResponseCard` – An image with buttons that the customer can select. See [ImageResponseCard](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_ImageResponseCard.html) for more information.
Type: String
Valid Values: `PlainText | CustomPayload | SSML | ImageResponseCard`
Required: No

 ** imageResponseCard **   <a name="lexv2-Type-UtteranceBotResponse-imageResponseCard"></a>
A card that is shown to the user by a messaging platform. You define the contents of the card, the card is displayed by the platform.
When you use a response card, the response from the user is constrained to the text associated with a button on the card.
Type: [ImageResponseCard](API_ImageResponseCard.md) object
Required: No

## See Also
<a name="API_UtteranceBotResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UtteranceBotResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UtteranceBotResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UtteranceBotResponse)
