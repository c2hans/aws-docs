---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UrlRedirectionConfig.html
---

# UrlRedirectionConfig

Configuration for URL redirection in a specific direction (host-to-client or client-to-host). When enabled, URLs matching the allowed or denied patterns are redirected accordingly. The denied list takes precedence over the allowed list.

## Contents
<a name="API_UrlRedirectionConfig_Contents"></a>

 ** Enabled **   <a name="WorkSpacesApplications-Type-UrlRedirectionConfig-Enabled"></a>
Whether URL redirection is enabled for this direction.
Type: Boolean
Required: Yes

 ** AllowedUrls **   <a name="WorkSpacesApplications-Type-UrlRedirectionConfig-AllowedUrls"></a>
List of URL patterns that are allowed to be redirected. URLs matching these patterns will be redirected unless they also match a pattern in the denied list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((https?|ftp|sftp)://|mailto:)[^\s,;<>]+$`
Required: No

 ** DeniedUrls **   <a name="WorkSpacesApplications-Type-UrlRedirectionConfig-DeniedUrls"></a>
List of URL patterns that are denied from redirection. This list takes precedence over the allowed list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((https?|ftp|sftp)://|mailto:)[^\s,;<>]+$`
Required: No

## See Also
<a name="API_UrlRedirectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UrlRedirectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UrlRedirectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UrlRedirectionConfig)
