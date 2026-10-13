---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CertificateConfiguration.html
---

# CertificateConfiguration
<a name="API_CertificateConfiguration"></a>

A reference to a private certificate authority (CA) certificate that the gateway uses to verify TLS connections to the target endpoint. Use this when the target presents a certificate issued by a private CA that is not trusted by default. Specify exactly one certificate source. The configuration is a reference only and never contains the certificate content.

## Contents
<a name="API_CertificateConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="bedrockagentcorecontrol-Type-CertificateConfiguration-s3"></a>
The Amazon S3 location of the PEM-encoded private CA certificate.
Type: [S3CertificateConfiguration](API_S3CertificateConfiguration.md) object
Required: No

 ** secretsManager **   <a name="bedrockagentcorecontrol-Type-CertificateConfiguration-secretsManager"></a>
The AWS Secrets Manager location of the PEM-encoded private CA certificate.
Type: [SecretsManagerCertificateConfiguration](API_SecretsManagerCertificateConfiguration.md) object
Required: No

## See Also
<a name="API_CertificateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CertificateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CertificateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CertificateConfiguration)
