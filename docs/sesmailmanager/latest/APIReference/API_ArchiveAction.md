---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveAction.html
---

# ArchiveAction
<a name="API_ArchiveAction"></a>

The action to archive the email by delivering the email to an Amazon SES archive.

## Contents
<a name="API_ArchiveAction_Contents"></a>

 ** TargetArchive **   <a name="sesmailmanager-Type-ArchiveAction-TargetArchive"></a>
The identifier of the archive to send the email to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-ArchiveAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified archive has been deleted.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

## See Also
<a name="API_ArchiveAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ArchiveAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ArchiveAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ArchiveAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
