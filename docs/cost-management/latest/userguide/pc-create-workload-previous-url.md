---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/pc-create-workload-previous-url.html
---

# Adding previously saved estimates to my workload estimate
<a name="pc-create-workload-previous-url"></a>

This section outlines how to add previously saved estimates from the public Pricing Calculator to a workload estimate. For instructions on how to generate a public Pricing Calculator URL, see [Sharing an estimate link](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/save-share-estimate.html#create-estimate-link) in the public Pricing Calculator user guide.

**Note**
Any Savings Plans or Reserved Instances you have modeled in your public Pricing Calculator estimates won't be included when you're adding these estimates from the public Pricing Calculator to a workload estimate or bill scenario.

## Prerequisites
<a name="pc-create-workload-previous-url-prerequisites"></a>

The following procedure assumes that you have already completed the [Creating a workload estimate](pc-create-workload.md) process.

## Procedure
<a name="pc-create-workload-previous-url-procedure"></a>

**To add previously saved estimates to a workload estimate**

1. Open the Pricing Calculator console at [ https://console.aws.amazon.com/costmanagement/ ](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Pricing Calculator**.

1. Navigate to the workload estimate where you want to add previously saved estimates (URL).

1. From the **Add** dropdown, choose **Previously saved estimates**.

1. In the **Shared estimate URL** section, paste the URL of your previously saved estimate. For instruction on how to generate a public Pricing Calculator URL, see [Sharing an estimate link](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/save-share-estimate.html#create-estimate-link) in the public Pricing Calculator user guide.

1. Select an account

1. You can choose to add your usage to an existing group or a new group you create.

1. Choose **Import**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
