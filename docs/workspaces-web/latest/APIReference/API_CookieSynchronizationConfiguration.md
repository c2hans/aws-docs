---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_CookieSynchronizationConfiguration.html
---

# CookieSynchronizationConfiguration
<a name="API_CookieSynchronizationConfiguration"></a>

The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.

## Contents
<a name="API_CookieSynchronizationConfiguration_Contents"></a>

 ** allowlist **   <a name="workspacesweb-Type-CookieSynchronizationConfiguration-allowlist"></a>
The list of cookie specifications that are allowed to be synchronized to the remote browser.
Type: Array of [CookieSpecification](API_CookieSpecification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** blocklist **   <a name="workspacesweb-Type-CookieSynchronizationConfiguration-blocklist"></a>
The list of cookie specifications that are blocked from being synchronized to the remote browser.
Type: Array of [CookieSpecification](API_CookieSpecification.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CookieSynchronizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/CookieSynchronizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/CookieSynchronizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/CookieSynchronizationConfiguration)
