---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SessionMetadata.html
---

# SessionMetadata
<a name="API_SessionMetadata"></a>

Contains metadata about the client that streamed the video for a Face Liveness session.

## Contents
<a name="API_SessionMetadata_Contents"></a>

 ** SDKType **   <a name="rekognition-Type-SessionMetadata-SDKType"></a>
The type of SDK that was used to stream the video for the Face Liveness session.
This value is self-reported by the client that streamed the session, and Amazon Rekognition doesn't verify it. Don't rely on it for authentication, authorization, or any other security decision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_SessionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SessionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/SessionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SessionMetadata)
