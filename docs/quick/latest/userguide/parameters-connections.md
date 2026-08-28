---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/parameters-connections.html
---

# Connecting to parameters in Amazon Quick
<a name="parameters-connections"></a>

Use this section after you have a parameter set up, to connect it and make it work.

After you create a parameter, you can create consumers of the parameters. *Parameter consumers* are components that consume the value of a parameter, such as filters, controls, calculated fields, or custom actions.

You can navigate to each of these options in another way, as follows:
+ To create a filter, choose the **Filter** icon at the top of the page. In short, you create a **Custom Filter** and enable **Use parameters**. The list shows only eligible parameters.
+ To add a new control for the parameter, choose the **Parameters** icon at the top of the page. In short, choose your parameter, and then **Add control**.
+ To use a parameter in a calculated field, either edit an existing calculated field, or add a new one by choosing **Add** at the top left. The parameter list appears below the field list.
**Note**
You can't use multivalue parameters with calculated fields.
+ To create a URL action, choose the **v**-shaped menu on a visual, and then choose **URL Actions**.

For more information on each of these topics, see the following sections.

**Topics**
+ [Using filters with parameters](parameters-filtering-by.md)
+ [Using calculated fields with parameters](parameters-calculated-fields.md)
+ [Using custom actions with parameters](parameters-custom-actions.md)
+ [Parameters in URLs](parameters-in-a-url.md)
+ [Parameters in titles and descriptions](parameters-in-titles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
