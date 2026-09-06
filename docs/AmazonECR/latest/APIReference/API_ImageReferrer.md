---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageReferrer.html
---

# ImageReferrer
<a name="API_ImageReferrer"></a>

An object representing an artifact associated with a subject image.

## Contents
<a name="API_ImageReferrer_Contents"></a>

 ** digest **   <a name="ECR-Type-ImageReferrer-digest"></a>
The digest of the artifact manifest.
Type: String
Required: Yes

 ** mediaType **   <a name="ECR-Type-ImageReferrer-mediaType"></a>
The media type of the artifact manifest.
Type: String
Required: Yes

 ** size **   <a name="ECR-Type-ImageReferrer-size"></a>
The size, in bytes, of the artifact.
Type: Long
Required: Yes

 ** annotations **   <a name="ECR-Type-ImageReferrer-annotations"></a>
A map of annotations associated with the artifact.
Type: String to string map
Required: No

 ** artifactStatus **   <a name="ECR-Type-ImageReferrer-artifactStatus"></a>
The status of the artifact. Valid values are `ACTIVE`, `ARCHIVED`, or `ACTIVATING`.
Type: String
Valid Values: `ACTIVE | ARCHIVED | ACTIVATING`
Required: No

 ** artifactType **   <a name="ECR-Type-ImageReferrer-artifactType"></a>
A string identifying the type of artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ImageReferrer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageReferrer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageReferrer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageReferrer)
