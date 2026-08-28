---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/service_case_updates_queue.html
---

# Alternate rule: Security Incident Response Case Updates
<a name="service_case_updates_queue"></a>

To create an event rule that monitors for all case updates, repeat these tutorials with the following alterations:

1. **In [Tutorial: Create and subscribe to an Amazon SNS topic](service_sns_create_topic.md) **, use {{CaseUpdates}} as the topic name.

1. **In [Tutorial: Register an event rule](service_sns_reg_rule.md) **, use the following pattern in the JSON editor:

   ```
                              {
                                "source": ["aws.security-ir"],
                                "detail-type": [
                                  "Case Created",
                                  "Case Updated",
                                  "Case Closed",
                                  "Case Comment Added",
                                  "Case Comment Updated"
                                ]
                              }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
