---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AuthorizationCodeGrant.html
---

# AuthorizationCodeGrant
<a name="API_AuthorizationCodeGrant"></a>

A structure that defines configuration settings for an application that supports the OAuth 2.0 Authorization Code Grant.

## Contents
<a name="API_AuthorizationCodeGrant_Contents"></a>

 ** RedirectUris **   <a name="singlesignon-Type-AuthorizationCodeGrant-RedirectUris"></a>
A list of URIs that are valid locations to redirect a user's browser after the user is authorized.
RedirectUris is required when the grant type is `authorization_code`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AuthorizationCodeGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AuthorizationCodeGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AuthorizationCodeGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AuthorizationCodeGrant)
