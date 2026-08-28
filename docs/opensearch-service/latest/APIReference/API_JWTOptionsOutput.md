---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_JWTOptionsOutput.html
---

# JWTOptionsOutput
<a name="API_JWTOptionsOutput"></a>

Describes the JWT options configured for the domain.

## Contents
<a name="API_JWTOptionsOutput_Contents"></a>

 ** Enabled **   <a name="opensearchservice-Type-JWTOptionsOutput-Enabled"></a>
True if JWT use is enabled.
Type: Boolean
Required: No

 ** JwksUrl **   <a name="opensearchservice-Type-JWTOptionsOutput-JwksUrl"></a>
The configured JWKS URL endpoint from which the cluster retrieves public keys to verify JWT requests.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^$|^https://(?!(?:10|127|169\.254|192\.168|172\.(?:1[6-9]|2[0-9]|3[01]))\.)[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}(?::[0-9]{1,5})?(?:/[a-zA-Z0-9\-._~%!$&'()*+,;=:'@]*(?:/[a-zA-Z0-9\-._~%!$&'()*+,;=:'@]*)*)?(?:\?[a-zA-Z0-9\-._~%!$&'()*+,;=:'/@?]+)?$`
Required: No

 ** PublicKey **   <a name="opensearchservice-Type-JWTOptionsOutput-PublicKey"></a>
The key used to verify the signature of incoming JWT requests.
Type: String
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-JWTOptionsOutput-RolesKey"></a>
The key used for matching the JWT roles attribute.
Type: String
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-JWTOptionsOutput-SubjectKey"></a>
The key used for matching the JWT subject attribute.
Type: String
Required: No

## See Also
<a name="API_JWTOptionsOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/JWTOptionsOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/JWTOptionsOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/JWTOptionsOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
