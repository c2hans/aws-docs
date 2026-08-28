---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/submit-array-job.html
---

# Submit an AWS Batch array job
<a name="submit-array-job"></a>

After you registered your job definition, you can submit an AWS Batch array job that uses your new container image.

**To submit an AWS Batch array job**

1. Create a file named `print-color-job.json` in your workspace directory and paste the following into it.
**Note**
This example uses the job queue mentioned in the [Prerequisites](array-tutorial-prereqs.md) section.

   ```
   {
     "jobName": "print-color",
     "jobQueue": "{{{{existing-job-queue}}}}",
     "arrayProperties": {
       "size": 7
     },
     "jobDefinition": "print-color"
   }
   ```

1. Submit the job to your AWS Batch job queue. Note the job ID that's returned in the output.

   ```
   $ aws batch submit-job --cli-input-json file://print-color-job.json
   ```

1. Describe the job's status and wait for the job to move to `SUCCEEDED`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
