---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/site-organization.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Organizing a project into sites
<a name="site-organization"></a>

You can organize a project into sites based on your business needs. For example, you can organize a project in one of the following ways:
+ **No sites at all**. Everything is contained in a project, without any sites. This option is best for projects with a few assets and users that you can easily keep track of because it provides the greatest simplicity.
+ **Sites based on geography**. Group resources and users by locale, such as by city, building, or areas within a building. For example, you might set up a site for the equipment in a factory test lab.
+ **Sites based on function**. Group resources and users by functionality, either by machine functionality or by how they're used in your factory. For example, you might set up a site for all of the conveyor belts involved in moving an item from one side of the factory to the other.
+ **Sites based on organization**. Sites represent a specific organizational structure in the company or factory. For example, you might want a single site that includes resources and users assigned to the shipping department.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
