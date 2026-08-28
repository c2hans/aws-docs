---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/no-code-ui-builder-sample-data.html
---

# Use sample data to preview your view in Connect Customer
<a name="no-code-ui-builder-sample-data"></a>

You can use sample data to see what the view will look like to the user. You can even see data fields that are dynamically determined at runtime. When a field is set to dynamic (the lightning bolt is selected), sample data can be entered in the input field under the **Sample Data** section of that property. This sample data is for view purposes only. It appears only in the Connect Customer UI builder.

For example, the following image shows an example of a **Mailing address form**.

![The DefaultValue and Sample data sections of the Customize panel.](http://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-sample-data-example.png)

+ **Street address** is a dynamic default value. It is populated at runtime by the address found in the customer profile.
+ To see how the final UI appears to the agent, you can enter a text default value.
+ The value `7 W 34th St` is for display purposes only in the Connect Customer admin website. It does not appear to the agent.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
