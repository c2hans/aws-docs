---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageDetail.html
---

# ImageDetail
<a name="API_ImageDetail"></a>

An object that describes an image that's returned by a [DescribeImages](API_DescribeImages.md) operation.

## Contents
<a name="API_ImageDetail_Contents"></a>

 ** artifactMediaType **   <a name="ecrpublic-Type-ImageDetail-artifactMediaType"></a>
The artifact media type of the image.
Type: String
Required: No

 ** imageDigest **   <a name="ecrpublic-Type-ImageDetail-imageDigest"></a>
The `sha256` digest of the image manifest.
Type: String
Required: No

 ** imageManifestMediaType **   <a name="ecrpublic-Type-ImageDetail-imageManifestMediaType"></a>
The media type of the image manifest.
Type: String
Required: No

 ** imagePushedAt **   <a name="ecrpublic-Type-ImageDetail-imagePushedAt"></a>
The date and time, expressed in standard JavaScript date format, that the current image was pushed to the repository at.
Type: Timestamp
Required: No

 ** imageSizeInBytes **   <a name="ecrpublic-Type-ImageDetail-imageSizeInBytes"></a>
The size, in bytes, of the image in the repository.
If the image is a manifest list, this is the max size of all manifests in the list.
Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size, so it might return a larger image size than the image sizes that are returned by [DescribeImages](API_DescribeImages.md).
Type: Long
Required: No

 ** imageTags **   <a name="ecrpublic-Type-ImageDetail-imageTags"></a>
The list of tags that's associated with this image.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** registryId **   <a name="ecrpublic-Type-ImageDetail-registryId"></a>
The AWS account ID that's associated with the public registry where this image belongs.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** repositoryName **   <a name="ecrpublic-Type-ImageDetail-repositoryName"></a>
The name of the repository where this image belongs.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: No

## See Also
<a name="API_ImageDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/ImageDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/ImageDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/ImageDetail)
