---
source_url: https://docs.aws.amazon.com/sap/latest/general/allawssecurity.html
---

# Using All AWS Security Services
<a name="allawssecurity"></a>

Combining together all services described above allow for an architecture monitoring multiple areas of a RISE on AWS deployment: network traffic, DNS logs, CloudTrail API activity, sensitive information extracted SAP data. Amazon GuardDuty and AWS Security Hub are fed from multiple services and uses AIML intelligence to detect malicious activities and anomalies. Findings are passed to Amazon Detective for a deeper RCA analysis or sent to Amazon EventBridge for custom reporting and alerting.

Below is example architecture of GuardDuty, AWS Network Firewall, Amazon Macie, AWS Security Hub and Amazon Detective combined together to improve security posture of RISE with SAP on AWS deployment

![GuardDuty](http://docs.aws.amazon.com/sap/latest/general/images/rise-security-allawssecurity.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
