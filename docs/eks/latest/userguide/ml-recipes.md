---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/ml-recipes.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Recipes to optimize your Amazon EKS cluster for AI/ML workloads
<a name="ml-recipes"></a>

**Tip**
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section is designed to provide bite-sized recipes for optimizing your Amazon EKS cluster, particularly for AI/ML workloads involving specialized hardware. You’ll find guidance on preventing pods from being scheduled on specific nodes by adding taints to managed node groups, including prerequisites, step-by-step procedures, and deployment considerations.

**Topics**
+ [Recipe: Prevent pods from being scheduled on specific nodes](node-taints-managed-node-groups.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
