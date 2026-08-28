---
source_url: https://docs.aws.amazon.com/whitepapers/latest/unpicking-vendor-lock-in/how-the-aws-cloud-helps-to-eliminate-lock-in.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# How the AWS Cloud helps to eliminate lock-in
<a name="how-the-aws-cloud-helps-to-eliminate-lock-in"></a>

 This section provides examples of AWS features and services that customers can use to keep their data portable and avoid lock-in while keeping switching costs to a minimum.

## Data migration
<a name="data-migration"></a>

 When moving data in or out of the cloud, you need to understand where you are moving your data, the type of data you are moving, and the network resources available— among other considerations. AWS offers a wide variety of services and partner tools to help customers migrate their datasets, whether they are files, databases, machine images, block volumes, or even tape backups.

 The suite of data transfer services created by AWS includes many methods that help you migrate your data more effectively. They are broken into two categories:
+  **[Online data transfer and hybrid cloud storage](https://aws.amazon.com/cloud-data-migration/#optimized)** —These methods make it simple to create a network link to your VPC, transfer data to AWS, or use Amazon S3 for hybrid cloud storage with your existing on- premises applications. These services can help you both lift and shift large datasets once, as well as help you integrate existing process flows like backup and recovery or continuous data streams directly with cloud storage.
+  **[Offline data migration to Amazon S3](https://aws.amazon.com/cloud-data-migration/#friendly)** — One should never underestimate the bandwidth of a semi-truck filled with 100 petabytes of hard drives, or a 100 terabytes suitcase-sized device. These offline data migration services that use shippable, ruggedized devices are ideal for moving large archives, data lakes, or in situations where bandwidth and data volumes cannot pass over your networks within your desired time frame.

 *Table 1 – Some online AWS data transfer options*

|  If you need an online link to AWS Cloud storage services so you can:  |   Consider using:   |
| --- | --- |
|  Privately connect your data center with a network link directly to your VPC in an AWS region  |  [AWS Direct Connect](https://aws.amazon.com/cloud-data-migration/#directconnect)  |
|  Copy or replicate file system data into Amazon S3 or Amazon EFS  |  [AWS DataSync](https://aws.amazon.com/datasync/)  |
|  **Connect existing on-premises applications to cloud storage** +   **for files stored as objects in Amazon S3**  <br />+   **for tape backups**  <br />+   **for block volumes**   |  [AWS Storage Gateway](https://aws.amazon.com/storagegateway/), [File Gateway](https://aws.amazon.com/storagegateway/file/) <br /> [Tape Gateway](https://aws.amazon.com/storagegateway/vtl/), [Volume Gateway](https://aws.amazon.com/storagegateway/volume/) <br /> (or) <br /> [Partner Products](https://aws.amazon.com/backup-recovery/partner-solutions/)  |
|  Migrate databases to AWS quickly and securely, with minimal downtime  |  [AWS Database Migration Service](https://aws.amazon.com/dms/)  |
|  Migrate running machine images into Amazon EC2 with their data  |  [CloudEndure](https://www.cloudendure.com/)  |
|  Read and write data to Amazon S3 over long geographic distances  |  [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/faqs/#Amazon_S3_Transfer_Acceleration)  |
|  Collect and ingest multiple streaming data sources  |  [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/)  |
|  Push backups or archives to the cloud with minimal disruption  |  [Technology Partnerships](https://aws.amazon.com/cloud-data-migration/#partnerships)  |

* Table 2 - Some offline AWS data transfer options *

|  If you need an offline way to move data in large batches so you can:  |   Consider using:   |
| --- | --- |
|  Physically transport petabytes of data in batches to the cloud  |  [*AWS Snowball Edge*](https://aws.amazon.com/cloud-data-migration/#snowball)  |
|  Physically transport petabytes of data in an appliance with on-board storage and compute capabilities  |  [*AWS Snowball Edge Edge*](https://aws.amazon.com/cloud-data-migration/#snowballedge)  |
|  Migrate tens of petabytes to exabytes of data in batches to the cloud  |  [*AWS Snowmobile*](https://aws.amazon.com/cloud-data-migration/#snowmobile)  |

## Containers
<a name="containers"></a>

 Containers isolate code from the IT environment it’s stored in, making it more portable and less disruptive to your existing environment when it’s removed. This improvement in portability reduces the switching costs of moving your application to another CSP.

 AWS works closely with the open-source community, contributes to hundreds of open-source projects, and builds services that are compatible with open source tools. You can use AWS to run sophisticated open -source software for containers such as Docker, Kubernetes, Mesos, Swarm, Envoy, Linkerd, and Prometheus.

 In the Kubernetes community, AWS is an active contributor, leading SIG-AWS and helping to maintain projects that make it easier to run Kuberentes on AWS, such as [etcd](https://github.com/etcd-io/etcd/), [Kubernetes CSI](https://github.com/kubernetes-csi), [AWS IAM authenticator](https://github.com/kubernetes-sigs/aws-iam-authenticator), [CNI plugin](https://github.com/containernetworking/cni), and [External DNS](https://github.com/kubernetes-incubator/external-dns).

 AWS offers the widest range of services for storing, managing, and running containers which enable customers to choose the right AWS service for their workload, from small experiments to critical production applications.

* Table 3 - Some AWS container options *

|  If you want to...  |  Consider using:  |  Reason:  |
| --- | --- | --- |
|  Store, encrypt, and manage container images  |  [Amazon ECR](https://aws.amazon.com/ecr/)  |  ECR compresses and encrypts your container images, making them fast to start and available to run anywhere.  |
|  Run containerized applications or build microservices  |  [Amazon ECS](https://aws.amazon.com/ecs/)  |  ECS eliminates the need for you to install and operate your own container orchestration software, or manage and scale a cluster of virtual machines.  |
|  Manage containers with Kubernetes  |  [Amazon EKS](https://aws.amazon.com/eks/)  |  EKS provisions and manages a conformant, upstream Kubernetes control plane and is integrated with many AWS services to provide scalability and security for your applications.  |
|  Run containers without managing servers  |  [AWS Fargate](https://aws.amazon.com/fargate/)  |  Fargate scales and manages the infrastructure required to run your containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.  |
|  Run containers with server-level control  |  [Amazon EC2](https://aws.amazon.com/ec2/)  |  EC2 virtual machines give you control of your server clusters and provide a broad range of customization options.  |

## VMWare on AWS
<a name="vmware-on-aws"></a>

 [VMware on AWS](https://aws.amazon.com/vmware/) is a native, fully managed VMware environment on the AWS Cloud that can be accessed on an hourly, on-demand basis or by subscription. It includes the same core VMware technologies that customers run in their data centers today including [vSphere Hypervisor](http://www.vmware.com/products/esxi-and-esx.html) (ESXi), [Virtual SAN](https://www.vmware.com/products/cloud-infrastructure/vsan) (vSAN), and the [NSX network virtualization platform](http://www.vmware.com/products/nsx.html) to allow them to continue to leverage investments in VMware without continuing to buy and maintain hardware.

 VMware Cloud on AWS runs directly on the physical hardware to avoid nested virtualization, while still taking advantage of a host of network and hardware features designed to support our security-first design model. Also, the entire roster of AWS compute, storage, database, analytics, mobile, and IoT services can be directly accessed from your applications.

 VMware on AWS can be consumed either on-demand, or over a multi-year subscription, depending on the customer’s choice. This ensures that any contractual commitments made by the customer are a conscious choice for the benefit of the customer, rather than an unavoidable switching cost.

## DevOps tools to maximize code portability
<a name="devops-tools-to-maximize-code-portability"></a>

 AWS provides a set of flexible services designed to enable organizations to more rapidly and reliably build and deliver products using AWS and DevOps practices. These services simplify provisioning and managing infrastructure, deploying application code, automating software release processes, and monitoring your application and infrastructure performance.

 These tools help build, deploy, and manage services in a decoupled way that makes them easy to move if necessary.

* Table 4 - Some AWS DevOps tools to maximize code portability *

|  If you want to:  |  Consider using:  |  Because:  |
| --- | --- | --- |
|  Run and manage web apps  |  [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)  |  AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.  |
|  Automate deployment  |  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)  |  AWS CodeDeploy automates code deployments to any instance, including Amazon EC2 instances and on-premises servers. AWS CodeDeploy makes it easier for you to rapidly release new features, helps you avoid downtime during application deployment, and handles the complexity of updating your applications.  |

|   **If you want to:**   |   **Consider using:**   |   **Because:**   |
| --- | --- | --- |
|  Unify CI/CD projects  |  [AWS CodeStar](https://aws.amazon.com/codestar/)  |  AWS CodeStar enables you to quickly develop, build, and deploy applications on AWS. AWS CodeStar provides a unified user interface, enabling you to easily manage your software development activities in one place. With AWS CodeStar, you can set up your entire continuous delivery toolchain in minutes, allowing you to start releasing code faster.  |
|  Use Chef for configuration management  |  [AWS OpsWorks](https://aws.amazon.com/opsworks/)  |  AWS OpsWorks is a configuration management service that uses Chef, an automation platform that treats server configurations as code. OpsWorks uses Chef to automate how servers are configured, deployed, and managed across your Amazon Elastic Compute Cloud (Amazon EC2) instances or on- premises compute environments. OpsWorks has two offerings, AWS Opsworks for Chef Automate, and AWS OpsWorks Stacks.  |
|  Configuration management  |  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  AWS Systems Manager is a management service that helps you automatically collect software inventory, apply OS patches, create system images, and configure Windows and Linux operating systems. These capabilities help you define and track system configurations, prevent drift, and maintain software compliance of your EC2 and on-premises configurations.  |
|  Private Git hosting  |  [AWS CodeCommit](https://aws.amazon.com/codecommit/)  |  AWS CodeCommit is a fully-managed [source control](https://aws.amazon.com/devops/source-control/) service that makes it easy for companies to host secure and highly scalable private Git repositories. You can use CodeCommit to securely store anything from source code to binaries, and it works seamlessly with your existing Git tools.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
