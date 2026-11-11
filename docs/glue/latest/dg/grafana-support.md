---
source_url: https://docs.aws.amazon.com/glue/latest/dg/grafana-support.html
---

# AWS Glue support for Grafana
<a name="grafana-support"></a>

AWS Glue supports Grafana as follows:

**Supported as a source?**
Yes. You can use AWS Glue ETL jobs to query data from Grafana.

**Supported as a target?**
No.

**Supported Grafana API versions**
The connector uses the Grafana HTTP API under `/api`, including the alerting provisioning API under `/api/v1/provisioning`. The API version is not configurable.
