---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LifecycleExpiration.html
---

# LifecycleExpiration
<a name="API_control_LifecycleExpiration"></a>

The container of the Outposts bucket lifecycle expiration.

## Contents
<a name="API_control_LifecycleExpiration_Contents"></a>

 ** Date **   <a name="AmazonS3-Type-control_LifecycleExpiration-Date"></a>
Indicates at what date the object is to be deleted. Should be in GMT ISO 8601 format.
Type: Timestamp
Required: No

 ** Days **   <a name="AmazonS3-Type-control_LifecycleExpiration-Days"></a>
Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.
Type: Integer
Required: No

 ** ExpiredObjectDeleteMarker **   <a name="AmazonS3-Type-control_LifecycleExpiration-ExpiredObjectDeleteMarker"></a>
Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired. If set to false, the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy. To learn more about delete markers, see [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).
Type: Boolean
Required: No

## See Also
<a name="API_control_LifecycleExpiration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LifecycleExpiration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LifecycleExpiration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LifecycleExpiration)
