---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/projects-chapter.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Projects
<a name="projects-chapter"></a>

A *Project* is the foundation for using Amazon Monitron. A project is where your team sets up the gateways, assets, and sensors that Amazon Monitron uses to detect the abnormal conditions that can lead to equipment failure.

An Amazon Monitron Project is structured like this:

Project **→** site or sites **→** assets **→** positions **→** sensors

You can't share these resources between projects. Before you begin creating a project, we recommend that you consider your project's needs. Make sure that it contains all the resources required to predict the maintenance needs for all your assets.

Only a project-level admin user or IT manager can create, update, and delete projects and use the Amazon Monitron console for those tasks.

**Topics**
+ [Creating a project](mp-creating-project.md)
+ [Using tags with your project](tagging.md)
+ [Updating a project](mp-updating-project.md)
+ [Switching between projects](monitron-switch-projects.md)
+ [Deleting a project](mp-delete-project.md)
+ [Additional project tasks](mp-project-tasks.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
