---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/logging-monitoring.html
---

# Centralized logging and monitoring

Organizations often create dedicated AWS accounts for centralized logging and monitoring. These accounts collect and store logs from various AWS accounts and services within the organization for long-term archival and auditing. They also monitor activity in all accounts for threats and vulnerabilities. In the security organizational unit (OU), AWS Control Tower implements a centralized log store (Log Archive) for logs and a centralized audit account (Audit) for auditor access and security tooling.

**Note**
You might have customized these default account and OU names while setting up your landing zone in AWS Control Tower.

Logging, monitoring, and alerting are important components of an AWS Control Tower landing zone. When you set up the landing zone, it automatically launches some functionality. You can add other functionality later for a more comprehensive monitoring solution.
