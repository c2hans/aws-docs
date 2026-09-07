---
source_url: https://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/o-ran-use-cases.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# O-RAN use cases
<a name="o-ran-use-cases"></a>

## MEC-RAN integration for low-latency use case
<a name="mec-ran-integration-for-low-latency-use-case"></a>

 As described in the *[5G Network Evolution on AWS](https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf?did=wp_card&trk=wp_card)* whitepaper, AWS compute and edge services such as EKS, EC2, Outposts, and Local Zone can provide a hosting environment for a Multi-Edge Computing (MEC) platform and application, When the CU is collocated with an UPF and MEC platform and application at the edge site, this configuration can provide a local breakout of user traffic at a distributed edge site that is closer to the mobile user, which can result in a low-latency service access such as [Ultra-Reliable Low Latency](https://rcrwireless.com/20190107/5g/what-is-urllc) (URLLC).

 This configuration allows user traffic to be consumed locally at the edge site without pumping traffics to the backhaul network, which is efficiently applicable to high-bandwidth services with regard to saving the cost of backhaul network. In addition, if you collocate a CU, UPF, and MEC together, on the same network functions virtualization infrastructure (NFVI) layer such as AWS Outposts, it can help for the MEC platform and application to use a network quality status for the Radio Network Information Service (RNIS) through the [API exchange within the platform](https://www.etsi.org/images/files/ETSIWhitePapers/etsi_wp23_MEC_and_CRAN_ed1_FINAL.pdf).

 Co-hosting of CU and UPF-like network functions (NFs) and MEC applications on the AWS brings the benefit of a single pane of glass for the orchestration for all network and service applications.

![A diagram depicting MEC and O-RAN collocation on the AWS.](https://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/mec-and-o-ran.png)

## RIC-CU/DU operation to optimize radio resources (traffic steering and QoE optimization)
<a name="ric-cudu-operation-to-optimize-radio-resources-traffic-steering-and-qoe-optimization"></a>

 An O-RAN architecture on AWS enables ISVs (and DSPs) to dynamically interact with the radio resources, allowing them to dictate how compute and network resources are allocated to steer traffic, improve QoS, and control Quality of Experience (QoE).

 As discussed earlier, the separation of RU/DU/CU provides an opportunity to steer traffic from RUs to a pool of DUs, steer control traffic from a DU to a pool of CUs, and steer traffic from RAN to a pool of 5GC resources, such as from DU to a pool of UPFs.

 AWS helps you achieve traffic steering, as defined in 3GPP TR 23.793. By using a Telco data lake on AWS, operators can feed telemetry, infrastructure, and application data from their access networks (5G and 4G), from UE environments (such as Wi-Fi, 5G private networks, and so on) to predict when it becomes beneficial to offload PDU sessions from the 5G radio network to an underlying 4G network, or to a Wi-Fi network.

 [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides RF engineers, DSPs/ISVs data scientists, and DSPs/ISVs developers with the ability to build ML radio applications and models to provide the instructions to UEs, DUs, and CUs with the steering mechanisms that are advantageous for a given user. As discussed earlier, these mechanisms work with the near RT-RIC to address traffic steering use cases.

AWS enables you easily use data from a multitude of sources when combined into a [data lake](https://aws.amazon.com/free/analytics/). This is particularly useful for QoE optimization, where solely using RAN resources doesn’t provide you with the user context. By combining data across the spectrum of available data such as BSS and OSS, QoE optimization algorithms are more accurate because of that data enrichment. With the simplification that [AWS Lake Formation](https://aws.amazon.com/lake-formation/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) brings to your data lake management and the ease of use of [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), RF engineers can build QoE models that are rich and accurate.

## Network slicing, and service level specifications (SLS) fulfillment
<a name="network-slicing-and-service-level-specifications-sls-fulfillment"></a>

 The idea of network slicing is to create virtualized logical networks over a physical network which consists of RANs, core networks, and transport networks. This virtual network overlaying allows the end customers, including business companies, to have an isolated and tailored network connectivity for their own business purpose.

 For example, a customer can establish a network enabling low latency and ultra-reliability communications for a critical Internet of Things (IoT) use case. Another example would be the networks of connected cars. The concept of connected cars has been introduced with in-car entertainment, assisted or fully automated driving, and maintenance data gathering. On the 5G network, car manufacturers could create a virtual network with the required service level specifications to accommodate millions of connected cars.

 Network slicing on the 3GPP network components like RAN has been standardized in terms of interface and functionality. In addition, one important component is needed to manage and orchestrate network slicing across RAN and core network. This management and orchestration entity oversees the operator's entire network, and creates or deletes a slice based on the customers' demands. The management and orchestration are responsible for allocating network resources and managing the life cycle of network slices.

 The network slicing management and orchestration can be implemented on the AWS Cloud, as shown in the following figure. By using AWS services such as Amazon EKS (for CNF management), Amazon RDS (for data management), AWS Lambda, CodePipeline (for lifecycle and resource management), and AWS CloudFormation (for infrastructure management), the network slice manager can create a slice by allocating and configuring network resources through the AWS programmable infrastructure and well-defined APIs.

 All the created slices and allocated resources can be monitored by the network slicing manager, which provides full visibility to the operator via a graphical view. In addition, AWS provides APIs to allocate resources on AWS Outposts, which are placed in the operator's own data centers or corporate edge sites so that the network slicing manager can control the on-premises resources. The following figure shows the 5G network architecture and the AWS services for network slicing.

![A diagram depicting network slicing manager architecture on AWS.](https://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/images/network-slicing.png)

 All management operations are performed via AWS APIs, which enables network operators to have no dependency on specific resource mapping across a wide range of network domains. The consistent infrastructure APIs further allows the development of new services such as AI-powered monitoring and service assurance, by using AWS services such as Amazon SageMaker AI.

## DevOps, CI/CD, and network management (a single pane of glass)
<a name="devops-cicd-and-network-management-a-single-pane-of-glass"></a>

 As described in the *[5G Network Evolution on AWS](https://d1.awsstatic.com/whitepapers/5g-network-evolution-with-aws.pdf)* whitepaper, as 5G networks are increasing in complexity in terms of their heterogeneous network environment as well as microservice-based architecture, CNF lifecycle management should be fully automated to maximize the efficiency of operation in scale and minimize the cost. In case of a CSP, the network would be built out of multiple instances of CNF microservices, supplied from various RAN vendors as binary Docker images. These images regularly undergo updates from individual vendors to release new features, and need to be deployed as updates into the network environment.

 Multiple CD pipelines are deployed per individual vendor, that are kicked-off with the upload of updated Docker images or configuration (such as helm charts and YAML files). Each respective pipeline runs through various stages for vetting the updates by deploying it first on test environments for unit testing, later in the staging environment for system-level integration testing, and finally in production using [blue/green](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html), [canary-based](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html) deployments. [AWS CodePipeline](https://aws.amazon.com/codepipeline/) is used in the source stage of the pipeline with [AWS CodeCommit](https://aws.amazon.com/codecommit/) as a configuration repository and Amazon ECR for container registry, whereas in the test and deployment stages, [AWS CodeBuild](https://aws.amazon.com/codebuild/) is commonly used.

 From an RIC perspective, it is important to manage each characteristic of underlying network resources such as CPU, hardware accelerators (such as [FPGA](https://en.wikipedia.org/wiki/Field-programmable_gate_array), [GPU](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html), [ASIC](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit)), throughput, latency, jitter, and so on to optimize performance with deploying NFs on the appropriate NFVI. To achieve the closed loop automation and flexible deployment, tight integration of [AWS CI/CD pipeline](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/) and [DevOps tools](https://aws.amazon.com/devops/) with RIC and SMO is required.
