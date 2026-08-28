---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-forms-creating-app.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Creating a new Q App with a data collection form
<a name="qapps-forms-creating-app"></a>

To create a new data collection app, you create a new app, add a data collection form with one or more fields, and publish the app.

1. Go to your Amazon Q Business web experience URL.

1. In the navigation pane, choose **Apps**.

1. Choose one of four methods to start creating your Q App data collection form:
   + In **Recently used** choose the pencil icon.
   + Choose a tile that contains a **Data collection** pill
   + Describe your Q App data collection form use case in the text entry box and choose **Generate**.
   + Choose **Create blank app**
   + Choose **Explore the Q Apps library** to start with any existing apps your team may have already created and shared.

1. Choose **\+ Add card** and choose **Data collection form**.

1. Choose the pencil icon on the data collection form.

1. For **Title**, give the form a name.

1. Under **Fields**, add one or more fields with field labels.
   + Choose **\+ Add a field** to add more fields.
   + Choose the trash can icon to delete a field.

1. Choose **Save** to save the form.

1. Add any necessary output cards to analyze the collected data. Use `@cardname` to reference the data from the form card in the prompt.

1. When you are finished, the top right, choose **Share**.

1. Configure how you want to share the app and optionally edit its categories.

1. Choose **Share**. When complete, you can find the new app in your library.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
