---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **remediation, remediation runbook**

An implementation of a set of steps that resolves a finding. For example, a remediation for the control Security Control (SC) Lambda.1 "Lambda function policies should prohibit public access" would modify the policy of the relevant AWS Lambda Function to remove statements that allow public access.

 **control runbook**

One of a set of AWS Systems Manager (SSM) automation documents that the Orchestrator uses to route an initiated remediation for a specific control to the correct remediation runbook. For example, the remediations for SC Lambda.1 and AWS Foundational Security Best Practices (FSBP) Lambda.1 are implemented with the same remediation runbook. The Orchestrator invokes the control runbook for each control, which are named ASR-AFSBP\_Lambda.1 and ASR-SC\_2.0.0\_Lambda.1, respectively. Each control runbook invokes the same remediation runbook, which in this case would be ASR-RemoveLambdaPublicAccess.

 **orchestrator**

The Step Functions deployed by the solution that takes as input a finding object from AWS Security Hub and invokes the correct control runbook in the target account and Region. The Orchestrator also notifies the solution SNS Topic when the remediation is started and when the remediation succeeds or fails.

 **standard**

A group of controls defined by an organization as part of a compliance framework. For example, one of the standards supported by AWS Security Hub and this solution is AWS FSBP.

 **control**

A description of the properties that a resource should or should not have in order to be in compliance. For example, the control AWS FSBP Lambda.1 states that AWS Lambda Functions should prohibit public access. A function that allows public access would fail this control.

 **consolidated control findings, security control, security controls view**

A feature of AWS Security Hub that, when activated, displays findings with their consolidated control IDs rather than IDs that correspond to a particular standard. For example, the controls AWS FSBP S3.2, CIS v1.2.0 2.3, CIS v1.4.0 2.1.5.2, and PCI-DSS v3.2.1 S3.1 all map to the consolidated (SC) control S3.2 "S3 Buckets should prohibit public read access." When this feature is turned on, SC runbooks are used.

 **[Solution Web UI] delegated admin**

In the context of the solution’s Web UI, a delegated admin is a user that has been invited by the admin and has full access to run remediations and view remediation history. This user can also view and manage other Account Operator users.

 **[Solution Web UI] account operator**

In the context of the solution’s Web UI, an account operator is a user invited by an admin or delegated admin to access the solution’s Web UI. This user is associated with a list of AWS Account Ids provided in their invitation; they may only run remediations and view remediation history as it pertains to resources in these accounts.

For a general reference of AWS terms, refer to the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
