---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteMarkerEntry.html
---

# DeleteMarkerEntry
<a name="API_DeleteMarkerEntry"></a>

Information about the delete marker.

## Contents
<a name="API_DeleteMarkerEntry_Contents"></a>

 ** IsLatest **   <a name="AmazonS3-Type-DeleteMarkerEntry-IsLatest"></a>
Specifies whether the object is (true) or is not (false) the latest version of an object.
Type: Boolean
Required: No

 ** Key **   <a name="AmazonS3-Type-DeleteMarkerEntry-Key"></a>
The object key.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** LastModified **   <a name="AmazonS3-Type-DeleteMarkerEntry-LastModified"></a>
Date and time when the object was last modified.
Type: Timestamp
Required: No

 ** Owner **   <a name="AmazonS3-Type-DeleteMarkerEntry-Owner"></a>
The account that created the delete marker.
Type: [Owner](API_Owner.md) data type
Required: No

 ** VersionId **   <a name="AmazonS3-Type-DeleteMarkerEntry-VersionId"></a>
Version ID of an object.
Type: String
Required: No

## See Also
<a name="API_DeleteMarkerEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeleteMarkerEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeleteMarkerEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeleteMarkerEntry)
