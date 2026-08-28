---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ExportRevisionsToS3RequestDetails.html
---

# ExportRevisionsToS3RequestDetails
<a name="API_ExportRevisionsToS3RequestDetails"></a>

Details of the operation to be performed by the job.

## Contents
<a name="API_ExportRevisionsToS3RequestDetails_Contents"></a>

 ** DataSetId **   <a name="dataexchange-Type-ExportRevisionsToS3RequestDetails-DataSetId"></a>
The unique identifier for the data set associated with this export job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** RevisionDestinations **   <a name="dataexchange-Type-ExportRevisionsToS3RequestDetails-RevisionDestinations"></a>
The destination for the revision.
Type: Array of [RevisionDestinationEntry](API_RevisionDestinationEntry.md) objects
Required: Yes

 ** Encryption **   <a name="dataexchange-Type-ExportRevisionsToS3RequestDetails-Encryption"></a>
Encryption configuration for the export job.
Type: [ExportServerSideEncryption](API_ExportServerSideEncryption.md) object
Required: No

## See Also
<a name="API_ExportRevisionsToS3RequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ExportRevisionsToS3RequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ExportRevisionsToS3RequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ExportRevisionsToS3RequestDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
