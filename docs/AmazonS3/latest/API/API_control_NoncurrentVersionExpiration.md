---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_NoncurrentVersionExpiration.html
---

# NoncurrentVersionExpiration
<a name="API_control_NoncurrentVersionExpiration"></a>

The container of the noncurrent version expiration.

## Contents
<a name="API_control_NoncurrentVersionExpiration_Contents"></a>

 ** NewerNoncurrentVersions **   <a name="AmazonS3-Type-control_NoncurrentVersionExpiration-NewerNoncurrentVersions"></a>
Specifies how many noncurrent versions S3 on Outposts will retain. If there are this many more recent noncurrent versions, S3 on Outposts will take the associated action. For more information about noncurrent versions, see [Lifecycle configuration elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html) in the *Amazon S3 User Guide*.
Type: Integer
Required: No

 ** NoncurrentDays **   <a name="AmazonS3-Type-control_NoncurrentVersionExpiration-NoncurrentDays"></a>
Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see [How Amazon S3 Calculates When an Object Became Noncurrent](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations) in the *Amazon S3 User Guide*.
Type: Integer
Required: No

## See Also
<a name="API_control_NoncurrentVersionExpiration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/NoncurrentVersionExpiration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/NoncurrentVersionExpiration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/NoncurrentVersionExpiration)
