---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ExportStatus.html
---

# ExportStatus
<a name="API_ExportStatus"></a>

The current status of an archive export job.

## Contents
<a name="API_ExportStatus_Contents"></a>

 ** CompletionTimestamp **   <a name="sesmailmanager-Type-ExportStatus-CompletionTimestamp"></a>
The timestamp of when the export job completed (if finished).
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="sesmailmanager-Type-ExportStatus-ErrorMessage"></a>
An error message if the export job failed.
Type: String
Required: No

 ** State **   <a name="sesmailmanager-Type-ExportStatus-State"></a>
The current state of the export job.
Type: String
Valid Values: `QUEUED | PREPROCESSING | PROCESSING | COMPLETED | FAILED | CANCELLED`
Required: No

 ** SubmissionTimestamp **   <a name="sesmailmanager-Type-ExportStatus-SubmissionTimestamp"></a>
The timestamp of when the export job was submitted.
Type: Timestamp
Required: No

## See Also
<a name="API_ExportStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ExportStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ExportStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ExportStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
