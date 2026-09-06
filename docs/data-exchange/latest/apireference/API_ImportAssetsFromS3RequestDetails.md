---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromS3RequestDetails.html
---

# ImportAssetsFromS3RequestDetails
<a name="API_ImportAssetsFromS3RequestDetails"></a>

Details of the operation to be performed by the job.

## Contents
<a name="API_ImportAssetsFromS3RequestDetails_Contents"></a>

 ** AssetSources **   <a name="dataexchange-Type-ImportAssetsFromS3RequestDetails-AssetSources"></a>
Is a list of Amazon S3 bucket and object key pairs.
Type: Array of [AssetSourceEntry](API_AssetSourceEntry.md) objects
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetsFromS3RequestDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetsFromS3RequestDetails-RevisionId"></a>
The unique identifier for the revision associated with this import request.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_ImportAssetsFromS3RequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetsFromS3RequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetsFromS3RequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetsFromS3RequestDetails)
