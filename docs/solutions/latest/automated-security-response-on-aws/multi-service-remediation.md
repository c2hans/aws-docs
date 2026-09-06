---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/multi-service-remediation.html
---

# Multi-service remediation
<a name="multi-service-remediation"></a>

In addition to AWS Security Hub CSPM control findings (identified by control IDs such as `S3.1` or `IAM.7`), the solution can remediate findings from additional AWS security services. These findings are categorized by service name, finding type, and resource type rather than by a Security Hub control ID. The preprocessor maps each service and finding type to the appropriate remediation. Multi-service remediations use the same two-tier runbook architecture, ingestion, and orchestration flow as control-based remediations. Configure them the same way through the Remediation Configuration Amazon DynamoDB table.

This release supports one finding type per service:

| Service | Control ID | Supported resource types | Remediation | Manual follow-up required |
| --- | --- | --- | --- | --- |
| Amazon Inspector |  `Inspector.InstanceVulnerability`  | EC2 instances managed by AWS Systems Manager | Runs the `AWS-RunPatchBaseline` Systems Manager command to install the specific vulnerable packages identified in the finding. The Systems Manager Agent must be version 2.0.834.0 or later. | No |
| Amazon GuardDuty |  `GuardDuty.IAMUser`  | IAM access keys | Contains the potentially compromised IAM user by disabling its access keys, removing console access, and attaching a deny-all policy, using the AWS-managed `AWSSupport-ContainIAMPrincipal` runbook. The solution backs up the original configuration so you can roll back the containment from the Web UI. | Yes |
| Amazon Macie |  `Macie.SensitiveDataS3Object`  | S3 buckets containing objects with sensitive data | Enables S3 Block Public Access on the bucket to prevent public exposure of the sensitive data. | Yes |

**Manual follow-up required**
The Amazon GuardDuty and Amazon Macie remediations are a first line of defense and do not resolve the underlying finding. They contain or limit exposure of the affected resource, but a security team must investigate and complete service-specific follow-up before resolving the finding. The finding remains visible in the solution for that follow-up.
For `GuardDuty.IAMUser`, the containment can be rolled back from the Web UI. If auto-remediation is enabled for the control, the Web UI warns you when you start a rollback that the solution might re-remediate the finding, because rolling back leaves the finding eligible for the solution to act on again. Disable auto-remediation for the control before rolling back if you want the rollback to persist.
Because a rollback restores the resource to its pre-remediation (non-compliant) state, the underlying finding remains unresolved. Re-enabling auto-remediation for the control while that finding is still unresolved makes it eligible again, so the solution re-applies the remediation the next time AWS Security Hub emits an event for the finding. Keep auto-remediation disabled for the control until you have investigated and resolved the underlying finding.

**GuardDuty.IAMUser temporary credentials**
The `AWSSupport-ContainIAMPrincipal` runbook contains a long-term IAM user (its access key ID begins with `AKIA`). A `GuardDuty.IAMUser` finding whose compromised principal is a temporary credential from an assumed-role or federated session — its access key ID begins with `ASIA` — has no IAM user to contain, so every remediation attempt would fail. The solution does not automatically remediate these findings; it records them for visibility but never triggers the remediation. Investigate the originating role or identity provider and revoke the active session directly.

 **GuardDuty.IAMUser rollback button in the Web UI Remediation History**

![GuardDuty.IAMUser rollback button in the Remediation History table.](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/remediation-history-showing-rollback-button-guard-duty-finding.png)

 **GuardDuty.IAMUser rollback warning in the Web UI**

![GuardDuty.IAMUser rollback warning.](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/guarddutyrollback-warning-popup.png)

## Finding formats
<a name="finding-formats"></a>

Security Hub represents findings in two schema formats, and the solution processes both:
+  **ASFF (AWS Security Finding Format)** – The format used by AWS Security Hub CSPM (Classic). The solution processes AWS Security Hub CSPM control findings in ASFF.
+  **OCSF (Open Cybersecurity Schema Framework)** – The format used by AWS Security Hub v2. The solution processes Amazon Inspector, Amazon GuardDuty, and Amazon Macie findings in their native OCSF format.

Rather than forcing every finding into a single schema, the solution processes each finding in the format its source service emits. Existing remediations that use AWS Config continue to work unchanged in ASFF, while multi-service findings are processed in their native OCSF format.
