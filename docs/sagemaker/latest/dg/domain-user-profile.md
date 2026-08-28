---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile.html
---

# Domain user profiles
<a name="domain-user-profile"></a>

A user profile represents a single user within an Amazon SageMaker AI domain. The user profile is the main way to reference a user for the purposes of sharing, reporting, and other user-oriented features. This entity is created when a user onboards to the Amazon SageMaker AI domain. A user profile can have (at most) a single JupyterServer application outside the context of a shared space. The user profile's Studio Classic application is directly associated with the user profile and has an isolated Amazon EFS directory, an execution role associated with the user profile, and Kernel Gateway applications. A user profile can also create other applications from the console or from Amazon SageMaker Studio.

**Topics**
+ [Add user profiles](domain-user-profile-add.md)
+ [Remove user profiles](domain-user-profile-remove.md)
+ [View user profiles in a domain](domain-user-profile-view.md)
+ [View user profile details](domain-user-profile-describe.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
