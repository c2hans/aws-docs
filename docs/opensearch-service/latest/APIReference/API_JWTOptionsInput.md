---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_JWTOptionsInput.html
---

# JWTOptionsInput
<a name="API_JWTOptionsInput"></a>

The JWT authentication and authorization configuration for an Amazon OpenSearch Service domain.

## Contents
<a name="API_JWTOptionsInput_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-JWTOptionsInput-Enabled"></a>
True to enable JWT authentication and authorization for a domain.
Type: Boolean
Required: No

 ** JwksUrl **   <a name="opensearchservice-Type-JWTOptionsInput-JwksUrl"></a>
The URL endpoint that hosts the JSON Web Key Set (JWKS) containing public keys used to verify JWT signatures.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^$|^https://(?!(?:10|127|169\.254|192\.168|172\.(?:1[6-9]|2[0-9]|3[01]))\.)[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}(?::[0-9]{1,5})?(?:/[a-zA-Z0-9\-._~%!$&'()*+,;=:'@]*(?:/[a-zA-Z0-9\-._~%!$&'()*+,;=:'@]*)*)?(?:\?[a-zA-Z0-9\-._~%!$&'()*+,;=:'/@?]+)?$`
Required: No

 ** PublicKey **   <a name="opensearchservice-Type-JWTOptionsInput-PublicKey"></a>
Element of the JWT assertion used by the cluster to verify JWT signatures.
Type: String
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-JWTOptionsInput-RolesKey"></a>
Element of the JWT assertion to use for roles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-JWTOptionsInput-SubjectKey"></a>
Element of the JWT assertion to use for the user name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_JWTOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/JWTOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/JWTOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/JWTOptionsInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
