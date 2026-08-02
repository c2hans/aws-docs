---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReadSetUploadPartListItem.html
---

# ReadSetUploadPartListItem
<a name="API_ReadSetUploadPartListItem"></a>

 The metadata of a single part of a file that was added to a multipart upload. A list of these parts is returned in the response to the ListReadSetUploadParts API.

## Contents
<a name="API_ReadSetUploadPartListItem_Contents"></a>

 ** checksum **   <a name="omics-Type-ReadSetUploadPartListItem-checksum"></a>
 A unique identifier used to confirm that parts are being added to the correct upload.
Type: String
Required: Yes

 ** partNumber **   <a name="omics-Type-ReadSetUploadPartListItem-partNumber"></a>
 The number identifying the part in an upload.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

 ** partSize **   <a name="omics-Type-ReadSetUploadPartListItem-partSize"></a>
 The size of the the part in an upload.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 5368709120.
Required: Yes

 ** partSource **   <a name="omics-Type-ReadSetUploadPartListItem-partSource"></a>
 The origin of the part being direct uploaded.
Type: String
Valid Values: `SOURCE1 | SOURCE2`
Required: Yes

 ** creationTime **   <a name="omics-Type-ReadSetUploadPartListItem-creationTime"></a>
 The time stamp for when a direct upload was created.
Type: Timestamp
Required: No

 ** lastUpdatedTime **   <a name="omics-Type-ReadSetUploadPartListItem-lastUpdatedTime"></a>
 The time stamp for the most recent update to an uploaded part.
Type: Timestamp
Required: No

## See Also
<a name="API_ReadSetUploadPartListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReadSetUploadPartListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReadSetUploadPartListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReadSetUploadPartListItem)
