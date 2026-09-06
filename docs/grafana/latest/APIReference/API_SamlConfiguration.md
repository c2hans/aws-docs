---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_SamlConfiguration.html
---

# SamlConfiguration
<a name="API_SamlConfiguration"></a>

A structure containing information about how this workspace works with SAML.

## Contents
<a name="API_SamlConfiguration_Contents"></a>

 ** idpMetadata **   <a name="ManagedGrafana-Type-SamlConfiguration-idpMetadata"></a>
A structure containing the identity provider (IdP) metadata used to integrate the identity provider with this workspace.
Type: [IdpMetadata](API_IdpMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** allowedOrganizations **   <a name="ManagedGrafana-Type-SamlConfiguration-allowedOrganizations"></a>
Lists which organizations defined in the SAML assertion are allowed to use the Amazon Managed Grafana workspace. If this is empty, all organizations in the assertion attribute have access.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** assertionAttributes **   <a name="ManagedGrafana-Type-SamlConfiguration-assertionAttributes"></a>
A structure that defines which attributes in the SAML assertion are to be used to define information about the users authenticated by that IdP to use the workspace.
Type: [AssertionAttributes](API_AssertionAttributes.md) object
Required: No

 ** loginValidityDuration **   <a name="ManagedGrafana-Type-SamlConfiguration-loginValidityDuration"></a>
How long a sign-on session by a SAML user is valid, before the user has to sign on again.
Type: Integer
Required: No

 ** roleValues **   <a name="ManagedGrafana-Type-SamlConfiguration-roleValues"></a>
A structure containing arrays that map group names in the SAML assertion to the Grafana `Admin` and `Editor` roles in the workspace.
Type: [RoleValues](API_RoleValues.md) object
Required: No

## See Also
<a name="API_SamlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/SamlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/SamlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/SamlConfiguration)
