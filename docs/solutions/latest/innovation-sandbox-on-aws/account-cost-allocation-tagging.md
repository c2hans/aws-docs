---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-cost-allocation-tagging.html
---

# Account cost allocation tagging
<a name="account-cost-allocation-tagging"></a>

Innovation Sandbox on AWS applies [AWS Organizations account tags](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html) to sandbox accounts throughout the account lifecycle. After you activate them as [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html), these tags appear as dimensions in the AWS Billing and Cost Management console. You can then filter, group, and analyze sandbox costs by lease, user, cost report group, lease template, and account state in AWS Cost Explorer, AWS Budgets, and Cost and Usage Reports (CUR).

Tags apply to the AWS account itself, so all costs incurred in the account inherit the tag values. This complements the solution’s monthly CSV cost reports. Tagging is automatic for new leases and requires no action to enable. Leases that existed before you deployed this feature keep using the solution’s existing Cost Explorer attribution until they are terminated.

## ISB account tag schema
<a name="isb-account-tag-schema"></a>

The solution manages the following five account tag keys. All keys are prefixed with `ISB-<namespace>:`, where `<namespace>` is the namespace of your deployment. This namespacing keeps tag keys distinct across multiple deployments in the same organization, so cost queries do not aggregate across them. The keys are restricted through the Org Management Spoke Role IAM policy so that the solution can only tag accounts with these specific keys.

| Tag key | Applied on | Removed on | Purpose |
| --- | --- | --- | --- |
|  `ISB-<namespace>:LeaseId`  | Lease approval | Cleanup completion | Cost attribution per lease |
|  `ISB-<namespace>:CostReportGroup`  | Lease approval (from the lease template) | Cleanup completion | Cost attribution per team or department |
|  `ISB-<namespace>:LeaseTemplate`  | Lease approval (lease template ID) | Cleanup completion | Cost attribution per sandbox type |
|  `ISB-<namespace>:User`  | Lease approval (user ID) | Cleanup completion | Cost attribution per user |
|  `ISB-<namespace>:Status`  | Every organizational unit (OU) transition (value = current account state) | Account ejection | Tracks account state across all lifecycle states |

The `ISB-<namespace>:Status` tag value reflects the current account state (`Available`, `Active`, `Frozen`, `CleanUp`, or `Quarantine`) and is written on every OU transition. During the `Active` and `Frozen` states, the four lease tags identify the lease, while `ISB-<namespace>:Status` adds the lifecycle state as an additional Cost Explorer dimension.

Account tags are a best-effort cost-visibility mechanism. The authoritative source of account and lease state is the solution’s Amazon DynamoDB records. If a tagging operation fails, the failure is logged (see [Alarms](monitoring-alarms.md)) and the account lifecycle operation still proceeds.

## Tag lifecycle
<a name="tag-lifecycle"></a>

The solution applies and removes account tags in step with the account lifecycle:
+  **Lease approval (Available → Active)**: The four lease tags (`ISB-<namespace>:LeaseId`, `ISB-<namespace>:CostReportGroup`, `ISB-<namespace>:LeaseTemplate`, `ISB-<namespace>:User`) and `ISB-<namespace>:Status=Active` are applied after the lease is successfully approved.
+  **Freeze and unfreeze (Active <→ Frozen)**: Only `ISB-<namespace>:Status` changes (`Frozen` or `Active`). The four lease tags remain on the account.
+  **Cleanup completion (CleanUp → Available)**: The four lease tags are removed and `ISB-<namespace>:Status` is updated to `Available`.
+  **Quarantine**: Tags persist on quarantined accounts. They are removed when cleanup is retried and succeeds, or when the account is ejected.
+  **Account ejection (any state → Exit)**: All five ISB tags are removed before the account moves to the Exit OU.

## Tag activation workflow
<a name="tag-activation-workflow"></a>

Before account tags can be used for cost analysis, the ISB tag keys must be activated as cost allocation tags in the AWS Billing and Cost Management console. The solution automates this using an AWS Step Functions workflow deployed in the Hub account as part of the Compute stack.

On stack deployment or update, a custom resource starts the workflow. The workflow:

1. Tags the Hub account with the ISB tag keys so that the keys propagate into the billing system.

1. Invokes a checker AWS Lambda function that queries `ce:ListCostAllocationTags` to determine whether the ISB tag keys are available in the billing system.

1. If the tag keys are not yet available, the workflow waits one hour and retries, for a maximum of 24 attempts (up to 24 hours).

1. When the tag keys appear, the checker Lambda function activates them as cost allocation tags and removes the temporary tags from the Hub account.

The custom resource returns success to AWS CloudFormation immediately without waiting for activation to complete, so deployment is not blocked by the activation process. The workflow is idempotent, so re-running it on a stack update completes immediately if the tag keys are already active.

The following table describes the workflow behavior for each stack lifecycle event.

| Stack event | Tag activation behavior |
| --- | --- |
| Create or Update | Triggers the activation workflow without waiting for it to complete. If tag keys are already active, the workflow completes on the first check. |
| Delete | Deactivates the ISB cost allocation tags. Historical cost data remains queryable in Cost Explorer for the retention window AWS provides even after deactivation. |
| Rollback | Stops any in-progress activation workflow and removes the temporary seed tags from the Hub account. Tags that were already activated remain active. |

A CloudWatch alarm monitors for any terminal non-success of the workflow that is not operator-initiated. It fires when the sum of the state machine’s `ExecutionsFailed` and `ExecutionsTimedOut` metrics over 1 hour is 1 or more. The following conditions trigger the alarm: an unhandled Lambda error; the `TagActivationMaxAttemptsReached` failure, which occurs when the workflow exhausts all 24 retry attempts; or the state machine’s own timeout. In this case, you can manually activate the ISB tag keys in the AWS Billing and Cost Management console. For more information, see the [Manually activating cost allocation tags](troubleshooting.md#manually-activating-cost-allocation-tags) section.

## Tag-based cost attribution
<a name="tag-based-cost-attribution"></a>

The lease monitoring Lambda function uses a tag-first approach to attribute costs for budget threshold evaluation:

1. It first queries AWS Cost Explorer using a filter on the `accountTag/ISB-<namespace>:LeaseId` tag to retrieve costs for tagged accounts.

1. For any lease that does not return tag-based cost data (a lease created before this feature, or a lease whose tags are not yet active in billing), it falls back to the existing `LINKED_ACCOUNT` dimension query with date-based correlation.

This tag-first approach keeps cost monitoring accurate while tag keys propagate and for leases created before the feature was deployed, with negligible added Cost Explorer API cost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
