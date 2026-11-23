---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IdpAuthorizingConfigUpdateInput.html
---

# IdpAuthorizingConfigUpdateInput

The identity provider settings to update. To manage client secrets, use the client secret operations instead.

## Contents
<a name="API_IdpAuthorizingConfigUpdateInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IdpAuthorizingType **   <a name="QS-Type-IdpAuthorizingConfigUpdateInput-IdpAuthorizingType"></a>
How users of the access control application are authenticated.
Type: String
Valid Values: `EXTERNAL_IDP_PUBLIC_AUTH_CODE | EXTERNAL_IDP_CONFIDENTIAL_AUTH_CODE | QUICK_MANAGED_AUTH_CODE | IDC_AUTH_CODE`
Required: Yes

 ** IdcTrustedTokenIssuerConfiguration **   <a name="QS-Type-IdpAuthorizingConfigUpdateInput-IdcTrustedTokenIssuerConfiguration"></a>
A trusted token issuer configuration. When you provide it, Quick Sight authenticates the user with the external IdP and then exchanges the token with IAM Identity Center through the specified trusted token issuer. You can't change it after the application is created.
Type: [IdcTrustedTokenIssuerConfig](API_IdcTrustedTokenIssuerConfig.md) object
Required: No

 ** IdpAuthorizingConfigurationDetailInput **   <a name="QS-Type-IdpAuthorizingConfigUpdateInput-IdpAuthorizingConfigurationDetailInput"></a>
The details of the external IdP configuration. This is present when the `IdpAuthorizingType` is `EXTERNAL_IDP_PUBLIC_AUTH_CODE` or `EXTERNAL_IDP_CONFIDENTIAL_AUTH_CODE`.
Type: [IdpAuthorizingConfigurationDetailUpdateInput](API_IdpAuthorizingConfigurationDetailUpdateInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_IdpAuthorizingConfigUpdateInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IdpAuthorizingConfigUpdateInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IdpAuthorizingConfigUpdateInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IdpAuthorizingConfigUpdateInput)
