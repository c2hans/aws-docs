---
source_url: https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/cfd-approaches-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# CFD approaches on AWS
<a name="cfd-approaches-on-aws"></a>

 Most CFD solvers have locality of data and use sparse matrix solvers. Once properly organized (application dependent), a well-configured job exhibits good strong and weak scaling on simple AWS cluster architectures. “Structured” and “Unstructured” codes are commonly run on AWS. Spectral and pseudo-spectral methods involve [fast Fourier transforms](https://en.wikipedia.org/wiki/Fast_Fourier_transform) (FFTs), and while less common than traditional CFD algorithms, they also scale well on AWS. Your architectural decisions have tradeoffs, and AWS makes it quick and easy to try different architectures to optimize for cost and performance.

## Architectures
<a name="architectures"></a>

 There are two primary design patterns to consider when choosing an AWS architecture for CFD applications: the *traditional* cluster and the *cloud native* cluster. Customers choose their preferred architecture based on the use case and the CFD users’ needs. For example, use cases that require frequent involvement and monitoring, such as when you need to start and stop the CFD case several times on the way to convergence, often prefer a traditional style cluster.

 Conversely, cases that are easily automated often prefer a cloud native setup, which enables you to easily submit large numbers of cases simultaneously or automate your run for a complete end-to-end solution. Cloud native is useful when cases require special pre- or post-processing steps which benefit from automation. Whether choosing traditional or cloud native architectures, the cloud offers the advantage of elastic scalability — enabling you to only consume and pay for resources when you need them.

### Traditional cluster environments
<a name="traditional-cluster-environments"></a>

 In the cloud, a traditional cluster is also referred to as a *persistent cluster* due to the persistence of minimal AWS infrastructure required for preserving the cluster environment. Examples of persistent infrastructure include a node running a scheduler and hosting data even after a completed run campaign. The persistent cluster mimics a traditional on-premises cluster or supercomputer experience. Clusters include a login instance with a scheduler that allows multiple users to submit jobs. The compute node fleet can be a fixed size or a dynamic group to increase and decrease the number of compute instances depending on the jobs submitted.

 [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html) is an example of a persistent cluster that simplifies the deployment and management of HPC clusters in the AWS Cloud. It enables you to quickly launch and terminate an HPC compute environment in AWS as needed. AWS ParallelCluster orchestrates the creation of the required resources (for example, compute nodes and shared filesystems) and provides an automatic scaling mechanism to adjust the size of the cluster to match the submitted workload. You can use AWS ParallelCluster with a variety of batch schedulers, including [Slurm](https://slurm.schedmd.com/overview.html) and [AWS Batch](https://aws.amazon.com/batch/).

![An example AWS ParallelCluster architecture.](https://docs.aws.amazon.com/whitepapers/latest/computational-fluid-dynamics-on-aws/images/parallelcluster-architecture.png)

 An AWS ParallelCluster architecture enables the following workflow:
+  Creating a desired configuration through a text file
+  Launching a cluster through the AWS ParallelCluster Command Line Utility (CLI)
+  Orchestrating AWS services automatically through [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+  Accessing the cluster through the command line with Secure Shell Protocol (SSH) or graphically with NICE DCV

### Cloud native environments
<a name="cloud-native-environments"></a>

 A cloud native cluster is also called an *ephemeral cluster* due to its relatively short lifetime. A cloud native approach to tightly coupled HPC ties each run, or sweep of runs, to its own cluster. For each case, resources are provisioned and launched, data is placed on the instances, jobs run across multiple instances, and case output is retrieved automatically or sent to Amazon S3. Upon job completion, the infrastructure is ended. Clusters designed this way are ephemeral, treat infrastructure as code, and allow for complete version control of infrastructure changes. Login nodes and job schedulers are less critical and often not used at all with an ephemeral cluster. The following are a few frequently used methods to implement such a design:
+  **Scripted approach** — A common quick-start approach for CFD users getting started with AWS is to combine a custom [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI) with the AWS CLI and a bash script. After launching an Amazon EC2 instance, software can be added to the instance and an AMI is created to be used as the starting point for all compute nodes. It is typical to set up the [SSH](https://en.wikipedia.org/wiki/Secure_Shell_Protocol) files and the [.bashrc](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) file before creating the custom AMI or “golden image.” Although many CFD solvers do not require a shared file location, one can easily be created with an exported network file system (NFS) volume, or with [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/), an AWS managed Lustre file system.
+  **API based** — If preferred, an automated deployment can be developed with one of the [Software Development Kits](https://aws.amazon.com/tools/) (SDKs), such as Python, available for programming an end-to-end solution.
+  **CloudFormation templates** — [AWS CloudFormation](https://aws.amazon.com/cloudformation/) is an AWS Cloud native approach to provisioning AWS resources based on a JSON or YAML template. AWS CloudFormation offers an easily version-controlled cluster provisioning capability.
+  **AWS Batch** — [AWS Batch](https://aws.amazon.com/batch/) is a cloud-native, container-based approach that enables CFD users to efficiently run hundreds of thousands of batch computing jobs in containers on AWS. AWS Batch dynamically provisions the optimal quantity and type of compute resources (for example, compute or memory-optimized instances) based on the volume and specific resource requirements of the batch jobs submitted.

   With AWS Batch, there is no need to install and manage batch computing software or server infrastructure that you use to run your jobs — enabling you to focus on analyzing results and solving problems. AWS Batch plans, schedules, and runs your batch computing workloads across the full range of AWS compute services and features, such as Amazon EC2 and [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html). AWS Batch can also be used as a job scheduler with [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/).
