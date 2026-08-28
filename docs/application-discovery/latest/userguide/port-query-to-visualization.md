---
source_url: https://docs.aws.amazon.com/application-discovery/latest/userguide/port-query-to-visualization.html
---

AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

# Visualizing Amazon Athena data
<a name="port-query-to-visualization"></a>

To visualize your data, a query can be ported to a visualization program such as Amazon Quick or other open-source visualization tools such as Cytoscape, yEd, or Gelphi. Use these tools to render network diagrams, summary charts, and other graphical representations. When this method is used, you connect to Athena through the visualization program so that it can access your collected data as a source to produce the visualization.

**To visualize your Amazon Athena data using Quick**

1. Sign in to [Amazon Quick](https://aws.amazon.com/quicksight/).

1. Choose **Connect to another data source or upload a file**.

1. Choose **Athena**. The **New Athena data source** dialog box displays.

1. Enter a name in the **Data source name** field.

1. Choose **Create data source**.

1. Select the **Agents-servers-os** table in the **Choose your table** dialog box and choose **Select**.

1. In the **Finish dataset creation** dialog box, select **Import to SPICE for quicker analytics**, and choose **Visualize**.

   Your visualization is rendered.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
