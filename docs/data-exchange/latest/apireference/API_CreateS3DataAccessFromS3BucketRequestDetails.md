---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateS3DataAccessFromS3BucketRequestDetails.html
---

# CreateS3DataAccessFromS3BucketRequestDetails
<a name="API_CreateS3DataAccessFromS3BucketRequestDetails"></a>

Details of the operation to create an Amazon S3 data access from an S3 bucket.

## Contents
<a name="API_CreateS3DataAccessFromS3BucketRequestDetails_Contents"></a>

 ** AssetSource **   <a name="dataexchange-Type-CreateS3DataAccessFromS3BucketRequestDetails-AssetSource"></a>
Details about the S3 data access source asset.
Type: [S3DataAccessAssetSourceEntry](API_S3DataAccessAssetSourceEntry.md) object
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-CreateS3DataAccessFromS3BucketRequestDetails-DataSetId"></a>
The unique identifier for the data set associated with the creation of this Amazon S3 data access.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-CreateS3DataAccessFromS3BucketRequestDetails-RevisionId"></a>
The unique identifier for a revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## See Also
<a name="API_CreateS3DataAccessFromS3BucketRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CreateS3DataAccessFromS3BucketRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CreateS3DataAccessFromS3BucketRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CreateS3DataAccessFromS3BucketRequestDetails)
