---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/supported-log-formats-and-log-sources.html
---

# Supported log formats and log sources
<a name="supported-log-formats-and-log-sources"></a>

The table lists the log formats supported by each log source. For more information about how to create log ingestion for each log format, refer to [Log Config](log-config.md).

| Log Format | Instance Group | EKS Cluster | Amazon S3 | Syslog |
| --- | --- | --- | --- | --- |
| NGINX | Yes | Yes | Yes | No |
| Apache HTTP Server | Yes | Yes | Yes | No |
| JSON | Yes | Yes | Yes | Yes |
| Single-line Text | Yes | Yes | Yes | Yes |
| Multi-line Text | Yes | Yes | Yes (Not support in Light Engine Mode) | No |
| Multi-line Text (Spring Boot) | Yes | Yes | Yes (Not support in Light Engine Mode) | No |
| Syslog RFC5424/RFC3164 | No | No | No | Yes |
| Syslog Custom | No | No | No | Yes |
| Windows Event | Yes | No | No | No |
| IIS | Yes | No | No | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
