---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/exporting-and-importing-jobs.html
---

# Exporting and importing jobs
<a name="exporting-and-importing-jobs"></a>

Completed MediaConvert jobs remain on the **Jobs** page for three months. If you want to run a new job based on a completed job more than three months after you run it, export the job after it is complete and save it. Depending on how many jobs you run, exporting and then importing a job can be simpler than finding a particular job in your list and duplicating it.

**To export a job using the MediaConvert console**

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Choose the **Job ID** of the job that you want to export.

1. On the **Job summary** page, choose the **View JSON** button.

1. Choose **Copy** to copy the JSON to your clipboard.

1. Paste into your JSON editor and save.

**To import a job using the MediaConvert console**

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Choose **Import job**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
