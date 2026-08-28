---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/view-history-of-spice-ingestion.html
---

# View SPICE ingestion history
<a name="view-history-of-spice-ingestion"></a>

You can view the ingestion history for SPICE datasets to find out, for example, when the latest ingestion started and what its status is.

The SPICE ingestion history page includes the following information:
+ Date and time that the ingestion started (UTC)
+ Status of the ingestion
+ Amount of time that the ingestion took
+ The number of aggregated rows in the dataset.
+ The number of rows ingested during a refresh.
+ Rows skipped and rows ingested (imported) successfully
+ The job type for the refresh: scheduled, full refresh, and so on

Use the following procedure to view a dataset's SPICE ingestion history.

**To view a dataset's SPICE ingestion history**

1. From the homepage, choose **Data** at left.

1. On the **Datasets** tab, choose the dataset that you want to examine.

1. On the dataset details page that opens, choose the **Refresh** tab.

   SPICE ingestion history is shown at bottom.

1. (Optional) Choose a time frame to filter the entries from the last hour to the last 90 days.

1. (Optional) Choose a specific job status to filter the entries, for example **Running** or **Completed**. Otherwise, you can view all entries by choosing **All**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
