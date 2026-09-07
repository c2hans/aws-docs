---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/calculate-value-at-risk-var-by-using-aws-services.html
---

# Calculate value at risk (VaR) by using AWS services
<a name="calculate-value-at-risk-var-by-using-aws-services"></a>

*Sumon Samanta, Amazon Web Services*

## Summary
<a name="calculate-value-at-risk-var-by-using-aws-services-summary"></a>

This pattern describes how to implement a value at risk (VaR) calculation system by using AWS services. In an on-premises environment, most VaR systems use a large, dedicated infrastructure and in-house or commercial grid scheduling software to run batch processes. This pattern presents a simple, reliable, and scalable architecture to handle VaR processing in the AWS Cloud. It builds a serverless architecture that uses Amazon Kinesis Data Streams as a streaming service, Amazon Simple Queue Service (Amazon SQS) as a managed queue service, Amazon ElastiCache as a caching service, and AWS Lambda to process orders and calculate risk.

VaR is a statistical measure that traders and risk managers use to estimate potential loss in their portfolio beyond a certain confidence level. Most VaR systems involve running a large number of mathematical and statistical calculations and storing the results. These calculations require significant compute resources, so VaR batch processes have to be broken into smaller sets of compute tasks. Splitting a large batch into smaller tasks is possible because these tasks are mostly independent (that is, calculations for one task don’t depend other tasks).

Another important requirement for a VaR architecture is compute scalability. This pattern uses a serverless architecture that automatically scales in or out based on compute load. Because the batch or online compute demand is difficult to predict, dynamic scaling is required to complete the process within the timeline imposed by a service-level agreement (SLA). Also, a cost-optimized architecture should be able to scale down each compute resource as soon as the tasks on that resource are complete.

AWS services are well-suited for VaR calculations because they offer scalable compute and storage capacity, analytics services for processing in a cost-optimized way, and different types of schedulers to run your risk management workflows. Also, you pay only for the compute and storage resources that you use on AWS.

## Prerequisites and limitations
<a name="calculate-value-at-risk-var-by-using-aws-services-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ Input files, which depend on your business requirements. A typical use case involves the following input files:
  + Market data file (input to the VaR calculation engine)
  + Trade data file (unless trade data comes through a stream).
  + Configuration data file (model and other static configuration data)
  + Calculation engine model files (quantitative libraries)
  + Time series data file (for historical data such as the stock price for the last five years)
+ If the market data or other input comes in through a stream, Amazon Kinesis Data Streams set up, and Amazon Identity and Access Management (IAM) permissions configured to write to the stream.

This pattern builds an architecture in which trade data is written from a trading system to a Kinesis data stream. Instead of using a streaming service, you can save your trade data in small batch files, store them in an Amazon Simple Storage Service (Amazon S3) bucket, and invoke an event to start processing the data.

**Limitations**
+ Kinesis data stream sequencing is guaranteed on each shard, so trade orders that are written to multiple shards are not guaranteed to be delivered in the same order as write operations.
+ The AWS Lambda runtime limit is currently 15 minutes. (For more information, see the [Lambda FAQ](https://aws.amazon.com/lambda/faqs/).)

## Architecture
<a name="calculate-value-at-risk-var-by-using-aws-services-architecture"></a>

**Target architecture **

The following architecture diagram displays the AWS services and workflows for the risk assessment system.

![VaR calculation system with AWS services](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eb615fc5-3cc3-445a-af2c-8446ee7b5276/images/c60aec03-ff6c-410c-8ee8-f1f6efa22cf7.png)

The diagram illustrates the following:

1. Trades stream in from the order management system.

1. The *ticket position netting* Lambda function processes the orders and writes consolidated messages for each ticker to a risk queue in Amazon SQS.

1. The *risk calculation engine* Lambda function processes the messages from Amazon SQS, performs risk calculations, and updates the VaR profit and loss (PnL) information in the risk cache in Amazon ElastiCache.

1. The *read ElastiCache data* Lambda function retrieves the risk results from ElastiCache and stores them in a database and S3 bucket.

For more information about these services and steps, see the *Epics* section.

**Automation and scale**

You can deploy the entire architecture by using the AWS Cloud Development Kit (AWS CDK) or AWS CloudFormation templates. The architecture can support both batch processing and intraday (real-time) processing.

Scaling is built into the architecture. As more trades are written into the Kinesis data stream and are waiting to be processed, additional Lambda functions can be invoked to process those trades and can then scale down after processing is complete. Processing through multiple Amazon SQS risk calculation queues is also an option. If strict ordering or consolidation is required across queues, processing cannot be parallelized. However, for an end-of-the-day batch or a mini intraday batch, the Lambda functions can process in parallel and store the final results in ElastiCache.

## Tools
<a name="calculate-value-at-risk-var-by-using-aws-services-tools"></a>

** AWS services**
+ [Amazon Aurora MySQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html) is a fully managed, MySQL-compatible relational database engine that helps you set up, operate, and scale MySQL deployments. This pattern uses MySQL as an example, but you can use any RDBMS system to store data.
+ [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache/) helps you set up, manage, and scale distributed in-memory cache environments in the AWS Cloud.
+ [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) helps you collect and process large streams of data records in real time.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code **

This pattern provides an example architecture for a VaR system in the AWS Cloud and describes how you can use Lambda functions for VaR calculations. To create your Lambda functions, see the code examples in the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples.html). For assistance, contact [AWS Professional Services](https://pages.awscloud.com/AWS-Professional-Services.html).

## Best practices
<a name="calculate-value-at-risk-var-by-using-aws-services-best-practices"></a>
+ Keep each VaR compute task as small and lightweight as possible. Experiment with different numbers of trades in each compute task to see which one is most optimized for compute time and cost.
+ Store reusable objects in Amazon ElastiCache. Use a framework such as Apache Arrow to reduce serialization and deserialization.
+ Consider Lambda’s time limitation. If you think your compute tasks might exceed 15 minutes, try to break them down into smaller tasks to avoid the Lambda timeout. If this is not possible, you might consider a container orchestration solution with AWS Fargate, Amazon Elastic Container Service (Amazon ECS), and Amazon Elastic Kubernetes Service (Amazon EKS).

## Epics
<a name="calculate-value-at-risk-var-by-using-aws-services-epics"></a>

### Trade flow to risk system
<a name="trade-flow-to-risk-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start writing trades.  | New, settled, or partially settled trades are written from the order management system to a risk stream. This pattern uses Amazon Kinesis as the managed streaming service. The trade order ticker’s hash is used to put trade orders across multiple shards. | Amazon Kinesis |

### Run Lambda functions for order processing
<a name="run-lambda-functions-for-order-processing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start risk processing with Lambda. | Run an AWS Lambda function for the new orders. Based on the number of pending trade orders, Lambda will automatically scale. Each Lambda instance has one or more orders and retrieves the latest position for each ticker from Amazon ElastiCache. (You can use a CUSIP ID, a Curve name, or an index name for other financial derivative products as a key to store and retrieve data from ElasticCache.) In ElastiCache, the total position (quantity) and the key-value pair <*ticker*, *net position*>, where *net position* is the scaling factor, are updated once for each ticker.  | Amazon Kinesis, AWS Lambda, Amazon ElastiCache |

### Write messages for each ticker into queue
<a name="write-messages-for-each-ticker-into-queue"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Write consolidated messages to the risk queue. | Write the message to a queue. This pattern uses Amazon SQS as a managed queue service. A single Lambda instance might get a mini batch of trade orders at any given time, but will write only a single message for each ticker to Amazon SQS. A scaling factor is calculated: (*old net position* \+ *current position*) / *old net position*. | Amazon SQS, AWS Lambda |

### Invoke risk engine
<a name="invoke-risk-engine"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start risk calculations. | The Lambda function for the risk engine lambda is invoked. Each position is processed by a single Lambda function. However, for optimization purposes, each Lambda function can process multiple messages from Amazon SQS. | Amazon SQS, AWS Lambda |

### Retrieve risk results from cache
<a name="retrieve-risk-results-from-cache"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Retrieve and update risk cache. | Lambda retrieves the current net position for each ticker from ElastiCache. It also retrieves a VaR profit and loss (PnL) array for each ticker from ElastiCache. <br />If the PnL array already exists, the Lambda function updates the array and VaR with a scale, which comes from the Amazon SQS message written by the netting Lambda function. If the PnL array isn’t in ElasticCache, a new PnL and VaR are calculated by using simulated ticker price series data. | Amazon SQS, AWS Lambda, Amazon ElastiCache |

### Update data in Elastic Cache and store in database
<a name="update-data-in-elastic-cache-and-store-in-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Store risk results. | After the VaR and PnL numbers are updated in ElastiCache, a new Lambda function is invoked every five minutes. This function reads all stored data from ElastiCache and stores it in an Aurora MySQL-Compatible database and in an S3 bucket. | AWS Lambda, Amazon ElastiCache |

## Related resources
<a name="calculate-value-at-risk-var-by-using-aws-services-resources"></a>
+ [Basel VaR Framework](https://www.bis.org/basel_framework/chapter/DIS/50.htm)
