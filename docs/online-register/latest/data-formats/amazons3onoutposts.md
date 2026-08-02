---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazons3onoutposts.html
---

# Data retrieval APIs for Amazon S3 on Outposts
<a name="amazons3onoutposts"></a>

Amazon S3 on Outposts provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="s3-outposts-GetAccessPoint"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html) | Return configuration information about the specified access point | Read |
| <a name="s3-outposts-GetAccessPointPolicy"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html) | Returns the access point policy associated with the specified access point | Read |
| <a name="s3-outposts-GetBucket"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html) | Return the bucket configuration associated with an Amazon S3 bucket | Read |
| <a name="s3-outposts-GetBucketPolicy"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html) | Return the policy of the specified bucket | Read |
| <a name="s3-outposts-GetBucketTagging"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html) | Return the tag set associated with an Amazon S3 bucket | Read |
| <a name="s3-outposts-GetBucketVersioning"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) | Return the versioning state of an Amazon S3 bucket | Read |
| <a name="s3-outposts-GetLifecycleConfiguration"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html) | Return the lifecycle configuration information set on an Amazon S3 bucket | Read |
| <a name="s3-outposts-GetObject"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | Retrieve objects from Amazon S3 | Read |
| <a name="s3-outposts-GetObjectTagging"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) | Return the tag set of an object | Read |
| <a name="s3-outposts-GetObjectVersion"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | Retrieve a specific version of an object | Read |
| <a name="s3-outposts-GetObjectVersionForReplication"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | Replicate both unencrypted objects and objects encrypted with SSE-KMS | Read |
| <a name="s3-outposts-GetObjectVersionTagging"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | Return the tag set for a specific version of the object | Read |
| <a name="s3-outposts-GetReplicationConfiguration"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html) | Get the replication configuration information set on an Amazon S3 bucket | Read |
| <a name="s3-outposts-ListAccessPoints"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html) | List access points | List |
| <a name="s3-outposts-ListBucket"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) | List some or all of the objects in an Amazon S3 bucket (up to 1000) | List |
| <a name="s3-outposts-ListBucketMultipartUploads"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html) | List in-progress multipart uploads | List |
| <a name="s3-outposts-ListBucketVersions"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html) | List metadata about all the versions of objects in an Amazon S3 bucket | List |
| <a name="s3-outposts-ListEndpoints"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html) | List endpoints | List |
| <a name="s3-outposts-ListMultipartUploadParts"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html) | List the parts that have been uploaded for a specific multipart upload | List |
| <a name="s3-outposts-ListOutpostsWithS3"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListOutpostsWithS3.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListOutpostsWithS3.html) | List outposts with S3 capacity | List |
| <a name="s3-outposts-ListRegionalBuckets"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html) | List all buckets owned by the authenticated sender of the request | List |
| <a name="s3-outposts-ListSharedEndpoints"></a>[https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListSharedEndpoints.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListSharedEndpoints.html) | List shared endpoints | List |
