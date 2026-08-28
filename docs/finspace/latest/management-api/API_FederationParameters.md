---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_FederationParameters.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# FederationParameters
<a name="API_FederationParameters"></a>

Configuration information when authentication mode is FEDERATED.

## Contents
<a name="API_FederationParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** applicationCallBackURL **   <a name="finspace-Type-FederationParameters-applicationCallBackURL"></a>
The redirect or sign-in URL that should be entered into the SAML 2.0 compliant identity provider configuration (IdP).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^https?://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** attributeMap **   <a name="finspace-Type-FederationParameters-attributeMap"></a>
SAML attribute name and value. The name must always be `Email` and the value should be set to the attribute definition in which user email is set. For example, name would be `Email` and value `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`. Please check your SAML 2.0 compliant identity provider (IdP) documentation for details.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 1. Maximum length of 1000.
Value Pattern: `.*`
Required: No

 ** federationProviderName **   <a name="finspace-Type-FederationParameters-federationProviderName"></a>
Name of the identity provider (IdP).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[^_\p{Z}][\p{L}\p{M}\p{S}\p{N}\p{P}][^_\p{Z}]+`
Required: No

 ** federationURN **   <a name="finspace-Type-FederationParameters-federationURN"></a>
The Uniform Resource Name (URN). Also referred as Service Provider URN or Audience URI or Service Provider Entity ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Za-z0-9._\-:\/#\+]+$`
Required: No

 ** samlMetadataDocument **   <a name="finspace-Type-FederationParameters-samlMetadataDocument"></a>
SAML 2.0 Metadata document from identity provider (IdP).
Type: String
Length Constraints: Minimum length of 1000. Maximum length of 10000000.
Pattern: `.*`
Required: No

 ** samlMetadataURL **   <a name="finspace-Type-FederationParameters-samlMetadataURL"></a>
Provide the metadata URL from your SAML 2.0 compliant identity provider (IdP).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^https?://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

## See Also
<a name="API_FederationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/FederationParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/FederationParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/FederationParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
