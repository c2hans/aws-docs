---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/monitoring-cost.html
---

# Cost monitoring
<a name="monitoring-cost"></a>

Innovation Sandbox applies AWS Organizations account tags to sandbox accounts throughout the lease lifecycle and activates them as cost allocation tags. This allows you to analyze sandbox costs by lease, user, cost report group, lease template, and account state.

For planning details about the tagging feature, see [Account cost allocation tags](account-cost-allocation-tags-planning.md) in Plan your deployment. For an architectural description, see [Account cost allocation tagging](account-cost-allocation-tagging.md) in Architecture details.

## Querying sandbox costs by tag
<a name="querying-sandbox-costs-by-tag"></a>

After the ISB tag keys are active, you can analyze sandbox costs in AWS Cost Explorer:

1. Sign in to the AWS Organizations management account and open [AWS Cost Explorer](https://console.aws.amazon.com/cost-management/home#/cost-explorer).

1. Under **Filters**, choose **Tag**, and then select an ISB tag key (for example, `ISB-<namespace>:CostReportGroup` or `ISB-<namespace>:User`).

1. Optionally, set **Group by** to **Tag** and select an ISB tag key to break down costs by that dimension.

The solution attributes cost to a tag only from the time it applies the tag to the account — tags are not retroactive. Leases created before this feature was deployed do not have account tags and continue to use the solution’s existing cost attribution.

## Checking tag activation status
<a name="checking-tag-activation-status"></a>

To verify whether ISB tag keys are active:

1. Sign in to the AWS Organizations management account.

1. Open the [Cost allocation tags console](https://console.aws.amazon.com/billing/home#/tags).

1. Search for `ISB-<namespace>` to locate the five ISB tag keys.

1. Confirm each tag shows a status of **Active**.

If tags are not active after 24 hours, see [Manually activating cost allocation tags](troubleshooting.md#manually-activating-cost-allocation-tags) in the Troubleshooting section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
