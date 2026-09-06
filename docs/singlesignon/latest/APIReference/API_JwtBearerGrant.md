---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_JwtBearerGrant.html
---

# JwtBearerGrant
<a name="API_JwtBearerGrant"></a>

A structure that defines configuration settings for an application that supports the JWT Bearer Token Authorization Grant. The `AuthorizedAudience` field is the aud claim. For more information, see [RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523).

## Contents
<a name="API_JwtBearerGrant_Contents"></a>

 ** AuthorizedTokenIssuers **   <a name="singlesignon-Type-JwtBearerGrant-AuthorizedTokenIssuers"></a>
A list of allowed token issuers trusted by the Identity Center instances for this application.
 `AuthorizedTokenIssuers` is required when the grant type is `JwtBearerGrant`.
Type: Array of [AuthorizedTokenIssuer](API_AuthorizedTokenIssuer.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_JwtBearerGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/JwtBearerGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/JwtBearerGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/JwtBearerGrant)
