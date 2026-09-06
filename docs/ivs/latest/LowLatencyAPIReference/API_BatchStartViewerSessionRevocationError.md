---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocationError.html
---

# BatchStartViewerSessionRevocationError
<a name="API_BatchStartViewerSessionRevocationError"></a>

Error for a request in the batch for BatchStartViewerSessionRevocation. Each error is related to a specific channel-ARN and viewer-ID pair.

## Contents
<a name="API_BatchStartViewerSessionRevocationError_Contents"></a>

 ** channelArn **   <a name="ivs-Type-BatchStartViewerSessionRevocationError-channelArn"></a>
Channel ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** viewerId **   <a name="ivs-Type-BatchStartViewerSessionRevocationError-viewerId"></a>
The ID of the viewer session to revoke.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Required: Yes

 ** code **   <a name="ivs-Type-BatchStartViewerSessionRevocationError-code"></a>
Error code.
Type: String
Required: No

 ** message **   <a name="ivs-Type-BatchStartViewerSessionRevocationError-message"></a>
Error message, determined by the application.
Type: String
Required: No

## See Also
<a name="API_BatchStartViewerSessionRevocationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/BatchStartViewerSessionRevocationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/BatchStartViewerSessionRevocationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/BatchStartViewerSessionRevocationError)
