---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WorkspaceSearchSummary.html
---

# WorkspaceSearchSummary
<a name="API_WorkspaceSearchSummary"></a>

Contains summary information about a workspace returned from a search operation.

## Contents
<a name="API_WorkspaceSearchSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-WorkspaceSearchSummary-Arn"></a>
The Amazon Resource Name (ARN) of the workspace.
Type: String
Required: No

 ** CreatedAt **   <a name="connect-Type-WorkspaceSearchSummary-CreatedAt"></a>
The timestamp when the workspace was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-WorkspaceSearchSummary-Description"></a>
The description of the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `^[\\P{C}\r\n\t]*$`
Required: No

 ** Id **   <a name="connect-Type-WorkspaceSearchSummary-Id"></a>
The unique identifier of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Name **   <a name="connect-Type-WorkspaceSearchSummary-Name"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** Tags **   <a name="connect-Type-WorkspaceSearchSummary-Tags"></a>
The tags associated with the workspace.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Title **   <a name="connect-Type-WorkspaceSearchSummary-Title"></a>
The title displayed for the workspace.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 127.
Pattern: `^[\\P{C}]*$`
Required: No

 ** Visibility **   <a name="connect-Type-WorkspaceSearchSummary-Visibility"></a>
The visibility setting of the workspace.
Type: String
Valid Values: `ALL | ASSIGNED | NONE`
Required: No

## See Also
<a name="API_WorkspaceSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WorkspaceSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WorkspaceSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WorkspaceSearchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
