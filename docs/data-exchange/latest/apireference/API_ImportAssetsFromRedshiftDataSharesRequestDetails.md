---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ImportAssetsFromRedshiftDataSharesRequestDetails.html
---

# ImportAssetsFromRedshiftDataSharesRequestDetails
<a name="API_ImportAssetsFromRedshiftDataSharesRequestDetails"></a>

Details from an import from Amazon Redshift datashare request.

## Contents
<a name="API_ImportAssetsFromRedshiftDataSharesRequestDetails_Contents"></a>

 ** AssetSources **   <a name="dataexchange-Type-ImportAssetsFromRedshiftDataSharesRequestDetails-AssetSources"></a>
A list of Amazon Redshift datashare assets.
Type: Array of [RedshiftDataShareAssetSourceEntry](API_RedshiftDataShareAssetSourceEntry.md) objects
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ImportAssetsFromRedshiftDataSharesRequestDetails-DataSetId"></a>
The unique identifier for the data set associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ImportAssetsFromRedshiftDataSharesRequestDetails-RevisionId"></a>
The unique identifier for the revision associated with this import job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_ImportAssetsFromRedshiftDataSharesRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ImportAssetsFromRedshiftDataSharesRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ImportAssetsFromRedshiftDataSharesRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ImportAssetsFromRedshiftDataSharesRequestDetails)
