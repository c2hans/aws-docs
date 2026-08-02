---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AutoExportRevisionToS3RequestDetails.html
---

# AutoExportRevisionToS3RequestDetails
<a name="API_AutoExportRevisionToS3RequestDetails"></a>

Details of the operation to be performed by the job.

## Contents
<a name="API_AutoExportRevisionToS3RequestDetails_Contents"></a>

 ** RevisionDestination **   <a name="dataexchange-Type-AutoExportRevisionToS3RequestDetails-RevisionDestination"></a>
A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.
Type: [AutoExportRevisionDestinationEntry](API_AutoExportRevisionDestinationEntry.md) object
Required: Yes

 ** Encryption **   <a name="dataexchange-Type-AutoExportRevisionToS3RequestDetails-Encryption"></a>
Encryption configuration for the auto export job.
Type: [ExportServerSideEncryption](API_ExportServerSideEncryption.md) object
Required: No

## See Also
<a name="API_AutoExportRevisionToS3RequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/AutoExportRevisionToS3RequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/AutoExportRevisionToS3RequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/AutoExportRevisionToS3RequestDetails)
