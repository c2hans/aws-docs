---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/gitlab-group-webhook-setup.html
---

# Set up a group GitLab webhook
<a name="gitlab-group-webhook-setup"></a>

The high-level steps to set up a group GitLab webhook are as follows. For more information about group GitLab webhooks, see [GitLab group webhooks](gitlab-group-webhook.md).

1. Set your project's source location to `CODEBUILD_DEFAULT_WEBHOOK_SOURCE_LOCATION`.

1. In the webhook's scope configuration, set the scope to `GITLAB_GROUP`.

1. Specify a name as part of the webhook's scope configuration. For group webhooks, this is the group name.
**Note**
If the project's source type is `GITLAB_SELF_MANAGED`, you will also need to specify a domain as part of the webhook scope configuration.

1. (Optional) If you would only like to receive webhook events for specific repositories within your organization or enterprise, you can specify `REPOSITORY_NAME` as a filter when creating the webhook.

1. When creating a group webhook, ensure that CodeBuild has permissions to create group level webhooks within GitLab. To do so, you can use CodeBuild OAuth though CodeConnections. For more information, see [GitLab access in CodeBuild](access-tokens-gitlab-overview.md).

   Note that group webhooks work with any of the existing GitLab webhook event types.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
