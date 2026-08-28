---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-upstream-repositories-remove.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Removing an upstream repository
<a name="packages-upstream-repositories-remove"></a>

If you no longer want to access the packages within an upstream repository, you can remove the upstream repository from a package repository.

**Warning**
When you remove an upstream repository, you could break upstream relationship chains, which could break your projects or builds.

**To remove an upstream repository**

1. In the navigation pane, choose **Packages**.

1. On the **Package repositories** page, choose the package repository from which you want to remove an upstream repository.

1. Under the package repository's name, choose **Upstreams**.

1. In the **Edit upstream repositories** section, find the upstream repository you want to remove and choose ![Remove](http://docs.aws.amazon.com/codecatalyst/latest/userguide/images/packages/remove.png).

1. When you're finished removing upstream repositories, choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
