---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetToSignedUrlResponseDetails.html
---

# ExportAssetToSignedUrlResponseDetails
<a name="API_ExportAssetToSignedUrlResponseDetails"></a>

The details of the export to signed URL response.

## Contents
<a name="API_ExportAssetToSignedUrlResponseDetails_Contents"></a>

 ** AssetId **   <a name="dataexchange-Type-ExportAssetToSignedUrlResponseDetails-AssetId"></a>
The unique identifier for the asset associated with this export job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ExportAssetToSignedUrlResponseDetails-DataSetId"></a>
The unique identifier for the data set associated with this export job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ExportAssetToSignedUrlResponseDetails-RevisionId"></a>
The unique identifier for the revision associated with this export response.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** SignedUrl **   <a name="dataexchange-Type-ExportAssetToSignedUrlResponseDetails-SignedUrl"></a>
The signed URL for the export request.
Type: String
Required: No

 ** SignedUrlExpiresAt **   <a name="dataexchange-Type-ExportAssetToSignedUrlResponseDetails-SignedUrlExpiresAt"></a>
The date and time that the signed URL expires, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_ExportAssetToSignedUrlResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ExportAssetToSignedUrlResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ExportAssetToSignedUrlResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ExportAssetToSignedUrlResponseDetails)
