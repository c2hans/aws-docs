---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.Facets.html
---

# Facets
<a name="workbench.Modeler.Facets"></a>

 In NoSQL Workbench, *Facets* give you a way to view a subset of the data in a table, without having to see records that don't meet the constraints of the facet. Facets are considered a visual data modeling tool, and don't exist as a usable construct in DynamoDB, as they are purely an aid to modeling of access patterns.

**Note**
 We recommend you use [Adding and validating access patterns](workbench.Modeler.AccessPatterns.md) to visualize how your application will access data in DynamoDB instead of Facets. Access patterns mirror your actual database interactions and help you build the correct data model for your use case, although facets are non-functional visualizations.

**To create a facet**

1. In the resource selector panel, choose a **Table** you want to edit

1. In the top bar, choose **Edit**.

1. Scroll down to the **Facet filters** section.

1.  Choose **Add facet**. Specify the following:
   +  The **Facet name**.
   +  A **Partition key alias** to help distinguish this facet view.
   +  A **Sort key alias** if you provided a **Sort key** for the table.
   +  Choose the **Attributes** that are part of this facet.

    Repeat this step if you want to add more facets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
