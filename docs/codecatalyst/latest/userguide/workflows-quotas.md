---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-quotas.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Quotas for workflows in CodeCatalyst
<a name="workflows-quotas"></a>

The following table describes quotas and limits for workflows in Amazon CodeCatalyst.

For more information about quotas in Amazon CodeCatalyst, see [Quotas for CodeCatalyst](quotas.md).

|  |  |
| --- |--- |
| Maximum number of workflows per space | 800 |
| Maximum workflow definition file size | 256 KB |
| Maximum number of workflow files processed in a single source event | 50 |
| Maximum number of files processed in a single source event | 4,000 |
| Maximum number of active fleets per space | 10 |
| Maximum number of active compute instances per fleet | 20 |
| Maximum number of input artifacts per action | 10 |
| Maximum number of output artifacts per action | 10 |
| Maximum total size of a single action's output variables | 120 KB |
| Maximum length of an output variable value | 500 characters or more, depending on the action that emits the value.  Values may be truncated if they exceed the action's limit.  |
| Maximum number of days to keep artifacts generated during a workflow run | 30 |
| Maximum number of reports per action | 50 |
| Maximum number of test cases per test report | 20,000 |
| Maximum number of files per code coverage report | 20,000 |
| Maximum number of software composition analysis findings per report | 20,000 |
| Maximum number of files per static analysis report | 20,000 |
| Maximum number of concurrent workflow runs per space | 100 |
| Maximum number of actions per workflow | 50 |
| Maximum number of actions running concurrently per workflow | 50 |
| Maximum number of actions running concurrently per space | 200 |
| Maximum amount of time an action can run | For the build and test actions, the timeout is 8 hours.<br />For all other actions, the timeout is 1 hour. |
| Maximum number of environments associated with an AWS account per space | 5,000 |
| Maximum number of secrets per action | 5 |
| Maximum number of secrets per space | 500,000 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
