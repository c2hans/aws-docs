---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_MailboxExportJob.html
---

# MailboxExportJob
<a name="API_MailboxExportJob"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The details of a mailbox export job, including the user or resource ID associated with the mailbox and the S3 bucket that the mailbox contents are exported to.

## Contents
<a name="API_MailboxExportJob_Contents"></a>

 ** Description **   <a name="workmail-Type-MailboxExportJob-Description"></a>
The mailbox export job description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `[\S\s]*`
Required: No

 ** EndTime **   <a name="workmail-Type-MailboxExportJob-EndTime"></a>
The mailbox export job end timestamp.
Type: Timestamp
Required: No

 ** EntityId **   <a name="workmail-Type-MailboxExportJob-EntityId"></a>
The identifier of the user or resource associated with the mailbox.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** EstimatedProgress **   <a name="workmail-Type-MailboxExportJob-EstimatedProgress"></a>
The estimated progress of the mailbox export job, in percentage points.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** JobId **   <a name="workmail-Type-MailboxExportJob-JobId"></a>
The identifier of the mailbox export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9-]+`
Required: No

 ** S3BucketName **   <a name="workmail-Type-MailboxExportJob-S3BucketName"></a>
The name of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9.-]+`
Required: No

 ** S3Path **   <a name="workmail-Type-MailboxExportJob-S3Path"></a>
The path to the S3 bucket and file that the mailbox export job exports to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[A-Za-z0-9!_.*'()/-]+`
Required: No

 ** StartTime **   <a name="workmail-Type-MailboxExportJob-StartTime"></a>
The mailbox export job start timestamp.
Type: Timestamp
Required: No

 ** State **   <a name="workmail-Type-MailboxExportJob-State"></a>
The state of the mailbox export job.
Type: String
Valid Values: `RUNNING | COMPLETED | FAILED | CANCELLED`
Required: No

## See Also
<a name="API_MailboxExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/MailboxExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/MailboxExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/MailboxExportJob)
