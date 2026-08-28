---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights-default-behavior.html
---

# Default behavior
<a name="cloudwatch-container-insights-default-behavior"></a>

When you create a compute environment without specifying a Container Insights setting, AWS Batch does not pass a Container Insights configuration to the underlying Amazon ECS cluster. In this case, the Amazon ECS account-level default applies at cluster creation. The Amazon ECS default is `disabled` unless you have changed your account setting.

**Important**
Not specifying a value (omitting the field) is different from explicitly specifying `DISABLED`. If you omit the field, the Amazon ECS account-level default applies. If you set the value to `DISABLED`, Container Insights is explicitly turned off regardless of your Amazon ECS account setting.
For example, if you have Container Insights enabled at the Amazon ECS account level, omitting the field results in Container Insights being enabled on the compute environment. To override this, you must explicitly set the value to `DISABLED`.

For existing compute environments created before this feature was available, the `ecsSettings` field is absent from the `DescribeComputeEnvironments` response. The field only appears after you explicitly set a value using `UpdateComputeEnvironment`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
