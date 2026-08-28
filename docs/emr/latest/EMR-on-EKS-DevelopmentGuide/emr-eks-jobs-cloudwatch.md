---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-cloudwatch.html
---

# Configure a job run to use Amazon CloudWatch Logs
<a name="emr-eks-jobs-cloudwatch"></a>

To monitor job progress and to troubleshoot failures, you must configure your jobs to send log information to Amazon S3, Amazon CloudWatch Logs, or both. This topic helps you get started using CloudWatch Logs on your jobs that are launched with Amazon EMR on EKS. For more information about CloudWatch Logs, see [Monitoring Log Files](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html) in the Amazon CloudWatch User Guide.

**CloudWatch Logs IAM policy**

For your jobs to send log data to CloudWatch Logs, the following permissions must be included in the permissions policy for the job execution role. Replace {{my\_log\_group\_name}} and {{my\_log\_stream\_prefix}} with names of your CloudWatch log group and log stream names, respectively. Amazon EMR on EKS creates the log group and log stream if they do not exist as long as the execution role ARN has appropriate permissions.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Resource": [
        "arn:aws:logs:*:*:*"
      ],
      "Sid": "AllowLOGSCreatelogstream"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:PutLogEvents"
      ],
      "Resource": [
        "arn:aws:logs:*:*:log-group:{{my_log_group_name}}:log-stream:{{my_log_stream_prefix}}/*"
      ],
      "Sid": "AllowLOGSPutlogevents"
    }
  ]
}
```

------

**Note**
Amazon EMR on EKS can also create a log stream. If a log stream does not exist, the IAM policy should include the`"logs:CreateLogGroup"` permission.

After you've given your execution role the proper permissions, your application sends its log data to CloudWatch Logs when `cloudWatchMonitoringConfiguration` is passed in the `monitoringConfiguration` section of a `start-job-run` request, as shown in [Managing job runs with the AWS CLI](emr-eks-jobs-CLI.md).

In the `StartJobRun` API, {{log\_group\_name }}is the log group name for CloudWatch, and {{log\_stream\_prefix}} is the log stream name prefix for CloudWatch. You can view and search these logs in the AWS Management Console.
+ Submitter logs - {{logGroup}}/{{logStreamPrefix}}/{{virtual-cluster-id}}/jobs/{{job-id}}/containers/{{pod-name}}/(stderr/stdout)
+ Driver logs - {{logGroup}}/{{logStreamPrefix}}/{{virtual-cluster-id}}/jobs/{{job-id}}/containers/{{spark-application-id}}/spark-{{job-id}}-driver/(stderrstdout)
+ Executor logs - {{logGroup}}/{{logStreamPrefix}}/{{virtual-cluster-id}}/jobs/{{job-id}}/containers/{{spark-application-id}}/{{executor-pod-name}}/(stderr/stdout)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
