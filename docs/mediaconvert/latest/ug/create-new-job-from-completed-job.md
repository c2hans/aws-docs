---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/create-new-job-from-completed-job.html
---

# Duplicating a job
<a name="create-new-job-from-completed-job"></a>

To create a job that is similar to one that you ran before, you can duplicate a job from your job history. You can also modify any settings if you want to change them.

**To create a job based on a recent job using the MediaConvert console**

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Choose the **Job ID** of the job that you want to duplicate.

1. Choose **Duplicate**.

1. Optionally modify any job settings.

   Settings that are likely to change from job to job include the following: input file location, output destination locations, and output name modifiers. If you run transcoding jobs for your customers who have different AWS accounts from your account, you also must change the **IAM role** under **Job settings**.

1. Choose **Create** at the bottom of the page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
