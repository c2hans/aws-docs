---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/corruption-testing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Corruption testing
<a name="corruption-testing"></a>

 The Corruption Testing component establishes the ability to identify, evaluate, and measure the impact of a security event to files and components within the enterprise. This capability is essential to identify the last known good data for the data integrity recovery process.

* Table 3 — Corruption testing capability and the associated AWS services *

|  Capability and CSF mapping  |  AWS service  |  AWS service description  |  Function  |  [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) available?  |
| --- | --- | --- | --- | --- |
|  Corruption Testing <br /> PR.DS-6, PR.PT-1, DE.AE-4  |  [AWS Config rules](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html)  |  AWS Config rules are a configurable and extensible set of [AWS Lambda](https://aws.amazon.com/lambda/) functions (for which source code is available) that trigger when an environment configuration change is registered by the [AWS Config](https://aws.amazon.com/config/) service. If AWS Config rules deem a configuration change to be undesirable, customers can act to remediate it.  |  Provides notifications for changes to configuration, logs, detection, and re-porting in the event of changes to data on a system; provides notifications for changes to configuration.  |  Yes  |
|   |  [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html)  |  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) provides configuration management, which helps you maintain consistent configuration of your Amazon EC2 or on-premises instances. <br /> With Systems Manager, you can control configuration details such as server configurations, antivirus definitions, firewall settings, and more. <br /> You can define configuration policies for your servers through the [AWS Management Console](https://aws.amazon.com/console/) or use existing scripts, PowerShell modules, or Ansible playbooks directly from GitHub or S3 buckets. <br /> Systems Manager automatically applies your configurations across your instances at a time and frequency that you define. <br /> You can query Systems Manager at any time to view the status of your instance configurations, giving you on-demand visibility into your compliance status.  |  Provides notifications for changes to configuration, provides logs, detection, and re-porting in the event of changes to data on a system, and provides notifications for changes to configuration.  |  Yes  |
