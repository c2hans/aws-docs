---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-gauge.html
---

# Gauge panel
<a name="v9-panels-gauge"></a>

****
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Gauge is a single-value visualization that can repeat a gauge for every series, column or row.

**Value options**

Use the following options to refine how your visualization displays the value:

**Show**

Choose how Grafana displays your data.

**Calculate**

Show a calculated value based on all rows.
+ **Calculation** – Select a reducer function that Grafana will use to reduce many fields to a single value. For a list of available calculations, refer to [Calculation types](v9-panels-calculation-types.md).
+ **Fields** – Select the fields to display in the panel.

**All values**

Show a separate stat for every row. If you select this option, then you can also limit the number of rows to display.
+ **Limit** – The maximum number of rows to display. Default is 5,000.
+ **Fields** – Select the fields to display in the panel.

**Gauge**

Adjust how the gauge is displayed.
+ **Show threshold labels** – Controls if threshold values are shown.
+ **Show threshold markers** – Controls if a threshold band is shown outside the inner gauge value band.

**Text size**

Adjust the sizes of the gauge text.
+ **Title** – Enter a numeric value for the gauge title size.
+ **Value** – Enter a numeric value for the gauge value size.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
