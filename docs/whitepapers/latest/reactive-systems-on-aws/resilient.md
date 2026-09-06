---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/resilient.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Resilient
<a name="resilient"></a>

****
"Everything fails, all the time."
 - Werner Vogels (CTO, Amazon.com)

According to the [AWS Well-Architected Framework](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.resiliency.en.html), resiliency is “*The ability for a system to recover from a failure induced by load, attacks, and failures*”. Depending on the service used, resiliency is either part of the service offering or has to be designed by the customer, depending on the specific requirements. The following section discusses resiliency for different AWS services and how this can be implemented.

## AWS Global Infrastructure
<a name="global-infra"></a>

 The AWS Global Infrastructure consists of multiple building blocks that provide different levels of independent, redundant components. AWS partitions resources and requests via some dimension. These partitions or *cells* are designed to be independent and in the case of an error, contain faults to within a single cell. For example, Amazon Route53 uses the concept of shuffle sharding to isolate customer requests into cells.

 AWS also offers the fault isolation construct of Availability Zones (AZs). Each AWS Region consists of multiple, isolated, and physically separate AZs within a geographic area. Each AZ is separated by a large physical distance from other zones to avoid correlated failure scenarios. An AZ consists of one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. Despite being geographically separated, Availability Zones are located in the same regional area. This enables customers to use AZs in an active/active or active/standby configuration. Some AWS services are deployed as strictly zonal services. These services are used to independently operate resources (instances, databases, and other infrastructure) within the specific AZ.

 While AWS control planes typically provide the ability to manage resources at a regional level (multiple AZs), certain control planes (including Amazon EC2 and Amazon EBS) have the ability to filter results to a single Availability Zone.

 The most pervasive fault isolation construct is that of the AWS Region. Regions are designed to be autonomous, with dedicated copies of services deployed in each region. Regional AWS services internally use multiple Availability Zones in an active/active configuration to achieve the availability design goals you establish.

## AWS Lambda
<a name="lambda"></a>

 In addition to the benefits of the AWS global infrastructure, AWS Lambda offers several features to help support your data resiliency and backup needs. Lambda runs instances of your function in multiple AZs to ensure that it is available to process events in case of a service interruption in a single zone. If you configure your function to connect to a virtual private cloud (VPC) in your account, specify subnets in multiple AZs to ensure high availability. To make sure that your function can always scale to handle additional requests, you can reserve concurrency for it. Setting reserved concurrency for a function ensures that it can scale to, but not exceed, a specified number of concurrent invocations. This ensures that you don't lose requests due to other functions consuming all of the available concurrency. For asynchronous invocations and a subset of invocations triggered by other services, Lambda automatically retries on error with appropriate delays between retries. Other clients and AWS services that invoke functions synchronously are responsible for performing retries. In addition, you can configure Lambda to send requests to a dead-letter queue if all retries fail for asynchronous invocations. A dead-letter queue is an Amazon Simple Notification Service (Amazon SNS) topic or Amazon Simple Queue Service (Amazon SQS) queue that receives events for troubleshooting or reprocessing. You can use versioning in Lambda to save your function's code and configuration as you develop it. Together with aliases, you can use versioning to perform blue/green and rolling deployments.

## Amazon ECS
<a name="ecs"></a>

 [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) schedulers leverage the same cluster state information provided by the Amazon ECS API to make appropriate placement decisions. A *task placement strategy* is an algorithm for selecting instances for task placement or tasks for termination. A *task placement constraint* is a rule that is considered during task placement. For example, you can use constraints to place tasks based on AZ or instance type. Amazon ECS supports two *launch types* that determine how instances of tasks (containers) are being launched:

 Each task that uses the AWS Fargate launch type has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another task. AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

 When a task that uses the EC2 launch type is launched, Amazon ECS must determine on which EC2 instance in your ECS cluster to place the task based; this decision is based on the requirements specified in the task definition, such as CPU and memory. Similarly, when you scale down the task count, Amazon ECS must determine which tasks to terminate. You can apply task placement strategies and constraints to customize how Amazon ECS places and terminates tasks. Task placement strategies and constraints are not supported for tasks using the Fargate launch type. By default, Fargate tasks are spread across AZs.

## Amazon EKS
<a name="eks"></a>

 [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) runs Kubernetes control plane instances across multiple Availability Zones to ensure high availability. Amazon EKS automatically detects and replaces unhealthy control plane instances, and it provides automated version upgrades and patching for them. This control plane consists of at least two API server nodes and three `etcd` nodes that run across three AZs within a Region. Amazon EKS leverages the architecture of AWS Regions in order to maintain high availability. Because of this, Amazon EKS is able to offer an [SLA for API server endpoint availability](https://aws.amazon.com/eks/sla).

 For the data plane (for example, your worker nodes), you have to create at least a single node group spanning across multiple AZs. You can also start one node group per Availability Zone. The Kubernetes [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) automatically adjusts the number of nodes in your cluster when pods fail to launch due to lack of resources or when nodes in the cluster are underutilized and their pods can be rescheduled onto other nodes in the cluster.

 Amazon EKS integrates Kubernetes with AWS Fargate by using controllers that are built by AWS using the upstream, extensible model provided by Kubernetes. These controllers run as part of the Amazon EKS managed Kubernetes control plane and are responsible for scheduling native Kubernetes pods onto Fargate. The Fargate controllers include a new scheduler that runs alongside the default Kubernetes scheduler in addition to several mutating and validating admission controllers. When you start a pod that meets the criteria for running on Fargate, the Fargate controllers running in the cluster recognize, update, and schedule the pod onto Fargate.

 In addition to self-managed nodes, Amazon EKS offers managed node groups. With Amazon EKS managed node groups, you don’t need to separately provision or register the Amazon EC2 instances that provide compute capacity to run your Kubernetes applications. You can create, automatically update, or terminate nodes for your cluster with a single operation. Nodes run using the latest Amazon EKS optimized AMIs in your AWS account. Node updates and terminations automatically and gracefully drain nodes to ensure that your applications stay available.

## Amazon DynamoDB
<a name="dynamodb"></a>

 DynamoDB is a regional, cell-based service that offers a high degree of resiliency out of the box. The service provides on-demand backup capability. It enables you to store full backups of your tables for long-term retention and archival. Point-in-time recovery helps protect your DynamoDB tables from accidental write or delete operations. With point in time recovery, you don't have to worry about creating, maintaining, or scheduling on-demand backups.

## Amazon ElastiCache
<a name="elasticache"></a>

 Amazon ElastiCache helps mitigate common failure modes that could affect your (external) caching layer and thus the overall system’s responsiveness and resiliency. There are two types of failures you need to plan for, individual cache node failures and broad AZ failures. The best failure mitigation plan will address both kinds of failures.
+  **Minimizing the impact of failures**

   To minimize the impact of a node failure, it’s recommended that your implementation use multiple nodes in each shard and distribute the nodes across multiple AZs. When running Redis, AWS recommends that you enable multi-AZ on your replication group so that ElastiCache will automatically fail over to a replica if the primary node fails.
+ **Minimizing the impact of AZ failures**

  To minimize the impact of an AZ failure, it’s recommended launching your nodes in as many different Availability Zones as are available. Spreading your nodes evenly across AZs will minimize the impact in the unlikely event of an AZ failure.
+ **Other precautions**

   If you're running Redis, then in addition to the previous recommendations, it’s recommended that you schedule regular backups of your cluster. Backups (snapshots) create an `.rdb` file you can use to restore your cluster in case of failure or corruption.

## Amazon Kinesis Data Streams
<a name="kinesis"></a>

 **Amazon Kinesis Data Streams** Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. High availability and durability are achieved by synchronously replicating data to three AZs. Failure can occur at the following levels when you use an Amazon Kinesis Data Streams application to process data from a stream:
+  A record processor could fail
+  A worker could fail, or the instance of the application that instantiated the worker could fail
+  An EC2 instance that is hosting one or more instances of the application could fail

 For more information, refer to [Disaster Recovery in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/disaster-recovery-resiliency.html).
