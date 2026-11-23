---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerAccountBulkJobSummary.html
---

# CustomerAccountBulkJobSummary

A bulk job in the results of `ListCustomerAccountBulkJobs`. It includes the job status, the file name, and the record counts.

## Contents
<a name="API_CustomerAccountBulkJobSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-Arn"></a>
The Amazon Resource Name (ARN) of the bulk job.
Type: String
Pattern: `arn:[a-z\-]*:partnercentral:[a-z0-9\-]*:[0-9]{12}:catalog/[a-zA-Z]+/customer-account-bulk-job/bulkjob-[0-9a-z]{13}`
Required: Yes

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-CreatedAt"></a>
The date and time when the bulk job was created.
Type: Timestamp
Required: Yes

 ** DeletedCount **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-DeletedCount"></a>
The number of accounts imported by this job that have since been deleted. This counter only increases, so the accounts still present equal `SuccessCount` minus `DeletedCount`.
Type: Integer
Required: Yes

 ** FailureCount **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-FailureCount"></a>
The number of records that failed.
Type: Integer
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-Id"></a>
The unique identifier of the bulk job.
Type: String
Pattern: `bulkjob-[0-9a-z]{13}`
Required: Yes

 ** ProcessedRecords **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-ProcessedRecords"></a>
The number of records that the job has finished processing.
Type: Integer
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-Status"></a>
The current status of the bulk job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED`
Required: Yes

 ** SuccessCount **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-SuccessCount"></a>
The number of records that the job processed successfully.
Type: Integer
Required: Yes

 ** TotalRecords **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-TotalRecords"></a>
The total number of records in the file. The value is 0 until the job reads the file.
Type: Integer
Required: Yes

 ** CompletedAt **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-CompletedAt"></a>
The date and time when the job finished. Absent while the job is running.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-FailureReason"></a>
The reason that the job failed. Present only when the job status is `FAILED`.
Type: String
Required: No

 ** FileName **   <a name="AWSPartnerCentral-Type-CustomerAccountBulkJobSummary-FileName"></a>
The name of the file that the job processes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_CustomerAccountBulkJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerAccountBulkJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerAccountBulkJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerAccountBulkJobSummary)
