---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/cost-optimization-in-analytics-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost optimization in analytics services
<a name="cost-optimization-in-analytics-services"></a>

## Streaming
<a name="cost-optimiaztion-in-streaming-services"></a>

### Kinesis Data Streams
<a name="kinesis-data-streams"></a>

 The fundamental unit of scaling for Kinesis Data Streams is a shard. A Kinesis data stream consists of several shards, and each shard provides a specific data ingestion and delivery rate (1 MB/s write and 2 MB/s reads). Each Kinesis data stream (on-demand mode) gets a default capacity of 4 MB/s (4000 records/s) for writes and can burst up to 200 MB/s (200K records/s).

 On-demand mode is suitable for unpredictable traffic. In on-demand mode, Kinesis automatically manages the number of shards needed to provide the required throughput. For example, a data stream in on-demand mode observes peak write throughput for the last 30 days and automatically provisions capacity for double that rate. If a new peak is observed, capacity is adjusted to reflect that peak. As a result, aggregate read throughput for the whole stream increases proportionally to write throughput. Please note that if the traffic increases more than double the previous peak within 15 minutes, write throttling can occur. Requests that are throttled require a retry mechanism.

 Provisioned mode is suitable for predictable traffic volumes that are easy to forecast. In provisioned capacity mode, customers must provide an appropriate number of shards needed for the application. However, the number of shards can be dynamically modified using [UpdateShardCount](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateShardCount.html) API. Please be aware of these [limitations](https://aws.amazon.com/blogs/big-data/scaling-amazon-kinesis-data-streams-with-aws-application-auto-scaling/#:~:text=However%2C%20Kinesis%20Data%20Streams%20have,shard%20count%20for%20a%20stream) while configuring AWS Auto Scaling for Kinesis Data Streams.

#### How to optimize?
<a name="how-to-optimize-data-streams"></a>
+  Monitor your total number of records or data ingested per stream and adjust the number of shards. One shard can process up to 1000 records per second, so monitoring the data ingestion rate will give you the exact number of shards needed. Any unused/idle shard still incurs costs, so identifying and merging those shards is recommended.
+  Use provisioned capacity mode for predictable workloads. Provisioned capacity mode is more cost-effective than the on-demand mode. For a given uniform data ingestion rate, the on-demand mode can be many times more expensive than provisioned mode. However, the provisioned capacity mode has added overhead of monitoring and scaling shards as demands change. [AWS auto-scaling](https://aws.amazon.com/blogs/big-data/scaling-amazon-kinesis-data-streams-with-aws-application-auto-scaling/) can be used to automate Kinesis shard scaling for provisioned mode. Please note that Kinesis on-demand mode has autoscaling built-in.
+  For spiky workloads during a specific time of the day, consider switching capacity modes to on-demand during spikes and provisioned capacity modes during consistent hours. Please note that switching modes are limited to twice per 24-hour period.
+  Avoid hot or cold shards and evenly spread the load across all shards using appropriate partition keys. [Enhanced shard-level monitoring](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/enable-enhanced-monitoring.html) would give you visibility into the incoming traffic. You can then merge any cold shards or split hot shards to ensure every shard is working to its max capacity. On-demand mode automatically does this for customers by merging cold shards or splitting hot shards.
+  Avoid enhanced fan-out if possible. For example, an enhanced fan out gives dedicated 2 MB/Sec throughput per shard, it also costs a minimum of $8.43 per shard per day (@$0.05/GB in US-East-1 or US-West-2). However, enhanced fan-out is recommended for applications with many consumers for a single data stream with varying read rates. Otherwise, consider MSK as an option for many enhanced fan-out subscribers.
+  Use [Kinesis record aggregation](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-concepts.html#kinesis-kpl-concepts-aggretation) to pump more data with a 1000 records/sec/shard limit. This can offer a significant cost advantage, especially if you have many small files (<1 KB).
+  Kinesis data stream charges for data storage longer than 24 hours. While retaining data for up to 365 days is possible, KDS is not meant for long-term data storage. Without any business or regulatory requirement, data retention policies should be minimized per the application needs.

### Firehose
<a name="kinesis-data-firehose"></a>

 Kinesis Firehose and Data Analytics are serverless and fully managed services, so you don't have to worry about scaling. However, you must pay attention to the quotas(limits) for [Firehose](https://docs.aws.amazon.com/firehose/latest/dev/limits.html) and [Data Analytics](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html). Please also note that increasing the Firehose quota significantly more than your actual utilization can increase costs for the destination services. For example, Firehose will deliver data in smaller batches to the destination, which would impact API costs to your downstream destination, such as S3.

 For Apache Flink applications, you can use the application autoscaling. For autoscaling based on custom metrics, you can use the [custom autoscaling policy](https://aws.amazon.com/blogs/big-data/enhanced-monitoring-and-automatic-scaling-for-apache-flink/) of Amazon CloudWatch.

#### How to optimize?
<a name="how-to-optimize-firehose"></a>

Firehose
+  Kinesis data ingestion is billed with 5 KB increments. Therefore, please use PutRecordBatch API or aggregatedRecordSizeBytes (if you use the Kinesis agent) to keep the record size =< 5 KB.
+  Since you are billed for S3 request costs, minimize those requests by increasing the buffer (typically, the buffer should be greater than the amount of data you ingest into the delivery stream in 10 seconds). The Max buffer size is 128 MB.
+  Similar to buffer size, increase buffer interval as much as possible (depending on real-time or near real-time requirements). The Max buffer interval is 15 minutes.
+  Compress incoming data into [Parquet](https://parquet.apache.org/) or [ORC](https://orc.apache.org/) before delivering to the destination to save on storage costs. The default algorithm is SNAPPY, which prioritizes decompression speed rather than compression ratio,

Managed Service for Apache Flink
+  For Managed Service for Apache Flink, KPU usage can vary significantly based on data volume, velocity, and complexity. Test your applications with a production-like load to calculate KPU requirements.
+  While simple stateless applications can deliver 100s of MB/sec/KPU throughput, with complex machine learning algorithms, the throughput can be much less (to the tune of <1MB/sec/KPU). Consider this complexity variable while estimating cost – testing each application for cost is the most accurate way.
+  Consider your need for running analytics on streaming, real-time data. If real-time is not a must-have requirement, using Kinesis Streams with S3 and Athena would be a lower-cost alternative.
+  If you use Data Analytics for machine learning purposes such as anomaly detection, experiment with different values for numberofTrees, shinglesize, etc. More precise computation increases the cost (in terms of KPU), and at some point, that return on investment flattens out. Suppose real-time anomaly detection is not required; you can also use OpenSearch (near real-time), Quicksight, or Sagemaker for Anomaly detection, all of which use [RCF](https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html), a Sagemaker algorithm for anomalous data points.

### Amazon Managed Streaming for Apache Kafka (Amazon MSK)
<a name="amazon-managed-kafka-service-msk"></a>

 Amazon MSK provisioned has two options to expand cluster storage in response to increased usage – automatic and manual scaling. Increased usage may occur due to increased throughput from producers and data retention requirements. The size or family of brokers is adjusted to the MSK cluster's compute capacity based on changes in workloads without interrupting cluster I/O. Amazon MSK Serverless is an option for applications with intermittent or unpredictable workloads. Vertical scaling can be increased or decreased, but this will not work if the number of partitions per broker exceeds the maximum number specified for the new instance size.
+  **[Automatic Scaling](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand.html):** Amazon MSK can automatically scale using an auto-scaling policy where the target disk utilization and maximum scaling capacity are set. It is important to note that a storage scaling action can occur only once every six hours. Verify if the region you are using MSK supports automatic scaling in the [Automatic Scaling documentation](https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand.html). Manual scaling can be used if the chosen region is not listed.
+  **[Manual Scaling](https://docs.aws.amazon.com/msk/latest/developerguide/manually-expand-storage.html):** Amazon MSK can scale up broker storage via the Console or CLI. It is important to note that storage scaling has a cool-down period of at least six hours between events. Even though the operation makes additional storage available immediately, the service performs optimizations on your cluster that can take up to 24 hours or more. The duration of these optimizations is proportional to your storage size.
+  **[MSK Serverless](https://docs.aws.amazon.com/msk/latest/developerguide/serverless.html):** The Serverless is an option for Amazon MSK's cluster type, where it automatically provisions and scales capacity without thinking about right-sizing or scaling. Consider using a serverless cluster if your applications need the on-demand streaming capacity that scales up and down automatically. However, serverless performance is directly affected by the number of partitions, so partitions must be created accordingly to match the number of producers and consumers.

#### How to optimize?
<a name="how-to-optimize-msk"></a>

##### Right size broker instances
<a name="right-size-broker-instances"></a>

 To choose the right size and number of active broker instances and storage used, work backward to determine the use-case's throughput, availability, durability, and latency requirements. Begin with an initial sizing of the cluster based on throughput, storage, and durability requirements. Next, scale horizontally or use provisioned throughput to increase the write throughput of the cluster. Finally, scale vertically to increase the number of consumers that can consume from the cluster or to facilitate in-transit in-cluster encryption. It's also important to consider the disaster recovery strategy required and if the clusters should reside in 2 or 3 availability zones.

 It's vital to understand that the number of brokers cannot be decreased after the cluster is created. When designing for high availability, determine how many availability zones the brokers need. With Amazon MSK, you can only scale in units that match your number of deployed AZs - if you deploy with 3 AZs, you can only scale up by three brokers at a time

 Choose the broker type based on the maximum number of partitions required. If the number of partitions per broker exceeds the maximum value, the following operations will not be allowed on the cluster:
+  Updating the cluster configuration
+  Updating the Apache Kafka version for the cluster
+  Updating the cluster to a smaller broker type

 The kafka.t3.small broker type for Amazon MSK is ideal for getting started with Amazon MSK, looking to test in a development environment, or having low throughput production workloads.

 For guidance on choosing the correct number and type of brokers, see [right-size your cluster](https://docs.aws.amazon.com/console/msk/instancetype-best-practices) in the documentation. In addition, an [MSK Sizing and Pricing](https://dy7oqpxkwhskb.cloudfront.net/MSK_Sizing_Pricing.xlsx) spreadsheet can be used to determine the correct number of brokers and understand the cost breakdown.

##### Optimize storage
<a name="optimize-storage"></a>

 To optimize for storage, consider that the broker storage cannot be decreased, only increased. It is also important to choose the right storage volume type. Amazon MSK does not reduce cluster storage in response to reduced usage and does not support decreasing the size of storage volumes.

 Amazon MSK can be configured to expand your cluster's storage automatically in response to increased usage using Application Auto-Scaling policies. Your auto-scaling policy sets the target disk utilization and the maximum scaling capacity. The alternate method is manual scaling through the console or Command Line Interface (CLI). If it is a hard requirement to reduce the size of the cluster storage, you migrate the existing cluster to a cluster with smaller storage.

 When choosing the storage volume type, consider the required IOPS and throughput for the workload. If necessary, customers can choose to attach multiple volumes to a broker to increase the throughput beyond what can be delivered by a single volume. See [Best practices for right-sizing your Apache Kafka clusters to optimize performance and cost](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/) for more information.

 It is recommended to adjust data retention policies and delete inactive segments of logs. Consuming messages doesn't remove them from the log. To free up disk space regularly, customers can specify a retention period, which dictates how long messages stay in the log. To avoid running out of disk space for messages, create a CloudWatch alarm at a threshold of 80% that watches the KafkaDataLogsDiskUsed metric. When the value of this metric reaches or exceeds 80%, use automatic scaling, reduce the message retention period, and delete new topics.

##### Reduce throttling on underlying infrastructure and increase throughput
<a name="reduce-throttling-on-underlying-infrastructure-and-increase-throughput"></a>

 By default, Amazon MSK exposes three metrics that indicate when this throttling is applied to the underlying infrastructure. These can be used for continuous optimization of your Amazon MSK clusters.
+  **BurstBalance** - Indicates the remaining balance of I/O burst credits for EBS volumes. If this metric starts to drop, consider increasing the size of the EBS volume to increase the volume baseline performance. If [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) isn't reporting this metric for your cluster, your volumes are larger than 5.3 TB and no longer subject to burst credits.
+  **CPUCreditBalance** - Relevant for brokers from the T3 family and indicates the number of available CPU credits. When this metric drops, brokers consume CPU credits to burst beyond their CPU baseline performance. Consider changing the broker type to the M5 family.
+  **TrafficShaping** - A high-level metric indicating the number of packets dropped due to exceeding network allocations. Finer detail is available when the PER\_BROKER [monitoring level is configured](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html) for the cluster. Scale up brokers if this metric is elevated during your typical workloads.

##### Monitor the load and CPU Utilization
<a name="monitor-the-load-and-cpu-utilization"></a>

 Amazon MSK strongly recommends that you maintain the total CPU utilization for your brokers (defined as CPU User \+ CPU System) under 60%. However, suppose the CPU Utilization trends are greater than 60%. In that case, it is recommended to scale up for performance efficiency, but this may increase cost due to the additional broker instance that will be provisioned. Instead, you can use [Amazon CloudWatch metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) to create a composite metric and set an alarm that gets triggered when the composite metric reaches an average CPU utilization of 60%. When this alarm is triggered, there are three options:
+  The recommended approach is to update the broker type to the next larger type (vertical scaling). However, it is essential to note that the brokers will go offline in a rolling fashion and temporarily reassigns partition leadership to other brokers.
+  If there are topics with messages not keyed and ordering is not necessary to consumers, add brokers to expand the cluster and add partitions to existing topics with the highest throughput. This option should be used if the granularity of managing resources and costs is required. In addition, this option should be used if the CPU load is significantly greater than 60%, as it does not result in an increased load on existing brokers.
+  Expand clusters by adding brokers and reassigning existing partitions using the partition reassignment tool (Kafka-reassign-partitions.sh). However, this is not recommended if CPU utilization is >70% because replication causes additional CPU load and network traffic.

## Storage
<a name="storage"></a>

### Amazon Simple Storage Service
<a name="s3"></a>

#### How to optimize
<a name="how-to-optimize-s3"></a>

##### Storage Classes
<a name="storage-classes"></a>

 [S3 storage classes](https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3) – S3 offers a range of storage classes designed for different use cases. Choosing a suitable storage class can help you be more performant and save a lot of costs. Considerations when choosing a storage class
+  **Predictable access patterns** - Datasets such as medical records, media streaming, learning resources, and user-generated content such as photographs are frequently accessed during a specific time and then rarely accessed. For use cases like these, you can plan (lifecycle policies) to move to a lower-cost storage class optimized for infrequent or archive access once the usage of these objects reduce. For predictable workloads, leverage S3 Storage Class Analysis to monitor access patterns across objects and decide when to transition data to the proper storage class to optimize costs.
+  **Unpredictable access patterns** - Datasets such as long tail data, data lakes, and data analytics have unpredictable usage patterns. The access patterns for these use cases are highly variable over the year. They can range from little to no access to data being read multiple times in a month or even a single day, leading to high retrieval charges if stored in infrequent access or archive storage class. Use [S3 intelligent tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) for such workloads.
![A diagram showing how to optimize storage cost and performance for all stages of a data lake workflow.](http://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/images/optimize-storage.png)
+  **Cheaper storage class does not guarantee lower S3 costs** - Along with the storage fee, there is a fee for data retrieval, minimum duration, and API calls for a few storage classes. For example, [Amazon Glacier Instant Retrieval](https://aws.amazon.com/s3/storage-classes/glacier/instant-retrieval/) is the ideal storage class if you access data once per quarter. However, although the storage price is lower than S3 Standard-IA, there is an added cost to access the data. Therefore, there is a break-even point where if you’re storing data that is accessed too frequently, it makes sense to keep that in S3 Standard-IA (cheaper storage and no retrieval fee). In addition, Amazon Glacier Instant Retrieval has a minimum storage duration of 90 days. So, if you upload a file you expect to delete within 90 days, you will be charged a prorated early deletion fee. We recommend you choose the S3 Standard or the S3 Standard-IA storage classes in such cases.

 You should upload directly to [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/) if you know the data is accessed not more than once a quarter.

 Refer to [Amazon cost optimization](https://aws.amazon.com/s3/cost-optimization/) for more details on Amazon S3 cost optmization

##### Amazon S3 lifecycle policies
<a name="s3-lifecycle-policies"></a>

 A [lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) automatically move objects in your bucket from one storage class to another. Regular data cleanup into distinct storage classes is crucial in the big data processing. Data lakes have different data layers like source, raw, process, and business data. Once the data is processed, the source and raw data layers are rarely accessed. As a result, transitioning them to infrequent and archive storage class could save money. You can avoid the manual cleanup process with lifecycle policies to save on costs.

 Create a lifecycle rule to automatically transition your objects to Standard-IA storage class, archive them to Glacier storage class, and remove them after a specified period.

 Lifecycle transition costs are directly proportional to the number of objects transitioned, so reduce the number of objects by aggregating or zipping and compressing them before moving them to archive tiers. Apply life cycle policies to the source, staging, and other data sets that are processed and would no longer be needed.

 Create lifecycle policies to clean up incomplete multipart uploads. Also, you can organize data to make life cycle policies simpler and more effective. For example, keep all source data under one prefix so you can have a single lifecycle policy for all the source data sets rather than one for each source prefix. In addition, use lifecycle policies to delete many objects to avoid S3 API costs. Finally, if your bucket is versioned, ensure there is a rule action for both current and non-current objects to either transition or expire.

##### Type of encryption
<a name="type-of-encryption"></a>

 Choosing appropriate server-side encryption techniques: [S3 encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) helps you protect data against cybercriminals; this is especially important for sensitive data. You can encrypt an object using either Amazon S3-managed keys (SSE-S3), AWS KMS keys stored in AWS Key Management Service (AWS KMS) (SSE-KMS) or using customer-provided keys (SSE-C).

 SSE-KMS is for users who want more control over the encryption keys. Enable [Amazon S3 bucket keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) while using SSE KMS. Bucket Keys decrease the number of transactions from Amazon S3 to AWS KMS, thereby reducing the AWS KMS costs by up to 99 percent. Enabling bucket keys could also help avoid throttling on the KMS limits.

 SSE-S3 is the server-side encryption for Amazon S3. There are no additional fees for using server-side encryption with Amazon S3-managed keys (SSE-S3). Amazon S3 encrypts each object with a unique key and encrypts the key with a key that it rotates regularly.

 With server-side encryption with customer-provided keys (SSE-C), users manage the encryption keys and Amazon S3 manages the encryption, as it writes to disks, and decryption, when you access your objects.

 Client-Side Encryption: You could also choose to encrypt data client-side and upload the encrypted data to S3. In this case, users manage the encryption process, the encryption keys, and related tools.

##### Data transfer out
<a name="data-transfer-out"></a>

 As of today, AWS does not charge for data transfer in, data transferred between S3 buckets and to any AWS service within the same region, and data transfer out to Amazon Cloudfront. Different regions have different data transfer-out costs. Choose your region wisely. If possible, deploy your workloads within the same region to avoid inter-region data transfer fees.

##### Amazon S3 Storage lens
<a name="amazon-s3-storage-lens"></a>

 [Amazon S3 storage lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) is an analytics solution that provides visibility into object storage with point-in-time metrics, trend lines, and actionable recommendations. The Amazon S3 Storage lens will help you discover anomalies and identify cost efficiencies

##### File formats
<a name="file-formats"></a>

 Choose appropriate file formats. The file type, compression strategy, and partitioning you use on S3 will significantly impact performance and cost. Storing data in its raw format takes up a lot of space, is inefficient, and is expensive. Instead, use file formats such as parquet, Avro, and orc to speed up read/writes and compress data, using less storage space. Parquet and ORC are suitable for columnar storage and frequent reads over writes; they also compress better than Avro. On the other hand, Avro is suitable for row-based storage and is faster for frequent writes than reads.

##### Batch operations
<a name="batch-operations"></a>

 S3 Batch operations is a managed service that lets you manage billions of objects at scale. You can change object metadata and properties, copy or replicate objects between buckets, replacing object tag sets, modify access controls and restore archived objects from the S3 glacier. You need not write code, set up servers (compute charges) or figure out how to partition the loads between servers, worry about S3 throttling and pay no compute charge because AWS will handle all these tasks for you.

## Processing and analytics
<a name="processing-and-analytics"></a>

### Amazon EMR
<a name="amazon-emr"></a>

 There are four deployment options for Amazon EMR:
+  [Amazon EMR on Amazon EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan.html)
+  [Amazon EMR on Amazon EKS](https://aws.amazon.com/emr/features/eks/)
+  [EMR Outposts](https://aws.amazon.com/emr/features/outposts/?nc=sn&loc=3&dn=7)
+  [EMR Serverless](https://aws.amazon.com/emr/serverless/)

 Amazon EMR on Amazon EC2 we scale by the cluster. You can define an Amazon EMR cluster with the number of nodes supporting the capacity needed for your workload. To right-size your Amazon EMR cluster, refer to the [Cluster configuration and guidelines best practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html). You can start with a smaller number of core nodes and increase/decrease the number of task nodes to meet your workload requirements. You can also use the Amazon EMR Managed Scaling or custom autoscaling policies on Amazon EMR. You can specify the minimum and the maximum number of nodes and let Amazon EMR adjust the number of nodes it needs as it optimizes cost and performance.

 Amazon EMR on Amazon EKS scales by the job corresponding to the number of vCPU and Memory allocation.

 You can create and run Amazon EMR clusters on AWS Outposts. Amazon EMR on AWS Outposts is ideal for low latency workloads running close to on-premises data and applications. Scaling could be challenging due to the limited availability of Amazon EC2 on Outpost. S3 is the only supported option for Amazon EMR on Outposts. S3 on Outposts is not supported for Amazon EMR on AWS Outposts. EMR on outpost could get expensive since spot instances are not available.

 Amazon EMR Serverless is a serverless managed service. You need not worry about scaling. Serverless can be cost-effective for cases where you have unpredictable workloads.

#### How to optimize
<a name="how-to-optimize-emr"></a>

 This whitepaper primarily focuses on optimization techniques for Amazon EMR on Amazon EC2 and Amazon EMR on EKS. The following are the considerations.

##### EMR on EC2
<a name="emr-on-ec2"></a>

##### Type of infrastructure matching your workload
<a name="type-of-infrastructure-matching-your-workload"></a>

 Choose Amazon EC2 if you know your job profile. If you plan to create a multi-tenant environment where multiple teams and software versions are required to run your applications, use Amazon EKS. If your workload is adhoc or you are unsure of what infrastructure capacity it needs, use Amazon EMR Serverless. AWS Outpost if you need to deploy in a low latency hybrid environment or if you have any restrictions requiring Amazon EMR to run in your own data center.

##### Spot instances
<a name="spot-instances"></a>

 In an Amazon EMR cluster, you have the master, core, and task nodes. The Master and Core nodes are necessary for any job processing; therefore, you either need to run this on-demand, with different purchase options and cost savings, which we will discuss later. Spot instances allow you to use unused EC2 capacity at a discounted price. Still, they have the possibility of being interrupted after a two-minute of notice when Amazon EC2 needs to reclaim its capacity back. The Task node is an ideal candidate for spot instances as it reduces the cost of failure since this node does not have the data. However, when a spot instance terminates, Amazon EMR has to reallocate nodes. Since the core nodes have HDFS, Amazon EMR needs significant rework on Hadoop replication.

 The Amazon EMR Amazon EC2 cluster has an [Instance Fleet](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html) configuration, allowing you to use various spot instances in provisioning EC2. For example, if you use an [Allocation strategy for instance fleets](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html#emr-instance-fleet-allocation-strategy) and create a cluster using the AWS CLI or the Amazon EMR API, you can specify up to 30 Amazon EC2 instance types per instance fleet. In the allocation strategy, you can have two options on how Spot instances will be allocated. First is the spot pool, which checks which Availability Zone has the largest capacity for spot instances. Second is the on-demand, where it checks for the lowest price.

##### Reserved instances and Savings Plan
<a name="reserved-instances-and-savings-plan"></a>

Depending on the workload, RIs for OnDemand instances can be a reasonable cost-saving strategy. As of today, you cannot purchase RIs for a few hours a day, so you need to plan to use RIs for 24 hours a day for x days for maximum benefits. You can re-purpose the instances for other workloads when you finish running your Amazon EMR workloads. There is a break-even point in switching to RI. If you use your cluster at least 70% of the time, that is the break-even point. And the number can change on the type of instance.

Savings Plans is a flexible pricing model offering lower prices than On-Demand pricing in exchange for a specific usage commitment (measured in $/hour) for one or three years. AWS offers three types of Savings Plans – Compute Savings Plans, Amazon EC2 Instance Savings Plans, and Amazon SageMaker AI Savings Plans. Compute Savings Plans apply to usage across Amazon EC2, AWS Lambda, and AWS Fargate. The Amazon EC2 Instance Savings Plans apply to Amazon EC2 usage, and Amazon SageMaker AI Savings Plans apply to Amazon SageMaker AI usage. Use Cost explorer to sign up for a 1- or 3-year Savings Plan and manage your plans by taking advantage of recommendations, performance reporting, and budget alerts.

##### Considerations for using Graviton
<a name="considerations-for-using-graviton"></a>

 Amazon EMR now supports Graviton instance types. On Graviton2 instances, Amazon EMR runtime for Apache Spark provides an additional cost savings of up to 30% and improved performance of up to 15% relative to equivalent previous generation instances. Additionally, for Apache Spark, TPC-DS3 TB benchmark queries run up to 32 times faster using Amazon EMR runtime. Refer to the [supported instance types](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-supported-instance-types.html).

##### Storage using EMFRS
<a name="storage-using-emfrs"></a>

 Choose wisely between HDFS and [EMRFS](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html), and both have their benefits. While EMRFS provides scalability, durability, and persistent storage, performance might take a hit due to higher latency in Ec2/S3 and back. HDFS offers better performance. It's best used for caching the results produced by intermediate job-flow steps.

 Use the latest releases of EBS Volumes. The latest volumes usually provide better IOPS and offer more price performance compared to previous releases.

##### Amazon S3 data transfer charges
<a name="amazon-s3-data-transfer-charges"></a>

 Avoid Amazon S3 cross-region data transfer charges by creating the same region's Amazon EMR clusters and S3 buckets.

##### Job optimization
<a name="job-optimization"></a>

 Configure jobs for multiple checkpoints and rerun from the last successful checkpoint. This reduces the cost of the duration of the rerun, thereby reducing the cost of failure;

##### Monitoring and right-sizing
<a name="monitoring-and-right-sizing"></a>

 Choosing the right type and then the proper sizing of Amazon EC2 is critical. First, you must understand your workload's characteristics. Is your job memory intensive or CPU intensive? What are your storage needs? You then can choose from a variety of instances offered by AWS. Each Amazon EC2 instance type has a specific purpose and price, C for compute-optimized, R for memory-optimized, and M/T for general purpose.

 Amazon EMR provides several tools you can use to gather information about your cluster. You can access information about the cluster from the console, the CLI, or programmatically. The standard Hadoop web interfaces and log files are available on the master node. You can choose to archive the application and cluster logs on Amazon S3. You can also use monitoring services such as CloudWatch and Ganglia to track the performance of your cluster. [Application history](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cluster-application-history.html) is available from the console using the "persistent" application UIs for Spark History, persistent YARN timeline server, and Tez user interfaces. These services are hosted off-cluster, so you can access application history for 30 days after the cluster terminates.

##### Elasticity
<a name="elasticity"></a>

 You can automatically or manually adjust the number of Amazon EC2 instances available to an Amazon EMR cluster in response to workloads with varying demands. To use automatic scaling, you have two options. [EMR Managed scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-scaling.html) or [custom automatic scaling policy](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html). Each scaling has one type of application (spark, hive, or YARN). The metric you choose to monitor and the rate of scale in and out are vital factors in choosing one over the other.

##### Terminating unused clusters
<a name="terminating-unused-clusters"></a>

 You can now specify the number of idle hours and minutes, after which the cluster can [auto-terminate](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-auto-termination-policy.html). The default idle time is one hour. Enable termination protection to ensure Amazon EC2 instances are not shut down by an accident or error. In addition, termination protection is beneficial if your cluster might have data stored on local disks that you need to recover before the instances are terminated.

##### EMR on EKS
<a name="emr-on-eks"></a>

 You can leverage Amazon EMR on Amazon EKS as a deployment option to run Apache Spark applications on Amazon EKS cost-effectively. EMR on Amazon EKS can provide up to 61% lower costs and up to 68% performance improvement for spark workloads. It includes multiple performance optimization features, such as Adaptive Query Execution (AQE), dynamic partition pruning, flattening scalar subqueries, bloom filter join, and [more](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-performance.html).

 You could use Spot instances and Arm-based Graviton E2 instances to optimize costs further. Leverage [graceful executor decommissioning](https://issues.apache.org/jira/browse/SPARK-20624) feature that makes Amazon EMR on Amazon EKS workloads more robust by enabling Spark to anticipate Spot Instance interruptions. Amazon EMR on Amazon EKS can further reduce job costs via critical stability and performance improvements without recomputing or rerun impacted Spark jobs.

 Finally, you can use familiar command line tools such as kubectl to interact with a job processing environment and observe Spark jobs in real-time, reducing development time.

### AWS Glue
<a name="aws-glue"></a>

 The main factors that influence the cost for AWS Glue are:

#### Number and size of jobs
<a name="number-and-size-of-jobs"></a>

 With AWS Glue ETL jobs, you only pay for the time your ETL job takes to run. There are no resources to manage, no upfront costs, and you are not charged for startup or shutdown time. You are charged hourly based on the number of Data Processing Units (DPUs) used to run your ETL job. A single Data Processing Unit (DPU) provides four vCPU and 16 GB of memory. AWS bills for jobs and development endpoints in increments of 1 second, rounded up to the nearest second. Depending on the type of job that you are running, Glue may require a minimum number of DPUs to be provisioned and used to run the job. For example, Apache Spark and Spark Streaming jobs require a minimum of 2 DPUs. By default, Glue will allocate 10 DPU to each Apache Spark job and 2 DPU to each Spark streaming job. Jobs using AWS Glue version 0.9 or 1.0 have a 10-minute minimum billing duration, while jobs that use Glue versions 2.0 and later have a 1-minute minimum. For Python shell jobs, you can allocate either 0.0625 DPUs or 1 DPU. By default, Glue will allocate 0.0625 DPU, and the jobs have a 1-minute minimum billing duration.

#### AWS Glue Data Catalog
<a name="glue-data-catalog"></a>

 With AWS Glue Data Catalog, you are charged based on the storage of objects and the requests made to the Data Catalog. An AWS AWS Glue Data Catalog object is a table, table version, partition, or database. The first million objects stored are free, and the first million requests per month are free.

#### Glue crawlers
<a name="glue-crawlers"></a>

 For Glue crawlers, there is an hourly rate based on the crawler runtime to discover data and populate the AWS Glue Data Catalog. You are billed in increments of 1 second, rounded up to the nearest second, with a 10-minute minimum duration for each crawl. Use of AWS Glue crawlers is optional, and you can populate the AWS AWS Glue Data Catalog directly through the API.

#### How to optimize?
<a name="how-to-optimize-glue"></a>

##### File sizing and formatting
<a name="file-sizing-and-formatting"></a>

 The first step to optimizing your Glue ETL and crawl jobs is ensuring your source data is formatted correctly. For Spark jobs, it is important that your data set is splittable or can fit into the Spark executor memory. Standard file formats to choose from are Apache Parquet or Apache ORC, as they are splittable and have columnar formats. Additionally, you should ensure high-quality data to avoid Glue crawlers misinterpreting data or having incorrect columns in the data. You can also use [Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) to clean and normalize data. Glue DataBrew is a feature of AWS Glue that can help reduce the time it takes to prepare data and make intelligent suggestions to help fix data quality issues. It is important to note that Glue DataBrew can incur [costs](https://aws.amazon.com/glue/pricing/) based on the number of nodes used to run your Glue DataBrew job. Therefore, having optimally sized and formatted files can reduce the processing time for Glue jobs and consequently reduce the cost of running Glue.

##### Combine small files into larger files
<a name="combine-small-files-into-larger-files"></a>

 It takes longer to crawl a large number of small files than a small number of large files. The reason is the crawler must list each file and read the first megabyte of each new file. However, suppose you know the pattern or schema of the data being crawled, and the data is stored in Amazon S3. In that case, you can combine multiple files by setting the groupFiles and groupSize parameters ([https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html\#aws-glue-programming-etl-connect-s3](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html#aws-glue-programming-etl-connect-s3), https://docs.aws.amazon.com/glue/latest/dg/grouping-input-files.html). By combining smaller files into larger files, you can reduce your crawler's runtime and costs.

##### Glue crawler configurations
<a name="glue-crawler-configurations"></a>

 Enable your Glue crawlers to use incremental crawls so that you crawl only new subsets of data, and your crawler will not extraneously perform data discovery on files that have already been crawled. The incremental crawls will allow for shorter Glue crawls that will reduce cost. Additionally, it would help if you only run your AWS Glue crawlers when you are aware of new schema changes in your dataset; your AWS Glue crawler should not constantly be running.

 Choose specific files or partitions of data to scan by using include paths and exclude patterns. A crawler will start by evaluating the required included path, and for Amazon S3, MongoDB, Amazon DocumentDB, and relational data stores, you must specify an exclude path. Exclude paths will tell the crawler to skip specific files or paths and can reduce the number of files a crawler needs to list. The specific path to scan can make the crawler run faster and reduce cost.

 You can run multiple crawlers simultaneously instead of having one crawler running on the entire data store. AWS Glue version 3.0 or later supports autoscaling for AWS Glue ETL and streaming ETL jobs (excludes Python shell jobs). When crawlers are run in parallel, job runtime can be shortened, which lowers the cost of running Glue jobs.

##### Data partitioning
<a name="data-partitioning"></a>

 Use data partitioning to improve performance on your Glue jobs. By default, DynamicFrames are not partitioned when written. However, DynamicFrames now supports native partitioning using the partitionKeys option. You can also use pushdown predicates to filter on partitions without having to list and read all the files in the dataset. Data partitioning allows you to list and read only what you need into a DynamicFrame, instead of reading the whole dataset and filtering inside the DynamicFrame. These functionalities allow you to restrict and reduce what is read into a DynamicFrame, reducing the total data processing done.

##### Job monitoring and efficient data processing
<a name="job-monitoring-and-efficient-data-processing"></a>

 Monitor your Glue jobs using job metrics in AWS Glue to help you plan for DPU capacity for your Glue jobs and determine the optimal DPU capacity. AWS Glue also has a feature called AWS Glue job run insights that simplifies job debugging and optimization for your Glue jobs. In addition, AWS Glue provides the Spark UI and CloudWatch logs and metrics to monitor your Glue jobs. With Glue job run insights, you get information about your job executions, including the line number where a Glue job script fails, root cause analysis, and recommended actions. For example, the last Spark action executed before a job failure.

 Improve your data processing for large datasets by using Workload partitioning with [Bounded Execution](https://docs.aws.amazon.com/glue/latest/dg/bounded-execution.html) to reduce common errors like inefficient Spark scripts, distributed in-memory execution of large-scale transformations, and dataset abnormalities. Again, this is supported for S3 data sources only.

 [Shuffling](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-shuffle-manager.html) is essential in Spark jobs whenever data is rearranged between partitions. This is because wide transformations like join, groupByKey, reduceByKey, and repartition require information from other partitions to complete processing. Spark will gather the required data from each partition and combine it into a new partition. With Glue 2.0, you can use Amazon S3 to store Spark shuffle and spill data, which will disaggregate compute and storage for your Spark jobs and give complete elasticity and low-cost shuffle storage.

 Use [job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html) to track data that has already been processed in previous runs of an ETL job. Job bookmarks will help AWS Glue maintain state information and prevent reprocessing old data, reducing the amount of data scanned and compute resources utilized, therefore reducing costs.

##### Minimize usage of development endpoints
<a name="minimize-usage-of-development-endpoints"></a>

 [Development endpoints](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoints.html) are environments that can be used to develop and test AWS Glue scripts. These are optional to use and have an additional cost associated with them. Alternatively, you can [develop your jobs locally](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html) to save on endpoint costs.

### Lambda
<a name="lambda"></a>

 The first time you invoke a Lambda function, it creates an instance of the function to process the event. After that, the instance stays active to process additional events after finishing the response. If you invoke the function again before the first event is complete, Lambda initializes another instance, and the function processes the two events concurrently. After that, Lambda creates new instances as needed as more events come in and drop instances if the demand reduces.

 A function’s concurrency is the number of instances that can serve requests at any time. The concurrency varies by region, and you can increase the limit using AWS Service Quota Dashboard. You can find more details in the [Lambda Function Scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html).

#### How to optimize?
<a name="how-to-optimize-lambda"></a>

##### Right-sizing
<a name="right-sizing"></a>
+  Use [Compute Optimizer](https://aws.amazon.com/blogs/compute/optimizing-aws-lambda-cost-and-performance-using-aws-compute-optimizer/) and [Lambda Power tuner](https://github.com/alexcasalboni/aws-lambda-power-tuning) to right-size the functions and memory configurations, especially after new deployments. Compute Optimizer would take days to gather historical data. Lambda Power tuning can be executed right away and will assist in prioritizing cost vs. execution time.
+  Remove unneeded Codes and Libraries to reduce function size. Use [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) to share code and libraries used from multiple functions. This would help reduce memory footprint and, hence, the GB per second cost.
+  There might be some use cases where Lambda is not the most efficient solution. For example, you might want to evaluate some alternatives for long-running jobs, large payload (> 6 MB), or scheduled workloads. One such use case is covered in this [document](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-event-driven-and-scheduled-workloads-at-scale-with-aws-fargate.html). AWS Batch is another alternative for scheduled jobs.

##### Performance efficiency
<a name="performance-efficiency"></a>
+  A 128 MB function that runs for 10 seconds costs more than a 1 GB function that runs for 1 second, so less memory is not always cheaper. A critical aspect of right-sizing is comparing execution duration vs. the cost of increasing memory. Ensure Compute Optimizer has one to two weeks of data before executing the recommendations.
+  Use X-Ray and CodeGuru to identify bottlenecks and expensive Lambda codes. These tools are not free but can provide significant value in reducing costs and identifying bottlenecks. For example, use X-Ray analytics to identify and review subsets of requests with higher latency. [Amazon CodeGuru](https://aws.amazon.com/blogs/machine-learning/optimizing-application-performance-with-amazon-codeguru-profiler/) uses machine learning for automated code review and application performance profiling to identify the most expensive lines of code. It also provides recommendations to improve code quality. Typically, you want to use X-ray in production and CodeGuru in Development environments.
+  Use [CloudWatch Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html) for a deeper understanding of usage and bottlenecks/saturation points, if any. However, shipping custom metrics to CloudWatch using put-metrics needs a synchronous blocking call which adds to the idle wait time. Use Embedded Metric Format ([EMF](https://serverless-observability.workshop.aws/en/030_cloudwatch/async_metrics_emf.html)) for asynchronous calls instead.
+  It is important to maximize the amount of time your application spends processing. To minimize the time it is waiting on other resources, identify areas where one Lambda function is waiting for a response from another lambda or other downstream AWS service. Avoid using Lambda as an orchestrator. Instead, use dedicated orchestration tools like Step functions, which can reduce Lambda execution times waiting for a response from another Lambda function or other AWS services. It would also avoid Lambda idle wait times. Additionally, try to break down a Lambda into smaller functions to reduce I/O waits.
+  Identify Lambda functions as a proxy to AWS SDK calls. You can replicate those functions by direct SDK integrations in the workflow/step functions or API gateway/Eventbridge/AppSync.
+  You can reduce the number of invocations by effectively using [Event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html). Currently, you can use event filtering with [Kinesis](https://aws.amazon.com/kinesis/), [DynamoDB](https://aws.amazon.com/dynamodb/), and [SQS](https://aws.amazon.com/sqs/) event sources. A Lambda function will be executed only when a particular event pattern is matched. This also eliminates the need to use filtering logic in the application code.
+  Watch out for infinite loops between your Lambda function and S3 bucket and avoid this [recursion](https://aws.amazon.com/blogs/compute/avoiding-recursive-invocation-with-amazon-s3-and-aws-lambda/#:~:text=To%20avoid%20recursive%20invocations%20between,in%20the%20same%20source%20bucket) problem, as it can significantly hit your Lambda invocation cost.

#####  Operational efficiency
<a name="operational-efficiency"></a>
+  Whenever possible, use AWS Graviton2 for your functions, which provides [34% better price/performance](https://aws.amazon.com/blogs/aws/aws-lambda-functions-powered-by-aws-graviton2-processor-run-your-functions-on-arm-and-get-up-to-34-better-price-performance/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+AmazonWebServicesBlog+%28Amazon+Web+Services+Blog%29). Popular runtimes such as Node.JS, Python, Ruby, and Java are already supported on the Graviton2 platform. Use Lambda Power tuning to compare costs between x86 and Graviton2. You can upgrade to Graviton2 in place without redeploying (but testing is required).
+  For a consistent pattern of traffic, use Lambda provisioned concurrency. This will help reduce Lambda [cold starts](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/) and avoid burst throttling. Provisioned concurrency can result in \~16% cost savings if fully utilized. Additionally, you can use provisioned concurrency in conjunction with AWS autoscaling to adjust automatically for peaks and troughs.
+  Be aware of log storage costs (in CloudWatch). Use log retention policies for every log group. If you need to retain logs for a long time, move them to S3 and use retention policies.
+  Remove logging that does not add value to investigations to save on CloudWatch data ingestion costs and log storage costs. Turn off debug logs in production. Instead, use structured formats such as JSON. Don’t use CloudWatch for trace data; X-Ray is a better tool.

##### Pricing model
<a name="pricing-model"></a>
+  If you have a consistent monthly usage for your Lambda functions, use Compute Savings Plan for your baseline Lambda usage. Using the Savings plan, customers can save up to 17% (applicable to both on-demand and provisioned concurrency). The best practice is to analyze Lambda usage for a consistent monthly baseline and apply provisioned concurrency and savings plans to that baseline usage.
+  Customers can now take advantage of Lambda’s [tiered pricing](https://aws.amazon.com/blogs/compute/introducing-tiered-pricing-for-aws-lambda/). There is no action needed to avail of this feature. However, please note that this new pricing model is per region and platform (x86 and ARM64). So, consolidating them into one would maximize the savings if customers are running functions using both platforms.

### Amazon Athena
<a name="amazon-athena"></a>

 Athena scales automatically to handle queries, so you do not need to worry about the underlying infrastructure and how it scales. Athena will also automatically execute queries in parallel without worrying about managing or tuning clusters.

 Athena provides connectors for enterprise data sources, including Amazon DynamoDB, Amazon Redshift, Amazon OpenSearch Service, MySQL, PostgreSQL, Redis, and other popular third-party data stores. Athena's data connectors allow you to generate insights from multiple data sources using Athena's easy-to-use SQL syntax without needing to move your data with ETL scripts. In addition, data connectors run as AWS Lambda functions and can be enabled for cross-account access, allowing you to scale SQL queries to hundreds of end-users.

#### How to optimize?
<a name="how-to-optimize-athena"></a>

##### Athena configurations
<a name="athena-configurations"></a>
+  **Use workgroups** - [Workgroups](https://docs.aws.amazon.com/athena/latest/ug/manage-queries-control-costs-with-workgroups.html) can be used to separate users, teams, applications, or workloads to limit the amount of data each query or the entire workgroup can process and help track costs. Resource-level identity-based policies can control access to a specific workgroup and view query-related metrics in Amazon CloudWatch.
+  **Minimize data scans** - Athena does not cache query results, meaning repeated queries will re-scan any data, even if it has been scanned before. Data scans can increase the overall Athena cost as data scanned will directly impact the cost. Avoid running the same query multiple times if the table data hasn't changed.

##### Optimizing storage
<a name="optimizing-storage"></a>
+  **Partitioning data** - Partitioning data will divide your table into parts and keep the related data together based on the columns used for partitioning. Data partitioning can reduce the amount of data scanned per query. When deciding which columns to partition, you should consider which columns may be common filters for queries and how granular your partitions are. Run the EXPLAIN ANALYZE query command to determine if a table is partitioned and use a partitioned column as a filter.
+  **Compressing data** - Compress your data to speed up queries, as long as the files are either an optimal size (generally greater than 128MB) or splittable. Splittable files can be read in parallel by the execution engine in Athena, taking less time when reading a splittable file. Ideal file types include Avro, Parquet, and ORC, as they are splittable regardless of the compression codec. Only files compressed with BZIP2 and LZO codec are splittable for text files.
+  **Optimal file size** - Files should also not be too small as they may add to the overhead of opening S3 files, listing directories, getting object metadata, setting up data transfer, reading file headers, reading compression dictionaries, etc. Amazon S3 and Amazon Athena currently have a limit of 5500 requests per second, so combining smaller files into a larger file is recommended to avoid throttling or excessive scanning.
+  **Partition Projection** - With [partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html), partition values and locations are calculated from configuration rather than read from a repository like AWS AWS Glue Data Catalog. Since in-memory operations tend to be faster than remote operations, partition projects can reduce the runtime of queries against highly partitioned tables. Using partition projection is ideal when your partitions' schemas are the same or if the tables' schema consistently accurately describes the partition's schemas.
+  **Storage lifecycle policies** - The results of Athena queries are stored in S3. Configure [lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) on buckets to reduce storage costs for data that is not used.

##### Performance and Query Tuning
<a name="performance-and-query-tuning"></a>
+  **ORDER BY** - Athena will use distributed sort to run the sort operation in parallel on multiple nodes, so if you use the ORDER BY clause to look at the top or bottom N values, use a LIMIT clause to reduce the cost of the sort and save on query runtime.
+  **GROUP BY** - The GROUP BY operator distributes rows based on the GROUP BY columns to worker nodes, which hold the GROUP BY values in memory. When using the GROUP BY operator, order the columns by the highest cardinality to the lower. You can also reduce the number of columns included in the SELECT clause to reduce the amount of memory required to store if they are unneeded.
+  **JOIN Queries**: Athena will distribute the table on the right to worker nodes and stream the table on the left to join. Therefore, when joining two tables, you should specify the larger table on the left side of the join and the smaller one on the right side. However, suppose you are joining three or more tables. In that case, you can consider joining the largest tables with the smallest ones to reduce the intermediate results and then join the remaining tables.

##### Function efficiency
<a name="function-efficiency"></a>
+  **Minimize the use of window functions** - Window functions are memory intensive and, in general, require an entire dataset to be loaded into a single Athena node for processing. Loading large datasets can risk crashing the node. Instead, consider partitioning the data, filtering the data to run the window function on a subset of the data, or finding an alternative way to construct the query.
+  **Use efficient functions** - Some queries have multiple ways to construct the same query. Use more efficient methods to reduce processing done on the data set. For example, use regular expressions instead of LIKE on large strings, or reduce nested functions.
+  **Use approximate functions** - If you do not require exact numbers, you can use approximate functions to minimize memory usage; [approximate functions](https://prestodb.io/docs/current/functions/aggregate.html) will count unique hashes of values instead of entire strings, with a standard error of 2.3%.
+  **Include only necessary columns** - Limit your final SELECT statements to only include columns that you need to reduce the amount of data that needs to be processed through the entire query run pipeline. Filtering a query is particularly useful when querying large string-based tables that require multiple joins or aggregations.

### Amazon Redshift
<a name="amazon-redshift"></a>

 An Amazon Redshift data warehouse is a collection of computing resources called nodes, which are organized into a group called a cluster. Each cluster runs an Amazon Redshift engine and contains one or more databases. Amazon Redshift scales by the number of clusters and nodes within each cluster.

 With RA3 node types, your compute and storage can scale separately. For example, with previous generation nodes DC2 and DS2, you scale compute and storage depending on the size of your instance. In addition, you can resize your cluster as needed depending on changes to your capacity or performance requirements.

 Concurrency Scaling is a feature of Amazon Redshift that allows you to add cluster capacity to support concurrent users and queries without resizing your cluster.

#### How to optimize?
<a name="how-to-optimize-redshift"></a>

 Additionally, some best practices can help you reduce costs and optimize query performance when running queries on Redshift. Redshift also includes a Redshift Advisor that will provide recommendations and insights into optimizing your workloads. We discuss these recommendations are below: table compression, Workload Management (WLM), and cluster resizing.

##### Choose the right node size
<a name="choosing-the-right-node-size"></a>

 The first step to optimizing your Redshift clusters is choosing the right node type and instance size to meet your requirements. Keep in mind that Redshift can compress your data up to four times. Redshift will provide suggestions for node types when you start using it based on your needs, like CPU, RAM, storage capacity, and availability, but you can quickly scale up or down as needed.

##### Use Redshift AQUA
<a name="use-redshift-aqua"></a>

 Advanced Query Accelerator, or AQUA, is a distributed and hardware-accelerated cache that improves query performance. AQUA is only supported on RA3 node types but is available at no additional charge and with no code changes.

##### Use Reserved nodes when possible
<a name="use-reserved-nodes-when-possible"></a>

 If you have steady-state production workloads, you can choose to run Reserved nodes, which can offer additional cost savings. These savings come with 1-year or 3-year term lengths with the option to pay all upfront, partial upfront, or no upfront.

##### Use the Pause and Resume feature for On-Demand nodes
<a name="use-the-pause-and-resume-feature-for-on-demand-nodes"></a>

 With Redshift on-demand, you pay for what you use based on the storage and compute depending on the node type used to run your cluster. With On-demand clusters, utilize the pause and resume feature when clusters do not need to be running. On-demand billing will be suspended while the cluster is paused, so you will not be charged when the cluster is paused.

##### Table compression, partitions, and columnar format
<a name="table-compression-partitions-and-columnar-format"></a>

 Without data compression, data consume additional storage space and utilize additional disk I/O, which are factors that directly affect your Redshift usage and cost. You can use the ANALYZE COMPRESSION command to get suggestions for compression for your data.

 Store data in columnar formats like Apache Parquet or ORC and leverage partitions to reduce the amount of data scanned when data is stored in Amazon S3 for Amazon Redshift Spectrum, as the amount of data scanned is directly correlated to the cost.

##### Compressing Amazon S3 file objects loaded by the COPY command.
<a name="compressing-amazon-s3-file-objects-loaded-by-the-copy-command"></a>

 The `COPY` command integrates with the massively parallel processing (MPP) architecture of Amazon Redshift. It allows you to read and load data in parallel from Amazon S3, Amazon DynamoDB, and text output. You can apply compression when you create and load brand new tables or use the `COPY` command with COMPUPDATE set to ON to analyze and apply compression automatically.

##### Cluster Resize
<a name="cluster-resize"></a>

 **Elastic Resize**: Elastic Resize lets you quickly add, remove, or change node types from an existing cluster by automating the process of taking a snapshot, creating a new cluster deleting the old cluster, and renaming the new cluster. You can use this process to upgrade to the new RA3 node type from previous generation node types (DC2 or DS2). The process takes about ten to fifteen minutes to complete, and you will not be able to write to the cluster temporarily while the data is transferring to the new cluster. This process automatically redistributes the data to the new nodes.

 **Classic Resize**: Classic Resize is the manual approach to resizing your cluster and is the predecessor of Elastic Resize; Elastic Resize is the recommended option.

##### Amazon Redshift Spectrum
<a name="amazon-redshift-spectrum"></a>

 Amazon Redshift Spectrum allows you to run queries directly against the data you have stored in Amazon S3, and you are charged only for the bytes scanned, rounded up to the next megabyte. You are charged the standard S3 rates for storing objects in your S3 buckets and requests made against your S3 buckets. Additionally, you can implement an “aging-off” process for historical data or less frequently queried data to save costs, as S3 storage is more cost-effective than Redshift’s direct-attached storage. For any hot and frequently accessed data, it is preferable to keep that data in direct-attached storage for performance.

##### Workload management (WLM) and concurrency scaling
<a name="workload-management-wlm-and-concurrency-scaling"></a>

 When you have multiple sessions or users running queries simultaneously, some queries may take longer to run or consume more resources than others and affect the performance of other queries. Workload Management can define multiple query queues and route queries to the appropriate queues at runtime to help handle these situations.

 There are options for Automatic WLM and Manual WLM. Automatic WLM will automatically manage how many queries run concurrently and how much memory is allocated to each dispatched query. In addition, you can specify the priority of workloads or users that map to each queue. With Manual WLM, you configure the specific queues used to manage queries. You can also set up rules to route queries to particular queues based on the user running the query or specified labels.

 Concurrency scaling is cost-effective for spiky workloads where you require additional capacity for short periods instead of provisioning additional persistent nodes in your cluster. To implement concurrency scaling, you can route queries to Concurrency scaling clusters with a workload manager.

##### Trusted Advisor Recommendations
<a name="trusted-advisor-recommendations"></a>

 Trusted Advisor would run checks against your Amazon Redshift resources in your account to notify you about cost optimization opportunities. These include providing recommendations for purchasing Reserved nodes to optimize based on usage and shutting underutilized clusters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
