---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AuthChallengeRequest.html
---

# AuthChallengeRequest
<a name="API_AuthChallengeRequest"></a>

A request made by Amazon Q Business to a third paty authentication server to authenticate a custom plugin user.

## Contents
<a name="API_AuthChallengeRequest_Contents"></a>

 ** authorizationUrl **   <a name="qbusiness-Type-AuthChallengeRequest-authorizationUrl"></a>
The URL sent by Amazon Q Business to the third party authentication server to authenticate a custom plugin user through an OAuth protocol.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: Yes

## See Also
<a name="API_AuthChallengeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AuthChallengeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AuthChallengeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AuthChallengeRequest)
