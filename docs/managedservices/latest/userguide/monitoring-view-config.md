---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-view-config.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Viewing the monitoring configuration for an AMS account
<a name="monitoring-view-config"></a>

There are two key parts to the monitoring configuration of an account that you can view:
+ CloudWatch Alarms: You can view all the CW alarms in the account by going to the CloudWatch console and selecting different services of interest.
+ CloudWatch Events:
  + **Multi-Account Landing Zone**: CloudWatch Events monitored in the account can be found by filtering for all CW event rules with the string `"ams-"`.
  + **Single-Account Landing Zone**: CloudWatch Events monitored in the account can be found by filtering for all CW event rules with the string `"mc-"`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
