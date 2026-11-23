---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_OpportunityBulkJobSummary.html
---

# OpportunityBulkJobSummary

The status, record counts, and input file name of an opportunity bulk job.

## Contents
<a name="API_OpportunityBulkJobSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-CreatedAt"></a>
The date and time, in UTC, when you created the bulk job.
Type: Timestamp
Required: Yes

 ** FailureCount **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-FailureCount"></a>
The number of records that failed.
Type: Integer
Required: Yes

 ** JobId **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-JobId"></a>
The unique identifier of the bulk job.
Type: String
Pattern: `bulkjob-[0-9a-z]{13}`
Required: Yes

 ** ProcessedRecords **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-ProcessedRecords"></a>
The number of records that Partner Central has processed so far.
Type: Integer
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-Status"></a>
The current status of the bulk job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** SuccessCount **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-SuccessCount"></a>
The number of records that succeeded.
Type: Integer
Required: Yes

 ** TotalRecords **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-TotalRecords"></a>
The total number of records in the input file.
Type: Integer
Required: Yes

 ** CompletedAt **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-CompletedAt"></a>
The date and time, in UTC, when the bulk job finished.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-FailureReason"></a>
The reason that the bulk job failed. Present only when `Status` is `FAILED`.
Type: String
Required: No

 ** FileName **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-FileName"></a>
The name of the input file that started the bulk job. Use it to identify the job by its file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** OperationType **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-OperationType"></a>
Indicates whether the bulk job creates or updates opportunities, based on the template of the input file. Partner Central doesn't set this field until it reads the file.
Type: String
Valid Values: `BULK_CREATE | BULK_UPDATE`
Required: No

 ** StartedAt **   <a name="AWSPartnerCentral-Type-OpportunityBulkJobSummary-StartedAt"></a>
The date and time, in UTC, when the bulk job started processing records.
Type: Timestamp
Required: No

## See Also
<a name="API_OpportunityBulkJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/OpportunityBulkJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/OpportunityBulkJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/OpportunityBulkJobSummary)
