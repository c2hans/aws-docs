---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/incident-response.html
---

# Incident response in Amazon WorkSpaces Secure Browser
<a name="incident-response"></a>

You can detect incidents by monitoring the `SessionFailure` Amazon CloudWatch metric. To receive alerts for incidents, use a CloudWatch alarm for the `SessionFailure` metric. For more information, see [Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch](monitoring-cloudwatch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
