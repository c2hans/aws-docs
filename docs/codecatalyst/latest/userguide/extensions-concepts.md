---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-concepts.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Extensions concepts
<a name="extensions-concepts"></a>

Here are some concepts and terms to know when working with extensions in CodeCatalyst.

## Extensions
<a name="extensions-concepts-extensions"></a>

An *extension* is an add-on that you can install into your CodeCatalyst space to add new functionality to your projects and integrate with services outside of CodeCatalyst. Extensions can be browsed and installed from the CodeCatalyst catalog.

## CodeCatalyst catalog
<a name="extensions-concepts-catalog"></a>

The CodeCatalyst catalog is a centralized listing of all the extensions available in CodeCatalyst. You can browse the CodeCatalyst catalog to find extensions that can improve your team's experiences in areas of CodeCatalyst such as source, workflows, and more.

## Connecting and linking
<a name="extensions-concepts-connect-link"></a>

Depending on the third-party resources you want to use or manage, you need to connect your GitHub account, Bitbucket workspace, or Jira project. Then, you need to link your GitHub repository, Bitbucket repository, or Jira project to your CodeCatalyst project.
+ **GitHub repositories**: Connect GitHub account and then link GitHub repositories.
+ **Bitbucket repositories**: Connect Bitbucket workspace and then link Bitbucket repositories.
+ **GitLab repositories**: Connect GitLab user and then link GitLab project repositories.
+ **Jira Software**: Connect Jira site and then link Jira projects.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
