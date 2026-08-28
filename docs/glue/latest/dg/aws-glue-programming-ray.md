---
source_url: https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-ray.html
---

# Programming Ray scripts
<a name="aws-glue-programming-ray"></a>

**Important**
AWS Glue for Ray is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Glue for Ray end of support](https://docs.aws.amazon.com/glue/latest/dg/awsglue-ray-jobs-availability-change.html).

AWS Glue makes it easy to write and run Ray scripts. This section describes the supported Ray capabilities that are available in AWS Glue for Ray. You program Ray scripts in Python.

Your custom script must be compatible with the version of Ray that's defined by the `Runtime` field in your job definition. For more information about `Runtime` in the Jobs API, see [Jobs](aws-glue-api-jobs-job.md). For information about each runtime environment, see [Supported Ray runtime environments](ray-jobs-section.md#author-job-ray-runtimes).

**Topics**
+ [Tutorial: Writing an ETL script in AWS Glue for Ray](edit-script-ray-intro-tutorial.md)
+ [Using Ray Core and Ray Data in AWS Glue for Ray](edit-script-ray-scripting.md)
+ [Providing files and Python libraries to Ray jobs](edit-script-ray-env-dependencies.md)
+ [Connecting to data in Ray jobs](edit-script-ray-connections-formats.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
