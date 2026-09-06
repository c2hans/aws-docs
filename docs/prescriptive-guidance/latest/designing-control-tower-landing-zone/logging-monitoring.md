---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/logging-monitoring.html
---

# Centralized logging and monitoring
<a name="logging-monitoring"></a>

Organizations often create dedicated AWS accounts for centralized logging and monitoring purposes. These accounts are used to collect and store logs from various AWS accounts and services within the organization for long-term archival and auditing as well as monitoring the activity in all accounts for threats and vulnerabilities. In the security OU, AWS Control Tower implements a centralized log store (Log Archive) for logs and a centralized audit account (Audit) for auditor access and security tooling.

**Note**
You might have customized these default account and OU names while setting up your landing zone in AWS Control Tower.

Logging, monitoring, and alerting are important components of an AWS Control Tower landing zone. Some functionalities are automatically launched when you set up the landing zone, and you can add other functionalities later for a more comprehensive landing zone monitoring solution.
