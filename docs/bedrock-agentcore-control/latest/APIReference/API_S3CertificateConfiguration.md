---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_S3CertificateConfiguration.html
---

# S3CertificateConfiguration
<a name="API_S3CertificateConfiguration"></a>

A reference to a PEM-encoded private CA certificate stored as an Amazon S3 object.

## Contents
<a name="API_S3CertificateConfiguration_Contents"></a>

 ** uri **   <a name="bedrockagentcorecontrol-Type-S3CertificateConfiguration-uri"></a>
The URI of the Amazon S3 object that contains the PEM-encoded certificate.
Type: String
Pattern: `s3://.{1,2043}`
Required: Yes

 ** bucketOwnerAccountId **   <a name="bedrockagentcorecontrol-Type-S3CertificateConfiguration-bucketOwnerAccountId"></a>
The account ID of the Amazon S3 bucket owner. This ID is used for cross-account access to the bucket.
Type: String
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_S3CertificateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/S3CertificateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/S3CertificateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/S3CertificateConfiguration)
