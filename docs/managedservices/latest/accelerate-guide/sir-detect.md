---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/sir-detect.html
---

# Detect
<a name="sir-detect"></a>

During the management of your AWS accounts, AMS monitors for anomalies in user behavior, account activities and potential security events using data collected from detection sources and controls including but not limited to Amazon CloudWatch, Amazon GuardDuty, VPC Flow Logs, Amazon Macie, AWS Config and Amazon internal Threat Intelligence feeds.

AMS uses both native AWS services and other detection technologies to respond to security events created by:
+ Config Conformance Finding Types
+ GuardDuty Finding Types
+ Macie Finding Types
+ Amazon Route 53 Resolver DNS Firewall Events
+ AMS Security events (cloud watch alarms)

Additional findings are added as services, products and threat ecosystems evolves.

## Report security events to AMS
<a name="sir-report"></a>

Raise an incident through the AMS Support Portal or Support Center to notify AMS of a security incident or to request investigations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
