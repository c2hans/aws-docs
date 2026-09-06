---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_ArtifactConfigInput.html
---

# ArtifactConfigInput
<a name="API_ArtifactConfigInput"></a>

A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.

## Contents
<a name="API_ArtifactConfigInput_Contents"></a>

 ** S3Encryption **   <a name="synthetics-Type-ArtifactConfigInput-S3Encryption"></a>
A structure that contains the configuration of the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3. Artifact encryption functionality is available only for canaries that use Synthetics runtime version syn-nodejs-puppeteer-3.3 or later. For more information, see [Encrypting canary artifacts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_artifact_encryption.html)
Type: [S3EncryptionConfig](API_S3EncryptionConfig.md) object
Required: No

## See Also
<a name="API_ArtifactConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/ArtifactConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/ArtifactConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/ArtifactConfigInput)
