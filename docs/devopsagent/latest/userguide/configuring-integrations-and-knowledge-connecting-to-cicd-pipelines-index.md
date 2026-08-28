---
source_url: https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-connecting-to-cicd-pipelines-index.html
---

# Connecting to CI/CD pipelines
<a name="configuring-integrations-and-knowledge-connecting-to-cicd-pipelines-index"></a>

CI/CD pipeline integration enables AWS DevOps Agent to monitor deployments and correlate code changes with operational incidents during investigations. By connecting your CI/CD providers, the agent can track deployment events and associate them with AWS resources to help identify potential root causes during incident response.

AWS DevOps Agent supports integration with popular CI/CD platforms through a two-step process:

1. **Account-level registration** – Register your CI/CD provider at the AWS account level. You can create more than one registration per provider, for example, one per organization or group.

1. **Agent Space connection** – Connect specific projects or repositories to individual Agent Spaces based on your organizational needs

This approach allows you to share CI/CD provider registrations across multiple Agent Spaces while maintaining granular control over which projects are monitored by each space.

## Supported CI/CD providers
<a name="supported-cicd-providers"></a>

AWS DevOps Agent supports the following CI/CD platforms:
+ **GitHub** – Connect repositories from [GitHub.com](http://GitHub.com) using the AWS DevOps Agent GitHub app.
+ **GitLab** – Connect projects from [GitLab.com,](http://gitlab.com) managed GitLab instances, or publicly accessible self-hosted GitLab deployments.

**Topics**
+ [Connecting GitHub](connecting-to-cicd-pipelines-connecting-github.md)
+ [Connecting GitLab](connecting-to-cicd-pipelines-connecting-gitlab.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
