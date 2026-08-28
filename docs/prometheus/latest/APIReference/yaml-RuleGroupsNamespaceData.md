---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html
---

# RuleGroupsNamespaceData YAML structure
<a name="yaml-RuleGroupsNamespaceData"></a>

The `RuleGroupsNamespaceData` structure contains the rule groups file as a base64-encoded blob of the YAML file. The following is an example of an rules file YAML.

```
groups:
  - name: test
    rules:
    - record: metric:recording_rule
      expr: avg(rate(container_cpu_usage_seconds_total[5m]))
  - name: alert-test
    rules:
    - alert: metric:alerting_rule
      expr: avg(rate(container_cpu_usage_seconds_total[5m])) > 0
      for: 2m
```

For more details about rules, see [Recording rules and alerting rules](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-Ruler.html) in the *Amazon Managed Service for Prometheus User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
