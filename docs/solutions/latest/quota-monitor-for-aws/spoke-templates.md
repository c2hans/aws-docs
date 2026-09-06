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
