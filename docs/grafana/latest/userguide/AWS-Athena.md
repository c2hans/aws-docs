---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/AWS-Athena.html
---

# Connect to an Amazon Athena data source
<a name="AWS-Athena"></a>

**Note**
In workspaces that support version 9 or newer, this data source might require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md).

**Note**
 This guide assumes that you are familiar with the Amazon Athena service before you use the Athena data source.

With Amazon Managed Grafana, you can add Athena as a data source by using the AWS data source configuration option in the Grafana workspace console. This feature simplifies adding Athena as a data source by discovering your existing Athena accounts and manages the configuration of the authentication credentials that are required to access Athena. You can use this method to set up authentication and add Athena as a data source, or you can manually set up the data source and the necessary authentication credentials using the same method that you would on a self-managed Grafana server.

 There are prerequisites for Athena to be accessible by Amazon Managed Grafana. For prerequisites associated with using the Athena data source, see [Prerequisites](Athena-prereq.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
