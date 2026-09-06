---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_HttpHeader.html
---

# HttpHeader
<a name="API_HttpHeader"></a>

The HTTP header in the `ContextData` parameter.

This data type is a request parameter of server-side authentication operations like [AdminInitiateAuth](API_AdminInitiateAuth.md) and [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md).

## Contents
<a name="API_HttpHeader_Contents"></a>

 ** headerName **   <a name="CognitoUserPools-Type-HttpHeader-headerName"></a>
The header name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** headerValue **   <a name="CognitoUserPools-Type-HttpHeader-headerValue"></a>
The header value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_HttpHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/HttpHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/HttpHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/HttpHeader)
