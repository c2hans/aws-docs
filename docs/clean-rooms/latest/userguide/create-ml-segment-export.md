---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-segment-export.html
---

# Exporting a lookalike segment
<a name="create-ml-segment-export"></a>

After you have created a lookalike segment, you can export that data to an Amazon S3 bucket.

**To export a lookalike segment in AWS Clean Rooms**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. On the **With active membership** tab, choose a collaboration.

1. On the **ML Models** tab, select a lookalike segment and choose **Export**.

1. For **Export lookalike model**, for **Export lookalike model details** enter a **Name** and optional **Description**.

1. For **Segment size**, choose the size you want for the exported segment.

1. Choose **Export**.

For the corresponding API action, see [StartAudienceExportJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceExportJob.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
