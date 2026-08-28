---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Troubleshooting.html
---

# Troubleshooting assessment runs
<a name="CHAP_Tasks.AssessmentReport.Troubleshooting"></a>

Following, you can find topics about troubleshooting issues with running assessment reports with AWS Database Migration Service. These topics can help you to resolve common issues.

**Topics**
+ [ResourceNotFoundFault when running StartReplicationTaskAssessment](#CHAP_Tasks.AssessmentReport.Troubleshooting.ResourceNotFoundFault)

## ResourceNotFoundFault when running StartReplicationTaskAssessment
<a name="CHAP_Tasks.AssessmentReport.Troubleshooting.ResourceNotFoundFault"></a>

You may encounter the following exception when running the [StartReplicationTaskAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html) action.

```
An error occurred (ResourceNotFoundFault) when calling the StartReplicationTaskAssessment operation: Task assessment has not been run or dms-access-for-tasks IAM Role not configured correctly
```

If you encounter this exception, create the **dms-access-for-tasks** role by doing the following:

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **Custom trust policy**.

1. Paste the following JSON in the editor, replacing the existing text.

------
#### [ JSON ]

****

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Sid": "1",
               "Effect": "Allow",
               "Principal": {
                   "Service": "dms.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

   The preceding policy grants the `sts:AssumeRole` permission to AWS DMS. When you add the **AmazonDMSRedshiftS3Role** policy, DMS can to create the S3 bucket in your account, and put the data type assessment results into this S3 bucket.

1. Choose **Next**.

1. On the **Add permissions** page, search for and add the **AmazonDMSRedshiftS3Role** policy. Choose **Next**.

1. On the **Name, review, and create** page, name the role **dms-access-for-tasks**. Choose **Create role**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
