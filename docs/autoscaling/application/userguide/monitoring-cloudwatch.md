---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-cloudwatch.html
---

# Monitor usage of scalable resources using CloudWatch
<a name="monitoring-cloudwatch"></a>

With Amazon CloudWatch, you get nearly continuous visibility into your applications across scalable resources. CloudWatch is a monitoring service for AWS resources. You can use CloudWatch to collect and track metrics, set alarms, and automatically react to changes in your AWS resources. You can also create dashboards to monitor the specific metrics or sets of metrics you need.

When you interact with the services that integrate with Application Auto Scaling, they send the metrics shown in the following table to CloudWatch. In CloudWatch, metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace. These metrics can help you monitor resource usage and plan capacity for your applications. If your application's workload is not constant, this indicates that you should consider using auto scaling. For detailed descriptions of these metrics, see the documentation for the metric of interest.

**Topics**
+ [CloudWatch metrics for monitoring resource usage](#metrics-to-monitor)
+ [Predefined metrics for target tracking scaling policies](#predefined-metrics)
+ [Predictive scaling metrics and dimensions](#metrics-predictive-scaling)

## CloudWatch metrics for monitoring resource usage
<a name="metrics-to-monitor"></a>

The following table lists the CloudWatch metrics that are available to support monitoring resource usage. The list is not exhaustive but will give you a good starting point. If you do not see these metrics in the CloudWatch console, make sure that you have completed the set up of the resource. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

| Scalable resource | Namespace | CloudWatch metric | Link to documentation |
| --- | --- | --- | --- |
| WorkSpaces Applications |  |  |  |
| Fleets |  AWS/AppStream | Name: AvailableCapacity<br />Dimension: Fleet | [WorkSpaces Applications metrics](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html) |
| Fleets | AWS/AppStream | Name: CapacityUtilization<br />Dimension: Fleet | [WorkSpaces Applications metrics](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html) |
| Aurora |  |  |  |
| Replicas | AWS/RDS | Name: CPUUtilization<br />Dimensions: DBClusterIdentifier, Role (READER) | [Aurora cluster-level metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) |
| Replicas | AWS/RDS | Name: DatabaseConnections<br />Dimensions: DBClusterIdentifier, Role (READER) | [Aurora cluster-level metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) |
| Amazon Comprehend |  |  |  |
|  Document classification endpoints | AWS/Comprehend | Name: InferenceUtilization<br />Dimension: EndpointArn | [Amazon Comprehend endpoint metrics](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-monitor.html) |
|  Entity recognizer endpoints | AWS/Comprehend | Name: InferenceUtilization<br />Dimension: EndpointArn | [Amazon Comprehend endpoint metrics](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-monitor.html) |
| DynamoDB  |  |  |  |
| Tables and global secondary indexes | AWS/DynamoDB | Name: ProvisionedReadCapacityUnits<br />Dimensions: TableName, GlobalSecondaryIndexName | [DynamoDB metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) |
|  Tables and global secondary indexes | AWS/DynamoDB | Name: ProvisionedWriteCapacityUnits<br />Dimensions: TableName, GlobalSecondaryIndexName | [DynamoDB metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) |
|  Tables and global secondary indexes | AWS/DynamoDB | Name: ConsumedReadCapacityUnits<br />Dimensions: TableName, GlobalSecondaryIndexName | [DynamoDB metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) |
|  Tables and global secondary indexes | AWS/DynamoDB | Name: ConsumedWriteCapacityUnits<br />Dimensions: TableName, GlobalSecondaryIndexName | [DynamoDB metrics](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) |
| Amazon ECS |  |  |  |
| Services | AWS/ECS | Name: CPUUtilization<br />Dimensions: ClusterName, ServiceName | [Amazon ECS metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html) |
| Services | AWS/ECS | Name: MemoryUtilization<br />Dimensions: ClusterName, ServiceName | [Amazon ECS metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html) |
| Services | AWS/ApplicationELB | Name: RequestCountPerTarget<br />Dimension: TargetGroup | [Application Load Balancer metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html) |
| ElastiCache |  |  |  |
| Clusters (replication groups) | AWS/ElastiCache | Name: DatabaseMemoryUsageCountedForEvictPercentage<br />Dimension: ReplicationGroupId | [ElastiCache Valkey and Redis OSS metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Redis.html) |
| Clusters (replication groups) | AWS/ElastiCache | Name: DatabaseCapacityUsageCountedForEvictPercentage<br />Dimension: ReplicationGroupId | [ElastiCache Valkey and Redis OSS metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Redis.html) |
| Clusters (replication groups) | AWS/ElastiCache | Name: EngineCPUUtilization<br />Dimensions: ReplicationGroupId, Role (Primary) | [ElastiCache Valkey and Redis OSS metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Redis.html) |
| Clusters (replication groups) | AWS/ElastiCache | Name: EngineCPUUtilization<br />Dimensions: ReplicationGroupId, Role (Replica) | [ElastiCache Valkey and Redis OSS metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Redis.html) |
| Clusters (cache) | AWS/ElastiCache | Name: EngineCPUUtilization<br />Dimensions: CacheClusterId, Node | [ElastiCache Memcached metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Memcached.html) |
| Clusters (cache) | AWS/ElastiCache | Name: DatabaseCapacityMemoryUsagePercentage<br />Dimensions: CacheClusterId | [ElastiCache Memcached metrics](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.Memcached.html) |
| Amazon EMR |  |  |  |
| Clusters | AWS/ElasticMapReduce | Name: YARNMemoryAvailablePercentage<br />Dimension: ClusterId | [Amazon EMR metrics](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.html) |
| Amazon Keyspaces  |  |  |  |
| Tables | AWS/Cassandra | Name: ProvisionedReadCapacityUnits<br />Dimensions: Keyspace, TableName | [Amazon Keyspaces metrics](https://docs.aws.amazon.com/keyspaces/latest/devguide/metrics-dimensions.html) |
| Tables | AWS/Cassandra | Name: ProvisionedWriteCapacityUnits<br />Dimensions: Keyspace, TableName | [Amazon Keyspaces metrics](https://docs.aws.amazon.com/keyspaces/latest/devguide/metrics-dimensions.html) |
| Tables | AWS/Cassandra | Name: ConsumedReadCapacityUnits<br />Dimensions: Keyspace, TableName | [Amazon Keyspaces metrics](https://docs.aws.amazon.com/keyspaces/latest/devguide/metrics-dimensions.html) |
| Tables | AWS/Cassandra | Name: ConsumedWriteCapacityUnits<br />Dimensions: Keyspace, TableName | [Amazon Keyspaces metrics](https://docs.aws.amazon.com/keyspaces/latest/devguide/metrics-dimensions.html) |
| Lambda |  |  |  |
|  Provisioned concurrency | AWS/Lambda | Name: ProvisionedConcurrencyUtilization<br />Dimensions: FunctionName, Resource | [Lambda function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html) |
| Amazon MSK  |  |  |  |
| Broker storage | AWS/Kafka | Name: KafkaDataLogsDiskUsed<br />Dimensions: Cluster Name | [Amazon MSK metrics](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html) |
| Broker storage | AWS/Kafka | Name: KafkaDataLogsDiskUsed<br />Dimensions: Cluster Name, Broker ID | [Amazon MSK metrics](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html) |
| Neptune |  |  |  |
| Clusters | AWS/Neptune | Name: CPUUtilization<br />Dimensions: DBClusterIdentifier, Role (READER) | [Neptune metrics](https://docs.aws.amazon.com/neptune/latest/userguide/cw-metrics.html) |
| SageMaker AI  |  |  |  |
| Endpoint variants | AWS/SageMaker  | Name: InvocationsPerInstance<br />Dimensions: EndpointName, VariantName | [Invocation metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html) |
| Inference components | AWS/SageMaker  | Name: InvocationsPerCopy<br />Dimensions: InferenceComponentName | [Invocation metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html) |
| Provisioned concurrency for a serverless endpoint | AWS/SageMaker  | Name: ServerlessProvisionedConcurrencyUtilization<br />Dimensions: EndpointName, VariantName | [Serverless endpoint metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-monitoring.html) |
| Spot Fleet (Amazon EC2) |  |  |  |
| Spot Fleets | AWS/EC2Spot | Name: CPUUtilization<br />Dimension: FleetRequestId | [Spot Fleet metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-cloudwatch-metrics.html) |
| Spot Fleets | AWS/EC2Spot | Name: NetworkIn<br />Dimension: FleetRequestId | [Spot Fleet metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-cloudwatch-metrics.html) |
| Spot Fleets | AWS/EC2Spot | Name: NetworkOut<br />Dimension: FleetRequestId | [Spot Fleet metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-cloudwatch-metrics.html) |
| Spot Fleets | AWS/ApplicationELB | Name: RequestCountPerTarget<br />Dimension: TargetGroup | [Application Load Balancer metrics](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html) |

## Predefined metrics for target tracking scaling policies
<a name="predefined-metrics"></a>

The following table lists the predefined metric types from the [Application Auto Scaling API Reference](https://docs.aws.amazon.com/autoscaling/application/APIReference/) with their corresponding CloudWatch metric name. Each predefined metric represents an aggregation of the values of the underlying CloudWatch metric. The result is the average resource usage over a one-minute period, based on a percentage unless otherwise noted. The predefined metrics are only used within the context of setting up target tracking scaling policies.

You can find more information about these metrics in the service's documentation that's available from the table in [CloudWatch metrics for monitoring resource usage](#metrics-to-monitor).

| Predefined metric type | CloudWatch metric name |
| --- | --- |
| WorkSpaces Applications |  |
| AppStreamAverageCapacityUtilization | CapacityUtilization |
| Aurora |  |
| RDSReaderAverageCPUUtilization | CPUUtilization |
| RDSReaderAverageDatabaseConnections | DatabaseConnections¹ |
| Amazon Comprehend |  |
| ComprehendInferenceUtilization | InferenceUtilization |
| DynamoDB |  |
| DynamoDBReadCapacityUtilization | ProvisionedReadCapacityUnits, ConsumedReadCapacityUnits² |
| DynamoDBWriteCapacityUtilization | ProvisionedWriteCapacityUnits, ConsumedWriteCapacityUnits² |
| Amazon ECS |  |
| ECSServiceAverageCPUUtilization | CPUUtilization |
| ECSServiceAverageMemoryUtilization | MemoryUtilization |
| ECSServiceAverageCPUUtilizationHighResolution | CPUUtilization |
| ECSServiceAverageMemoryUtilizationHighResolution | MemoryUtilization |
| ALBRequestCountPerTarget | RequestCountPerTarget¹ |
| ElastiCache |  |
| ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage | DatabaseMemoryUsageCountedForEvictPercentage |
|  ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage  | DatabaseCapacityUsageCountedForEvictPercentage |
| ElastiCachePrimaryEngineCPUUtilization | EngineCPUUtilization |
| ElastiCacheReplicaEngineCPUUtilization | EngineCPUUtilization |
| ElastiCacheEngineCPUUtilization | EngineCPUUtilization |
|  ElastiCacheDatabaseMemoryUsagePercentage  | DatabaseMemoryUsagePercentage |
| Amazon Keyspaces |  |
| CassandraReadCapacityUtilization | ProvisionedReadCapacityUnits, ConsumedReadCapacityUnits² |
| CassandraWriteCapacityUtilization | ProvisionedWriteCapacityUnits, ConsumedWriteCapacityUnits² |
| Lambda |  |
| LambdaProvisionedConcurrencyUtilization | ProvisionedConcurrencyUtilization |
| Amazon MSK |  |
| KafkaBrokerStorageUtilization | KafkaDataLogsDiskUsed |
| Neptune |  |
| NeptuneReaderAverageCPUUtilization | CPUUtilization |
| SageMaker AI |  |
| SageMakerVariantInvocationsPerInstance | InvocationsPerInstance¹ |
| SageMakerInferenceComponentInvocationsPerCopy | InvocationsPerCopy¹ |
| SageMakerVariantProvisionedConcurrencyUtilization | ServerlessProvisionedConcurrencyUtilization |
| SageMakerInferenceComponentConcurrentRequestsPerCopyHighResolution | ConcurrentRequestsPerCopy |
| SageMakerVariantConcurrentRequestsPerModelHighResolution | ConcurrentRequestsPerModel |
| Spot Fleet |  |
| EC2SpotFleetRequestAverageCPUUtilization | CPUUtilization³ |
| EC2SpotFleetRequestAverageNetworkIn³ | NetworkIn¹ ³ |
| EC2SpotFleetRequestAverageNetworkOut³ | NetworkOut¹ ³ |
| ALBRequestCountPerTarget | RequestCountPerTarget¹ |

¹ Metric is based on a count instead of a percentage.

² For DynamoDB and Amazon Keyspaces, the predefined metrics are an aggregation of two CloudWatch metrics to support scaling based on provisioned throughput consumption.

³ For best scaling performance, Amazon EC2 detailed monitoring should be used.

## Predictive scaling metrics and dimensions
<a name="metrics-predictive-scaling"></a>

The `AWS/ApplicationAutoScaling` namespace includes the following metrics for predictive scaling policies. These metrics are available with a resolution of one hour and can help you evaluate forecast accuracy by comparing forecasted values with actual values.

| Metric | Description | Dimensions |
| --- | --- | --- |
|  PredictiveScalingLoadForecast  | The amount of load that's anticipated to be generated by your application.<br />The `Average`, `Minimum`, and `Maximum` statistics are useful, but the `Sum` statistic is not. <br />**Reporting criteria**: Reported after the initial forecast is created. |  ResourceId, ServiceNamespace, PolicyName, ScalableDimension, PairIndex  |
| PredictiveScalingCapacityForecast | The anticipated amount of capacity needed to meet application demand. This is based on the load forecast and target utilization level at which you want to maintain your Application Auto Scaling resources.<br />The `Average`, `Minimum`, and `Maximum` statistics are useful, but the `Sum` statistic is not.<br />**Reporting criteria**: Reported after the initial forecast is created. |  ResourceId, ServiceNamespace, PolicyName, ScalableDimension  |
| PredictiveScalingMetricPairCorrelation | The correlation between the scaling metric and the per-instance average of the load metric. Predictive scaling assumes high correlation. Therefore, if you observe low value for this metric, it's better not to use a metric pair.<br />The `Average`, `Minimum`, and `Maximum` statistics are useful, but the `Sum` statistic is not.<br />**Reporting criteria**: Reported after the initial forecast is created. |  ResourceId, ServiceNamespace, PolicyName, ScalableDimension, PairIndex  |
