---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/spoke-templates.html
---

# Spoke templates
<a name="spoke-templates"></a>

The spoke templates packaged with the solution are standalone templates, and you can deploy them independently. To determine which templates to deploy, ask the following questions:
+ Do you have a hub or monitoring account?
+ Do you need the entire solution deployment with all of its features?

If you answered `No` to any of the questions above, then you can deploy just the spoke templates in the account to be monitored:
+  `quota-monitor-ta-spoke.template` to support quota checks offered by Trusted Advisor
+  `quota-monitor-sq-spoke.template` to support quota checks offered by Service Quotas

Additionally, the spoke templates offer extensions (such as sending notifications to different destinations). The spoke templates provision EventBridge rules for capturing OK, WARN, or ERROR quota events. You can configure these rules to send the events to destinations according to your requirements. For more details, refer to [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
