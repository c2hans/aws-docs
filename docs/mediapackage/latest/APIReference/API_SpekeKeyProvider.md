---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_SpekeKeyProvider.html
---

# SpekeKeyProvider
<a name="API_SpekeKeyProvider"></a>

The parameters for the SPEKE key provider.

## Contents
<a name="API_SpekeKeyProvider_Contents"></a>

 ** DrmSystems **   <a name="mediapackage-Type-SpekeKeyProvider-DrmSystems"></a>
The DRM solution provider you're using to protect your content during distribution.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `CLEAR_KEY_AES_128 | FAIRPLAY | PLAYREADY | WIDEVINE | IRDETO`
Required: Yes

 ** EncryptionContractConfiguration **   <a name="mediapackage-Type-SpekeKeyProvider-EncryptionContractConfiguration"></a>
Configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.
Type: [EncryptionContractConfiguration](API_EncryptionContractConfiguration.md) object
Required: Yes

 ** ResourceId **   <a name="mediapackage-Type-SpekeKeyProvider-ResourceId"></a>
The unique identifier for the content. The service sends this to the key server to identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.
The following example shows a resource ID: `MovieNight20171126093045`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z_-]+`
Required: Yes

 ** RoleArn **   <a name="mediapackage-Type-SpekeKeyProvider-RoleArn"></a>
The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.
Valid format: `arn:aws:iam::{accountID}:role/{name}`. The following example shows a role ARN: `arn:aws:iam::444455556666:role/SpekeAccess`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Url **   <a name="mediapackage-Type-SpekeKeyProvider-Url"></a>
The URL of the API Gateway proxy that you set up to talk to your key server. The API Gateway proxy must reside in the same AWS Region as MediaPackage and must start with https://.
The following example shows a URL: `https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** CertificateArn **   <a name="mediapackage-Type-SpekeKeyProvider-CertificateArn"></a>
The ARN for the certificate that you imported to AWS Certificate Manager to add content key encryption to this endpoint. For this feature to work, your DRM key provider must support content key encryption.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^:\n]+):acm:([^:\n]+):([0-9]+):certificate/[a-zA-Z0-9-_]+`
Required: No

## See Also
<a name="API_SpekeKeyProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/SpekeKeyProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/SpekeKeyProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/SpekeKeyProvider)
