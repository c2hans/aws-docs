---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-APIs.html
---

# Directory bucket API operations
<a name="s3-express-APIs"></a>

To manage directory buckets, you can use Regional (bucket level, or control plane) endpoint API operations. To manage objects in your directory buckets, you can use Zonal (object level, or data plane) endpoint API operations. For more information, see [Networking for directory buckets](s3-express-networking.md) and [Endpoints and gateway VPC endpoints](directory-bucket-high-performance.md#s3-express-overview-endpoints).

**Regional endpoint API operations**
The following Regional endpoint API operations are supported for directory buckets:
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointScope.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointScope.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointScope.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointScope.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointScope.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointScope.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html)

**Zonal endpoint API operations**
The following Zonal endpoint API operations are supported for directory buckets:
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateSession.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_RenameObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RenameObject.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)
+ [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)
