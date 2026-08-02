---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_compute_evaluate_options.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP01 Evaluate the available compute options
<a name="perf_select_compute_evaluate_options"></a>

 Understand how your workload can benefit from the use of different compute options, such as instances, containers and functions.

 **Desired outcome:** By understanding all of the compute options available, you will be aware of the opportunities to increase performance, reduce unnecessary infrastructure costs, and lower the operational effort required to maintain your workload. You can also accelerate your time to market when you deploy new services and features.

 **Common anti-patterns:**
+  In a post-migration workload, using the same compute solution that was being used on premises.
+  Lacking awareness of the cloud compute solutions and how those solutions might improve your compute performance.
+  Oversizing an existing compute solution to meet scaling or performance requirements, when an alternative compute solution would align to your workload characteristics more precisely.

 **Benefits of establishing this best practice:** By identifying the compute requirements and evaluating the available compute solutions, business stakeholders and engineering teams will understand the benefits and limitations of using the selected compute solution. The selected compute solution should fit the workload performance criteria. Key criteria include processing needs, traffic patterns, data access patterns, scaling needs, and latency requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Understand the virtualization, containerization, and management solutions that can benefit your workload and meet your performance requirements. A workload can contain multiple types of compute solutions. Each compute solution has differing characteristics. Based on your workload scale and compute requirements, a compute solution can be selected and configured to meet your needs. The cloud architect should learn the advantages and disadvantages of instances, containers, and functions. The following steps will help you through how to select your compute solution to match your workload characteristics and performance requirements.

|  **Type**  |  **Server**  |  **Containers**  |  **Function**  |
| --- | --- | --- | --- |
|  AWS service  |  Amazon Elastic Compute Cloud (Amazon EC2)  |  Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS)  |  AWS Lambda  |
|  Key Characteristics  |  Has dedicated option for hardware license requirements, Placement Options, and a large selection of different instance families based on compute metrics  |  Easy deployment, consistent environments, runs on top of EC2 instances, Scalable  |  Short runtime (15 minutes or less), maximum memory and CPU are not as high as other services, Managed hardware layer, Scales to millions of concurrent requests  |
|  Common use-cases  |  Lift and shift migrations, monolithic application, hybrid environments, enterprise applications  |  Microservices, hybrid environments,  |  Microservices, event-driven applications  |

 **Implementation steps:**

1.  Select the location of where the compute solution must reside by evaluating [PERF05-BP06 Choose your workload’s location based on network requirements](perf_select_network_location.md). This location will limit the types of compute solution available to you.

1.  Identify the type of compute solution that works with the location requirement and application requirements

   1.  [https://aws.amazon.com/ec2/](https://aws.amazon.com/ec2/) virtual server instances come in a wide variety of different families and sizes. They offer a wide variety of capabilities, including solid state drives (SSDs) and graphics processing units (GPUs). EC2 instances offer the greatest flexibility on instance choice. When you launch an EC2 instance, the instance type that you specify determines the hardware of your instance. Each instance type offers different compute, memory, and storage capabilities. Instance types are grouped in instance families based on these capabilities. Typical use cases include: running enterprise applications, high performance computing (HPC), training and deploying machine learning applications and running cloud native applications.

   1.  [https://aws.amazon.com/ecs/](https://aws.amazon.com/ecs/) is a fully managed container orchestration service that allows you to automatically run and manage containers on a cluster of EC2 instances or serverless instances using AWS Fargate. You can use Amazon ECS with other services such as Amazon Route 53, Secrets Manager, AWS Identity and Access Management (IAM), and Amazon CloudWatch. Amazon ECS is recommended if your application is containerized and your engineering team prefers Docker containers.

   1.  [https://aws.amazon.com/eks/](https://aws.amazon.com/eks/) is a fully managed Kubernetes service. You can choose to run your EKS clusters using AWS Fargate, removing the need to provision and manage servers. Managing Amazon EKS is simplified due to integrations with AWS Services such as Amazon CloudWatch, Auto Scaling Groups, AWS Identity and Access Management (IAM), and Amazon Virtual Private Cloud (VPC). When using containers, you must use compute metrics to select the optimal type for your workload, similar to how you use compute metrics to select your EC2 or AWS Fargate instance types. Amazon EKS is recommended if your application is containerized and your engineering team prefers Kubernetes over Docker containers.

   1.  You can use [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/) to run code that supports the allowed runtime, memory, and CPU options. Simply upload your code, and AWS Lambda will manage everything required to run and scale that code. You can set up your code to automatically run from other AWS services or call it directly. Lambda is recommended for short running, microservice architectures developed for the cloud.

1.  After you have experimented with your new compute solution, plan your migration and validate your performance metrics. This is a continual process, see [PERF02-BP04 Determine the required configuration by right-sizing](perf_select_compute_right_sizing.md).

 **Level of effort for the implementation plan:** If a workload is moving from one compute solution to another, there could be a *moderate* level of effort involved in refactoring the application.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Compute with AWS ](https://aws.amazon.com/products/compute/?ref=wellarchitected)
+  [EC2 Instance Types ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected)
+  [Processor State Control for Your EC2 Instance ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html?ref=wellarchitected)
+  [EKS Containers: EKS Worker Nodes ](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected)
+  [Amazon ECS Containers: Amazon ECS Container Instances ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration)
+  [Prescriptive Guidance for Containers](https://aws.amazon.com/prescriptive-guidance/?apg-all-cards.sort-by=item.additionalFields.sortText&apg-all-cards.sort-order=desc&awsf.apg-new-filter=*all&awsf.apg-content-type-filter=*all&awsf.apg-code-filter=*all&awsf.apg-category-filter=categories%23containers&awsf.apg-rtype-filter=*all&awsf.apg-isv-filter=*all&awsf.apg-product-filter=*all&awsf.apg-env-filter=*all)
+  [Prescriptive Guidance for Serverless](https://aws.amazon.com/prescriptive-guidance/?apg-all-cards.sort-by=item.additionalFields.sortText&apg-all-cards.sort-order=desc&awsf.apg-new-filter=*all&awsf.apg-content-type-filter=*all&awsf.apg-code-filter=*all&awsf.apg-category-filter=categories%23serverless&awsf.apg-rtype-filter=*all&awsf.apg-isv-filter=*all&awsf.apg-product-filter=*all&awsf.apg-env-filter=*all)

 **Related videos:**
+  [How to choose compute option for startups](https://aws.amazon.com/startups/start-building/how-to-choose-compute-option/)
+  [Optimize performance and cost for your AWS compute (CMP323-R1)](https://www.youtube.com/watch?v=zt6jYJLK8sg)
+  [Amazon EC2 foundations (CMP211-R2) ](https://www.youtube.com/watch?v=kMMybKqC2Y0&ref=wellarchitected)
+  [Powering next-gen Amazon EC2: Deep dive into the Nitro system ](https://www.youtube.com/watch?v=rUY-00yFlE4&ref=wellarchitected)
+  [Deliver high-performance ML inference with AWS Inferentia (CMP324-R1) ](https://www.youtube.com/watch?v=17r1EapAxpk&ref=wellarchitected)
+  [Better, faster, cheaper compute: Cost-optimizing Amazon EC2 (CMP202-R1) ](https://www.youtube.com/watch?v=_dvh4P2FVbw&ref=wellarchitected)

 **Related examples:**
+  [Migrating the web application to containers](https://application-migration-with-aws.workshop.aws/en/container-migration.html)
+  [Run a Serverless Hello World](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/)
