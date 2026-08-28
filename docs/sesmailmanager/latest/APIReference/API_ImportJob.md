---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ImportJob.html
---

# ImportJob
<a name="API_ImportJob"></a>

Details about an import job.

## Contents
<a name="API_ImportJob_Contents"></a>

 ** AddressListId **   <a name="sesmailmanager-Type-ImportJob-AddressListId"></a>
The unique identifier of the address list the import job was created for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** CreatedTimestamp **   <a name="sesmailmanager-Type-ImportJob-CreatedTimestamp"></a>
The timestamp of when the import job was created.
Type: Timestamp
Required: Yes

 ** ImportDataFormat **   <a name="sesmailmanager-Type-ImportJob-ImportDataFormat"></a>
The format of the input for the import job.
Type: [ImportDataFormat](API_ImportDataFormat.md) object
Required: Yes

 ** JobId **   <a name="sesmailmanager-Type-ImportJob-JobId"></a>
The identifier of the import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** Name **   <a name="sesmailmanager-Type-ImportJob-Name"></a>
A user-friendly name for the import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** PreSignedUrl **   <a name="sesmailmanager-Type-ImportJob-PreSignedUrl"></a>
The pre-signed URL target for uploading the input file.
Type: String
Required: Yes

 ** Status **   <a name="sesmailmanager-Type-ImportJob-Status"></a>
The status of the import job.
Type: String
Valid Values: `CREATED | PROCESSING | COMPLETED | FAILED | STOPPED`
Required: Yes

 ** CompletedTimestamp **   <a name="sesmailmanager-Type-ImportJob-CompletedTimestamp"></a>
The timestamp of when the import job was completed.
Type: Timestamp
Required: No

 ** Error **   <a name="sesmailmanager-Type-ImportJob-Error"></a>
The reason for failure of an import job.
Type: String
Required: No

 ** FailedItemsCount **   <a name="sesmailmanager-Type-ImportJob-FailedItemsCount"></a>
The number of addresses in the input that failed to get imported into address list.
Type: Integer
Required: No

 ** ImportedItemsCount **   <a name="sesmailmanager-Type-ImportJob-ImportedItemsCount"></a>
The number of addresses in the input that were successfully imported into the address list.
Type: Integer
Required: No

 ** StartTimestamp **   <a name="sesmailmanager-Type-ImportJob-StartTimestamp"></a>
The timestamp of when the import job was started.
Type: Timestamp
Required: No

## See Also
<a name="API_ImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
