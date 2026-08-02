---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/analytics-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Analytics architecture
<a name="analytics-architecture"></a>

 Analytics pipelines are designed to handle large volumes of incoming streams of data from heterogeneous sources such as databases, applications, and devices.

 A typical analytics pipeline has the following stages:

1.  Collect data

1.  Store the data

1.  Process the data

1.  Analyze and visualize the data

![Analytics Pipeline](http://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/images/analytics-pipeline.jpg)

*Analytics pipeline *

## Data collection
<a name="data-collection"></a>

 At the data collection stage, consider that you probably have different types of data, such as transactional data, log data, streaming data, and Internet of Things (IoT) data. AWS provides solutions for data storage for each of these types of data.

### Log data
<a name="log-data"></a>

 Reliably capturing system-generated logs helps you troubleshoot issues, conduct audits, and perform analytics using the information stored in the logs. [Amazon S3](https://aws.amazon.com/s3/) is a popular storage solution for non-transactional data, such as log data, that is used for analytics. Because it provides 99.999999999 percent durability, S3 is also a popular archival solution.

### Streaming data
<a name="streaming-data"></a>

 Web applications, mobile devices, and many software applications and services can generate staggering amounts of [streaming data](https://aws.amazon.com/streaming-data/)—sometimes terabytes per hour—that need to be collected, stored, and processed continuously. Using [Amazon Kinesis](https://aws.amazon.com/kinesis/) services, you can do that simply and at a low cost. Alternatively, you can use [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK) to run applications that use Apache Kafka to process streaming data. With Amazon MSK, you can use native Apache Kafka application programming interfaces (APIs) to populate data lakes, stream changes to and from databases, and power ML and analytics applications.

### IoT data
<a name="iot-data"></a>

 Devices and sensors around the world send messages continuously. Enterprises today need to capture this data and derive intelligence from it. Using [AWS IoT](https://aws.amazon.com/iot/), connected devices interact easily and securely with the AWS Cloud. Use AWS IoT to leverage AWS services like [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon Kinesis](https://aws.amazon.com/kinesis/) Services, [Amazon S3](https://aws.amazon.com/s3/), [Amazon Machine Learning](https://aws.amazon.com/machine-learning/), and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) to build applications that gather, process, analyze, and act on IoT data, without having to manage any infrastructure.
