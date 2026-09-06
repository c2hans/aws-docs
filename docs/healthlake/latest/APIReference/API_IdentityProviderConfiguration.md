---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html
---

# IdentityProviderConfiguration
<a name="API_IdentityProviderConfiguration"></a>

The identity provider configuration selected when the data store was created.

## Contents
<a name="API_IdentityProviderConfiguration_Contents"></a>

 ** AuthorizationStrategy **   <a name="HealthLake-Type-IdentityProviderConfiguration-AuthorizationStrategy"></a>
The authorization strategy selected when the AWS HealthLake data store is created.
 AWS HealthLake provides support for both SMART on FHIR V1 and V2 as described below.
+  `SMART_ON_FHIR_V1` – Support for only SMART on FHIR V1, which includes `read` (read/search) and `write` (create/update/delete) permissions.
+  `SMART_ON_FHIR` – Support for both SMART on FHIR V1 and V2, which includes `create`, `read`, `update`, `delete`, and `search` permissions.
+  ` AWS_AUTH` – The default AWS HealthLake authorization strategy; not affiliated with SMART on FHIR.
Type: String
Valid Values: `SMART_ON_FHIR_V1 | SMART_ON_FHIR | AWS_AUTH`
Required: Yes

 ** FineGrainedAuthorizationEnabled **   <a name="HealthLake-Type-IdentityProviderConfiguration-FineGrainedAuthorizationEnabled"></a>
The parameter to enable SMART on FHIR fine-grained authorization for the data store.
Type: Boolean
Required: No

 ** IdpLambdaArn **   <a name="HealthLake-Type-IdentityProviderConfiguration-IdpLambdaArn"></a>
The Amazon Resource Name (ARN) of the Lambda function to use to decode the access token created by the authorization server.
Type: String
Length Constraints: Minimum length of 49. Maximum length of 256.
Pattern: `arn:aws:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9\-_\.]+(:(\$LATEST|[a-zA-Z0-9\-_]+))?`
Required: No

 ** Metadata **   <a name="HealthLake-Type-IdentityProviderConfiguration-Metadata"></a>
The JSON metadata elements to use in your identity provider configuration. Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see [Metadata](https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata) in SMART's App Launch specification.
 `authorization_endpoint`: The URL to the OAuth2 authorization endpoint.
 `grant_types_supported`: An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are `authorization_code` and `client_credentials`.
 `token_endpoint`: The URL to the OAuth2 token endpoint.
 `capabilities`: An array of strings of the SMART capabilities that the authorization server supports.
 `code_challenge_methods_supported`: An array of strings of supported PKCE code challenge methods. You must include the `S256` method in the array of PKCE code challenge methods.
Type: String
Required: No

## See Also
<a name="API_IdentityProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/IdentityProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/IdentityProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/IdentityProviderConfiguration)
