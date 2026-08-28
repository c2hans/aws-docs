---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html
---

# AlertManagerDefinitionData YAML structure
<a name="yaml-AlertManagerDefinitionData"></a>

This structure contains the alert manager configuration as a blob (binary data). It is a base64-encoded YAML file. The following is an example of an alert manager configuration file YAML.

```
alertmanager_config: |
  route:
    receiver: 'default'
  receivers:
    - name: 'default'
      sns_configs:
      - topic_arn: arn:aws:sns:us-east-2:123456789012:My-Topic
        sigv4:
          region: us-east-2
        attributes:
          key: key1
          value: value1
```

For more information about alert manager configurations and their use, see [Creating an alert manager configuration file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html) in the *Amazon Managed Service for Prometheus User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
