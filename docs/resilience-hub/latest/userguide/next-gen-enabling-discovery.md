---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-enabling-discovery.html
---

# Enabling dependency discovery for a service
<a name="next-gen-enabling-discovery"></a>

You can enable dependency discovery from the console or using the AWS CLI.

**To enable dependency discovery for a single service (console)**

Navigate to your service in the console and choose the **Assessment** tab. Then choose **Enable dependency discovery**.

**To enable dependency discovery for a single service (CLI)**

```
aws resiliencehubv2 update-service \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123" \
  --dependency-discovery "ENABLED"
```

After you enable dependency discovery, Next generation Resilience Hub performs the following steps:

1. Queries 35 days of historical DNS data for your service's compute resources.

1. Identifies, deduplicates, and attributes dependencies to your service.

1. Continues monitoring hourly to detect new dependencies and update existing ones.

1. Displays results for your service in the console under the "Assessments" tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
