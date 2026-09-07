---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-replication-of-amazon-rds-instances-across-aws-accounts.html
---

# Automate the replication of Amazon RDS instances across AWS accounts
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts"></a>

*Parag Nagwekar and Arun Chandapillai, Amazon Web Services*

## Summary
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-summary"></a>

This pattern shows you how to automate the process of replicating, tracking, and rolling back your Amazon Relational Database Service (Amazon RDS) DB instances across different AWS accounts by using AWS Step Functions and AWS Lambda. You can use this automation to perform large-scale replication of RDS DB instances without any performance impact or operational overhead—regardless of the size of your organization. You can also use this pattern to help your organization comply with mandatory data governance strategies or compliance requirements that call for your data to be replicated and redundant across different AWS accounts and AWS Regions. Cross-account replication of Amazon RDS data at scale is an inefficient and error-prone manual process that can be costly and time-consuming, but the automation in this pattern can help you achieve cross-account replication safely, effectively, and efficiently.

## Prerequisites and limitations
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-prereqs"></a>

**Prerequisites**
+ Two AWS accounts
+ An RDS DB instance, up and running in the source AWS account
+ A subnet group for the RDS DB instance in the destination AWS account
+ An AWS Key Management Service (AWS KMS) key created in the source AWS account and shared with the destination account (For more information about policy details, see the [Additional information](#automate-the-replication-of-amazon-rds-instances-across-aws-accounts-additional) section of this pattern.)
+ An AWS KMS key in the destination AWS account to encrypt the database in the destination account

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ Python 3.9 (using AWS Lambda)
+ PostgreSQL 11.3, 13.x, and 14.x

## Architecture
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-architecture"></a>

**Technology stack**
+ Amazon Relational Database Service (Amazon RDS)
+ Amazon Simple Notification Service (Amazon SNS)
+ AWS Key Management Service (AWS KMS)
+ AWS Lambda
+ AWS Secrets Manager
+ AWS Step Functions

**Target architecture**

The following diagram shows an architecture for using Step Functions to orchestrate scheduled, on-demand replication of RDS DB instances from a source account (account A) to a destination account (account B).

![Replicating Amazon RDS DB instances across source and destination accounts by using Step Functions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6310ad9b-1b1a-4a67-b684-ef605fef3e87/images/001550bb-cf6b-493d-9de9-0229a43753a1.png)

In the source account (account A in the diagram), the Step Functions state machine performs the following:

1. Creates a snapshot from the RDS DB instance in account A.

1. Copies and encrypts the snapshot with an AWS KMS key from account A. To ensure encryption in transit, the snapshot is encrypted whether or not the DB instance is encrypted.

1. Shares the DB snapshot with account B by giving account B access to the snapshot.

1. Pushes a notification to the SNS topic, and then the SNS topic invokes the Lambda function in account B.

In the destination account (account B in the diagram), the Lambda function runs the Step Functions state machine to orchestrate the following:

1. Copies the shared snapshot from account A to account B, while using the AWS KMS key from account A to decrypt the data first and then encrypt the data by using the AWS KMS key in account B.

1. Reads the secret from Secrets Manager to capture the name of the current DB instance.

1. Restores the DB instance from the snapshot with a new name and default AWS KMS key for Amazon RDS.

1. Reads the endpoint of the new database and updates the secret in Secrets Manager with the new database endpoint, and then tags the previous DB instance so that it can be deleted later.

1. Keeps the latest N instances of the databases and deletes all the other instances.

## Tools
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-tools"></a>

**AWS services**
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine Lambda functions and other AWS services to build business-critical applications.

**Code repository**

The code for this pattern is available in the GitHub [Crossaccount RDS Replication](https://github.com/aws-samples/aws-rds-crossaccount-replication) repository.

## Epics
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-epics"></a>

### Automate the replication of RDS DB instances across AWS accounts with a single click
<a name="automate-the-replication-of-rds-db-instances-across-aws-accounts-with-a-single-click"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation stack in the source account. | 1. Sign in to the AWS Management Console for the source account (account A) and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. In the navigation pane, choose **Stacks**.<br />3. Choose **Create stack**, and then choose **With existing resources (import resources)**.<br />4. On the **Identify resources** page, choose **Next**.<br />5. On the **Specify template** page, select **Upload a template**.<br />6. Choose **Choose file**, select the `Cloudformation-SourceAccountRDS.yaml` file from the GitHub [Crossaccount RDS Replication](https://github.com/aws-samples/aws-rds-crossaccount-replication) repository, and then choose **Next**.<br />7. For **Stack name**, enter a name for your stack.<br />8. In the **Parameters** section, specify the parameters that are defined in the stack template:For **DestinationAccountNumber**, enter the account number for your destination RDS DB instance.For **KeyName**, enter your AWS KMS key.For **ScheduleExpression**, enter a [cron expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) (the default is **12:00 am daily**).For **SourceDBIdentifier**, enter the name of the source database.For **SourceDBSnapshotName**, enter the name of the snapshot or accept the default.<br />9. Choose **Next**.<br />10. On the **Configure stack options** page, leave the default values, and then choose **Next**.<br />11. Review your stack configuration, and then choose **Submit**.<br />12. Choose the **Resources** tab for your stack, and then note the Amazon Resource Name (ARN) of the SNS topic. | Cloud administrator, Cloud architect |
| Deploy the CloudFormation stack in the destination account. | 1. Sign in to the AWS Management Console for the destination account (account B) and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. In the navigation pane, choose **Stacks**.<br />3. Choose **Create stack**, and then choose **With existing resources (import resources)**.<br />4. On the **Identify resources** page, choose **Next**.<br />5. On the **Specify template** page, select **Upload a template**.<br />6. Choose** file**, select the `Cloudformation-DestinationAccountRDS.yaml` file from the GitHub [Crossaccount RDS Replication](https://github.com/aws-samples/aws-rds-crossaccount-replication) repository, and then choose **Next**.<br />7. For **Stack name**, enter a name for your stack.<br />8. In the **Parameters** section, specify the parameters that are defined in the stack template:For **DatabaseName**, enter a name for your database.For **Engine**, enter the database engine type that matches the source database.For **DBInstanceClass**, enter the preferred database instance type or accept the default.For **Subnetgroups**, enter the existing VPC subnet group. For instructions about creating a subnet group, see [Step 2: Create a DB subnet group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.CreateDBSubnetGroup) in the Amazon RDS documentation.For **SecretName**, enter the path and secret name, or accept the default.For **SGID**, enter the security group ID of your destination cluster.For **KMSKey**, enter the ARN of the KMS key in your destination account.For **NoOfOlderInstances**, enter the number of old copies of the RDS DB instances that you want to keep for the rollback.<br />9. Choose **Next**.<br />10. On the **Configure stack options** page, leave the default values, and then choose **Next**.<br />11. Review your stack configuration, and then choose **Submit**.<br />12. Choose the **Resources** tab for your stack, and then note the Physical ID and ARN of `InvokeStepFunction`. | Cloud architect, DevOps engineer, Cloud administrator |
| Verify the creation of the RDS DB instance in the destination account. | 1. Sign in to the AWS Management Console and open the [Amazon RDS console](https://console.aws.amazon.com/rds/).<br />2. In the navigation pane, choose **Databases**, and then verify that the new RDS DB instance appears under the new cluster. | Cloud administrator, Cloud architect, DevOps engineer |
| Subscribe the Lambda function to the SNS topic. | You must run the following AWS Command Line Interface (AWS CLI) commands to subscribe the Lambda function in the destination account (account B) to the SNS topic in the source account (account A).<br />In account A, run following command:<pre>aws sns add-permission \<br />--label lambda-access --aws-account-id <DestinationAccount> \<br />--topic-arn <Arn of SNSTopic > \<br />--action-name Subscribe ListSubscriptionsByTopic </pre><br />In account B, run following command:<pre>aws lambda add-permission \<br />--function-name <Name of InvokeStepFunction> \<br />--source-arn <Arn of SNSTopic > \<br />--statement-id function-with-sns \<br />--action lambda:InvokeFunction \<br />--principal sns.amazonaws.com</pre><br />In account B, run following command:<pre>aws sns subscribe \<br />--protocol "lambda" \<br />--topic-arn <Arn of SNSTopic> \<br />--notification-endpoint <Arn of InvokeStepFunction></pre> | Cloud administrator, Cloud architect, DBA |
| Sync the RDS DB instance from the source account with the destination account. | Initiate the on-demand database replication by starting the Step Functions state machine in the source account.1. Open the [Step Functions console](https://console.aws.amazon.com/states/).<br />2. In the navigation pane, choose **State machines**.<br />3. Choose your state machine.<br />4. On the **Executions** tab, select your function, and then choose **Start execution** to start the workflow.A scheduler is in place to help you run the replication automatically on schedule, but the scheduler is turned off by default. You can find the name of the Amazon CloudWatch rule for the scheduler in the **Resources** tab of the CloudFormation stack in the destination account. For instructions on how to modify the CloudWatch Events rule, see [Deleting or Disabling a CloudWatch Events Rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Delete-or-Disable-Rule.html) in the CloudWatch documentation. | Cloud architect, DevOps engineer, Cloud administrator |
| Roll back your database to any of the previous copies when needed. | 1. Open the [Secrets Manager console](https://console.aws.amazon.com/secretsmanager/).<br />2. From the list of secrets, choose the secret that you created by using the CloudFormation template earlier. Your application uses the secret to access the database in the destination cluster.<br />3. To update the secret value from the details page, in the **Secret value **section, choose **Retrieve secret** value, and then choose **Edit**.<br />4. Enter the details of the database endpoint. | Cloud administrator, DBA, DevOps engineer |

## Related resources
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-resources"></a>
+ [Cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.html) (Amazon RDS documentation)
+ [Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.html) (Amazon RDS documentation)

## Additional information
<a name="automate-the-replication-of-amazon-rds-instances-across-aws-accounts-additional"></a>

You can use the following example policy to share your AWS KMS key across AWS accounts.

```
{
    "Version": "2012-10-17",
    "Id": "cross-account-rds-kms-key",
    "Statement": [
        {
            "Sid": "Enable user permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<SourceAccount>:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow administration of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<DestinationAccount>:root"
            },
            "Action": [
                "kms:Create*",
                "kms:Describe*",
                "kms:Enable*",
                "kms:List*",
                "kms:Put*",
                "kms:Update*",
                "kms:Revoke*",
                "kms:Disable*",
                "kms:Get*",
                "kms:Delete*",
                "kms:ScheduleKeyDeletion",
                "kms:CancelKeyDeletion"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::<DestinationAccount>:root",
                    "arn:aws:iam::<SourceAccount>:root"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey",
                "kms:CreateGrant"
            ],
            "Resource": "*"
        }
    ]
}
```
