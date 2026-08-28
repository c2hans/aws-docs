---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Attachments.html
---

# Attachments
<a name="API_Attachments"></a>

The job attachments.

## Contents
<a name="API_Attachments_Contents"></a>

 ** manifests **   <a name="deadlinecloud-Type-Attachments-manifests"></a>
The manifest properties for the attachments.
Type: Array of [ManifestProperties](API_ManifestProperties.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** fileSystem **   <a name="deadlinecloud-Type-Attachments-fileSystem"></a>
The file system location for the attachments.
Type: String
Valid Values: `COPIED | VIRTUAL`
Required: No

## See Also
<a name="API_Attachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/Attachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/Attachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/Attachments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
