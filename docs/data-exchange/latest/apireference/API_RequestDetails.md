---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RequestDetails.html
---

# RequestDetails
<a name="API_RequestDetails"></a>

The details for the request.

## Contents
<a name="API_RequestDetails_Contents"></a>

 ** CreateS3DataAccessFromS3Bucket **   <a name="dataexchange-Type-RequestDetails-CreateS3DataAccessFromS3Bucket"></a>
Details of the request to create S3 data access from the Amazon S3 bucket.
Type: [CreateS3DataAccessFromS3BucketRequestDetails](API_CreateS3DataAccessFromS3BucketRequestDetails.md) object
Required: No

 ** ExportAssetsToS3 **   <a name="dataexchange-Type-RequestDetails-ExportAssetsToS3"></a>
Details about the export to Amazon S3 request.
Type: [ExportAssetsToS3RequestDetails](API_ExportAssetsToS3RequestDetails.md) object
Required: No

 ** ExportAssetToSignedUrl **   <a name="dataexchange-Type-RequestDetails-ExportAssetToSignedUrl"></a>
Details about the export to signed URL request.
Type: [ExportAssetToSignedUrlRequestDetails](API_ExportAssetToSignedUrlRequestDetails.md) object
Required: No

 ** ExportRevisionsToS3 **   <a name="dataexchange-Type-RequestDetails-ExportRevisionsToS3"></a>
Details about the export to Amazon S3 request.
Type: [ExportRevisionsToS3RequestDetails](API_ExportRevisionsToS3RequestDetails.md) object
Required: No

 ** ImportAssetFromApiGatewayApi **   <a name="dataexchange-Type-RequestDetails-ImportAssetFromApiGatewayApi"></a>
Details about the import from signed URL request.
Type: [ImportAssetFromApiGatewayApiRequestDetails](API_ImportAssetFromApiGatewayApiRequestDetails.md) object
Required: No

 ** ImportAssetFromSignedUrl **   <a name="dataexchange-Type-RequestDetails-ImportAssetFromSignedUrl"></a>
Details about the import from Amazon S3 request.
Type: [ImportAssetFromSignedUrlRequestDetails](API_ImportAssetFromSignedUrlRequestDetails.md) object
Required: No

 ** ImportAssetsFromLakeFormationTagPolicy **   <a name="dataexchange-Type-RequestDetails-ImportAssetsFromLakeFormationTagPolicy"></a>
Request details for the ImportAssetsFromLakeFormationTagPolicy job.
Type: [ImportAssetsFromLakeFormationTagPolicyRequestDetails](API_ImportAssetsFromLakeFormationTagPolicyRequestDetails.md) object
Required: No

 ** ImportAssetsFromRedshiftDataShares **   <a name="dataexchange-Type-RequestDetails-ImportAssetsFromRedshiftDataShares"></a>
Details from an import from Amazon Redshift datashare request.
Type: [ImportAssetsFromRedshiftDataSharesRequestDetails](API_ImportAssetsFromRedshiftDataSharesRequestDetails.md) object
Required: No

 ** ImportAssetsFromS3 **   <a name="dataexchange-Type-RequestDetails-ImportAssetsFromS3"></a>
Details about the import asset from API Gateway API request.
Type: [ImportAssetsFromS3RequestDetails](API_ImportAssetsFromS3RequestDetails.md) object
Required: No

## See Also
<a name="API_RequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/RequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/RequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/RequestDetails)
