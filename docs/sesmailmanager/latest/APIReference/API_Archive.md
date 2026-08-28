---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Archive.html
---

# Archive
<a name="API_Archive"></a>

An archive resource for storing and retaining emails.

## Contents
<a name="API_Archive_Contents"></a>

 ** ArchiveId **   <a name="sesmailmanager-Type-Archive-ArchiveId"></a>
The unique identifier of the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 66.
Required: Yes

 ** ArchiveName **   <a name="sesmailmanager-Type-Archive-ArchiveName"></a>
The unique name assigned to the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]`
Required: No

 ** ArchiveState **   <a name="sesmailmanager-Type-Archive-ArchiveState"></a>
The current state of the archive:
+  `ACTIVE` – The archive is ready and available for use.
+  `PENDING_DELETION` – The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state.
Type: String
Valid Values: `ACTIVE | PENDING_DELETION`
Required: No

 ** LastUpdatedTimestamp **   <a name="sesmailmanager-Type-Archive-LastUpdatedTimestamp"></a>
The timestamp of when the archive was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Archive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Archive)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Archive)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Archive)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
