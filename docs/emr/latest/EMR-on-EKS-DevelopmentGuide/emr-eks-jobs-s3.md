---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/emr-eks-jobs-s3.html
---

# Configure a job run to use Amazon S3 logs
<a name="emr-eks-jobs-s3"></a>

To be able to monitor the job progress and to troubleshoot failures, you must configure your jobs to send log information to Amazon S3, Amazon CloudWatch Logs, or both. This topic helps you get started publishing application logs to Amazon S3 on your jobs that are launched with Amazon EMR on EKS.

**S3 logs IAM policy**

Before your jobs can send log data to Amazon S3, the following permissions must be included in the permissions policy for the job execution role. Replace {{amzn-s3-demo-logging-bucket}} with the name of your logging bucket.

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
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ],
      "Sid": "AllowS3Putobject"
    }
  ]
}
```

------

**Note**
Amazon EMR on EKS can also create an Amazon S3 bucket. If an Amazon S3 bucket is not available, include the `“s3:CreateBucket”` permission in the IAM policy.

After you've given your execution role the proper permissions to send logs to Amazon S3, your log data are sent to the following Amazon S3 locations when `s3MonitoringConfiguration` is passed in the `monitoringConfiguration` section of a `start-job-run` request, as shown in [Managing job runs with the AWS CLI](emr-eks-jobs-CLI.md).
+ Submitter Logs - /{{logUri}}/{{virtual-cluster-id}}/jobs/{{job-id}}/containers/{{pod-name}}/(stderr.gz/stdout.gz)
+ Driver Logs - /{{logUri}}/{{virtual-cluster-id}}/jobs/{{job-id}}/containers/{{spark-application-id}}/spark-{{job-id}}-driver/(stderr.gz/stdout.gz)
+ Executor Logs - /{{logUri}}/{{virtual-cluster-id}}/jobs/{{job-id}}/containers/{{spark-application-id}}/{{executor-pod-name}}/(stderr.gz/stdout.gz)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
