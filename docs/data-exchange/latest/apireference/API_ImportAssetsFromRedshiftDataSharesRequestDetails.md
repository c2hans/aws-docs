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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
