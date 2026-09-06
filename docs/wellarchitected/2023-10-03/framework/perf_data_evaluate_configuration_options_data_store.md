---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_data_evaluate_configuration_options_data_store.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF03-BP02 Evaluate available configuration options for data store
<a name="perf_data_evaluate_configuration_options_data_store"></a>

 Understand and evaluate the various features and configuration options available for your data stores to optimize storage space and performance for your workload.

 **Common anti-patterns:**
+  You only use one storage type, such as Amazon EBS, for all workloads.
+  You use provisioned IOPS for all workloads without real-world testing against all storage tiers.
+  You are not aware of the configuration options of your chosen data management solution.
+  You rely solely on increasing instance size without looking at other available configuration options.
+  You are not testing the scaling characteristics of your data store.

 **Benefits of establishing this best practice:** By exploring and experimenting with the data store configurations, you may be able to reduce the cost of infrastructure, improve performance, and lower the effort required to maintain your workloads.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 A workload could have one or more data stores used based on data storage and access requirements. To optimize your performance efficiency and cost, you must evaluate data access patterns to determine the appropriate data store configurations. While you explore data store options, take into consideration various aspects such as the storage options, memory, compute, read replica, consistency requirements, connection pooling, and caching options. Experiment with these various configuration options to improve performance efficiency metrics.

### Implementation steps
<a name="implementation-steps"></a>
+  Understand the current configurations (like instance type, storage size, or database engine version) of your data store.
+  Review AWS documentation and best practices to learn about recommended configuration options that can help improve the performance of your data store. Key data store options to consider are the following:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_data_evaluate_configuration_options_data_store.html)
+  Perform experiments and benchmarking in non-production environment to identify which configuration option can address your workload requirements.
+  Once you have experimented, plan your migration and validate your performance metrics.
+  Use AWS monitoring (like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)) and optimization (like [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/)) tools to continuously optimize your data store using real-world usage pattern.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected)
+  [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
+  [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
+  [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
+  [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
+  [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
+  [Amazon Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
+  [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/)
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected)
+  [Amazon EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
+  [Cloud Databases with AWS ](https://aws.amazon.com/products/databases/?ref=wellarchitected)
+  [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected)
+  [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected)
+  [Amazon Aurora best practices ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected)
+  [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected)
+  [Amazon Athena top 10 performance tips ](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected)
+  [Amazon Redshift Spectrum best practices ](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected)
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html?ref=wellarchitected)

 **Related videos:**
+  [Deep dive on Amazon EBS](https://www.youtube.com/watch?v=wsMWANWNoqQ)
+  [Optimize your storage performance with Amazon S3](https://www.youtube.com/watch?v=54AhwfME6wI)
+ [Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0)
+ [ Amazon Aurora storage demystified: How it all works ](https://www.youtube.com/watch?v=uaQEGLKtw54)
+ [ Amazon DynamoDB deep dive: Advanced design patterns ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:**
+  [Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver)
+  [Amazon EBS CSI Driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver)
+  [Amazon EFS Utilities](https://github.com/aws/efs-utils)
+  [Amazon EBS Autoscale](https://github.com/awslabs/amazon-ebs-autoscale)
+  [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
+  [Amazon DynamoDB Examples](https://github.com/aws-samples/aws-dynamodb-examples)
+  [AWS Database migration samples](https://github.com/aws-samples/aws-database-migration-samples)
+  [Database Modernization Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop)
+  [Working with parameters on your Amazon RDS for Postgress DB](https://github.com/awsdocs/amazon-rds-user-guide/blob/main/doc_source/Appendix.PostgreSQL.CommonDBATasks.Parameters.md)
