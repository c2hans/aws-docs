---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ApprovalAction.html
---

# ApprovalAction
<a name="API_ApprovalAction"></a>

An approval decision supplied when resuming a paused agent execution. When an agent execution pauses to request approval for an elevated action, SendMessage streams an approval request carrying interrupt identifiers. This structure carries the decision back to the service — which paused tool invocation is being resumed, the opaque interrupt identifier that resumes it, the identifier of the approval request being resolved, optional display text of the control the user chose, and the action taken (APPROVED or REJECTED) — so the service can resume the paused execution. All members are optional on the wire; service-side validation is applied against the populated subset.

## Contents
<a name="API_ApprovalAction_Contents"></a>

 ** action **   <a name="devopsagent-Type-ApprovalAction-action"></a>
The action taken on the approval request — APPROVED or REJECTED.
Type: String
Valid Values: `APPROVED | REJECTED`
Required: No

 ** approvalId **   <a name="devopsagent-Type-ApprovalAction-approvalId"></a>
Identifier of the approval request being resolved.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-7[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: No

 ** buttonText **   <a name="devopsagent-Type-ApprovalAction-buttonText"></a>
Optional display text of the UI control the user chose (for example, "Approve Exact", "Approve Broader", or "Reject"), provided as auxiliary decision context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** interruptId **   <a name="devopsagent-Type-ApprovalAction-interruptId"></a>
An opaque resume identifier issued by the service when an agent execution pauses for approval. Provide it when resuming so the service can resume the correct paused execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** toolUseId **   <a name="devopsagent-Type-ApprovalAction-toolUseId"></a>
Identifier of the specific paused tool invocation that requested approval. Correlates the approval decision back to the paused invocation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_ApprovalAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ApprovalAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ApprovalAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ApprovalAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
