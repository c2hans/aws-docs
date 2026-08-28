---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial.html
---

# Tutorial: Export an Amazon Keyspaces table to Amazon S3 using AWS Glue
<a name="S3-tutorial"></a>

This tutorial shows you how to export an Amazon Keyspaces table to an Amazon S3 bucket using AWS Glue. The tutorial uses the `keyspaces-bulk-cli` CLI tool available in the Amazon Keyspaces [GitHub](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue) repo. Using this tool, you can export Amazon Keyspaces data to Amazon S3 without having to set up a Spark cluster.

**Topics**
+ [Prerequisites for exporting data from Amazon Keyspaces to Amazon S3](S3-tutorial-prerequisites.md)
+ [Step 1: Bootstrap the infrastructure and AWS Glue jobs](S3-tutorial-step1.md)
+ [Step 2: Run the export job](S3-tutorial-step2.md)
+ [Step 3: (Optional) Create a trigger to schedule the export job](S3-tutorial-step3.md)
+ [Step 4: (Optional) Cleanup](S3-tutorial-step4.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
