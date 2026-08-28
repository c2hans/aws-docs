---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/remediate-example-findings.html
---

# Remediate example findings
<a name="remediate-example-findings"></a>

**Important**
This example requires the use of the Security Hub CSPM console. The Security Hub (non-CSPM) console does not currently support manual remediations via custom action. To remediate findings without using the Security Hub CSPM console, see the [Remediate using the Web UI](remediate-with-ui.md) section.

In the admin account, navigate to the [Security Hub CSPM console](https://console.aws.amazon.com/securityhub/) and locate the finding for the resource with an insecure configuration that you created as part of this tutorial.

This can be done in several ways:

1. In partitions which support the consolidated control findings feature, a page labeled "Controls" allows you to locate the finding by the consolidated control ID.

1. In the "Security standards" page, you can locate the control according to which standard it belongs to.

1. You can view all findings on the "Findings" page and search by attribute.

The consolidated control ID for the public Lambda Function we created is Lambda.1.

## Initiate the remediation
<a name="initiate-the-remediation"></a>

Select the checkbox to the left of the finding related to the resource we created. In the "Actions" drop-down menu, select "Remediate with ASR". You will see a notification that the finding was sent to Amazon EventBridge.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Initiate the remediation | None |
|  `222222222222`  | Member | None | None |

## Confirm that the remediation resolved the finding
<a name="confirm-the-remediation-resolved-finding"></a>

You should receive two SNS notifications. The first will indicate that a remediation has been initiated, and the second will indicate that the remediation succeeded. After receiving the second notification, navigate to the [Lambda console](https://console.aws.amazon.com/lambda/) in the member account and confirm that the public access has been revoked.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | None | None |
|  `222222222222`  | Member | None | Confirm that the remediation succeeded |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
