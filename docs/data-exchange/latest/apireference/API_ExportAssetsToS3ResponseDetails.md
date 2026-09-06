---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportAssetsToS3ResponseDetails.html
---

# ExportAssetsToS3ResponseDetails
<a name="API_ExportAssetsToS3ResponseDetails"></a>

Details about the export to Amazon S3 response.

## Contents
<a name="API_ExportAssetsToS3ResponseDetails_Contents"></a>

 ** AssetDestinations **   <a name="dataexchange-Type-ExportAssetsToS3ResponseDetails-AssetDestinations"></a>
The destination in Amazon S3 where the asset is exported.
Type: Array of [AssetDestinationEntry](API_AssetDestinationEntry.md) objects
Required: Yes

 ** DataSetId **   <a name="dataexchange-Type-ExportAssetsToS3ResponseDetails-DataSetId"></a>
The unique identifier for the data set associated with this export job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-ExportAssetsToS3ResponseDetails-RevisionId"></a>
The unique identifier for the revision associated with this export response.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Encryption **   <a name="dataexchange-Type-ExportAssetsToS3ResponseDetails-Encryption"></a>
Encryption configuration of the export job.
Type: [ExportServerSideEncryption](API_ExportServerSideEncryption.md) object
Required: No

## See Also
<a name="API_ExportAssetsToS3ResponseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ExportAssetsToS3ResponseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ExportAssetsToS3ResponseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ExportAssetsToS3ResponseDetails)
