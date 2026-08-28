---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/service_sns_tutorial.html
---

# Tutorial: Sending Amazon Simple Notification Service alerts for `Membership Updated` events
<a name="service_sns_tutorial"></a>

In this tutorial, you configure an Amazon EventBridge event rule that only captures events where the your subscription enters a `Membership Updated` status.

## Prerequisites
<a name="service_sns_prereq"></a>

This tutorial assumes that you have a working subscription and active AWS accounts in your membership.

**Topics**
+ [Prerequisites](#service_sns_prereq)
+ [Tutorial: Create and subscribe to an Amazon SNS topic](service_sns_create_topic.md)
+ [Tutorial: Register an event rule](service_sns_reg_rule.md)
+ [Tutorial: Test your rule](service_sns_test_rule.md)
+ [Alternate rule: Security Incident Response Case Updates](service_case_updates_queue.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
