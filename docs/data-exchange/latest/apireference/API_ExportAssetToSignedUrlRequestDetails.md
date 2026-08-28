---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetToSignedUrlRequestDetails.html
---

# ExportAssetToSignedUrlRequestDetails
<a name="API_ExportAssetToSignedUrlRequestDetails"></a>

Details of the operation to be performed by the job.

## Contents
<a name="API_ExportAssetToSignedUrlRequestDetails_Contents"></a>

 ** AssetId **   <a name="dataexchange-Type-ExportAssetToSignedUrlRequestDetails-AssetId"></a>
The unique identifier for the asset that is exported to a signed URL.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ExportAssetToSignedUrlRequestDetails-DataSetId"></a>
The unique identifier for the data set associated with this export job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ExportAssetToSignedUrlRequestDetails-RevisionId"></a>
The unique identifier for the revision associated with this export request.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_ExportAssetToSignedUrlRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ExportAssetToSignedUrlRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ExportAssetToSignedUrlRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ExportAssetToSignedUrlRequestDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
