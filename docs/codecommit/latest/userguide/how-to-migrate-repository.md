---
source_url: https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-migrate-repository.html
---

# Migrate to AWS CodeCommit
<a name="how-to-migrate-repository"></a>

You can migrate a Git repository to a CodeCommit repository in a number of ways: by cloning it, mirroring it, migrating all or just some of the branches, and so on. You can also migrate local, unversioned content on your computer to CodeCommit.

The following topics show you some of the ways you can migrate a repository. Your steps might vary, depending on the type, style, or complexity of your repository and the decisions you make about what and how you want to migrate. For very large repositories, you might want to consider [migrating incrementally](how-to-push-large-repositories.md).

**Note**
You can migrate to CodeCommit from other version control systems, such as Perforce, Subversion, or TFS, but you must first migrate to Git.
For more options, see your Git documentation.
Alternatively, you can review the information about [migrating to Git](http://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git) in the *Pro Git* book by Scott Chacon and Ben Straub.

**Topics**
+ [Migrate a Git repository to AWS CodeCommit](how-to-migrate-repository-existing.md)
+ [Migrate content to CodeCommit](how-to-migrate-repository-local.md)
+ [Migrate a repository in increments](how-to-push-large-repositories.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
