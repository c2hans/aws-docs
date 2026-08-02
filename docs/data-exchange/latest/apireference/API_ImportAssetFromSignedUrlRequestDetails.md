---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetFromSignedUrlRequestDetails.html
---

# ImportAssetFromSignedUrlRequestDetails
<a name="API_ImportAssetFromSignedUrlRequestDetails"></a>

Details of the operation to be performed by the job.

## Contents
<a name="API_ImportAssetFromSignedUrlRequestDetails_Contents"></a>

 ** AssetName **   <a name="dataexchange-Type-ImportAssetFromSignedUrlRequestDetails-AssetName"></a>
The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name.
Type: String
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetFromSignedUrlRequestDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Md5Hash **   <a name="dataexchange-Type-ImportAssetFromSignedUrlRequestDetails-Md5Hash"></a>
The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetFromSignedUrlRequestDetails-RevisionId"></a>
The unique identifier for the revision associated with this import request.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_ImportAssetFromSignedUrlRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetFromSignedUrlRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetFromSignedUrlRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetFromSignedUrlRequestDetails)
