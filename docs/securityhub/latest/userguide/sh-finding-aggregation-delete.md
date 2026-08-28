---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/sh-finding-aggregation-delete.html
---

# Deleting cross-Region aggregation
<a name="sh-finding-aggregation-delete"></a>

If you do not want AWS Security Hub to aggregate data, you can delete your finding aggregator. Alternatively, you can keep your finding aggregator but not link any AWS Regions to the home Region by updating the existing aggregator to have no linked Regions selected.

To change your home Region, you must delete your current finding aggregator and create a new one.

When you delete your finding aggregator, Security Hub stops aggregating data. It does not remove any existing aggregated data from the home Region.

**Deleting the finding aggregator (console)**
You can delete your finding aggregator from the current home Region only.

In Regions other than the home Region, the Finding aggregation panel on the Security Hub console displays a message that you must edit the configuration in the home Region. Choose this message to display a link to switch to the home Region.

**To stop cross-Region aggregation (console)**

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. Ensure that you are signed in to your current home Region.

1. In the Security Hub navigation menu, choose **Settings**, then choose **General**.

1. Under **Cross-Region aggregation**, choose **Edit**.

1. Under **Aggregation Region**, choose **No aggregation Region**.

1. Choose **Save**.

1. On the confirmation dialog, in the confirmation field, type **Confirm**.

1. Choose **Confirm**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
