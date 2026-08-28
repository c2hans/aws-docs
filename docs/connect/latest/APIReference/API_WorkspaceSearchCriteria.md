---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WorkspaceSearchCriteria.html
---

# WorkspaceSearchCriteria
<a name="API_WorkspaceSearchCriteria"></a>

Defines the search criteria for filtering workspaces.

## Contents
<a name="API_WorkspaceSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-WorkspaceSearchCriteria-AndConditions"></a>
A list of conditions that must all be satisfied.
Type: Array of [WorkspaceSearchCriteria](#API_WorkspaceSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-WorkspaceSearchCriteria-OrConditions"></a>
A list of conditions to be met, where at least one condition must be satisfied.
Type: Array of [WorkspaceSearchCriteria](#API_WorkspaceSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-WorkspaceSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_WorkspaceSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WorkspaceSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WorkspaceSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WorkspaceSearchCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
