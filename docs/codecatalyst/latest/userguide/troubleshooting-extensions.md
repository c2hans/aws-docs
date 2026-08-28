---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-extensions.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Troubleshooting problems with extensions
<a name="troubleshooting-extensions"></a>

Consult the following sections to troubleshoot problems related to extensions in CodeCatalyst. For more information about extensions, see [Add functionality to projects with extensions in CodeCatalyst](extensions.md).

**Topics**
+ [I can't see the changes to a linked third-party repositories or search for results of those changes](#troubleshooting-detect-3p-changes)

## I can't see the changes to a linked third-party repositories or search for results of those changes
<a name="troubleshooting-detect-3p-changes"></a>

**Problem:** The changes in my third-party reposiory aren't showing up in CodeCatalyst.

**Possible fixes:** CodeCatalyst currently doesn't support detecting changes in the default branch for linked repositories. To change the default branch for a linked repository, you must first unlink it from CodeCatalyst, change the default branch, and then link it again. For more information, see [Linking GitHub repositories, Bitbucket repositories, GitLab project repositories, and Jira projects in CodeCatalyst](extensions-link.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
