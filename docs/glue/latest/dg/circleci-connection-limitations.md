---
source_url: https://docs.aws.amazon.com/glue/latest/dg/circleci-connection-limitations.html
---

# CircleCI limitations
<a name="circleci-connection-limitations"></a>

The following are limitations or notes for CircleCI:
+ CircleCI does not support either field based or record based partitioning.
+ Filter fields containing '-' (hyphen) will work only if they are wrapped within backticks. For example: `workflow-name` = "abc"
+ The GitLab VCS type cannot be supported as there is no programmatic way to retrieve the 'Project ID' required for the GitLab VCS entity path.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
