---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CookieSpecification.html
---

# CookieSpecification
<a name="API_CookieSpecification"></a>

Specifies a single cookie or set of cookies in an end user's browser.

## Contents
<a name="API_CookieSpecification_Contents"></a>

 ** domain **   <a name="workspacesweb-Type-CookieSpecification-domain"></a>
The domain of the cookie.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 253.
Pattern: `(\.?)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)*[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
Required: Yes

 ** name **   <a name="workspacesweb-Type-CookieSpecification-name"></a>
The name of the cookie.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** path **   <a name="workspacesweb-Type-CookieSpecification-path"></a>
The path of the cookie.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Pattern: `/(\S)*`
Required: No

## See Also
<a name="API_CookieSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/CookieSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/CookieSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/CookieSpecification)
