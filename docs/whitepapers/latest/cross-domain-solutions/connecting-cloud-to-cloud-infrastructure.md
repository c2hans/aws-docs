---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/connecting-cloud-to-cloud-infrastructure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connecting Cloud-to-Cloud Infrastructure
<a name="connecting-cloud-to-cloud-infrastructure"></a>

 AWS provides service offerings to help you transfer information from one AWS Cloud Region to another. Many of the services AWS offers are common for on-premises as well as in the cloud. The following sections describe some of the key services that AWS offers, including:
+  Amazon Virtual Private Cloud (Amazon VPC)
+  Amazon Elastic Compute Cloud (Amazon EC2)
+  Amazon Simple Storage Service (Amazon S3)
+  AWS Diode
**Note**
 As of paper publication in December 2020, AWS Diode has the sole purpose of directly supporting the US Government, in that it controls data flowing to AWS classified regions. Commercial entities can use the service, to supply the US Government with their data or services. Commercial entities cannot use the service in any other way. For information about how to determine current availability, see [AWS Diode](#aws-diode).

## Amazon VPC
<a name="amazon-vpc"></a>

 [Amazon VPC](https://aws.amazon.com/vpc/) lets you provision a logically isolated section of your AWS environment so that you can launch resources in a virtual network you define. You have complete control over your virtual networking environment, including the selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. The network configuration for a VPC is easily customized using multiple layers of security, including security groups and network access control lists (ACLs). The security layers control access to Amazon EC2 instances in each subnet. Additionally, you can create a hardware virtual private network (VPN) connection between your corporate data center and your VPC, and leverage AWS as an extension of your corporate data center.

## Amazon EC2
<a name="amazon-ec2"></a>

 [Amazon EC2](https://aws.amazon.com/ec2/) is a web service that provides secure, resizable compute capacity in the cloud. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment.

## Amazon S3
<a name="amazon-s3"></a>

 [Amazon S3](https://aws.amazon.com/s3/) provides cost-effective object storage for a wide variety of use cases, including cloud applications, content distribution, backup and archiving, disaster recovery, and big data analytics. Customers can use Amazon S3 to store and protect objects in transit by using SSL or client-side encryption. Data at rest in Amazon S3 can be protected by using server-side encryption (you request Amazon S3 to encrypt your object before saving it on disks in its data centers, and decrypt it when you download the objects) and/or using client-side encryption (you encrypt data client-side and then upload the data to Amazon S3). Using client-side encryption, you manage the encryption process, the encryption keys, and related tools.

## AWS Diode
<a name="aws-diode"></a>

 AWS Diode is a cloud-based CDS service that provides scalable and reliable delivery of data from one cloud security domain to another. It provides you with complete control of your transfer options, including an API, and runs as a service within Amazon’s proven infrastructure. The service runs completely within the AWS infrastructure but is accessible from on-premises services using Amazon S3 as the storage location for the data being transferred. The AWS Diode service workflows follow the ICD-503 Risk Management Framework (RMF). This results in an approved System Security Plan (SSP) and successful Joint Test Team (JTT) assessment using the NIST 800-53rev4 controls. This significantly eases the onboarding to AWS Diode service.

 For more information on AWS Diode, reach out to your account Solutions Architect or Enterprise support member. You can also email the diode team at *awsdiode@amazon.com*.

**Note**
 As of paper publication in December 2020, AWS Diode has the sole purpose of directly supporting the US Government, in that it controls data flowing to AWS classified regions. Commercial entities can use the service, to supply the US Government with their data or services. Commercial entities cannot use the service in any other way.
