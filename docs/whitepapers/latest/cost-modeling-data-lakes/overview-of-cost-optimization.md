---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/overview-of-cost-optimization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview of cost optimization
<a name="overview-of-cost-optimization"></a>

 Across stages, the following are general practices to optimize cost of the services used.

## Use data compression
<a name="use-data-compression"></a>

 There are many different formats for compression. You should be selective about which one you choose to make sure it is supported by the services you are using.

 The formats provide different features for example some formats support splitting meaning they support parallelization better, whilst others have better compression but at the cost of performance. Compressing the data, reduces the storage cost and also reduces the cost for scanning data.

 To give an example of how compression can help reduce costs we took a CSV dataset and compressed it using bzip2. This reduced the data from 8 GB to 2 GB a 75% reduction. If we extrapolate this compression ratio to a larger dataset, 100 TB the savings are significant:
+  Without compression: $2,406.40 per month
+  With compression: $614.40 per month This represents a saving of 75%.

**Note**
 Compression also reduces the amount of data scanned by compute services such as Amazon Athena. An example of this covered in the Columnar format section.

## Reduce run frequency
<a name="reduce-run-frequency"></a>

 In this scenario, let’s assume we generate 1 TB of data daily. We could potentially stream this data, because it’s available, or choose to batch it and transfer it in one go. Let’s assume we have 1 Gbps bandwidth available for the transfer from our source system, for example on-premises systems. A single push of 1 TB daily would take around two hours. In this case we’ll allow three hours for some variance in speed.

 Also, in this scenario, we will use AWS SFTP to transfer the data. In the first scenario, we need the AWS SFTP service constantly running. In the second scenario, we only need it running for three hours a day to complete our transfer.
+  Running constant transfers as the data is available: $259.96 per month
+  Running a single batch transfer daily: $68.34 per month This represents a saving of just over 73%.

## Partition data
<a name="partition-data"></a>

 Partitioning data allows you to reduce the amount of data that is scanned within queries. This helps both reduce cost and improve performance. To demonstrate this, we used the [*GDELT dataset*.](https://registry.opendata.aws/gdelt/) It contains around 300 million rows stored in many CSV files. We stored one copy un-partitioned and a second copy partitioned by year, month, day.

`SELECT count(*) FROM "gdeltv2"."non-partioned|partitioned" WHERE year = 2019;`

 Unpartitioned:
+  Cost of query (102.9 GB scanned): $0.10 per query
+  Speed of query: 4 minutes 20 seconds Partitioned:
+  Cost of query (6.49 GB scanned): $0.006 per query
+  Speed of query: 11 seconds

 This represents a saving of 94% and improved performance by 95%.

## Choose a columnar format
<a name="choose-a-columnar-format"></a>

 Choosing a columnar format such as parquet, ORC or Avro helps reduce disk I/O requirements which can reduce costs and drastically improve performance in data lakes. To demonstrate this, we will again use GDELT. In both examples there is no partitioning but one dataset is stored as CSV and one as parquet.

 ` SELECT * FROM "gdeltv2"."csv|parquet" WHERE globaleventid = `

 CSV:
+  Cost of query (102.9 GB scanned): $0.10 per query
+  Speed of query: 4 minutes 20 seconds Partitioned:
+  Cost of query (1.04 GB scanned): $0.001 per query
+  Speed of query: 12.65 seconds

 This represents a saving of 99% and improved performance by 95%.

## Create data lifecycle policies
<a name="create-data-lifecycle-policies"></a>

 With Amazon S3, you can save significant costs by moving your data between storage tiers. In data lakes we generally keep a copy of the raw in-case we need to reprocess data as we find new questions to ask of our data. However, often this data isn’t required during general operations. Once we have processed our raw data for the organization, we can choose to move this to a cheaper tier of storage. In this example we are going to move data from standard Amazon S3 to Amazon Glacier.

 For our example, we will model these costs with 100TB of data.
+  Standard Amazon S3: **$2,406.40** per month
+  Amazon Glacier: **$460.80** per month This represents a saving of just over 80%.

## Right size your instances
<a name="right-size-your-instances"></a>

 AWS services are consumed on demand. This means that you pay only for what you consume. Like many AWS services, when you run the job you define how many resources you want and you also choose the instance size you want. You also have ability to stop the instance when it’s not being used and you can spin it up based on specific schedule. For example, transient EMR clusters can be used for scenarios where data has to be processed once a day or once a month.

 Monitor instance metrics with analytic workloads and downsize the instances if they are over provisioned.

## Use Spot Instances
<a name="use-spot-instances"></a>

 Amazon EC2 Spot Instances let you take advantage of unused Amazon EC2 capacity in the AWS Cloud. Spot Instances are available at up to a 90% discount compared to ondemand prices. For example, using spot helps the Salesforce save up to 40 percent over Amazon EC2 Reserved Instance pricing and up to 80 percent over on-demand pricing. Spot is a great use case for batch when time to insight is less critical.

 In the following example, we have modeled a transient Amazon EMR cluster that takes six hours to complete its job.
+  On-Demand Instance: $106.56 per month
+  Spot Instance (estimated at a conservative 70%): $31.96 per month This represents a saving of just over 70%.

## Use Reserved Instances
<a name="use-reserved-instances"></a>

 Amazon EC2 Reserved Instances (RI) provide a significant discount (up to 72%) compared to On-Demand pricing and provide a capacity reservation when used in a specific Availability Zone. This can be useful if some services used in the data lake will be constantly utilized.

 A good example of this can be Amazon OpenSearch Service. In this scenario we’ll model a 10 node Amazon OpenSearch Service cluster (3 master \+ 7 data) with both on-demand and reserved pricing. In this model, we’ll use c5.4xlarge instances with a total storage capacity of 1 TB.
+  On-demand: $ 7,420.40 per month
+  RI (three years, all up front): $ 3,649.44 per month This represents a saving of just over 50%.

## Choose the right tool for the job
<a name="choose-the-right-tool-for-the-job"></a>

 There are many different ways to interact with AWS services. Picking the right tool for the job, helps reduce cost.

 If you are using Kinesis Data Streams and pushing data into it, you can choose between the AWS SDK, the Kinesis Producer Library (KPL), or the Kinesis Agent. Sometimes the option is based on the source of the data and sometimes the developer can choose.

 Using the latest KPL enables you to use a native capability to aggregate multiple messages/events into a single PUT unit (Kinesis record aggregation). Kinesis data streams shards support up to 1000 records per second or 1-MB throughput. Record aggregation by KPL enables customers to combine multiple records into a single Kinesis Data Streams record. This allows customers to improve their per shard throughput.

 For example, if you have a scenario of pushing 100,000 messages/sec with 150 bytes in each message into a Kinesis data stream, you can use KPL to aggregate them into 15 Kinesis data stream records. The following is the difference in cost between using (latest version) KPL and not.
+  Without KPL (latest version): $4,787.28 per month
+  With KPL (latest version): $201.60 per month This represents a saving of 95%.

## Use automatic scaling
<a name="use-automatic-scaling"></a>

 Automatic scaling is the ability to spin resources up and down based on the need. Building application elasticity enables you to incur cost only for your fully utilized resources.

 Building EC2 instances using an Auto Scaling group can provide elasticity for Amazon EC2 based services where applicable. Even for serverless services like Kinesis where shards are defined per stream during provisioning, [*AWS Application Auto Scaling*](https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html) provides ability to automatically add or remove shards based on utilization.

 For example, if you are using Kinesis streams to capture user activity for an application hosted in specific Region the streaming information might vary between day and night. During day times, when the user activity is higher you might need more shards compared to night times when the user activity would be very low. Being able to configure [*AWS Application Auto Scaling*](https://aws.amazon.com/blogs/big-data/scaling-amazon-kinesis-data-streams-with-aws-application-auto-scaling/) based on your utilization enables you to optimize your cost for Kinesis.

 Data flowing at rate of 50,000 records/sec with each record having 2 K bytes, will require 96 shards. If the data flow reduces to 1000 records/sec for eight hours during night, it would only need two shards.
+  Without AWS Application Auto Scaling: $1068.72 per month
+  With AWS Application Auto Scaling (downsizing): $725.26 per month

 This represents a saving of 32%.

## Choose serverless services
<a name="choose-serverless-services"></a>

 Serverless services are fully managed services that incur costs only when you use them. By choosing a serverless service, you are eliminating the operational cost of managing the service.

 For example, in scenarios where you want to run a job to process your data once a day, using serverless service incurs a cost only when the job is run. In comparison, using a self-managed service incurs a cost for the provisioned instance that is hosting the service.

 Running a Spark job in AWS Glue to process a CSV file stored in Amazon S3 requires

 10 minutes of 6 DPU’s and cost $0.44. To execute the same job on Amazon EMR, you need at least three m5.xlarge instances (for high availability) running at a rate of $0.240 per hour.
+  Using a serverless service: $13.42 price per month
+  Not using a serverless service: $527.04 price per month This represents a saving of 97%.

 Similar savings are applicable between running Amazon Kinesis vs Amazon MSK and between Amazon Athena vs Amazon EMR.

 For more information on cost optimization in detail, see the [Cost optimization in analytics services](cost-optimization-in-analytics-services.md) section.
