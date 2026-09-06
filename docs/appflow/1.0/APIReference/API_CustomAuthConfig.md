---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CustomAuthConfig.html
---

# CustomAuthConfig
<a name="API_CustomAuthConfig"></a>

Configuration information required for custom authentication.

## Contents
<a name="API_CustomAuthConfig_Contents"></a>

 ** authParameters **   <a name="appflow-Type-CustomAuthConfig-authParameters"></a>
Information about authentication parameters required for authentication.
Type: Array of [AuthParameter](API_AuthParameter.md) objects
Required: No

 ** customAuthenticationType **   <a name="appflow-Type-CustomAuthConfig-customAuthenticationType"></a>
The authentication type that the custom connector uses.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

## See Also
<a name="API_CustomAuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CustomAuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CustomAuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CustomAuthConfig)
