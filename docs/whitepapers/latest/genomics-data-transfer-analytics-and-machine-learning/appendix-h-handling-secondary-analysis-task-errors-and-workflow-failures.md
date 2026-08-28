---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-h-handling-secondary-analysis-task-errors-and-workflow-failures.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix H: Handling secondary analysis task errors and workflow failures
<a name="appendix-h-handling-secondary-analysis-task-errors-and-workflow-failures"></a>

 If your Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances are interrupted, jobs running on that instance will fail. Amazon EC2 terminates, stops, or hibernates your Spot Instance when the price exceeds the maximum price for your request or capacity is no longer available. If retries are enabled for the given task in the AWS Step Functions state machine and there are more retries left, the job will be resubmitted to AWS Batch. If a Spot Instance is available, it will be used to run the task. If there are no Spot Instances available and you have an On-Demand compute environment next in the compute environments list for the queue, AWS Batch will provision an On-Demand Instance to run the task. Verify that you have configured failover from a Spot Instance compute environment to an On-Demand Instance compute environment for a given job queue. Also verify you have configured retries on tasks in your Step Functions state machine.

 You can also specify a try/catch block to handle complex retry scenarios or to execute custom code such as submitting a ticket to an issue tracking system with custom code in the catch block. For more information about how AWS Step Functions handle errors, see [Error Handling in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) in the *AWS Step Functions Developer Guide*.

 Many organizations build in the ability to resume a secondary analysis state machine execution when it was interrupted due to a job failure. The idea is to skip jobs that have already produced their output files, resuming the state machine execution at the job that was next when resources were interrupted. This is commonly referred to as *checkpointing*. One approach is to add a gate clause to the beginning of your tool wrapper code to check for the job outputs and return if they already exist. If the output already exists, the tool immediately returns, allowing failed state machine executions to fast-forward to the point of failure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
