---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-semicon-workloads/prevent-unauthorized-access.html
---

# Preventing unauthorized access and data exfiltration
<a name="prevent-unauthorized-access"></a>

According to [2022 Cost of a Data Breach Report](https://securityintelligence.com/series/2022-cost-of-a-data-breach-report/) (Ponemon Institute report), the average cost of a data breach in 2022 was USD4.3 million. For semiconductor companies, protecting intellectual property (IP) is critical. Loss of IP due to unauthorized access can result in financial loss, reputational damage, or even regulatory consequences. These potential consequences make controlling access to the data and the flow of data critical aspects of a well-architected design.

Key considerations to secure your data include:
+ User authentication for access to the secure development environment
+ User authorization for access to data within the secure development environment
+ Logging all transfers into and out of the secure development environment
+ Architecting secure data flows between environments
+ Encryption of data in transit and rest
+ Limiting and logging outbound network traffic

## Configuring permissions
<a name="configure-permissions"></a>

[AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them. By default, any action in AWS is implicitly denied unless it is explicitly allowed. You manage access in AWS by creating *policies*. You can use policies to define, at a granular level, which users can access which resources and what actions they can perform on those resources. An AWS best practice is to apply least-privilege permissions, which means you grant users only the permissions they require to perform their tasks. For more information, see the following in the IAM documentation:
+ [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
+ [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#:~:text=Management%20User%20Guide.-,Apply%20least%2Dprivilege%20permissions,known%20as%20least%2Dprivilege%20permissions)

## Authenticating users
<a name="authenticate-users"></a>

It's an AWS best practice to require human users to use federation with an identity provider to access AWS by using temporary credentials. The recommended service for centralizing your user workforce access is [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). This service helps you securely create or connect your workforce identities and manage their access centrally across AWS accounts and applications. IAM Identity Center can federate with external identity providers (IdPs) by using SAML 2.0, Open ID Connect (OIDC), or OAuth 2.0 in order to provide seamless integration and user management. For more information, see [Identity federation in AWS](https://aws.amazon.com/identity/federation/) (AWS marketing) and [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) (IAM documentation).

You can also authenticate and authorize users by using [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) to manage users and groups that are defined in a directory, such as Active Directory. Within the secure development environment, you can use Linux file permissions to authorize and restrict data access within the virtual private cloud (VPC). Use [VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html) to provide access to AWS services without traversing the public internet. Use [endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) to restrict which AWS principals can use the endpoint, and use identity-based policies to restrict access to AWS services.

## Transferring data
<a name="transfer-data"></a>

AWS provides several ways to migrate on-premises data to the cloud. It's common to initially store the data in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). Amazon S3 is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. It provides bandwidth of up to 25 Gbps when transferring data to or from an Amazon Elastic Compute Cloud (Amazon EC2) instance. It also offers cross-Region data replication and data tiering. Data stored in Amazon S3 can serve as a replication source. You can use it to create new file systems or to transfer data to EC2 instances. You can use Amazon S3 as the backend of an AWS managed, Portable Operating System Interface (POSIX)-compliant file system for semiconductor tools and flows.

Another AWS storage service is [Amazon FSx](https://docs.aws.amazon.com/fsx/), which provides file systems that support industry-standard connectivity protocols and offers high availability and replication across AWS Regions. Common choices for the semiconductor industry include [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html), [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html), and [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html). The scalable, high-performance file systems in Amazon FSx are well suited to storing data locally within the secure development environment.

AWS recommends that you [define storage requirements](https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/define-storage-requirements-and-transfer-data.html) for your semiconductor workloads on AWS first and then identify the appropriate data transfer mechanism. AWS recommends using [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) to transfer data from on premises to AWS. DataSync is an online data transfer and discovery service that helps you move files or object data to, from, and between AWS storage services. Depending on whether you are using self-managed storage systems or a storage provider such as NetApp, you can configure DataSync to accelerate moving and replicating data to your secure development environment over the internet or through AWS Direct Connect. DataSync can transfer your file system data and metadata, such as ownership, timestamps, and access permissions. If you're transferring files between FSx for ONTAP and NetApp ONTAP, AWS recommends using [NetApp SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/migrating-fsx-ontap-snapmirror.html). Amazon FSx supports encryption at rest and in transit. Use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and other service-specific logging features to log all API calls and related data transfers. Centralize logs in a dedicated account, and apply granular access policies for immutable history.

AWS provides additional services to help control data flows, including application-aware network firewalls such as [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html), and web proxies. Control data flows within the environment by enforcing network segmentation with [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html), [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and VPC endpoints in Amazon Virtual Private Cloud (Amazon VPC), AWS Network Firewall, [transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html), and [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in AWS Organizations. Centrally log all network traffic by using [VPC Flow Logs](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/vpc-flow-logs.html) and the [available fields](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-fields) from versions 2­–5 of VPC Flow Logs.

## Encrypting data
<a name="encrypt-data"></a>

Encrypt all data at rest by using [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) customer managed keys or [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html). Create and maintain granular key resource policies. For more information, see [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/welcome.html).

Encrypt data in transit by enforcing a minimum of TLS 1.2 with an industry-standard 256-bit Advanced Encryption Standard (AES-256) cipher.

## Managing outbound network traffic
<a name="manage-outbound-traffic"></a>

If the secure development environment requires internet access, then all outbound internet traffic should be logged and restricted through a network-level enforcement point, such as through AWS Network Firewall or [Squid](https://www.squid-cache.org/Intro/), which is an open-source proxy. VPC endpoints and the internet proxy help protect against unauthorized exfiltration of data by users. This is critical to allow access to data within the secure development environment and only within the VPC.

Finally, you can use [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html), a feature of Amazon VPC, to perform network segmentation validation and identify potential network paths that do not meet your specified requirements.

By layering of security controls, you can establish and enforce a robust data perimeter. For more information, see [Building a Data Perimeter on AWS](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html).
