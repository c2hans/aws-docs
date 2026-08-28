---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-using-json-format-template-variables.html
---

# Using JSON format template variables
<a name="cloudwatch-using-json-format-template-variables"></a>

 Some queries accept filters in JSON format and Grafana supports the conversion of template variables to JSON.

 If `env = 'production', 'staging'`, the following query will return ARNs of EC2 instances for which the `Environment` tag is `production` or `staging`.

```
resource_arns(us-east-1, ec2:instance, {"Environment":${env:json}})
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
