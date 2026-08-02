---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/cluster-lifecycle.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cluster lifecycle
<a name="cluster-lifecycle"></a>

 AWS offers a variety of unique ways to design architectures that deploy HPC workloads. Your choice of deployment method for a particular workload depends on a number of factors, including your desired user experience, degree of automation, experience with AWS, preferred scripting languages, size and number of cases, and the lifecycle of your data. The [High Performance Computing Lens](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/welcome.html) whitepaper covers additional best practices for architectures beyond what is discussed in this paper.

 While the architecture for a cluster is typically unique and tailored for the workload, all HPC clusters benefit from lifecycle planning and management of the cluster and the data produced — allowing for optimized performance, reliability, and cost.

 It is not unusual for an on-premises cluster to run for many years, perhaps without significant operating system (OS) update or modification, until the hardware is obsolete thus rendering it useless. In contrast, AWS regularly releases new services and updates to improve performance and lower costs. The easiest way to take advantage of new AWS capabilities, such as new instances, is by maintaining the cluster as a script or template. AWS refers to this as “Infrastructure as Code” because it allows for the creation of clusters quickly, provides repeatable automation, and maintains reliable version control.

 Examples of “cluster as code” are the [AWS ParallelCluster configuration file](https://docs.aws.amazon.com/parallelcluster/latest/ug/configuration.html), deployment scripts, or [CloudFormation templates](https://aws.amazon.com/cloudformation/resources/templates/). These text-based configurations are easy to modify for a new capability or workload.

 A view of the cluster lifecycle includes infrastructure as code that starts before the cluster is deployed with the maintenance of the deployment scripts. Elements of a cluster maintained as code include:
+  Base AMI to build your cluster
+  Automated software installation scripts
+  Configuration files, such as scheduler configs, MPI configurations, and .bashrc
+  Text description of the infrastructure, such as a CloudFormation template, or an AWS ParallelCluster configuration file
+  Script to initiate cluster deployment and subsequent software installation

 While the nature of a cluster changes depending on the type of workload, the most cost-effective clusters are those that are deployed only when they are actively being used.

 The cluster lifecycle can have a significant impact on costs. For example, it is common with many traditional on-premises clusters to maintain a large storage volume. This is not necessary in the cloud because data can be easily moved to S3 where it is reliably and cheaply stored. Maintaining a cluster as code allows you to place a cluster under version control and repeatedly deploy replicas if needed.

 Each cluster maintained as code can be instantiated multiple times if multiple clusters are required for testing, onboarding new users, or running a large number of cases in parallel. If set up correctly, you avoid idle infrastructure when jobs are not running.
