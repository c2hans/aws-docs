---
source_url: https://docs.aws.amazon.com/glue/latest/dg/edit-script.html
---

# AWS Glue programming guide
<a name="edit-script"></a>

A script contains the code that extracts data from sources, transforms it, and loads it into targets. AWS Glue runs a script when it starts a job.

AWS Glue ETL scripts are coded in Python or Scala. While all job types can be written in Python, AWS Glue for Spark jobs can be written in Scala as well. When you automatically generate the source code logic for your job in AWS Glue Studio, a script is created. You can edit this script, or you can provide your own script to process your ETL work.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
