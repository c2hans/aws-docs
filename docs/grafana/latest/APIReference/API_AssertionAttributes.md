---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_AssertionAttributes.html
---

# AssertionAttributes
<a name="API_AssertionAttributes"></a>

A structure that defines which attributes in the IdP assertion are to be used to define information about the users authenticated by the IdP to use the workspace.

## Contents
<a name="API_AssertionAttributes_Contents"></a>

 ** email **   <a name="ManagedGrafana-Type-AssertionAttributes-email"></a>
The name of the attribute within the SAML assertion to use as the email names for SAML users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** groups **   <a name="ManagedGrafana-Type-AssertionAttributes-groups"></a>
The name of the attribute within the SAML assertion to use as the user full "friendly" names for user groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** login **   <a name="ManagedGrafana-Type-AssertionAttributes-login"></a>
The name of the attribute within the SAML assertion to use as the login names for SAML users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** name **   <a name="ManagedGrafana-Type-AssertionAttributes-name"></a>
The name of the attribute within the SAML assertion to use as the user full "friendly" names for SAML users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** org **   <a name="ManagedGrafana-Type-AssertionAttributes-org"></a>
The name of the attribute within the SAML assertion to use as the user full "friendly" names for the users' organizations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** role **   <a name="ManagedGrafana-Type-AssertionAttributes-role"></a>
The name of the attribute within the SAML assertion to use as the user roles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AssertionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/AssertionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/AssertionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/AssertionAttributes)
