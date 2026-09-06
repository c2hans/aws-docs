---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CustomDomainConfigType.html
---

# CustomDomainConfigType
<a name="API_CustomDomainConfigType"></a>

The configuration for a custom domain, including the SSL certificate and TLS security policy.

This data type is a request parameter of [CreateUserPoolDomain](API_CreateUserPoolDomain.md) and [UpdateUserPoolDomain](API_UpdateUserPoolDomain.md).

## Contents
<a name="API_CustomDomainConfigType_Contents"></a>

 ** CertificateArn **   <a name="CognitoUserPools-Type-CustomDomainConfigType-CertificateArn"></a>
The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: Yes

 ** SecurityPolicy **   <a name="CognitoUserPools-Type-CustomDomainConfigType-SecurityPolicy"></a>
The security policy for the custom domain. Defines the minimum TLS version and cipher suites that Amazon CloudFront supports when communicating with clients. For specific guidance, see [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html). Valid values are as follows:
+  `TLS_V1_3_2025` (strictest): A post-quantum-ready policy requiring TLS 1.3. It provides the strongest security posture and is ideal for workloads where all clients and browsers are updated to the latest versions. [Supported protocols and ciphers for TLSv1.3\_2025](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
+  `TLS_V1_2_2021` (recommended): A post-quantum-ready policy which prefers TLS 1.3 but allows fallback to TLS 1.2 to accommodate older clients. It is the recommended minimum for typical commercial-grade consumer applications. [Supported protocols and ciphers for TLSv1.2\_2021](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
+  `TLS_V1` (strongly discouraged): Permits fallback to TLS 1.0. It offers the broadest compatibility, including support for legacy clients that are more than a decade old. This compatibility comes at the expense of allowing TLS versions and cryptographic algorithms that are no longer considered safe for commercial use. [Supported protocols and ciphers for TLSv1](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
Type: String
Valid Values: `TLS_V1 | TLS_V1_2_2021 | TLS_V1_3_2025`
Required: No

## See Also
<a name="API_CustomDomainConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CustomDomainConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CustomDomainConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CustomDomainConfigType)
