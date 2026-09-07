---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch.html
---

# Automate backups for Amazon RDS for PostgreSQL DB instances by using AWS Batch
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch"></a>

*Kirankumar Chandrashekar, Amazon Web Services*

## Summary
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-summary"></a>

Backing up your PostgreSQL databases is an important task and can typically be completed with the [pg\_dump utility](https://www.postgresql.org/docs/current/app-pgdump.html), which uses the COPY command by default to create a schema and data dump of a PostgreSQL database. However, this process can become repetitive if you require regular backups for multiple PostgreSQL databases. If your PostgreSQL databases are hosted in the cloud, you can also take advantage of the [automated backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) feature provided by Amazon Relational Database Service (Amazon RDS) for PostgreSQL as well. This pattern describes how to automate regular backups for Amazon RDS for PostgreSQL DB instances using the pg\_dump utility.

Note: The instructions assume that you're using Amazon RDS. However, you can also use this approach for PostgreSQL databases that are hosted outside Amazon RDS. To take backups, the AWS Lambda function must be able to access your databases.

A time-based Amazon CloudWatch Events event initiates a Lambda function that searches for specific backup [tags applied to the metadata](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) of the PostgreSQL DB instances on Amazon RDS. If the PostgreSQL DB instances have the **bkp:AutomatedDBDump = Active** tag and other required backup tags, the Lambda function submits individual jobs for each database backup to AWS Batch.

AWS Batch processes these jobs and uploads the backup data to an Amazon Simple Storage Service (Amazon S3) bucket. This pattern uses a Dockerfile and an entrypoint.sh file to build a Docker container image that is used to make backups in the AWS Batch job. After the backup process is complete, AWS Batch records the backup details to an inventory table on Amazon DynamoDB. As an additional safeguard, a CloudWatch Events event initiates an Amazon Simple Notification Service (Amazon SNS) notification if a job fails in AWS Batch.

## Prerequisites and limitations
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing managed or unmanaged compute environment. For more information, see [Managed and unmanaged compute environments](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html) in the AWS Batch documentation.
+ [AWS Command Line Interface (CLI) version 2 Docker image](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-docker.html), installed and configured.
+ Existing Amazon RDS for PostgreSQL DB instances.
+ An existing S3 bucket.
+ [Docker](https://www.docker.com/), installed and configured on Linux, macOS, or Windows.
+ Familiarity with coding in Lambda.

## Architecture
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-architecture"></a>

![Architecture to back up Amazon RDS for PostgreSQL DB instances by using the pg_dump utility.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3283f739-980b-43d4-aca0-9d77a2ce3b85/images/352e2eab-1b7d-44ec-840a-a772a175e873.png)

**Technology stack  **
+ Amazon CloudWatch Events
+ Amazon DynamoDB
+ Amazon Elastic Container Registry (Amazon ECR)
+ Amazon RDS
+ Amazon SNS
+ Amazon S3
+ AWS Batch
+ AWS Key Management Service (AWS KMS)
+ AWS Lambda
+ AWS Secrets Manager
+ Docker

## Tools
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-tools"></a>
+ [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) – CloudWatch Events delivers a near real-time stream of system events that describe changes in AWS resources.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) – DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
+ [Amazon ECR](https://docs.aws.amazon.com/ecr/index.html) – Amazon Elastic Container Registry (Amazon ECR) is a managed AWS container image registry service that is secure, scalable, and reliable.
+ [Amazon RDS](https://docs.aws.amazon.com/rds/index.html) – Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) – Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers.
+ [Amazon S3](https://docs.aws.amazon.com/s3/index.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet.
+ [AWS Batch](https://docs.aws.amazon.com/batch/index.html) – AWS Batch helps you run batch computing workloads on the AWS Cloud.
+ [AWS KMS](https://docs.aws.amazon.com/kms/index.html) – AWS Key Management Service (AWS KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/index.html) – Lambda is a compute service that helps you run code without provisioning or managing servers.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/index.html) – Secrets Manager helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [Docker](https://www.docker.com/) – Docker helps developers easily pack, ship, and run any application as a lightweight, portable, and self-sufficient container.

Your PostgreSQL DB instances on Amazon RDS must have [tags applied to their metadata](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html). The Lambda function searches for tags to identify DB instances that should be backed up, and the following tags are typically used.

|
|
| Tag | Description |
| --- |--- |
| bkp:AutomatedDBDump = Active | Identifies an Amazon RDS DB instance as a candidate for backups. |
| bkp:AutomatedBackupSecret = <secret\_name > | Identifies the Secrets Manager secret that contains the Amazon RDS login credentials. |
| bkp:AutomatedDBDumpS3Bucket = <s3\_bucket\_name> | Identifies the S3 bucket to send backups to. |
| bkp:AutomatedDBDumpFrequency<br />bkp:AutomatedDBDumpTime | Identify the frequency and times when databases should be backed up.  |
| bkp:pgdumpcommand = <pgdump\_command> | Identifies the databases for which the backups need to be taken. |

## Epics
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-epics"></a>

### Create an inventory table in DynamoDB
<a name="create-an-inventory-table-in-dynamodb"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a table in DynamoDB. | Sign in to the AWS Management Console, open the Amazon DynamoDB console, and create a table. For help with this and other stories, see the *Related resources* section. | Cloud administrator, Database administrator |
| Confirm that the table was created.  | Run the `aws dynamodb describe-table --table-name <table-name> \| grep TableStatus` command. If the table exists, the command will return the `"TableStatus": "ACTIVE",` result. | Cloud administrator, Database administrator |

### Create an SNS topic for failed job events in AWS Batch
<a name="create-an-sns-topic-for-failed-job-events-in-aws-batch"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an SNS topic. | Open the Amazon SNS console, choose **Topics**, and create an SNS topic with the name `JobFailedAlert`. Subscribe an active email address to the topic, and check your email inbox to confirm the SNS subscription email from AWS Notifications. | Cloud administrator |
| Create a failed job event rule for AWS Batch.  | Open the Amazon CloudWatch console, choose **Events**, and then choose **Create rule**. Choose **Show advanced options**, and choose **Edit**. For **Build a pattern that selects events for processing by your targets**, replace the existing text with the "Failed job event" code from the *Additional information* section. This code defines a CloudWatch Events rule that initiates when AWS Batch has a `Failed` event. | Cloud administrator |
| Add event rule target.  | In **Targets**, choose **Add targets**, and choose the `JobFailedAlert` SNS topic. Configure the remaining details and create the Cloudwatch Events rule. | Cloud administrator |

### Build a Docker image and push it to an Amazon ECR repository
<a name="build-a-docker-image-and-push-it-to-an-amazon-ecr-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon ECR repository. | Open the Amazon ECR console and choose the AWS Region in which you want to create your repository. Choose **Repositories**, and then choose **Create repository**. Configure the repository according to your requirements. | Cloud administrator |
| Write a Dockerfile.  | Sign in to Docker and use the "Sample Dockerfile" and "Sample entrypoint.sh file" from the *Additional information* section to build a Dockerfile. | DevOps engineer |
| Create a Docker image and push it to the Amazon ECR repository. | Build the Dockerfile into a Docker image and push it to the Amazon ECR repository. For help with this story, see the *Related resources* section. | DevOps engineer |

### Create the AWS Batch components
<a name="create-the-aws-batch-components"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS Batch job definition. | Open the AWS Batch console and create a job definition that includes the Amazon ECR repository’s Uniform Resource Identifier (URI) as the property `Image`. | Cloud administrator |
| Configure the AWS Batch job queue.  | On the AWS Batch console, choose **Job queues**, and then choose **Create queue**. Create a job queue that will store jobs until AWS Batch runs them on the resources within your compute environment. Important: Make sure you write logic for AWS Batch to record the backup details to the DynamoDB inventory table. | Cloud administrator |

### Create and schedule a Lambda function
<a name="create-and-schedule-a-lambda-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Lambda function to search for tags. | Create a Lambda function that searches for tags on your PostgreSQL DB instances and identifies backup candidates. Make sure your Lambda function can identify the `bkp:AutomatedDBDump = Active` tag and all other required tags. Important: The Lambda function must also be able to add jobs to the AWS Batch job queue. | DevOps engineer |
| Create a time-based CloudWatch Events event.  | Open the Amazon CloudWatch console and create a CloudWatch Events event that uses a cron expression to run your Lambda function on a regular schedule. Important: All scheduled events use the UTC time zone. | Cloud administrator |

### Test the backup automation
<a name="test-the-backup-automation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon KMS key. | Open the Amazon KMS console and create a KMS key that can be used to encrypt the Amazon RDS credentials stored in AWS Secrets Manager. | Cloud administrator |
| Create an AWS Secrets Manager secret. | Open the AWS Secrets Manager console and store your Amazon RDS for PostgreSQL database credentials as a secret. | Cloud administrator |
| Add the required tags to the PostgreSQL DB instances. | Open the Amazon RDS console and add tags to the PostgreSQL DB instances that you want to automatically back up. You can use the tags from the table in the *Tools* section. If you require backups from multiple PostgreSQL databases within the same Amazon RDS instance, then use `-d test:-d test1` as the value for the `bkp:pgdumpcommand` tag. `test` and `test1` are database names. Make sure that there is no space after the colon (:). | Cloud administrator |
| Verify the backup automation.  | To verify the backup automation, you can either invoke the Lambda function or wait for the backup schedule to begin. After the backup process is complete, check that the DynamoDB inventory table has a valid backup entry for your PostgreSQL DB instances. If they match, then the backup automation process is successful. | Cloud administrator |

## Related resources
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-resources"></a>

**Create an inventory table in DynamoDB**
+ [Create an Amazon DynamoDB table ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html)

**Create an SNS topic for failed job events in AWS Batch**
+ [Create an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-topic.html)
+ [Send SNS alerts for failed job events in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_tutorial.html)

**Build a Docker image and push it to an Amazon ECR repository**
+ [Create an Amazon ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)
+ [Write a Dockerfile, create a Docker image, and push it to Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html)

**Create the AWS Batch components **
+ [Create an AWS Batch job definition](https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html#first-run-step-1)
+ [Configure your compute environment and AWS Batch job queue ](https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html#first-run-step-2)
+ [Create a job queue in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue.html)

**Create a Lambda function**
+ [Create a Lambda function and write code](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html)
+ [Use Lambda with DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html)

**Create a CloudWatch Events event**
+ [Create a time-based CloudWatch Events event ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Scheduled-Rule.html)
+ [Use cron expressions in Cloudwatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)

**Test the backup automation**
+ [Create an Amazon KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)
+ [Create a Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html)
+ [Add tags to an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)

## Additional information
<a name="automate-backups-for-amazon-rds-for-postgresql-db-instances-by-using-aws-batch-additional"></a>

**Failed job event:**

```
{
  "detail-type": [
    "Batch Job State Change"
  ],
  "source": [
    "aws.batch"
  ],
  "detail": {
    "status": [
      "FAILED"
    ]
  }
}
```

**Sample Dockerfile:**

```
FROM alpine:latest
RUN apk --update add py-pip postgresql-client jq bash && \
pip install awscli && \
rm -rf /var/cache/apk/*
ADD entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
```

**Sample entrypoint.sh file:**

```
 #!/bin/bash
set -e
DATETIME=`date +"%Y-%m-%d_%H_%M"`
FILENAME=RDS_PostGres_dump_${RDS_INSTANCE_NAME}
FILE=${FILENAME}_${DATETIME}

aws configure --profile new-profile set role_arn arn:aws:iam::${TargetAccountId}:role/${TargetAccountRoleName}
aws configure --profile new-profile set credential_source EcsContainer

echo "Central Account access provider IAM role is: "
aws sts get-caller-identity

echo "Target Customer Account access provider IAM role is: "
aws sts get-caller-identity --profile new-profile

securestring=$(aws secretsmanager get-secret-value --secret-id $SECRETID --output json --query 'SecretString' --region=$REGION --profile new-profile)

if [[ ${securestring} ]]; then
    echo "successfully accessed secrets manager and got the credentials"
    export PGPASSWORD=$(echo $securestring | jq --raw-output | jq -r '.DB_PASSWORD')
    PGSQL_USER=$(echo $securestring | jq --raw-output | jq -r '.DB_USERNAME')
    echo "Executing pg_dump for the PostGres endpoint ${PGSQL_HOST}"
    # pg_dump -h $PGSQL_HOST -U $PGSQL_USER -n dms_sample | gzip -9 -c  | aws s3 cp - --region=$REGION  --profile new-profile s3://$BUCKET/$FILE
    # in="-n public:-n private"
    IFS=':' list=($EXECUTE_COMMAND);
    for command in "${list[@]}";
      do
        echo $command;
        pg_dump -h $PGSQL_HOST -U $PGSQL_USER ${command} | gzip -9 -c  | aws s3 cp - --region=$REGION --profile new-profile s3://${BUCKET}/${FILE}-${command}".sql.gz"
        echo $?;
        if  [[ $? -ne 0 ]]; then
            echo "Error occurred in database backup process. Exiting now....."
            exit 1
        else
            echo "Postgresql dump was successfully taken for the RDS endpoint ${PGSQL_HOST} and is uploaded to the following S3 location s3://${BUCKET}/${FILE}-${command}.sql.gz"
            #write the details into the inventory table in central account
            echo "Writing to DynamoDB inventory table"
            aws dynamodb put-item --table-name ${RDS_POSTGRES_DUMP_INVENTORY_TABLE} --region=$REGION --item '{ "accountId": { "S": "'"${TargetAccountId}"'" }, "dumpFileUrl": {"S": "'"s3://${BUCKET}/${FILE}-${command}.sql.gz"'" }, "DumpAvailableTime": {"S": "'"`date +"%Y-%m-%d::%H::%M::%S"` UTC"'"}}'
            echo $?
            if  [[ $? -ne 0 ]]; then
                echo "Error occurred while putting item to DynamoDb Inventory Table. Exiting now....."
                exit 1
            else
                echo "Successfully written to DynamoDb Inventory Table ${RDS_POSTGRES_DUMP_INVENTORY_TABLE}"
            fi
        fi
      done;
else
    echo "Something went wrong {$?}"
    exit 1
fi

exec "$@"
```
