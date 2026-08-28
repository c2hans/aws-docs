---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/creating-parameter-groups-cli.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Creating Parameter Groups with the AWS CLI
<a name="creating-parameter-groups-cli"></a>

You can create custom parameter groups using the AWS CLI to configure your InfluxDB 3 clusters. The following examples demonstrate how to create parameter groups with commonly modified parameters.

Example: Creating an Enterprise parameter group with custom query settings:

```
aws timestream-influxdb create-db-parameter-group \
  --name "my-enterprise-pg" \
  --description "Custom Enterprise parameter group" \
  --parameters '{
    "InfluxDBv3Enterprise": {
      "queryFileLimit": 500,
      "queryLogSize": 2000
    }
  }'
```

Example: Creating a Core parameter group with custom DataFusion threading:

```
aws timestream-influxdb create-db-parameter-group \
  --name "my-core-pg" \
  --description "Custom Core parameter group" \
  --parameters '{
    "InfluxDBv3Core": {
      "dataFusionNumThreads": 32,
      "queryFileLimit": 600
    }
  }'
```

**Note:** After creating a parameter group, you can use it when creating a new DB cluster by specifying `--db-parameter-group-identifier`, or when updating an existing cluster using the `update-db-cluster` command. Parameter groups cannot be modified after creation.

**Verifying your current running configuration:** You can check the effective parameter values on a running cluster by querying the `_internal` database's `nodes` table:

```
SELECT * FROM _internal.nodes
```

This query returns the active configuration for each node in your cluster, allowing you to verify parameter values before and after applying a new parameter group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
