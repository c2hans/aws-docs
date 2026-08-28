---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-experimentation-about-defining.html
---

# Documenting your hypothesis
<a name="appconfig-experimentation-about-defining"></a>

When you create a new experiment, you specify a name for it and define the goals on the **Document your hypothesis** page in AWS AppConfig experimentation. Enter a name that identifies the experiment goal, for example *Increase add-to-cart rate by adding a button for each product displayed*. If you're creating multiple versions of the same experiment, specify version numbers in the name, for example *V2-Increase add-to-cart rate by adding a button for each product displayed*.

In the **Experiment hypothesis** text box, define the outcome you're trying to achieve and other details so that other users can quickly understand the experiment goals. Focus on a measurable customer or business impact. Here's an example:
+ Goal: Increase add-to-cart rate by adding a button for each product displayed
+ Hypothesis: Implementing 'Add-to-cart' buttons beneath every product displayed on the page will improve clicks
+ Primary metric: Add-to-cart rate
+ Guardrail metrics: Page load time, checkout completion rate

After naming and defining the experiment hypothesis, select the application where you want to run the experiment. An application in AWS AppConfig is simply an organizational construct like a folder that identifies the namespace of your application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
