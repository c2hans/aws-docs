---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageFailure.html
---

# ImageFailure
<a name="API_ImageFailure"></a>

An object that represents an Amazon ECR image failure.

## Contents
<a name="API_ImageFailure_Contents"></a>

 ** failureCode **   <a name="ecrpublic-Type-ImageFailure-failureCode"></a>
The code that's associated with the failure.
Type: String
Valid Values: `InvalidImageDigest | InvalidImageTag | ImageTagDoesNotMatchDigest | ImageNotFound | MissingDigestAndTag | ImageReferencedByManifestList | KmsError`
Required: No

 ** failureReason **   <a name="ecrpublic-Type-ImageFailure-failureReason"></a>
The reason for the failure.
Type: String
Required: No

 ** imageId **   <a name="ecrpublic-Type-ImageFailure-imageId"></a>
The image ID that's associated with the failure.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: No

## See Also
<a name="API_ImageFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/ImageFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/ImageFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/ImageFailure)
