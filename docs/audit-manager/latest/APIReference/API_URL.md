---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_URL.html
---

# URL
<a name="API_URL"></a>

 Short for uniform resource locator. A URL is used as a unique identifier to locate a resource on the internet.

## Contents
<a name="API_URL_Contents"></a>

 ** hyperlinkName **   <a name="auditmanager-Type-URL-hyperlinkName"></a>
 The name or word that's used as a hyperlink to the URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** link **   <a name="auditmanager-Type-URL-link"></a>
 The unique identifier for the internet resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^(https?:\/\/)?(www\.)?[a-zA-Z0-9-_]+([\.]+[a-zA-Z]+)+[\/\w]*$`
Required: No

## See Also
<a name="API_URL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/URL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/URL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/URL)
