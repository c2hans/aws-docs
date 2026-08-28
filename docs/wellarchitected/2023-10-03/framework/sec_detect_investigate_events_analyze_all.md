---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_detect_investigate_events_analyze_all.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC04-BP02 Analyze logs, findings, and metrics centrally
<a name="sec_detect_investigate_events_analyze_all"></a>

 Security operations teams rely on the collection of logs and the use of search tools to discover potential events of interest, which might indicate unauthorized activity or unintentional change. However, simply analyzing collected data and manually processing information is insufficient to keep up with the volume of information flowing from complex architectures. Analysis and reporting alone don’t facilitate the assignment of the right resources to work an event in a timely fashion.

A best practice for building a mature security operations team is to deeply integrate the flow of security events and findings into a notification and workflow system such as a ticketing system, a bug or issue system, or other security information and event management (SIEM) system. This takes the workflow out of email and static reports, and allows you to route, escalate, and manage events or findings. Many organizations are also integrating security alerts into their chat or collaboration, and developer productivity platforms. For organizations embarking on automation, an API-driven, low-latency ticketing system offers considerable flexibility when planning what to automate first.

This best practice applies not only to security events generated from log messages depicting user activity or network events, but also from changes detected in the infrastructure itself. The ability to detect change, determine whether a change was appropriate, and then route that information to the correct remediation workflow is essential in maintaining and validating a secure architecture, in the context of changes where the nature of their undesirability is sufficiently subtle that they cannot currently be prevented with a combination of AWS Identity and Access Management (IAM) and AWS Organizations configuration.

Amazon GuardDuty and AWS Security Hub CSPM provide aggregation, deduplication, and analysis mechanisms for log records that are also made available to you via other AWS services. GuardDuty ingests, aggregates, and analyzes information from sources such as AWS CloudTrail management and data events, VPC DNS logs, and VPC Flow Logs. Security Hub CSPM can ingest, aggregate, and analyze output from GuardDuty, AWS Config, Amazon Inspector, Amazon Macie, AWS Firewall Manager, and a significant number of third-party security products available in the AWS Marketplace, and if built accordingly, your own code. Both GuardDuty and Security Hub CSPM have an Administrator-Member model that can aggregate findings and insights across multiple accounts, and Security Hub CSPM is often used by customers who have an on- premises SIEM as an AWS-side log and alert preprocessor and aggregator from which they can then ingest Amazon EventBridge through a AWS Lambda-based processor and forwarder.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Evaluate log processing capabilities: Evaluate the options that are available for processing logs.
  +  [Find an AWS Partner that specializes in logging and monitoring solutions ](https://aws.amazon.com/security/partner-solutions/#Logging_and_Monitoring)
+  As a start for analyzing CloudTrail logs, test Amazon Athena.
  + [ Configuring Athena to analyze CloudTrail logs ](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html)
+  Implement centralize logging in AWS: See the following AWS example solution to centralize logging from multiple sources.
  +  [Centralize logging solution ](https://aws.amazon.com/solutions/centralized-logging/)
+  Implement centralize logging with partner: APN Partners have solutions to help you analyze logs centrally.
  + [ Logging and Monitoring ](https://aws.amazon.com/security/partner-solutions/#Logging_and_Monitoring)

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Answers: Centralized Logging ](https://aws.amazon.com/answers/logging/centralized-logging/)
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+  [Amazon EventBridge ](https://aws.amazon.com/eventbridge)
+ [ Getting started: Amazon CloudWatch Logs ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html)
+  [Security Partner Solutions: Logging and Monitoring](https://aws.amazon.com/security/partner-solutions/#logging-monitoring)

 **Related videos:**
+ [ Centrally Monitoring Resource Configuration and Compliance ](https://youtu.be/kErRv4YB_T4)
+  [Remediating Amazon GuardDuty and AWS Security Hub CSPM Findings ](https://youtu.be/nyh4imv8zuk)
+ [ Threat management in the cloud: Amazon GuardDuty and AWS Security Hub CSPM](https://youtu.be/vhYsm5gq9jE)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
