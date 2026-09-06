---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_AuthRequest.html
---

# AuthRequest
<a name="API_AuthRequest"></a>

Contains authorization request information, which is required for AWS AppFabric to get the OAuth2 access token for an application.

## Contents
<a name="API_AuthRequest_Contents"></a>

 ** code **   <a name="appfabric-Type-AuthRequest-code"></a>
The authorization code returned by the application after permission is granted in the application OAuth page (after clicking on the AuthURL).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** redirectUri **   <a name="appfabric-Type-AuthRequest-redirectUri"></a>
The redirect URL that is specified in the AuthURL and the application client.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `https://[-a-zA-Z0-9-._~:/?#@!$&'()*+,;=]+`
Required: Yes

## See Also
<a name="API_AuthRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/AuthRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/AuthRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/AuthRequest)
