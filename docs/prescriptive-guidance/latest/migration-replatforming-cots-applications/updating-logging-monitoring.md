---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/updating-logging-monitoring.html
---

# Updating the logging and monitoring components
<a name="updating-logging-monitoring"></a>

Some legacy environments use centralized logging and monitoring tools (for example, [Splunk](https://www.splunk.com/), [SolarWinds,](https://www.solarwinds.com/) or [Zabbix](https://www.zabbix.com/)) for infrastructure and application monitoring. Application support teams might also use Secure Shell (SSH) protocol or remote desktop protocol (RDP) to monitor and debug. To avoid this manual and repetitive process, you can use [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to automate monitoring on the AWS Cloud.

We recommend using CloudWatch metrics to monitor your infrastructure and CloudWatch agents to send application logs to CloudWatch. After application logs are received by CloudWatch, you can create [CloudWatch metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringPolicyExamples.html) and use [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to monitor application errors and automatically notify support teams.

CloudWatch also provides tools to build operational dashboards for ongoing reviews of production operations for your applications. Third-party centralized monitoring tools can be integrated with CloudWatch and other AWS services, and this helps extend your existing operational practices to infrastructure and applications on the AWS Cloud. However, you might have to retrain your support or operation teams if you choose to operate applications in the AWS Cloud. For more information about this, see the [Operations perspective: Manage and scale](https://d1.awsstatic.com/whitepapers/aws_cloud_adoption_framework.pdf) section of the AWS Cloud Adoption Framework (AWS CAF) whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
