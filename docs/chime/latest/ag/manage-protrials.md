---
source_url: https://docs.aws.amazon.com/chime/latest/ag/manage-protrials.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Managing Pro trials
<a name="manage-protrials"></a>

When a user accepts an Amazon Chime Team invitation or is added to an Enterprise account, their free trial ends and they have Pro permissions. This enables them to continue to host meetings that are scheduled. Changing a user’s permission tier to Basic prevents them from acting as a meeting host.

With Amazon Chime usage-based pricing, you only pay for users that host meetings on the days that they host them. Meeting attendees and chat users are not charged.

Pro users are considered Active Pro if they hosted a meeting that ended on a calendar day and at least one of the following occurred:
+ The meeting was scheduled.
+ The meeting included more than two attendees.
+ The meeting had at least one recording event.
+ The meeting included an attendee that dialed in.
+ The meeting included an attendee that joined with H.323 or SIP.

For more information, see [Plans and Pricing](https://aws.amazon.com/chime/pricing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
