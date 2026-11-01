---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ClientCertificate.html
---

# ClientCertificate
<a name="API_ClientCertificate"></a>

A client certificate for mutual TLS (mTLS) authentication to target hosts.

## Contents
<a name="API_ClientCertificate_Contents"></a>

 ** name **   <a name="securityagent-Type-ClientCertificate-name"></a>
A customer-chosen name for this client certificate, used in error messages and console display.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]*`
Required: Yes

 ** origins **   <a name="securityagent-Type-ClientCertificate-origins"></a>
The origins (scheme://host[:port]) this certificate applies to. Paths are not supported. Each hostname can have at most one client certificate.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** secretArn **   <a name="securityagent-Type-ClientCertificate-secretArn"></a>
The ARN of the Secrets Manager secret containing the certificate and private key.
Type: String
Required: Yes

## See Also
<a name="API_ClientCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ClientCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ClientCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ClientCertificate)
