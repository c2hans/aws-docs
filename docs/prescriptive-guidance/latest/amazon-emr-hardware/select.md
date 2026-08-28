---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/select.html
---

# Selecting and deploying an Amazon EMR cluster
<a name="select"></a>

Identify and organize the *node types*. When you define your Amazon EMR cluster, it is important to understand its hardware. How does it work? How is it composed? The answers to these questions include three parts:
+ The type of nodes
+ The function that each node carries
+ The types of Amazon Elastic Compute Cloud (Amazon EC2) instances that are most efficient for each node

Initially, the primary node is in charge of managing the general resources. It runs the main components of the distributed application. For example, it runs the Hadoop Distributed File System (HDFS) NameNode service, tracks the jobs to be done on the cluster, and monitors the health of the system.

In addition, Amazon EMR has core nodes and task nodes. Core nodes are managed by the primary node. Core nodes run task nodes and are in charge of storing data in the HDFS on the cluster. Task nodes are in charge of managing the tasks that come to the cluster. A task node doesn't store data. (Task nodes are not mandatory.)

When you are configuring and deploying your Amazon EMR cluster, an important consideration is the right choice of your Amazon EC2 instances that will represent your cluster nodes. There are several ways to add Amazon EC2 instances to a cluster, depending on whether you use the instance groups configuration or the instance fleets configuration for the cluster. For more information about supported instance types, see the [AWS documentation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-supported-instance-types.html).

The following guidelines apply to most [Amazon EMR clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-considerations.html). You can also review the [cluster configuration best practices](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html).

## Instance selection guidelines
<a name="instance-selection-guidelines"></a>

In general, which instances are preferred for your Amazon EMR implementation depends on the job that you are running. Consider the following questions:
+ Is your job memory intensive?
+ Is your job CPU intensive?
+ Do you need high amounts of storage?
+ Does your job require GPU capacity?

These questions will help you understand the type of instances you need and the actual characteristics that you need. Determine how many jobs you want to process at the same time and how fast you need the jobs to be processed. This is important, because Amazon EMR usage is charged in hourly increments. When you turn on a cluster, you are charged for the entire hour.

You can check the cost of each instance running in different AWS Regions. To compare prices between Regions, you can use the [AWS Pricing Calculator](https://calculator.aws/#/) and change the values based on your location.

## Selecting Amazon EC2 instances
<a name="selecting-ec2-instances"></a>

When you have answered the previous questions, it is time to select the instances based on those requirements. After you understand on your processing job needs, determine the instance type based on the characteristics that you need:
+ If you need general purpose instances, choose **M6g**, **T4g, **or** M5 i**nstances.
+ If you need compute-optimized instances, choose **C6g **or** C5 **instances.
+ If you need memory-optimized instances, choose **R6g, X1, R5, **or **z1d **instances.
+ If you must optimize for storage, choose **I3 i**nstances, which provide high I/O performance.
+ If you need accelerated computing such as GPU, choose **P3, G4, **or **Inf1 **instances. These instance types provide high performance for machine learning and fluid dynamics, among other processes.

Another way to understand the types of instances and their capabilities is to analyze the [default memory](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-task-config.html#emr-hadoop-task-config-m6g) for each instance type. This metric helps you to tune and improve the performance of your MapReduce jobs. For more information, see [Hadoop daemon configuration settings](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-daemons.html).

When you know the type of instances you need, you can plan your cluster capacity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
