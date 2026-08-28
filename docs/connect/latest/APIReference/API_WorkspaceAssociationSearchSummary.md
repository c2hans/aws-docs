---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WorkspaceAssociationSearchSummary.html
---

# WorkspaceAssociationSearchSummary
<a name="API_WorkspaceAssociationSearchSummary"></a>

Contains summary information about a workspace association with a user or routing profile.

## Contents
<a name="API_WorkspaceAssociationSearchSummary_Contents"></a>

 ** ResourceArn **   <a name="connect-Type-WorkspaceAssociationSearchSummary-ResourceArn"></a>
The Amazon Resource Name (ARN) of the associated resource.
Type: String
Required: No

 ** ResourceId **   <a name="connect-Type-WorkspaceAssociationSearchSummary-ResourceId"></a>
The identifier of the associated resource (user or routing profile).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ResourceName **   <a name="connect-Type-WorkspaceAssociationSearchSummary-ResourceName"></a>
The name of the associated resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\\S.*`
Required: No

 ** ResourceType **   <a name="connect-Type-WorkspaceAssociationSearchSummary-ResourceType"></a>
The type of resource associated with the workspace. Valid values are: `USER` and `ROUTING_PROFILE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** WorkspaceArn **   <a name="connect-Type-WorkspaceAssociationSearchSummary-WorkspaceArn"></a>
The Amazon Resource Name (ARN) of the workspace.
Type: String
Required: No

 ** WorkspaceId **   <a name="connect-Type-WorkspaceAssociationSearchSummary-WorkspaceId"></a>
The identifier of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_WorkspaceAssociationSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WorkspaceAssociationSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WorkspaceAssociationSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WorkspaceAssociationSearchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
