---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_BatchRevokeSessionError.html
---

# BatchRevokeSessionError

A session that could not be revoked.

## Contents
<a name="API_BatchRevokeSessionError_Contents"></a>

 ** code **   <a name="signin-Type-BatchRevokeSessionError-code"></a>
The error code, for example `ResourceNotFoundException`.
Type: String
Required: Yes

 ** message **   <a name="signin-Type-BatchRevokeSessionError-message"></a>
A description of why the session could not be revoked.
Type: String
Required: Yes

 ** sessionArn **   <a name="signin-Type-BatchRevokeSessionError-sessionArn"></a>
The ARN of the session that could not be revoked.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_BatchRevokeSessionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/BatchRevokeSessionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/BatchRevokeSessionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/BatchRevokeSessionError)
