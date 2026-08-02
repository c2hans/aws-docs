---
source_url: https://docs.aws.amazon.com/whitepapers/latest/containers-on-aws/containers-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Containers on AWS
<a name="containers-on-aws"></a>

Publication date: **March 8, 2024** ([Document history](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper provides guidance and options for running containers on AWS. Containers provide a way to develop, ship, and run applications in an isolated environment. AWS is a natural complement to containers and offers a wide range of scalable orchestration and infrastructure services, upon which containers can be deployed. This paper provides information about container orchestration and compute options such as AWS App Runner, Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and AWS Fargate and key considerations for container workloads on AWS.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

## Introduction
<a name="introduction"></a>

 Before containers were an option, developers and administrators faced challenges with compatibility restrictions. You would build applications specifically for their pre-determined environments. When a workload needed to be migrated (for example, from bare metal to a virtual machine (VM), from a VM to the cloud, or between service providers), you had to rebuild the application or the workload entirely to ensure compatibility with the new environment. Container technology was invented to overcome these incompatibilities by providing a common interface. With the release of Docker, the interest in containers technology rapidly increased.

 Container technology uses the resource-isolation features of the Linux kernel to sandbox an application, its dependencies, configuration files, and interfaces inside an atomic unit called a container. This allows a container to run on any host with the suitable kernel components, while shielding the application from behavioral inconsistencies through variances in software installed on the host. Containers use operating system (OS) level virtualization compared to VMs, which use hardware level virtualization using hypervisor. A hypervisor is a software or a firmware that creates and runs VMs. Multiple containers can run on a single host OS without needing a hypervisor, while isolated from neighboring containers. This layer of isolation allows consistency, flexibility, and portability, which enable rapid software deployment and testing. There are many ways in which using containers on AWS can benefit your organization. Containers have been widely employed in use cases such as distributed applications, batch jobs, and continuous deployment pipelines. The use cases for containers continue to grow in areas like distributed data processing, streaming media delivery, genomics, and machine learning, including generative AI.
