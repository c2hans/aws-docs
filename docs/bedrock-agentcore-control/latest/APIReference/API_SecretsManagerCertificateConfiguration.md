---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SecretsManagerCertificateConfiguration.html
---

# SecretsManagerCertificateConfiguration
<a name="API_SecretsManagerCertificateConfiguration"></a>

A reference to a PEM-encoded private CA certificate stored in an AWS Secrets Manager secret.

## Contents
<a name="API_SecretsManagerCertificateConfiguration_Contents"></a>

 ** secretArn **   <a name="bedrockagentcorecontrol-Type-SecretsManagerCertificateConfiguration-secretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the PEM-encoded certificate.
Type: String
Pattern: `arn:aws(-[^:]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:.+`
Required: Yes

## See Also
<a name="API_SecretsManagerCertificateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SecretsManagerCertificateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SecretsManagerCertificateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SecretsManagerCertificateConfiguration)
