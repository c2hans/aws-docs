---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-using-metrics.html
---

# Using the Metrics Destination
<a name="emr-hbase-using-metrics"></a>

With EMR 7.1, you have the option to send your metrics data to Amazon CloudWatch or Amazon Managed Service for Prometheus. This choice allows you to integrate seamlessly with different monitoring tools, based on your needs.

## Sending Metrics to Amazon CloudWatch
<a name="emr-hbase-using-metrics-cw"></a>

To send metrics to CloudWatch, use this configuration:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {
      "metrics_destination": "cloudwatch"
    },
    "Configurations": []
  }
]
```

## Sending Metrics to Amazon Managed Service for Prometheus
<a name="emr-hbase-using-metrics-prom"></a>

If you prefer using Prometheus, set the destination and provide the endpoint URL:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {
      "metrics_destination": "prometheus",
      "prometheus_endpoint": "https://aps-workspaces.{{region}}.amazonaws.com/workspaces/{{workspace_id}}/api/v1/remote_write"
    },
    "Configurations": []
  }
]
```

Replace `region` with your AWS region and `workspace_id` with your Prometheus workspace ID. This configuration directs your HBase metrics to Prometheus using the specified endpoint.

With above setup, you can see the below metrics under the **Monitoring** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
