---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_TlsConfig.html
---

# TlsConfig
<a name="API_TlsConfig"></a>

Specifies the TLS configuration for an integration.

## Contents
<a name="API_TlsConfig_Contents"></a>

 ** insecureSkipVerification **   <a name="apigw-Type-TlsConfig-insecureSkipVerification"></a>
Specifies whether or not API Gateway skips verification that the certificate for an integration endpoint is issued by a supported certificate authority. This isn’t recommended, but it enables you to use certificates that are signed by private certificate authorities, or certificates that are self-signed. If enabled, API Gateway still performs basic certificate validation, which includes checking the certificate's expiration date, hostname, and presence of a root certificate authority. Supported only for `HTTP` and `HTTP_PROXY` integrations.
Enabling `insecureSkipVerification` isn't recommended, especially for integrations with public HTTPS endpoints. If you enable `insecureSkipVerification`, you increase the risk of man-in-the-middle attacks.
Type: Boolean
Required: No

## See Also
<a name="API_TlsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/TlsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/TlsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/TlsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
