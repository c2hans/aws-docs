---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RcsCarousel.html
---

# RcsCarousel
<a name="API_RcsCarousel"></a>

A carousel of 2 to 10 scrollable rich cards.

## Contents
<a name="API_RcsCarousel_Contents"></a>

 ** CardContents **   <a name="pinpoint-Type-RcsCarousel-CardContents"></a>
The list of cards in the carousel. Minimum 2, maximum 10 cards.
Type: Array of [RcsCarouselCardContent](API_RcsCarouselCardContent.md) objects
Array Members: Minimum number of 2 items. Maximum number of 10 items.
Required: Yes

 ** CardWidth **   <a name="pinpoint-Type-RcsCarousel-CardWidth"></a>
The width of cards in the carousel. Valid values are SMALL and MEDIUM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[A-Z_]+`
Required: Yes

## See Also
<a name="API_RcsCarousel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RcsCarousel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RcsCarousel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RcsCarousel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
