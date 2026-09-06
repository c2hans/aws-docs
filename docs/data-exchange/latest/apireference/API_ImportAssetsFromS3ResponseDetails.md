---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromS3ResponseDetails.html
---

# ImportAssetsFromS3ResponseDetails
<a name="API_ImportAssetsFromS3ResponseDetails"></a>

Details from an import from Amazon S3 response.

## Contents
<a name="API_ImportAssetsFromS3ResponseDetails_Contents"></a>

 ** AssetSources **   <a name="dataexchange-Type-ImportAssetsFromS3ResponseDetails-AssetSources"></a>
Is a list of Amazon S3 bucket and object key pairs.
Type: Array of [AssetSourceEntry](API_AssetSourceEntry.md) objects
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetsFromS3ResponseDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetsFromS3ResponseDetails-RevisionId"></a>
The unique identifier for the revision associated with this import response.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_ImportAssetsFromS3ResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetsFromS3ResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetsFromS3ResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetsFromS3ResponseDetails)
