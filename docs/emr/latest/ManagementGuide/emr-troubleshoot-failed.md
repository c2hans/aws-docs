---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-troubleshoot-failed.html
---

# Troubleshoot an Amazon EMR cluster that has failed with an error code
<a name="emr-troubleshoot-failed"></a>

 This section walks you through the process of troubleshooting a cluster that has failed. This means that the cluster terminated with an error code.

**Note**
When an EMR cluster terminates with an error, the `DescribeCluster` and `ListClusters` APIs return an error code and an error message. For some cluster errors, the `ErrorDetail` data array can also help you troubleshoot the failure. For more information, see [Error codes with ErrorDetail information in Amazon EMR](emr-troubleshoot-error-errordetail.md).

If your cluster runs but takes a long time to return results, see [Troubleshoot a slow Amazon EMR cluster](emr-troubleshoot-slow.md).

**Topics**
+ [Step 1: Gather data about the issue with the Amazon EMR cluster](emr-troubleshoot-failed-1.md)
+ [Step 2: Check the environment](emr-troubleshoot-failed-2.md)
+ [Step 3: Look at the last state change](emr-troubleshoot-failed-3.md)
+ [Step 4: Examine the Amazon EMR log files](emr-troubleshoot-failed-4.md)
+ [Step 5: Test the Amazon EMR cluster step by step](emr-troubleshoot-failed-5-test-steps.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
