---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromSignedUrlResponseDetails.html
---

# ImportAssetFromSignedUrlResponseDetails
<a name="API_ImportAssetFromSignedUrlResponseDetails"></a>

The details in the response for an import request, including the signed URL and other information.

## Contents
<a name="API_ImportAssetFromSignedUrlResponseDetails_Contents"></a>

 ** AssetName **   <a name="dataexchange-Type-ImportAssetFromSignedUrlResponseDetails-AssetName"></a>
The name for the asset associated with this import job.
Type: String
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetFromSignedUrlResponseDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetFromSignedUrlResponseDetails-RevisionId"></a>
The unique identifier for the revision associated with this import response.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Md5Hash **   <a name="dataexchange-Type-ImportAssetFromSignedUrlResponseDetails-Md5Hash"></a>
The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
Required: No

 ** SignedUrl **   <a name="dataexchange-Type-ImportAssetFromSignedUrlResponseDetails-SignedUrl"></a>
The signed URL.
Type: String
Required: No

 ** SignedUrlExpiresAt **   <a name="dataexchange-Type-ImportAssetFromSignedUrlResponseDetails-SignedUrlExpiresAt"></a>
The time and date at which the signed URL expires, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_ImportAssetFromSignedUrlResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetFromSignedUrlResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetFromSignedUrlResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetFromSignedUrlResponseDetails)
