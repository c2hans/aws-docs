---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/using-influxdb-in-AMG.html
---

# Connect to an InfluxDB data source
<a name="using-influxdb-in-AMG"></a>

 Grafana ships with a feature-rich data source plugin for InfluxDB. The plugin includes a custom query editor and supports annotations and query templates.

## Adding the data source
<a name="influxdb-add-the-data-source"></a>

1.  Open the side menu by choosing the Grafana icon in the top header.

1.  In the side menu under the link,**Dashboards** you should find a link named **Data Sources**.

1.  Choose the **\+ Add data source** button in the top header.

1.  Select **InfluxDB** from the **Type** dropdown list.

1.  Select **InfluxQL** or **Flux** from the **Query Language** list.

**Note**
 If you don't see the **Data Sources** link in your side menu, it means that your current user does not have the `Admin` role.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
