---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/solution-logs.html
---

# Solution logs
<a name="solution-logs"></a>

This section includes Troubleshooting information for this solution, see left navigation for topics.

This solution collects output from remediation runbooks, which run under AWS Systems Manager, and logs the result to CloudWatch Logs group `SO0111-ASR` in the AWS Security Hub admin account. There is one stream per control per day.

The Orchestrator Step Functions logs all step transitions to the `SO0111-ASR-Orchestrator` CloudWatch Logs Group in the AWS Security Hub admin account. This log is an audit trail to record state transitions for each instance of the Step Functions. There is one log stream per Step Functions execution.

Both log groups are encrypted using an AWS KMS customer managed key.

The following troubleshooting information uses the `SO0111-ASR` log group. Use this log, as well as AWS Systems Manager Automation console, Automation Executions logs, Step Function console, and Lambda logs to troubleshoot problems.

If a remediation fails, a message similar to the following will be logged to `SO0111-ASR` in the log stream for the standard, control, and date. For example: **CIS-2.9-2021-08-12**

```
ERROR: a4cbb9bb-24cc-492b-a30f-1123b407a6253: Remediation failed for CIS control 2.9 in account 123412341234: See Automation Execution output for details (AwsEc2Vpc vpc-0e92bbe911cf08acb)
```

The following messages provide additional detail. This output is from the ASR runbook for the security standard and control. For example: **ASR-CIS\_1.2.0\_2.9**

```
Step fails when it is Execution complete: verified. Failed to run automation with executionId: eecdef79-9111-4532-921a-e098549f5259 Failed :
{Status=[Failed], Output=[No output available yet because the step is not successfully executed], ExecutionId=[eecdef79-9111-4532-921a-e098549f5259]}. Please refer to Automation Service Troubleshooting Guide for more diagnosis details.
```

This information points you to the failure, which in this case was a child automation running in the member account. To troubleshoot this issue, you must log in to the AWS Management Console in the member account (from the message above), go to AWS Systems Manager, navigate to **Automation**, and examine the log output for Execution ID `eecdef79-9111-4532-921a-e098549f5259`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
