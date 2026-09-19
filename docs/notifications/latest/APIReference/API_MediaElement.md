---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_MediaElement.html
---

# MediaElement
<a name="API_MediaElement"></a>

Describes a media element.

## Contents
<a name="API_MediaElement_Contents"></a>

 ** caption **   <a name="Notifications-Type-MediaElement-caption"></a>
The caption of the media.
Type: String
Required: Yes

 ** mediaId **   <a name="Notifications-Type-MediaElement-mediaId"></a>
The unique ID for the media.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** type **   <a name="Notifications-Type-MediaElement-type"></a>
The type of media.
Type: String
Valid Values: `IMAGE`
Required: Yes

 ** url **   <a name="Notifications-Type-MediaElement-url"></a>
The URL of the media.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_MediaElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/MediaElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/MediaElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/MediaElement)
