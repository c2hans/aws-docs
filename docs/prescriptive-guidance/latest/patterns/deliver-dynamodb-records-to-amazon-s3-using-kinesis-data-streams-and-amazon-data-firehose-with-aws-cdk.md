---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk.html
---

# Deliver DynamoDB records to Amazon S3 using Kinesis Data Streams and Firehose with AWS CDK
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk"></a>

*Shashank Shrivastava and Daniel Matuki da Cunha, Amazon Web Services*

## Summary
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk-summary"></a>

This pattern provides sample code and an application for delivering records from Amazon DynamoDB to Amazon Simple Storage Service (Amazon S3) by using Amazon Kinesis Data Streams and Amazon Data Firehose. The pattern’s approach uses [AWS Cloud Development Kit (AWS CDK) L3 constructs](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) and includes an example of how to perform data transformation with AWS Lambda before data is delivered to the target S3 bucket on the Amazon Web Services (AWS) Cloud.

Kinesis Data Streams records item-level modifications in DynamoDB tables and replicates them to the required Kinesis data stream. Your applications can access the Kinesis data stream and view the item-level changes in near-real time. Kinesis Data Streams also provides access to other Amazon Kinesis services, such as Firehose and Amazon Managed Service for Apache Flink. This means that you can build applications that provide real-time dashboards, generate alerts, implement dynamic pricing and advertising, and perform sophisticated data analysis.

You can use this pattern for your data integration use cases. For example, transportation vehicles or industrial equipment can send high volumes of data to a DynamoDB table. This data can then be transformed and stored in a data lake hosted in Amazon S3. You can then query and process the data and predict any potential defects by using serverless services such as Amazon Athena, Amazon Redshift Spectrum, Amazon Rekognition, and AWS Glue.

## Prerequisites and limitations
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk-prereqs"></a>

*Prerequisites*
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI), installed and configured. For more information, see [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the AWS CLI documentation.
+ Node.js (18.x\+) and npm, installed and configured. For more information, see [Downloading and installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) in the `npm` documentation.
+ aws-cdk (2.x\+), installed and configured. For more information, see [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) in the AWS CDK documentation.
+ The GitHub [aws-dynamodb-kinesisfirehose-s3-ingestion](https://github.com/aws-samples/aws-dynamodb-kinesisfirehose-s3-ingestion/) repository, cloned and configured on your local machine.
+ Existing sample data for the DynamoDB table. The data must use the following format: `{"SourceDataId": {"S": "123"},"MessageData":{"S": "Hello World"}}`

## Architecture
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk-architecture"></a>

The following diagram shows an example workflow for delivering records from DynamoDB to Amazon S3 by using Kinesis Data Streams and Firehose.

![An example workflow for delivering records from DynamoDB to Amazon S3 using Kinesis Data Streams and Firehose.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e2a9c412-312e-4900-9774-19a281c578e4/images/6e6df998-e6c2-4eaf-b263-ace752194689.png)

The diagram shows the following workflow:

1. Data is ingested using Amazon API Gateway as a proxy for DynamoDB. You can also use any other source to ingest data into DynamoDB.

1. Item-level changes are generated in near-real time in Kinesis Data Streams for delivery to Amazon S3.

1. Kinesis Data Streams sends the records to Firehose for transformation and delivery.

1. A Lambda function converts the records from a DynamoDB record format to JSON format, which contains only the record item attribute names and values.

## Tools
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk-tools"></a>

*AWS services*
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) is a command line cloud development kit that helps you interact with your AWS CDK app.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.

*Code repository*

The code for this pattern is available in the GitHub [aws-dynamodb-kinesisfirehose-s3-ingestion](https://github.com/aws-samples/aws-dynamodb-kinesisfirehose-s3-ingestion/) repository.

## Epics
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk-epics"></a>

### Set up and configure the sample code
<a name="set-up-and-configure-the-sample-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the dependencies. | On your local machine, install the dependencies from the `package.json` files in the `pattern/aws-dynamodb-kinesisstreams-s3` and `sample-application` directories by running the following commands:<pre>cd <project_root>/pattern/aws-dynamodb-kinesisstreams-s3 </pre><pre>npm install && npm run build</pre><pre>cd <project_root>/sample-application/</pre><pre>npm install && npm run build</pre><br />  | App developer, General AWS |
| Generate the CloudFormation template. | 1. Run the `cd <project_root>/sample-application/` command.<br />2. Run the `cdk synth` command to generate the CloudFormation template.<br />3. The `AwsDynamodbKinesisfirehoseS3IngestionStack.template.json` output is stored in the `cdk.out` directory.<br />4. Use AWS CDK or the AWS Management Console to process the template in CloudFormation. | App developer, General AWS, AWS DevOps |

### Deploy the resources
<a name="deploy-the-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check and deploy the resources. | 1. Run the `cdk diff` command to identify the resource types that are created by the AWS CDK construct.<br />2. Run the `cdk deploy` command to deploy the resources. | App developer, General AWS, AWS DevOps |

### Ingest data into the DynamoDB table to test the solution
<a name="ingest-data-into-the-dynamodb-table-to-test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Ingest your sample data into the DynamoDB table. | Send a request to your DynamoDB table by running the following command in AWS CLI:<br />`aws dynamodb put-item --table-name <your_table_name> --item '{"<table_partition_key>": {"S": "<partition_key_ID>"},"MessageData":{"S": "<data>"}}'`<br />example:<br />`aws dynamodb put-item --table-name SourceData_table --item '{"SourceDataId": {"S": "123"},"MessageData":{"S": "Hello World"}}'`<br />By default, the `put-item` doesn't return any value as output if the operation succeeds. If the operation fails, it returns an error. The data is stored in DynamoDB and then sent to Kinesis Data Streams and Firehose. You use different approaches to add data into a DynamoDB table. For more information, see [Load data into tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SampleData.LoadData.html) in the DynamoDB documentation. | App developer |
| Verify that a new object is created in the S3 bucket. | Sign in to the AWS Management Console and monitor the S3 bucket to verify that a new object was created with the data that you sent. <br />For more information, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the Amazon S3 documentation. | App developer, General AWS |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources.  | Run the `cdk destroy` command to delete all the resources used by this pattern. | App developer, General AWS |

## Related resources
<a name="deliver-dynamodb-records-to-amazon-s3-using-kinesis-data-streams-and-amazon-data-firehose-with-aws-cdk-resources"></a>
+ [s3-static-site-stack.ts](https://github.com/awslabs/aws-solutions-constructs/blob/main/source/use_cases/aws-s3-static-website/lib/s3-static-site-stack.ts#L25) (GitHub repository)
+ [aws-apigateway-dynamodb module](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-apigateway-dynamodb) (GitHub repository)
+ [aws-kinesisstreams-kinesisfirehose-s3 module](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-kinesisstreams-kinesisfirehose-s3) (GitHub repository)
+ [Change data capture for DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) (DynamoDB documentation)
+ [Using Kinesis Data Streams to capture changes to DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/kds.html) (DynamoDB documentation)
