---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/rolling-back-a-remediation.html
---

# Rolling back a remediation
<a name="rolling-back-a-remediation"></a>

If you enabled rollback by setting the **EnableRollback** parameter to `yes` when deploying the administrator stack, you can reverse a completed remediation for supported controls and return the resource to its pre-remediation state. For an overview of how rollback works, see [Remediation rollback](remediation-rollback.md).

 **Who can roll back:** Rollback is restricted to users in the **administrator** and **delegated administrator** roles. Account operators can’t trigger a rollback, even for findings in their assigned accounts. The solution’s API enforces this restriction, not just the Web UI.

 **Supported controls:** Rollback is available only for controls whose remediation is a single, reversible configuration change. It also requires that the solution captured a pre-remediation snapshot. When a remediation’s control supports roll back and its snapshot was stored successfully, the solution marks that execution as rollback-capable. The `GuardDuty.IAMUser` containment is also rollback-capable through its own mechanism; see [Multi-service remediation](multi-service-remediation.md). To see which controls support rollback, open the **Controls** page in the Web UI. The **Rollback** column shows **Enabled** or **Disabled** for controls that support rollback, and **Not supported** for the rest.

 **To roll back a remediation:**

1. Sign in to the solution’s Web UI as an administrator or delegated administrator.

1. Open the **Execution History** and locate the successful remediation you want to reverse. Rollback-capable records show a **Rollback** action in the **Rollback** column.
![The Remediation History table showing a rollback-capable remediation.](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/remediation-history-rollback-success.png)

1. Choose **Rollback** on that record. A confirmation dialog describes the control, the affected resource, and the exact change the rollback will make. The dialog also warns that the rollback weakens the resource’s security posture.
![The Confirm Rollback dialog showing the control](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/confirm-rollback-dialog.png)

1. Choose **Confirm Rollback**. The solution starts the rollback and updates the record to `ROLLBACK_SUCCESS` after it restores the resource, or to `ROLLBACK_FAILED` if it can’t complete the rollback.

**Note**
A rollback restores the resource to its pre-remediation (non-compliant) state, so the underlying finding remains unresolved. If auto-remediation is enabled for the control, the solution might re-remediate the resource after the current finding expires. Disable auto-remediation for the control before rolling back if you want the rollback to persist. Keep auto-remediation disabled until you investigate and resolve the underlying finding.

**Note**
If another process modified the resource after the remediation ran, rollback detects the drift and stops with `ROLLBACK_FAILED` without changing the resource. This prevents the rollback from overwriting a change the solution didn’t make. Review the resource’s current configuration before deciding how to proceed.
