---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_GoogleOidcConfig.html
---

# GoogleOidcConfig
<a name="API_GoogleOidcConfig"></a>

External identity parameters for Google Cloud Storage.

## Contents
<a name="API_GoogleOidcConfig_Contents"></a>

 ** IdentityPoolName **   <a name="DataSync-Type-GoogleOidcConfig-IdentityPoolName"></a>
Human-readable pool name (e.g. "my-pool").
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `^(?!gcp-)[a-z][a-z0-9-]{2,30}[a-z0-9]$`
Required: Yes

 ** IdentityProviderName **   <a name="DataSync-Type-GoogleOidcConfig-IdentityProviderName"></a>
Human-readable provider name (e.g. "my-oidc-provider").
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `^(?!gcp-)[a-z][a-z0-9-]{2,30}[a-z0-9]$`
Required: Yes

 ** ProjectName **   <a name="DataSync-Type-GoogleOidcConfig-ProjectName"></a>
Human-readable project name (e.g. "my-project").
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `^[a-z][a-z0-9-]{4,28}[a-z0-9]$`
Required: Yes

 ** ProjectNumber **   <a name="DataSync-Type-GoogleOidcConfig-ProjectNumber"></a>
Numeric project ID as a string (e.g. "123456789").
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[0-9]+$`
Required: Yes

## See Also
<a name="API_GoogleOidcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/GoogleOidcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/GoogleOidcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/GoogleOidcConfig)
