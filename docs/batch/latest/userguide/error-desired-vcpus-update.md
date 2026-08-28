---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/error-desired-vcpus-update.html
---

# Error message when you update the `desiredvCpus` setting
<a name="error-desired-vcpus-update"></a>

You see the following error message when you use the AWS Batch API to update the desired vCPUs (`desiredvCpus`) setting.

`Manually scaling down compute environment is not supported. Disconnecting job queues from compute environment will cause it to scale-down to minvCpus`.

This issue occurs if the updated `desiredvCpus` value is less than the current `desiredvCpus` value. When you update the `desiredvCpus` value, both of the following must be true:
+ The `desiredvCpus` value must be between the `minvCpus` and `maxvCpus` values.
+ The updated `desiredvCpus` value must be greater than or equal to the current `desiredvCpus` value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
