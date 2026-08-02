---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UrlEndpointInput.html
---

# UrlEndpointInput
<a name="API_UrlEndpointInput"></a>

The configuration for the URL endpoint type.

## Contents
<a name="API_UrlEndpointInput_Contents"></a>

 ** Url **   <a name="migrationhubrefactorspaces-Type-UrlEndpointInput-Url"></a>
The URL to route traffic to. The URL must be an [rfc3986-formatted URL](https://datatracker.ietf.org/doc/html/rfc3986). If the host is a domain name, the name must be resolvable over the public internet. If the scheme is `https`, the top level domain of the host must be listed in the [IANA root zone database](https://www.iana.org/domains/root/db).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]`
Required: Yes

 ** HealthUrl **   <a name="migrationhubrefactorspaces-Type-UrlEndpointInput-HealthUrl"></a>
The health check URL of the URL endpoint type. If the URL is a public endpoint, the `HealthUrl` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]`
Required: No

## See Also
<a name="API_UrlEndpointInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/UrlEndpointInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/UrlEndpointInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/UrlEndpointInput)
