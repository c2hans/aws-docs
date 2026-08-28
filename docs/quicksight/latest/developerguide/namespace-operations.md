---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html
---

# Namespace operations
<a name="namespace-operations"></a>

An Amazon Quick Sight *namespace* is a logical container that you can use to organize clients, subsidiaries, teams, and so on. By using a namespace, you can isolate the Amazon Quick Sight users and groups that are registered for that namespace. Users that access the namespace can share assets only with other users or groups in the same namespace. They can't see users and groups in other namespaces. For more information about namespaces, see [Supporting multitenancy with isolated namespaces](https://docs.aws.amazon.com/quicksight/latest/user/namespaces.html) in the *Quick Sight User guide*.

To implement namespaces, you use the following Quick Sight API operations.

**Topics**
+ [CreateNamespace](create-namespace.md)
+ [DeleteNamespace](delete-namespace.md)
+ [DescribeNamespace](describe-namespace.md)
+ [ListNamespaces](list-namespaces.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
