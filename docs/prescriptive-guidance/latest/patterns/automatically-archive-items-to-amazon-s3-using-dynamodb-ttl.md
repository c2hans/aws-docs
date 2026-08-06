---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-archive-items-to-amazon-s3-using-dynamodb-ttl.html
---

# Automatically archive items to Amazon S3 using DynamoDB TTL
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl"></a>

*Tabby Ward, Amazon Web Services*

## Summary
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-summary"></a>

This pattern provides steps to remove older data from an Amazon DynamoDB table and archive it to an Amazon Simple Storage Service (Amazon S3) bucket on Amazon Web Services (AWS) without having to manage a fleet of servers.

This pattern uses Amazon DynamoDB Time to Live (TTL) to automatically delete old items and Amazon DynamoDB Streams to capture the TTL-expired items. It then connects DynamoDB Streams to AWS Lambda, which runs the code without provisioning or managing any servers.

When new items are added to the DynamoDB stream, the Lambda function is initiated and writes the data to an Amazon Data Firehose delivery stream. Firehose provides a simple, fully managed solution to load the data as an archive into Amazon S3.

DynamoDB is often used to store time series data, such as webpage click-stream data or Internet of Things (IoT) data from sensors and connected devices. Rather than deleting less frequently accessed items, many customers want to archive them for auditing purposes. TTL simplifies this archiving by automatically deleting items based on the timestamp attribute.

Items deleted by TTL can be identified in DynamoDB Streams, which captures a time-ordered sequence of item-level modifications and stores the sequence in a log for up to 24 hours. This data can be consumed by a Lambda function and archived in an Amazon S3 bucket to reduce the storage cost. To further reduce the costs, [Amazon S3 lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) can be created to automatically transition the data (as soon as it gets created) to lowest-cost [storage classes](https://aws.amazon.com/s3/storage-classes/).

## Prerequisites and limitations
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ [AWS Command Line Interface (AWS CLI) 1.7 or later](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html), installed and configured on macOS, Linux, or Windows.
+ [Python 3.7](https://www.python.org/downloads/release/python-370/) or later.
+ [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), installed and configured. If Boto3 is not already installed, run the `python -m pip install boto3` command to install it.

## Architecture
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-architecture"></a>

**Technology stack  **
+ Amazon DynamoDB
+ Amazon DynamoDB Streams
+ Amazon Data Firehose
+ AWS Lambda
+ Amazon S3

![Four-step process from DynamoDB to the S3 bucket.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9dbc833f-cf3c-4574-8f09-d0b81134fe41/images/50d9da65-5398-4a99-bc8f-58afc80e9d7b.png)

1. Items are deleted by TTL.

1. The DynamoDB stream trigger invokes the Lambda stream processor function.

1. The Lambda function puts records in the Firehose delivery stream in batch format.

1. Data records are archived in the S3 bucket.

## Tools
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-tools"></a>
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) – The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) – Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale.
+ [Amazon DynamoDB Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html) – Amazon DynamoDB TTL helps you define a per-item timestamp to determine when an item is no longer required.
+ [Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types_Amazon_DynamoDB_Streams.html) – Amazon DynamoDB Streams captures a time-ordered sequence of item-level modifications in any DynamoDB table and stores this information in a log for up to 24 hours.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) – Amazon Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics services.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda runs code without the need to provision or manage servers. You pay only for the compute time you consume.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

**Code**

The code for this pattern is available in the GitHub [Archive items to S3 using DynamoDB TTL](https://github.com/aws-samples/automatically-archive-items-to-s3-using-dynamodb-ttl) repository.

## Epics
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-epics"></a>

### Set up a DynamoDB table, TTL , and a DynamoDB stream
<a name="set-up-a-dynamodb-table-ttl-and-a-dynamodb-stream"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a DynamoDB table. | Use the AWS CLI to create a table in DynamoDB called `Reservation`. Choose random read capacity unit (RCU) and write capacity unit (WCU), and give your table two attributes: `ReservationID` and `ReservationDate`. <pre>aws dynamodb create-table \<br />--table-name Reservation \<br />--attribute-definitions AttributeName=ReservationID,AttributeType=S AttributeName=ReservationDate,AttributeType=N \<br />--key-schema AttributeName=ReservationID,KeyType=HASH AttributeName=ReservationDate,KeyType=RANGE \<br />--provisioned-throughput ReadCapacityUnits=100,WriteCapacityUnits=100 </pre><br />`ReservationDate` is an epoch timestamp that will be used to turn on TTL. | Cloud architect, App developer |
| Turn on DynamoDB TTL. | Use the AWS CLI to turn on DynamoDB TTL for the `ReservationDate` attribute.<pre>aws dynamodb update-time-to-live \<br />--table-name Reservation\<br />  --time-to-live-specification Enabled=true,AttributeName=ReservationDate</pre> | Cloud architect, App developer |
| Turn on a DynamoDB stream. | Use the AWS CLI to turn on a DynamoDB stream for the `Reservation` table by using the `NEW_AND_OLD_IMAGES` stream type. <pre>aws dynamodb update-table \<br />--table-name Reservation \<br />  --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES</pre><br />This stream will contain records for new items, updated items, deleted items, and items that are deleted by TTL. The records for items that are deleted by TTL contain an additional metadata attribute to distinguish them from items that were deleted manually. The `userIdentity` field for TTL deletions indicates that the DynamoDB service performed the delete action. <br />In this pattern, only the items deleted by TTL are archived, but you could archive only the records where `eventName` is `REMOVE` and `userIdentity` contains `principalId` equal to `dynamodb.amazonaws.com`. | Cloud architect, App developer |

### Create and configure an S3 bucket
<a name="create-and-configure-an-s3-bucket"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | Use the AWS CLI to create a destination S3 bucket in your AWS Region, replacing `us-east-1` with your Region and amzn-s3-demo-destination-bucket with the name of your bucket. <pre>aws s3api create-bucket \<br />--bucket DOC-EXAMPLE-BUCKET \<br />--region us-east-1</pre><br />Make sure that your S3 bucket's name is globally unique, because the namespace is shared by all AWS accounts. | Cloud architect, App developer |
| Create a 30-day lifecycle policy for the S3 bucket. | 1. Sign in to the AWS Management Console and open the Amazon S3 console. <br />2. Choose the S3 bucket that contains the data from Firehose. <br />3. In the S3 bucket, choose the **Management** tab, and choose **Add lifecycle rule**. <br />4. Enter a name for your rule in the **Lifecycle rule** dialog box, and configure a 30-day lifecycle rule for your bucket. | Cloud architect, App developer |

### Create a Firehose delivery stream
<a name="create-a-akf-delivery-stream"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and configure a Firehose delivery stream. | Download and edit the `CreateFireHoseToS3.py` code example from the GitHub repository. <br />This code is written in Python and shows you how to create a Firehose delivery stream and an AWS Identity and Access Management (IAM) role. The IAM role will have a policy that can be used by Firehose to write to the destination S3 bucket.<br />To run the script, use the following command and command line arguments.<br />Argument 1= `<Your_S3_bucket_ARN>`, which is the Amazon Resource Name (ARN) for the bucket that you created earlier<br />Argument 2= Your Firehose name (This pilot is using  `firehose_to_s3_stream`.)<br />Argument 3= Your IAM role name (This pilot is using `firehose_to_s3`.)<pre>python CreateFireHoseToS3.py <Your_S3_Bucket_ARN> firehose_to_s3_stream firehose_to_s3</pre><br />If the specified IAM role does not exist, the script will create an assume role with a trusted relationship policy, as well as a policy that grants sufficient Amazon S3 permission. For examples of these policies, see the *Additional information* section. | Cloud architect, App developer |
| Verify the Firehose delivery stream. | Describe the Firehose delivery stream by using the AWS CLI to verify that the delivery stream was successfully created.<pre>aws firehose describe-delivery-stream --delivery-stream-name firehose_to_s3_stream </pre> | Cloud architect, App developer |

### Create a Lambda function to process the Firehose delivery stream
<a name="create-a-lambda-function-to-process-the-akf-delivery-stream"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a trust policy for the Lambda function. | Create a trust policy file with the following information.<pre> {<br />     "Version": "2012-10-17",		 	 	 <br />     "Statement": [<br />      {<br />          "Effect": "Allow",<br />          "Principal": {<br />              "Service": "lambda.amazonaws.com"<br />           },<br />           "Action": "sts:AssumeRole"<br />      }<br />    ]<br />  } </pre><br />This gives your function permission to access AWS resources. | Cloud architect, App developer |
| Create an execution role for the Lambda function. | To create the execution role, run the following code.<pre>aws iam create-role --role-name lambda-ex --assume-role-policy-document file://TrustPolicy.json</pre> | Cloud architect, App developer |
| Add permission to the role. | To add permission to the role, use the `attach-policy-to-role` command.<pre>aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole<br />aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole<br />aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/AmazonKinesisFirehoseFullAccess<br />aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/IAMFullAccess </pre> | Cloud architect, App developer |
| Create a Lambda function. | Compress the `LambdaStreamProcessor.py` file from the code repository by running the following command.<pre>zip function.zip LambdaStreamProcessor.py</pre><br />When you create the Lambda function, you will need the Lambda execution role ARN. To get the ARN, run the following code.<pre>aws iam get-role \<br />--role-name lambda-ex </pre><br />To create the Lambda function, run the following code.<pre># Review the environment variables and replace them with your values.<br /><br />aws lambda create-function --function-name LambdaStreamProcessor \<br />--zip-file fileb://function.zip --handler LambdaStreamProcessor.handler --runtime python3.8 \<br />--role {Your Lamda Execution Role ARN}\<br />  --environment Variables="{firehose_name=firehose_to_s3_stream,bucket_arn = <Your_S3_bucket_ARN>,iam_role_name = firehose_to_s3, batch_size=400}"</pre> | Cloud architect, App developer |
| Configure the Lambda function trigger. | Use the AWS CLI to configure the trigger (DynamoDB Streams), which invokes the Lambda function. The batch size of 400 is to avoid running into Lambda concurrency issues.<pre>aws lambda create-event-source-mapping --function-name LambdaStreamProcessor \<br />--batch-size 400 --starting-position LATEST \<br />--event-source-arn <Your Latest Stream ARN From DynamoDB Console></pre> | Cloud architect, App developer |

### Test the functionality
<a name="test-the-functionality"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add items with expired timestamps to the Reservation table. | To test the functionality, add items with expired epoch timestamps  to the `Reservation` table. TTL will automatically delete items based on the timestamp. <br />The Lambda function is initiated upon DynamoDB Stream activities, and it filters the event to identify `REMOVE` activity or deleted items. It then puts records in the Firehose delivery stream in batch format.<br />The Firehose delivery stream transfers items to a destination S3 bucket with the `firehosetos3example/year=current year/month=current month/ day=current day/hour=current hour/` prefix.To optimize data retrieval, configure Amazon S3 with the `Prefix` and `ErrorOutputPrefix` that are detailed in the *Additional information* section. | Cloud architect  |

### Clean up the resources
<a name="clean-up-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete all resources. | Delete all the resources to ensure that you aren't charged for any services that you aren't using.   | Cloud architect, App developer |

## Related resources
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-resources"></a>
+ [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-lifecycle.html)
+ [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)
+ [AWS SDK for Python (Boto3) documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Additional information
<a name="automatically-archive-items-to-amazon-s3-using-dynamodb-ttl-additional"></a>

**Create and configure a Firehose delivery stream – Policy examples**

*Firehose trusted relationship policy example document*

```
firehose_assume_role = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Sid': '',
                'Effect': 'Allow',
                'Principal': {
                    'Service': 'firehose.amazonaws.com'
                },
                'Action': 'sts:AssumeRole'
            }
        ]
    }
```

*S3 permissions policy example*

```
s3_access = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Action": [
                    "s3:AbortMultipartUpload",
                    "s3:GetBucketLocation",
                    "s3:GetObject",
                    "s3:ListBucket",
                    "s3:ListBucketMultipartUploads",
                    "s3:PutObject"
                ],
                "Resource": [
                    "{your s3_bucket ARN}/*",
                    "{Your s3 bucket ARN}"
                ]
            }
        ]
    }
```

**Test the functionality – Amazon S3 configuration**

The Amazon S3 configuration with the following `Prefix` and `ErrorOutputPrefix` is chosen to optimize data retrieval.

*Prefix *

```
firehosetos3example/year=! {timestamp: yyyy}/month=! {timestamp:MM}/day=! {timestamp:dd}/hour=!{timestamp:HH}/
```

Firehose first creates a base folder called `firehosetos3example` directly under the S3 bucket. It then evaluates the expressions `!{timestamp:yyyy}`, `!{timestamp:MM}`, `!{timestamp:dd}`, and `!{timestamp:HH}` to year, month, day, and hour using the Java [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) format.

For example, an approximate arrival timestamp of 1604683577 in Unix epoch time evaluates to `year=2020`, `month=11`, `day=06`, and `hour=05`. Therefore, the location in Amazon S3, where data records are delivered, evaluates to `firehosetos3example/year=2020/month=11/day=06/hour=05/`.

*ErrorOutputPrefix*

```
firehosetos3erroroutputbase/!{firehose:random-string}/!{firehose:error-output-type}/!{timestamp:yyyy/MM/dd}/
```

The `ErrorOutputPrefix` results in a base folder called `firehosetos3erroroutputbase` directly under the S3 bucket. The expression `!{firehose:random-string}` evaluates to an 11-character random string such as `ztWxkdg3Thg`. The location for an Amazon S3 object where failed records are delivered could evaluate to `firehosetos3erroroutputbase/ztWxkdg3Thg/processing-failed/2020/11/06/`.
