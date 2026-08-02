---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

An object representing an Amazon ECR image.

## Contents
<a name="API_Image_Contents"></a>

 ** imageId **   <a name="ECR-Type-Image-imageId"></a>
An object containing the image tag and image digest associated with an image.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: No

 ** imageManifest **   <a name="ECR-Type-Image-imageManifest"></a>
The image manifest associated with the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4194304.
Required: No

 ** imageManifestMediaType **   <a name="ECR-Type-Image-imageManifestMediaType"></a>
The manifest media type of the image.
Type: String
Required: No

 ** registryId **   <a name="ECR-Type-Image-registryId"></a>
The AWS account ID associated with the registry containing the image.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** repositoryName **   <a name="ECR-Type-Image-repositoryName"></a>
The name of the repository associated with the image.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/Image)
