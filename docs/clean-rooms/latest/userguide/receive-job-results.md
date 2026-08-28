---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/receive-job-results.html
---

# Receiving job results
<a name="receive-job-results"></a>

**Note**
The **Results destination in Amazon S3** can't be within the same S3 bucket as any data source.

The results of the job are located in the **Results settings defaults** section of the **Analysis** tab in the AWS Clean Rooms console.

**To receive job results**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Receive results**.

1. To receive the job results directly from AWS Clean Rooms, on the **Analysis** tab, under **Analyses**, select **All jobs** from the dropdown, and then under the **Protected job ID** column, select the job.

1. On the **Job details** page, under **Results**, copy the Job ID.

   Go back to the **Analysis** tab and expand the **Result settings defaults**.

   Under **Results destination**, select the link to view the results in Amazon S3.

   The Amazon S3 console opens in a separate tab.

   In Amazon S3, paste the Job ID in the Search bar and press enter.

   The folder containing the results appears. Select the folder to view the job results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
