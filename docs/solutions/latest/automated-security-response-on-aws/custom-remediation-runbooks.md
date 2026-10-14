---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/custom-remediation-runbooks.html
---

# Custom remediation runbooks
<a name="custom-remediation-runbooks"></a>

The solution ships built-in remediations for the controls listed in [Playbooks](playbooks-1.md). To remediate a control that the solution does not already cover, you can add your own remediation runbook. You don’t need to modify the solution’s source. For the authoring workflow and tooling, see [AI Toolkit for Custom Remediations](adding-new-remediations.md#ai-toolkit-for-custom-remediations).

There are two ways to add one, and they behave differently at run time:

Registered Custom Runbook
You register, test, and deploy the runbook through the optional MCP server. This option requires the administrator stack with **EnableMcpServer** set to `yes` (see [MCP server for AI clients](mcp-server.md)). The solution records the runbook and applies the safeguards described in this topic.

Manually deployed runbook
You create the AWS Systems Manager document and the IAM role yourself. This option requires the built-in naming convention for the document name. The solution keeps no record of the runbook, so the Orchestrator treats it the same way as a built-in remediation.

In the rest of this topic, *Custom Runbook* refers to a registered Custom Runbook unless stated otherwise.

The Orchestrator resolves which AWS Systems Manager document to run for a finding in this order:

1. The Orchestrator builds the built-in document name from the finding’s standard, version, and control ID. It then looks for a document with that name in the finding’s member account.

1. If a document with that name is active, the Orchestrator uses it and doesn’t look for a registered Custom Runbook. A manually deployed runbook resolves at this step, because it uses the built-in name.

1. Otherwise, the Orchestrator looks for a registered Custom Runbook for that control in the finding’s member account. It does this only when you initiate the remediation manually. For example, you can use the AWS Security Hub Cloud Security Posture Management (CSPM) custom action, the Web UI, or the API.

1. If that Custom Runbook’s document is active in the member account, the Orchestrator uses it. Otherwise, no runbook resolves for the finding.

This resolution order has these consequences:
+ An automatically triggered remediation never resolves to a registered Custom Runbook. A registered Custom Runbook runs only on findings that you remediate on demand.
+ A manually deployed runbook can run on an automatic trigger. Whether one fires depends on the control’s automated remediation setting, not on how you created the runbook.
+ Registering a Custom Runbook for a control that already has a built-in remediation has no effect on resolution.

The solution applies the following safeguards to registered Custom Runbooks:
+  **Built-in precedence and collision guard.** A registered Custom Runbook cannot shadow a built-in remediation. If a built-in control runbook exists for the control, it always wins.
+  **Per-member resolution.** The solution tracks deployment state per member account. A registered Custom Runbook runs in an account only when the solution records it as deployed and active there. As a result, it can cover a control in some accounts and not others.
+  **Test-gated deploy.** A registered Custom Runbook version must pass a recorded test before you can release it. The MCP server’s runbook-authoring tools enforce this rule.
+  **Coverage honesty.** The solution reports unverified coverage to operators as a *gap* rather than as coverage. The solution never counts an untested registered Custom Runbook as protecting a control.

**Important**
These safeguards apply only to a registered Custom Runbook. A manually deployed runbook uses the built-in naming convention, so the solution keeps no record of it. The solution does not gate its release on a test, does not limit it to manual remediation, and does not report its coverage. Review and test a manually deployed runbook yourself before you deploy it to a production member account.
