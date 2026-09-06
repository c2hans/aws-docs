---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3-directory-buckets_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for S3 Directory Buckets using AWS SDKs
<a name="s3-directory-buckets_code_examples"></a>

The following code examples show you how to use Amazon S3 Directory Buckets with an AWS software development kit (SDK).

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ S3 Directory Buckets User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html)** – More information about S3 Directory Buckets.
+ **[S3 Directory Buckets API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)** – Details about all available S3 Directory Buckets actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](s3-directory-buckets_code_examples_basics.md)
  + [Hello Amazon S3 directory buckets](s3-directory-buckets_example_s3-directory-buckets_Hello_section.md)
  + [Learn the basics](s3-directory-buckets_example_s3-directory-buckets_Scenario_ExpressBasics_section.md)
  + [Actions](s3-directory-buckets_code_examples_actions.md)
    + [`AbortMultipartUpload`](s3-directory-buckets_example_s3-directory-buckets_AbortMultipartUpload_section.md)
    + [`CompleteMultipartUpload`](s3-directory-buckets_example_s3-directory-buckets_CompleteMultipartUpload_section.md)
    + [`CopyObject`](s3-directory-buckets_example_s3-directory-buckets_CopyObject_section.md)
    + [`CreateBucket`](s3-directory-buckets_example_s3-directory-buckets_CreateBucket_section.md)
    + [`CreateMultipartUpload`](s3-directory-buckets_example_s3-directory-buckets_CreateMultipartUpload_section.md)
    + [`CreateSession`](s3-directory-buckets_example_s3-directory-buckets_CreateSession_section.md)
    + [`DeleteBucket`](s3-directory-buckets_example_s3-directory-buckets_DeleteBucket_section.md)
    + [`DeleteBucketEncryption`](s3-directory-buckets_example_s3-directory-buckets_DeleteBucketEncryption_section.md)
    + [`DeleteBucketPolicy`](s3-directory-buckets_example_s3-directory-buckets_DeleteBucketPolicy_section.md)
    + [`DeleteObject`](s3-directory-buckets_example_s3-directory-buckets_DeleteObject_section.md)
    + [`DeleteObjects`](s3-directory-buckets_example_s3-directory-buckets_DeleteObjects_section.md)
    + [`GetBucketEncryption`](s3-directory-buckets_example_s3-directory-buckets_GetBucketEncryption_section.md)
    + [`GetBucketPolicy`](s3-directory-buckets_example_s3-directory-buckets_GetBucketPolicy_section.md)
    + [`GetObject`](s3-directory-buckets_example_s3-directory-buckets_GetObject_section.md)
    + [`GetObjectAttributes`](s3-directory-buckets_example_s3-directory-buckets_GetObjectAttributes_section.md)
    + [`HeadBucket`](s3-directory-buckets_example_s3-directory-buckets_HeadBucket_section.md)
    + [`HeadObject`](s3-directory-buckets_example_s3-directory-buckets_HeadObject_section.md)
    + [`ListDirectoryBuckets`](s3-directory-buckets_example_s3-directory-buckets_ListDirectoryBuckets_section.md)
    + [`ListMultipartUploads`](s3-directory-buckets_example_s3-directory-buckets_ListMultipartUploads_section.md)
    + [`ListObjectsV2`](s3-directory-buckets_example_s3-directory-buckets_ListObjectsV2_section.md)
    + [`ListParts`](s3-directory-buckets_example_s3-directory-buckets_ListParts_section.md)
    + [`PutBucketEncryption`](s3-directory-buckets_example_s3-directory-buckets_PutBucketEncryption_section.md)
    + [`PutBucketPolicy`](s3-directory-buckets_example_s3-directory-buckets_PutBucketPolicy_section.md)
    + [`PutObject`](s3-directory-buckets_example_s3-directory-buckets_PutObject_section.md)
    + [`UploadPart`](s3-directory-buckets_example_s3-directory-buckets_UploadPart_section.md)
    + [`UploadPartCopy`](s3-directory-buckets_example_s3-directory-buckets_UploadPartCopy_section.md)
+ [Scenarios](s3-directory-buckets_code_examples_scenarios.md)
  + [Create a presigned URL to get an object](s3-directory-buckets_example_s3-directory-buckets_GeneratePresignedGetURLForDirectoryBucket_section.md)
