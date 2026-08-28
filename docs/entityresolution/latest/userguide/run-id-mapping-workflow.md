---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/run-id-mapping-workflow.html
---

# Running an ID mapping workflow
<a name="run-id-mapping-workflow"></a>

After you [create an ID mapping workflow for one AWS account](creating-id-mapping-workflow-same-account.md) or [create an ID mapping workflow across two AWS accounts](creating-id-mapping-workflow-two-accounts.md), you can run the ID mapping workflow. The ID mapping workflow outputs a CSV file.

**To run an ID mapping workflow**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **ID mapping**.

1. Choose the ID mapping workflow.

1. On the ID mapping workflow details page, in the upper right corner, choose **Run**.

1. On the matching workflow details page, on the **Metrics** tab, view the following under **Last job metrics**:
   + The **Job ID**
   + The **Status** of the matching workflow job: **Queued**, **In progress**, **Completed**, **Failed**
   + The **Run type**
   + The **Time started** for the workflow job
   + The **Time completed** for the workflow job
   + The **Duration** of the workflow job
   + The **Output destination**
   + The **AWS KMS key**
   + The **Service role**
   + The number of **Input records**
   + The number of **Unique records**
   + The number of **New unique records loaded**
   + The number of **Mapped records**
   + The number of **Mapped records removed**
   + The number of **New mapped records**
   + The number of **Mapped source records**
   + The number of **New mapped source records **
   + The number of **Mapped source records removed**
   + The number of **Mapped target records**
   + The number of **New mapped target records**
   + The number of **Mapped target records removed**
   + The number of **Delete records processed**
   + The number of **Records processed**
   + The number of **Records not processed**

   Under **Job history**, you can also view the job metrics for previously run ID mapping workflow jobs.

1. After the ID mapping workflow job completes (status is **Completed**), choose **Data output**, and then choose your **Amazon S3 location** to view the results.

   After you get your CSV file, you can join the `RAMPID` with the `TRANSCODED_ID`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
