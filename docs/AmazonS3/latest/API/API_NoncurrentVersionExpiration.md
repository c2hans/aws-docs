---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_NoncurrentVersionExpiration.html
---

# NoncurrentVersionExpiration
<a name="API_NoncurrentVersionExpiration"></a>

Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in the object's lifetime.

**Note**
This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.

## Contents
<a name="API_NoncurrentVersionExpiration_Contents"></a>

 ** NewerNoncurrentVersions **   <a name="AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions"></a>
Specifies how many noncurrent versions Amazon S3 will retain. You can specify up to 100 noncurrent versions to retain. Amazon S3 will permanently delete any additional noncurrent versions beyond the specified number to retain. For more information about noncurrent versions, see [Lifecycle configuration elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html) in the *Amazon S3 User Guide*.
This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.
Type: Integer
Required: No

 ** NoncurrentDays **   <a name="AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays"></a>
Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. The value must be a non-zero positive integer. For information about the noncurrent days calculations, see [How Amazon S3 Calculates When an Object Became Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations) in the *Amazon S3 User Guide*.
This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.
Type: Integer
Required: No

## See Also
<a name="API_NoncurrentVersionExpiration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/NoncurrentVersionExpiration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/NoncurrentVersionExpiration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/NoncurrentVersionExpiration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
