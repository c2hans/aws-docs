---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageDetail.html
---

# ImageDetail
<a name="API_ImageDetail"></a>

An object that describes an image returned by a [DescribeImages](API_DescribeImages.md) operation.

## Contents
<a name="API_ImageDetail_Contents"></a>

 ** artifactMediaType **   <a name="ECR-Type-ImageDetail-artifactMediaType"></a>
The artifact media type of the image.
Type: String
Required: No

 ** imageDigest **   <a name="ECR-Type-ImageDetail-imageDigest"></a>
The `sha256` digest of the image manifest.
Type: String
Required: No

 ** imageManifestMediaType **   <a name="ECR-Type-ImageDetail-imageManifestMediaType"></a>
The media type of the image manifest.
Type: String
Required: No

 ** imagePushedAt **   <a name="ECR-Type-ImageDetail-imagePushedAt"></a>
The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.
Type: Timestamp
Required: No

 ** imageScanFindingsSummary **   <a name="ECR-Type-ImageDetail-imageScanFindingsSummary"></a>
A summary of the last completed image scan.
Type: [ImageScanFindingsSummary](API_ImageScanFindingsSummary.md) object
Required: No

 ** imageScanStatus **   <a name="ECR-Type-ImageDetail-imageScanStatus"></a>
The current state of the scan.
Type: [ImageScanStatus](API_ImageScanStatus.md) object
Required: No

 ** imageSizeInBytes **   <a name="ECR-Type-ImageDetail-imageSizeInBytes"></a>
The size, in bytes, of the image in the repository.
If the image is a manifest list, this will be the max size of all manifests in the list.
Starting with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the `docker images` command shows the uncompressed image size. Therefore, Docker might return a larger image than the image shown in the AWS Management Console.
Type: Long
Required: No

 ** imageStatus **   <a name="ECR-Type-ImageDetail-imageStatus"></a>
The current status of the image.
Type: String
Valid Values: `ACTIVE | ARCHIVED | ACTIVATING`
Required: No

 ** imageTags **   <a name="ECR-Type-ImageDetail-imageTags"></a>
The list of tags associated with this image.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** lastActivatedAt **   <a name="ECR-Type-ImageDetail-lastActivatedAt"></a>
The date and time, expressed in standard JavaScript date format, when the image was last restored from Amazon ECR archive to Amazon ECR standard.
Type: Timestamp
Required: No

 ** lastArchivedAt **   <a name="ECR-Type-ImageDetail-lastArchivedAt"></a>
The date and time, expressed in standard JavaScript date format, when the image was last transitioned to Amazon ECR archive.
Type: Timestamp
Required: No

 ** lastRecordedPullTime **   <a name="ECR-Type-ImageDetail-lastRecordedPullTime"></a>
The date and time, expressed in standard JavaScript date format, when Amazon ECR recorded the last image pull.
Amazon ECR refreshes the last image pull timestamp at least once every 24 hours. For example, if you pull an image once a day then the `lastRecordedPullTime` timestamp will indicate the exact time that the image was last pulled. However, if you pull an image once an hour, because Amazon ECR refreshes the `lastRecordedPullTime` timestamp at least once every 24 hours, the result may not be the exact time that the image was last pulled.
Type: Timestamp
Required: No

 ** registryId **   <a name="ECR-Type-ImageDetail-registryId"></a>
The AWS account ID associated with the registry to which this image belongs.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** repositoryName **   <a name="ECR-Type-ImageDetail-repositoryName"></a>
The name of the repository to which this image belongs.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

 ** subjectManifestDigest **   <a name="ECR-Type-ImageDetail-subjectManifestDigest"></a>
The digest of the subject manifest for images that are referrers.
Type: String
Required: No

## See Also
<a name="API_ImageDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageDetail)
