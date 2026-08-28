---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/create-notebook-local.html
---

# Hosting a Neptune Analytics graph-notebook on your local machine
<a name="create-notebook-local"></a>

It is also possible to install and run a Neptune Analytics graph notebook on your local machine. You can find instructions in the [GitHub graph-notebook repository](https://github.com/aws/graph-notebook):
+ [Prerequisites](https://github.com/aws/graph-notebook/#prerequisites)
+ [Jupyter Classic Notebook](https://github.com/aws/graph-notebook/#installation) or [https://github.com/aws/graph-notebook/#jupyterlab-3x](https://github.com/aws/graph-notebook/#jupyterlab-3x) installation
+ [Connecting to Neptune ](https://github.com/aws/graph-notebook/#amazon-neptune)

When setting up for Neptune Analytics:
+ When setting the connection using [%%graph\_notebook\_config](https://docs.aws.amazon.com/neptune/latest/userguide/notebooks-magics.html#notebooks-cell-magics-graph-notebook-config), make sure to set the `neptune_service` field to the value `neptune-graph`.
+ If you're connecting to a private graph endpoint, you need to enable access to the VPC where the Neptune Analytics instance resides. The easiest way to set this is up is using an SSH tunnel to a proxy EC2 instance in the VPC. For more information, see [Connecting graph notebook locally to Amazon Neptune](https://github.com/aws/graph-notebook/blob/main/additional-databases/neptune/README.md#connecting-graph-notebook-locally-to-amazon-neptune-first-time-setup) in GitHub.
+ If you're using a public graph endpoint, no additional connectivity setup is required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
