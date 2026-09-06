---
source_url: https://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/example-architecture-3.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example architecture \#3
<a name="example-architecture-3"></a>

 An example architecture of a 5GC workload on the AWS Region, RAN CU on an [AWS Local Zone](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), and RAN distributed unit (DU) on customer premise.

![5G network architecture showing AWS Region with core functions, Local Zone with RAN vCU, and customer premise with RAN vDU.](http://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/images/architecture-5g-core-ran.png)

 Security description of the example architecture of 5G RAN network function on AWS Local Zones and customer on-premises network:

1.  Assuming 5G core network functions are deployed in the AWS Region, the security-related services and best practices described in the previous 5G Core deployment examples are also applied here.

1.  5G RAN vCU deployment at the AWS Local Zones. Due to the latency requirements of RAN network functions, the centralized unit (CU) functions of RAN need to be placed within tens of milliseconds from the end users. Therefore, [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) are ideal edge locations to host CU function due to their low-latency access to the end users. AWS Local Zones are fully managed by AWS, and includes secure cloud infrastructure providing compute, storage, database and other select AWS services to customers.

1.  5G RAN vDU deployment at customer on-premises network: due to the ultra-low latency requirements (\~100 microsecond) of the RAN DU network functions, they are typically deployed at customer on-premises locations, such as D-RAN cell sites, or C-RAN hubs.

1.  The infrastructure-level connectivity between the AWS Regions and AWS Local Zones uses high-speed and secure AWS backbone networks. At the service level, you can extend a VPC from the parent Region into AWS Local Zones by creating a new subnet and assigning it to the AWS Local Zone.

1.  EBS volumes are encrypted by default using Amazon EBS Encryption for data at rest and data in transition between the Local Zone and its parent Region. By default, Amazon EBS encryption uses AWS KMS and AWS-managed keys. However, customers can specify Customer Managed Keys as the default encryption key.

1.  [AWS Direct Connect](https://aws.amazon.com/directconnect) is recommended to provide a dedicated private network connection between the customer on-premises network and AWS networks. While in transit, your network traffic remains on the AWS global network and never touches the public internet; therefore, it is more secure and provides better performance. To add an extra layer of security, you can use AWS Direct Connect connections that support MACsec to encrypt your data from your on-premises network or collocated device to your chosen AWS Direct Connect point of presence.

1.  Network firewalls are typically deployed within CSP customers’ transport networks to filter traffic to/from the RAN.

1.  The customer-owned on-premises HSM can be used to generate cryptographic keys for importing to AWS KMS and securing an on-premises network, or for equipment purposes.

1.  Given the DU functions are typically deployed at the very far edge of the telco network with limited security monitoring (for example, unmanned cell sites), additional security measures (such as disk encryption, secure boot, and so on) should be considered to protect against physical equipment theft or tampering.
