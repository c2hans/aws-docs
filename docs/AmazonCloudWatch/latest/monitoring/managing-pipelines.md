---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/managing-pipelines.html
---

# Managing pipelines
<a name="managing-pipelines"></a>

After creating pipelines, you can monitor their performance and manage their configuration through the Pipelines tab.

**Pipeline status monitoring**

Each pipeline displays real-time status information including:
+ Pipeline status: Active, Creating, Updating, Deleting, Create Failed, Update Failed, or Delete Failed.
+ Data throughput metrics
+ Error rates and failure details

**Pipeline operations**

You can perform the following operations on existing pipelines:
+ **View details** – Review pipeline configuration and status
+ **Edit pipeline** – Edit pipeline configuration including processors, parsing, and source selection criteria
+ **Delete pipeline** – Remove pipelines that are no longer needed

**Note**
To programmatically manage metrics pipelines, use the Observability Admin APIs including `CreateTelemetryPipeline`, `UpdateTelemetryPipeline`, and `DeleteTelemetryPipeline`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
