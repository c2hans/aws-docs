---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateS3DataAccessFromS3BucketResponseDetails.html
---

# CreateS3DataAccessFromS3BucketResponseDetails
<a name="API_CreateS3DataAccessFromS3BucketResponseDetails"></a>

Details about the response of the operation to create an S3 data access from an S3 bucket.

## Contents
<a name="API_CreateS3DataAccessFromS3BucketResponseDetails_Contents"></a>

 ** AssetSource **   <a name="dataexchange-Type-CreateS3DataAccessFromS3BucketResponseDetails-AssetSource"></a>
Details about the asset source from an Amazon S3 bucket.
Type: [S3DataAccessAssetSourceEntry](API_S3DataAccessAssetSourceEntry.md) object
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-CreateS3DataAccessFromS3BucketResponseDetails-DataSetId"></a>
The unique identifier for this data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-CreateS3DataAccessFromS3BucketResponseDetails-RevisionId"></a>
The unique identifier for the revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_CreateS3DataAccessFromS3BucketResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CreateS3DataAccessFromS3BucketResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CreateS3DataAccessFromS3BucketResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CreateS3DataAccessFromS3BucketResponseDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
