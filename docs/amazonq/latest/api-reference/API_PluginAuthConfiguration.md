---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PluginAuthConfiguration.html
---

# PluginAuthConfiguration
<a name="API_PluginAuthConfiguration"></a>

Authentication configuration information for an Amazon Q Business plugin.

## Contents
<a name="API_PluginAuthConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** basicAuthConfiguration **   <a name="qbusiness-Type-PluginAuthConfiguration-basicAuthConfiguration"></a>
Information about the basic authentication credentials used to configure a plugin.
Type: [BasicAuthConfiguration](API_BasicAuthConfiguration.md) object
Required: No

 ** idcAuthConfiguration **   <a name="qbusiness-Type-PluginAuthConfiguration-idcAuthConfiguration"></a>
Information about the AWS IAM Identity Center Application used to configure authentication for a plugin.
Type: [IdcAuthConfiguration](API_IdcAuthConfiguration.md) object
Required: No

 ** noAuthConfiguration **   <a name="qbusiness-Type-PluginAuthConfiguration-noAuthConfiguration"></a>
Information about invoking a custom plugin without any authentication.
Type: [NoAuthConfiguration](API_NoAuthConfiguration.md) object
Required: No

 ** oAuth2ClientCredentialConfiguration **   <a name="qbusiness-Type-PluginAuthConfiguration-oAuth2ClientCredentialConfiguration"></a>
Information about the OAuth 2.0 authentication credential/token used to configure a plugin.
Type: [OAuth2ClientCredentialConfiguration](API_OAuth2ClientCredentialConfiguration.md) object
Required: No

## See Also
<a name="API_PluginAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PluginAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PluginAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PluginAuthConfiguration)
