---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/remediation-rollback.html
---

# Remediation rollback
<a name="remediation-rollback"></a>

Remediation rollback lets you reverse a completed remediation. It returns the affected resource to the state it was in before the solution changed it. Rollback is an opt-in feature. You enable it by setting the **EnableRollback** parameter to `yes` when you deploy the administrator stack. Only users in the administrator or delegated administrator roles can trigger it (see [Rolling back a remediation](rolling-back-a-remediation.md)). It is supported for a defined set of controls whose remediation is a single, reversible configuration change.

The following controls currently support snapshot-based rollback, grouped by service:
+ AWS KMS – `KMS.4`
+ Amazon SNS – `SNS.1`
+ Amazon RDS – `RDS.6`, `RDS.7`, `RDS.8`, `RDS.13`, `RDS.16`
+ Amazon ElastiCache – `ElastiCache.1`, `ElastiCache.2`
+ Amazon DynamoDB – `DynamoDB.6`
+ AWS Systems Manager – `SSM.7`
+ Amazon S3 – `S3.6`
+ AWS Secrets Manager – `SecretsManager.3`

To confirm which controls support rollback in your deployment, open the **Controls** page in the Web UI. The **Rollback** column shows a toggle for supported controls and **Not supported** for the rest.

For these controls, rollback is snapshot-based:

1.  **Capture (during remediation).** Before a supported remediation changes a resource, the AWS Systems Manager runbook reads the resource’s current configuration. The runbook writes this configuration as a JSON snapshot to the existing remediation configuration Amazon S3 bucket in the member account, under the `snapshots/` prefix. The bucket is encrypted, versioned, and blocks public access. Snapshot capture is *fail-open*. If the runbook can’t write the snapshot, the remediation still proceeds. The solution then marks the execution as not rollback-capable rather than blocking the fix.

1.  **Record.** When the snapshot is stored successfully, the solution records that the execution is rollback-capable, along with the snapshot’s version, on the remediation history record for the finding.

1.  **Restore (on demand).** When an authorized user triggers a rollback, the same runbook is invoked in reverse: it reads the recorded snapshot by its exact version, verifies the resource has not drifted, and restores the pre-remediation configuration. The execution completes as `ROLLBACK_SUCCESS` or `ROLLBACK_FAILED`.

The solution applies the following safeguards to snapshot-based rollback:
+  **Exact-version restore.** Rollback reads the snapshot by its recorded version and stops if that S3 object version has changed, so a tampered snapshot is never applied.
+  **Drift check.** Before restoring, rollback compares the resource’s current configuration to the post-remediation value the solution recorded. If they differ, another process changed the resource after the remediation. In that case, rollback aborts with `ROLLBACK_FAILED` and leaves the resource unchanged rather than overwriting the later change.
+  **One-shot.** After a successful rollback, the solution marks the finding as no longer rollback-capable, so you can’t replay a rollback.

**Note**
A rollback returns the resource to its pre-remediation, non-compliant state, so the underlying Security Hub finding remains unresolved. If auto-remediation is enabled for the control, the solution might re-remediate the resource after the current finding expires. To keep a rollback in place, disable auto-remediation for the control before you roll back, and keep it disabled until the underlying finding is investigated and resolved. For the steps, see [Rolling back a remediation](rolling-back-a-remediation.md).

**Note**
The `GuardDuty.IAMUser` remediation is also rollback-capable, but it uses a different mechanism: the AWS-managed `AWSSupport-ContainIAMPrincipal` runbook backs up the original IAM configuration and restores it on rollback, rather than the snapshot process described here. For its behavior and cautions, see [Multi-service remediation](multi-service-remediation.md).
