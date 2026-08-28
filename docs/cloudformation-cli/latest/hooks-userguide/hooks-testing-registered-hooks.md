---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-testing-registered-hooks.html
---

# Testing a custom Hook for public use
<a name="hooks-testing-registered-hooks"></a>

In order to publish your registered custom Hook, it must pass all test requirements defined for it. The following is a list of requirements needed before publishing your custom Hook as a third-party extension.

Each handler and target is tested twice. Once for `SUCCESS` and once for `FAILED`.
+ For `SUCCESS` response case:
  + Status must be `SUCCESS`.
  + Must not return an error code.
  + Callback delay should be set to `0` seconds, if specified.
+ For `FAILED` response case:
  + Status must be `FAILED`.
  + Must return an error code.
  + Must have a message in response.
  + Callback delay should be set to `0` seconds, if specified.
+ For `IN_PROGRESS` response case:
  + Must not return an error code.
  + `Result` field must not be set in response.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
