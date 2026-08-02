---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreStatus.html
---

# RestoreStatus
<a name="API_RestoreStatus"></a>

Specifies the restoration status of an object. Objects in certain storage classes must be restored before they can be retrieved. For more information about these storage classes and how to work with archived objects, see [ Working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html) in the *Amazon S3 User Guide*.

**Note**
This functionality is not supported for directory buckets. Directory buckets only support `EXPRESS_ONEZONE` (the S3 Express One Zone storage class) in Availability Zones and `ONEZONE_IA` (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.

## Contents
<a name="API_RestoreStatus_Contents"></a>

 ** IsRestoreInProgress **   <a name="AmazonS3-Type-RestoreStatus-IsRestoreInProgress"></a>
Specifies whether the object is currently being restored. If the object restoration is in progress, the header returns the value `TRUE`. For example:
 `x-amz-optional-object-attributes: IsRestoreInProgress="true"`
If the object restoration has completed, the header returns the value `FALSE`. For example:
 `x-amz-optional-object-attributes: IsRestoreInProgress="false", RestoreExpiryDate="2012-12-21T00:00:00.000Z"`
If the object hasn't been restored, there is no header response.
Type: Boolean
Required: No

 ** RestoreExpiryDate **   <a name="AmazonS3-Type-RestoreStatus-RestoreExpiryDate"></a>
Indicates when the restored copy will expire. This value is populated only if the object has already been restored. For example:
 `x-amz-optional-object-attributes: IsRestoreInProgress="false", RestoreExpiryDate="2012-12-21T00:00:00.000Z"`
Type: Timestamp
Required: No

## See Also
<a name="API_RestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RestoreStatus)
