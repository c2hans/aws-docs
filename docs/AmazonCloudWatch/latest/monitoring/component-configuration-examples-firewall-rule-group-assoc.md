---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-firewall-rule-group-assoc.html
---

# AWS Network Firewall rule group association
<a name="component-configuration-examples-firewall-rule-group-assoc"></a>

The following example shows a component configuration in JSON format for AWS Network Firewall rule group association.

```
{
  "alarmMetrics": [
    {
      "alarmMetricName": "FirewallRuleGroupQueryVolume",
      "monitor": true
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
