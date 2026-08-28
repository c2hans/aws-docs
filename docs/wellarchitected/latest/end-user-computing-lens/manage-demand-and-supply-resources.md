---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/manage-demand-and-supply-resources.html
---

# Manage demand and supply resources
<a name="manage-demand-and-supply-resources"></a>

|  EUCCOST06: How do you optimize cost using existing licenses when appropriate?  |
| --- |
|   |

 You may already have existing license agreements with Microsoft in place. You can use these licenses with AWS EUC services to reduce your cost.

|  EUCCOST07: How do you track and identify idle resources to avoid unnecessary charges?  |
| --- |
|   |

 Amazon WorkSpaces can be used in AlwaysOn and AutoStop running mode, which correspond to monthly and hourly billing respectively. If deployed your WorkSpaces with monthly billing but are using them less than expected, switching the billing mode can reduce your cost.

 With Amazon WorkSpaces Applications, you will likely use app block builders or image builders to generate app blocks and images. These resources are charged hourly or in one second increments with a 15-minute minimum if you keep them running.

**Topics**
+ [EUCCOST06-BP01 Explore a bring your own license (BYOL) approach](euccost06-bp01.md)
+ [EUCCOST07-BP01 Use the available cost optimizers for Amazon WorkSpaces and Amazon WorkSpaces Applications](euccost07-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
