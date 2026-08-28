---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_JwtValidationActionConfig.html
---

# JwtValidationActionConfig
<a name="API_JwtValidationActionConfig"></a>

Information about a JSON Web Token (JWT) validation action.

## Contents
<a name="API_JwtValidationActionConfig_Contents"></a>

 ** Issuer **
The issuer of the JWT. The maximum length is 256 characters.
Type: String
Required: Yes

 ** JwksEndpoint **
The JSON Web Key Set (JWKS) endpoint. This endpoint contains JSON Web Keys (JWK) that are used to validate signatures from the provider.
This must be a full URL, including the HTTPS protocol, the domain, and the path. The maximum length is 256 characters.
Type: String
Required: Yes

 ** AdditionalClaims.member.N **
Additional claims to validate. The maximum size of the list is 10. We validate the `exp`, `iss`, `nbf`, and `iat` claims by default.
Type: Array of [JwtValidationActionAdditionalClaim](API_JwtValidationActionAdditionalClaim.md) objects
Required: No

## See Also
<a name="API_JwtValidationActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/JwtValidationActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/JwtValidationActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/JwtValidationActionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
