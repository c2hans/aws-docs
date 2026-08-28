---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-experimentation-observing-treatment-traffic.html
---

# Observing treatment traffic
<a name="appconfig-experimentation-observing-treatment-traffic"></a>

AWS AppConfig Agent collects aggregated treatment assignment counts and emits them as CloudWatch metrics in your account through a service-linked role that AWS AppConfig manages. There is no additional charge for these metrics.
+ Namespace: `AWS/AppConfig`
+ Metric name: `ReturnedCount`
+ Dimensions: application ID, environment ID, configuration profile ID, flag key, and variant

These metrics show how much traffic each treatment is receiving, which you can use as a real-time check that your experiment is operating as expected. For example, in a 50/50 A/B test, you can confirm that about half of entities are assigned to the control and about half to the treatment.

**Note**
To emit experiment treatment traffic metrics to your account, you must opt in to the VendedMetrics account setting by using the `UpdateAccountSettings` operation. Vended metrics incur no additional cost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
