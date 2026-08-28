---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codepipeline_example_codepipeline_AcknowledgeJob_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AcknowledgeJob` with a CLI
<a name="codepipeline_example_codepipeline_AcknowledgeJob_section"></a>

The following code examples show how to use `AcknowledgeJob`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve information about a specified job**
This example returns information about a specified job, including the status of that job if it exists. This is only used for job workers and custom actions. To determine the value of nonce and the job ID, use aws codepipeline poll-for-jobs.
Command:

```
aws codepipeline acknowledge-job --job-id {{f4f4ff82-2d11-EXAMPLE}} --nonce {{3}}
```
Output:

```
{
  "status": "InProgress"
}
```
+  For API details, see [AcknowledgeJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/acknowledge-job.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets the status of the specified job.**

```
Confirm-CPJob -JobId f570dc12-5ef3-44bc-945a-6e133EXAMPLE -Nonce 3
```
**Output:**

```
Value
-----
InProgress
```
+  For API details, see [AcknowledgeJob](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets the status of the specified job.**

```
Confirm-CPJob -JobId f570dc12-5ef3-44bc-945a-6e133EXAMPLE -Nonce 3
```
**Output:**

```
Value
-----
InProgress
```
+  For API details, see [AcknowledgeJob](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
