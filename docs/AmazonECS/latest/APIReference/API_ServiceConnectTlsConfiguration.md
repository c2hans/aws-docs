---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectTlsConfiguration.html
---

# ServiceConnectTlsConfiguration
<a name="API_ServiceConnectTlsConfiguration"></a>

The key that encrypts and decrypts your resources for Service Connect TLS.

## Contents
<a name="API_ServiceConnectTlsConfiguration_Contents"></a>

 ** issuerCertificateAuthority **   <a name="ECS-Type-ServiceConnectTlsConfiguration-issuerCertificateAuthority"></a>
The signer certificate authority.
Type: [ServiceConnectTlsCertificateAuthority](API_ServiceConnectTlsCertificateAuthority.md) object
Required: Yes

 ** kmsKey **   <a name="ECS-Type-ServiceConnectTlsConfiguration-kmsKey"></a>
The AWS Key Management Service key.
Type: String
Required: No

 ** roleArn **   <a name="ECS-Type-ServiceConnectTlsConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that's associated with the Service Connect TLS.
Type: String
Required: No

## See Also
<a name="API_ServiceConnectTlsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceConnectTlsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceConnectTlsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceConnectTlsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
