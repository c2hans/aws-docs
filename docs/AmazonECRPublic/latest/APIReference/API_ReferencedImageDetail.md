---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ReferencedImageDetail.html
---

# ReferencedImageDetail
<a name="API_ReferencedImageDetail"></a>

An object that describes the image tag details that are returned by a [DescribeImageTags](API_DescribeImageTags.md) action.

## Contents
<a name="API_ReferencedImageDetail_Contents"></a>

 ** artifactMediaType **   <a name="ecrpublic-Type-ReferencedImageDetail-artifactMediaType"></a>
The artifact media type of the image.
Type: String
Required: No

 ** imageDigest **   <a name="ecrpublic-Type-ReferencedImageDetail-imageDigest"></a>
The `sha256` digest of the image manifest.
Type: String
Required: No

 ** imageManifestMediaType **   <a name="ecrpublic-Type-ReferencedImageDetail-imageManifestMediaType"></a>
The media type of the image manifest.
Type: String
Required: No

 ** imagePushedAt **   <a name="ecrpublic-Type-ReferencedImageDetail-imagePushedAt"></a>
The date and time, expressed in standard JavaScript date format, which the current image tag was pushed to the repository at.
Type: Timestamp
Required: No

 ** imageSizeInBytes **   <a name="ecrpublic-Type-ReferencedImageDetail-imageSizeInBytes"></a>
The size, in bytes, of the image in the repository.
If the image is a manifest list, this is the max size of all manifests in the list.
Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size, so it might return a larger image size than the image sizes that are returned by [DescribeImages](API_DescribeImages.md).
Type: Long
Required: No

## See Also
<a name="API_ReferencedImageDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/ReferencedImageDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/ReferencedImageDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/ReferencedImageDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
