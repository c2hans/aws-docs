---
source_url: https://docs.aws.amazon.com/chime/latest/ag/change-PINs.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Changing personal meeting PINs
<a name="change-PINs"></a>

A personal meeting PIN is a static ID generated when the user registers. The PIN makes it easy for an Amazon Chime user to schedule meetings with other Amazon Chime users. Using a personal meeting PIN means that meeting organizers don't have to remember meeting details for each new meeting that they schedule.

If a user feels that their personal meeting PIN has been compromised, you can reset their PIN and generate a new ID. After you update a personal meeting PIN, the user must update all meetings that were scheduled using the old personal meeting PIN.

**To change a personal meeting PIN**

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. On the **Accounts** page, select the name of the Amazon Chime account.

1. In the navigation pane, choose **Users**.

1. Search for the user who needs their PIN changed.

1. To open the **User detail** page, choose the name of the user.

1. Choose **User actions**, **Reset personal PIN**, **Confirm**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
