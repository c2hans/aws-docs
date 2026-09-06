---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_TLSCertificateConfiguration.html
---

# TLSCertificateConfiguration
<a name="API_TLSCertificateConfiguration"></a>

Configurations related to the TLS certificate for the security configuration.

## Contents
<a name="API_TLSCertificateConfiguration_Contents"></a>

 ** certificateProviderType **   <a name="emroneks-Type-TLSCertificateConfiguration-certificateProviderType"></a>
The TLS certificate type. Acceptable values: `PEM` or `Custom`.
Type: String
Valid Values: `PEM`
Required: No

 ** privateCertificateSecretArn **   <a name="emroneks-Type-TLSCertificateConfiguration-privateCertificateSecretArn"></a>
Secrets Manager ARN that contains the private TLS certificate contents, used for communication between the user job and the system job.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):secretsmanager:.+:(\d{12}):secret:[0-9a-zA-Z/_+=.@-]+$`
Required: No

 ** publicCertificateSecretArn **   <a name="emroneks-Type-TLSCertificateConfiguration-publicCertificateSecretArn"></a>
Secrets Manager ARN that contains the public TLS certificate contents, used for communication between the user job and the system job.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):secretsmanager:.+:(\d{12}):secret:[0-9a-zA-Z/_+=.@-]+$`
Required: No

## See Also
<a name="API_TLSCertificateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/TLSCertificateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/TLSCertificateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/TLSCertificateConfiguration)
