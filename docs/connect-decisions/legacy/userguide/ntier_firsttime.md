---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/ntier_firsttime.html
---

# Using N-Tier Visibility for the first time
<a name="ntier_firsttime"></a>

You can use N-Tier Visibility with Supply Planning or Work Order Insights to extend visibility beyond your organization to your external trading partners. This visibility lets you align and confirm orders with suppliers, improving the accuracy of planning and execution processes.

**Note**
You can update the Forecast Commits and Purchase Orders response timeline anytime in AWS Supply Chain. On the AWS Supply Chain web application, choose the **Settings** icon, **Organization**, **Forecast Commits**, or **Purchase Orders** to update.

**Note**
When you use N-Tier Visibility for the first time, you'll be able to view the onboarding pages that highlight the key features. This helps you to get familiar with the N-Tier Visibility capabilities.

1. Open the AWS Supply Chain web application.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose **N-Tier Visibility**.

1. On the **Connect with your partners** page, choose **Next**.

   You can read through to understand what N-Tier Visibility offers, or choose **Next** until you get to the **Configure N-Tier Visibility Settings**.

1. Under **Setup forecast response time**, you can do the following:
   + **Set response timeline** – Define the number of days by when the Partner should respond to your data request.
   + **Auto accept responses** – Define a threshold limit for which you can let N-Tier Visibility auto accept responses from the Partner.
   + **Auto reject responses** – Define a threshold limit for which you can let N-Tier Visibility auto reject responses from the Partner.
   + **EDI connection settings** – Define if you would like N-Tier Visibility to use EDI for collaboration on forecast commits with partners.

1. Choose **Continue**.

1. Under **Setup your Purchase Order response timeline**, you can do the following:
   + **Set response timeline** – Define the number of days by when the Partner should respond to your purchase order requests.
   + **Auto accept responses** – Define a threshold limit for which you can let N-Tier Visibility auto accept responses from the Partner.
   + **Auto reject responses** – Define a threshold limit for which you can let N-Tier Visibility auto reject responses from the Partner.
   + **EDI connection settings** – Define if you would like N-Tier Visibility to use EDI for collaboration on purchase orders with partners.

1. Choose **Finish**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
