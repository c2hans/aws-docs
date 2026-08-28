---
source_url: https://docs.aws.amazon.com/EDI/latest/eco-support-guide/eco-monitoring-mgmt.html
---

# Monitoring and event management for EDI
<a name="eco-monitoring-mgmt"></a>

The ECO monitors your EDI resources, including Amazon EKS resources for failures, performance degradation, and security issues.

As a managed account, ECO conﬁgures and deploys alarms for applicable EDI resources and Amazon Managed Service for Prometheus alert manager rules. ECO monitors these resources and performs incident management and remediation when needed.

ECO also relies on internal tools, such as AMS Accelerate [Resource Tagger](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-tagger.html) and [Alarm Manager](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-tag-alarms.html). ECO also uses native AWS services, such as AWS AppConfig, Amazon CloudWatch, Amazon EventBridge, Amazon GuardDuty, Amazon Macie, AWS Health, Amazon Managed Grafana and AWS Lambda.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Energy Data Insights on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query EDI` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
