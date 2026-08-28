---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/enter-script-rule.html
---

# Enter a script in a conversational analytics rule for agents to follow
<a name="enter-script-rule"></a>

Enter a script in a conversational analytics rule when you need agents to use exact wording in customer calls.

To enter a script in a rule, enter phrases. For example, if you want to highlight when agents say *Thank you for being a member. We appreciate your business*, enter two phrases:
+ Thank you for being a member.
+ We appreciate your business.

To apply the rule to certain lines of businesses, add a condition for which queues it applies to, or contact attributes. For example, the following image shows a rule that applies when an agent is working the BasicQueue or Billing and Payments queues, the customer is for auto insurance, and the agent is located in Seattle.

![The new rule page, the Words or phrases - Exact match section, multiple conditions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-add-category-rules-3.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
