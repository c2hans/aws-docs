---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/introduction.html
---

# Containerizing and migrating Java applications using AWS App2Container
<a name="introduction"></a>

*Durga Prasad Cheepuri, RAJA KOPPURAVURI, Dhananjay Karanjkar, Atul Langote, Varun Sharma, and Saurabh Singh, Amazon Web Services*

Containerizing applications on Amazon Web Services (AWS) is a way to modernize Java applications, providing portability between platforms, efficient resource utilization, scalability, agility, and faster delivery of enhancements. Containerizing applications also, reduces operational overhead and infrastructure costs, increases development and deployment agility, and standardizes build and deployment operations across the organization.

AWS App2Container (A2C) is a command line tool to help lift and shift applications running in on-premises data centers or on virtual machines. Applications can then run in containers that are managed by [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) (Amazon ECS), [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) (Amazon EKS), or [AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html).

App2Container can identify and create an inventory for application servers running ASP.NET (Windows) and Java applications (Linux) that are candidates for containerization. You can use App2Container to generate container images for one or more applications running on Windows or Linux servers that are compatible with the Open Containers Initiative (OCI), including commercial off-the-shelf applications (COTs). App2Container does not need the source code of the application to containerize it.

This guide focuses on the aspects that an organization should consider when choosing containerization as an approach and using AWS App2Container to modernize Java applications. This guide can help technical teams to identify the types of applications that make good candidates for containerization for quicker modernization. It also covers prerequisites to take care before containerization and different ways to use App2Container to accommodate any hardware, software, or network restrictions for using the tool on the application server.

## Targeted business outcomes
<a name="business-outcomes"></a>

Using AWS App2Container to modernize Java applications and run them as containers hosted on Amazon ECS, Amazon EKS, or Amazon AppRunner provides the following useful business outcomes:
+ It's more efficient and quicker to release enhancements to containerized applications.
+ Using the automatic scaling features provided by the AWS environment on Amazon ECS or Amazon EKS, the application can quickly respond to heavier traffic.
+ Because the containerized application is a standard Docker image, it's portable for any platform that can host a Docker image, making migration to other platforms more efficient.

## Attachments
<a name="attachments-ace2956a-8fd7-4706-9472-ed4af12c70ed"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
