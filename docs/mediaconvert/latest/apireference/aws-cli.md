---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/aws-cli.html
---

# AWS Elemental MediaConvert CreateJob Example Using the AWS CLI
<a name="aws-cli"></a>

A job does the work of transcoding a media file. When you create a job using the AWS CLI, you specify the job settings that AWS Elemental MediaConvert requires to perform the transcoding.

**To create a transcoding job using the AWS CLI:**
+ Specify your job settings with `--cli-input-json`:

  ```
  aws mediaconvert create-job \
      --region {{region-name-1}} \
      --cli-input-json {{file://job.json}}
  ```

  In the preceding example, `job.json` specifies your job settings. You can use the MediaConvert console to generate the JSON job specification. For more information and sample job specifications, see [Creating Your Job Specification](creating-your-json-job-specification.md).

  For more information about how to create a job using the AWS CLI, see the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
