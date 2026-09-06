---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AccessConfiguration.html
---

# AccessConfiguration
<a name="API_AccessConfiguration"></a>

Access configuration parameters.

## Contents
<a name="API_AccessConfiguration_Contents"></a>

 ** AccessType **   <a name="mediatailor-Type-AccessConfiguration-AccessType"></a>
The type of authentication used to access content from `HttpConfiguration::BaseUrl` on your source location.
 `S3_SIGV4` - AWS Signature Version 4 authentication for Amazon S3 hosted virtual-style access. If your source location base URL is an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the bucket where your source content is stored. Your MediaTailor source location baseURL must follow the S3 virtual hosted-style request URL format. For example, https://bucket-name.s3.Region.amazonaws.com/key-name.
Before you can use `S3_SIGV4`, you must meet these requirements:
• You must allow MediaTailor to access your S3 bucket by granting mediatailor.amazonaws.com principal access in IAM. For information about configuring access in IAM, see Access management in the IAM User Guide.
• The mediatailor.amazonaws.com service principal must have permissions to read all top level manifests referenced by the VodSource packaging configurations.
• The caller of the API must have s3:GetObject IAM permissions to read all top level manifests referenced by your MediaTailor VodSource packaging configurations.
 `AUTODETECT_SIGV4` - AWS Signature Version 4 authentication for a set of supported services: MediaPackage Version 2 and Amazon S3 hosted virtual-style access. If your source location base URL is a MediaPackage Version 2 endpoint or an Amazon S3 bucket, MediaTailor can use AWS Signature Version 4 (SigV4) authentication to access the resource where your source content is stored.
Before you can use `AUTODETECT_SIGV4` with a MediaPackage Version 2 endpoint, you must meet these requirements:
• You must grant MediaTailor access to your MediaPackage endpoint by granting `mediatailor.amazonaws.com` principal access in an Origin Access policy on the endpoint.
• Your MediaTailor source location base URL must be a MediaPackage V2 endpoint.
• The caller of the API must have `mediapackagev2:GetObject` IAM permissions to read all top level manifests referenced by the MediaTailor source packaging configurations.
Before you can use `AUTODETECT_SIGV4` with an Amazon S3 bucket, you must meet these requirements:
• You must grant MediaTailor access to your S3 bucket by granting `mediatailor.amazonaws.com` principal access in IAM. For more information about configuring access in IAM, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide.*.
• The `mediatailor.amazonaws.com` service principal must have permissions to read all top-level manifests referenced by the `VodSource` packaging configurations.
• The caller of the API must have `s3:GetObject` IAM permissions to read all top level manifests referenced by your MediaTailor `VodSource` packaging configurations.
Type: String
Valid Values: `S3_SIGV4 | SECRETS_MANAGER_ACCESS_TOKEN | AUTODETECT_SIGV4`
Required: No

 ** SecretsManagerAccessTokenConfiguration **   <a name="mediatailor-Type-AccessConfiguration-SecretsManagerAccessTokenConfiguration"></a>
AWS Secrets Manager access token configuration parameters.
Type: [SecretsManagerAccessTokenConfiguration](API_SecretsManagerAccessTokenConfiguration.md) object
Required: No

## See Also
<a name="API_AccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AccessConfiguration)
