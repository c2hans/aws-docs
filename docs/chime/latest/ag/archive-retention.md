---
source_url: https://docs.aws.amazon.com/chime/latest/ag/archive-retention.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Managing chat retention policies
<a name="archive-retention"></a>

If you administer one or more Amazon Chime Enterprise accounts, you can set chat retention policies for the following:
+ Chat conversations that include only members of your Enterprise account.
+ Chat rooms created by members of your Enterprise account.

A retention policy automatically deletes messages based on the time period that you set. You can set time periods lasting from one day to 15 years.

**Note**
Amazon Chime Enterprise accounts have a retention period of 90 days. The policy applies to conversations involving users who belong to the account, and to users who don't belong to the account.
Retention policies do not apply to the following:
Chat conversations that do not include members of Amazon Chime Enterprise accounts
Chat rooms created by users who don't belong to an Amazon Chime Enterprise account

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
