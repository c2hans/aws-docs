---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/identity-resolution-metrics.html
---

# View Identity Resolution metrics in Connect Customer Customer Profiles
<a name="identity-resolution-metrics"></a>

Whenever Identity Resolution matches or merges profiles, metrics about the process are displayed on the Customer Profiles dashboard. You can review metric for the pass week on the **Identity Resolution** summary page.

The following metrics are generated each time the Identity Resolution Job runs:
+ **Match groups found**: The number of match groups that were found.
  + Available for both ML-based and rule-based Identity Resolution.
+ **Profiles Merged**: The number of profiles that were merged.
  + Available for both ML-based and rule-based Identity Resolution.
+ **Match Group by rule**: The number of match group that were created by each rule level.
  + Only available for rule-based Identity Resolution.

![The Connect Customer Customer Profiles page, the Enable Identity Resolution button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/ir-metrics-example-1.png)

![The Connect Customer Customer Profiles page, the Enable Identity Resolution button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-enable-ir.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
