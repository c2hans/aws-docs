---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/add-precontact-form.html
---

# Add a pre-contact or pre-chat form
<a name="add-precontact-form"></a>

You can capture customer information before starting a contact:
+ **Pre-contact form**: Add to capture information from the customer before starting a task or email contact.
+ **Pre-chat form**: Add to capture information from the customer before starting a chat contact.

After you capture the information, you can display it to the agent through the Contact Control Panel (CCP), or use it elsewhere in the flow.

To create the form, you create a custom view and use the connect action button component. For more information on views, see [Use the UI builder in Connect Customer for resources in step-by-step guides](no-code-ui-builder.md).

With the connect action button, you can take in user input from the form and select what action to take when the form is submitted - start a task/email or chat.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
