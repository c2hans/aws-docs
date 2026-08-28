---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-examples.html
---

# Example queries
<a name="sql-examples"></a>

## Metadata filtering
<a name="sql-examples-meta-filter"></a>

The following example is for metadata filtering with a `SELECT` statement with the AWS IoT SiteWise query language:

```
SELECT a.asset_name, p.property_name
FROM asset a, asset_property p
WHERE a.asset_name LIKE '{{Windmill%}}'
```

## Value filtering
<a name="sql-examples-value-filter"></a>

The following is an example of value filtering using a `SELECT` statement with the AWS IoT SiteWise query language:

```
SELECT a.asset_name, r.int_value
FROM asset a, raw_time_series r
WHERE r.int_value > 30
AND r.event_timestamp > TIMESTAMP '{{2022-01-05 12:15:00}}'
AND r.event_timestamp < TIMESTAMP '{{2022-01-05 12:20:00}}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
