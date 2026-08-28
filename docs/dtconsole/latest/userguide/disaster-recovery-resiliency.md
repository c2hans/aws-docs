---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/disaster-recovery-resiliency.html
---

# Resilience in AWS CodeStar Notifications and AWS CodeConnections
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).
+ Notification rules are specific to the AWS Region where they are created. If you have notification rules in more than one AWS Region, use the Region selector to review notification rules in each AWS Region.
+ AWS CodeStar Notifications relies on Amazon Simple Notification Service (Amazon SNS) topics as notification rule targets. Information about your Amazon SNS topics and notification rule targets might be stored in an AWS Region different from the Region in which you configured the notification rule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
