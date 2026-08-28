---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/storage-migration.html
---

# Storage migration
<a name="storage-migration"></a>

AWS provides dedicated migration tools including AWS DataSync for data transfers, AWS Storage Gateway for hybrid integrations, and AWS Transfer Family for protocol-based transfers. These services use cloud-native services like S3, EBS, and EFS. Transitioning to AWS has advantages over VMware including automatic scaling versus manual capacity planning, pay-as-you-go pricing versus fixed infrastructure costs, built-in multi-AZ replication versus manual redundancy setups, and automated lifecycle policies versus manual storage administration.

AWS migrations employ phased approaches that integrate security with encryption in transit and at rest, automated data protection, and automated backups. The result is a resilient, scalable storage environment that supports growth and innovation while minimizing traditional storage-management complexities.

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Migration scenario | Exports VMs or data from VMware's on-premises infrastructure to new platforms | Uses native AWS tools and services for seamless data transition with minimal downtime |
| Storage type mapping | Block storage (VMFS), file storage (NFS), vSAN, and object storage (limited cases) | Amazon EBS (block storage), Amazon EFS (file storage), and Amazon S3 (object storage) |
| Network requirements | Requires dedicated VMkernel ports for storage traffic | Uses VPC endpoints for secure private network communication to storage services |
| Migration tools | VMware vCenter Converter or third-party migration tool | DataSync, Transfer Family, and Storage Gateway |
| Data transfer process | Manual transfer of VMDKs or use a third-party replication tool | Supports AWS DataSync for automation, Transfer Family for SFTP/FTP, and Storage Gatewayfor hybrid environments |
| Advantages | Depends on extent of manually updating resources and maintenance of on-premises infrastructure | Scalability, global reach, cost-effectiveness, and reduced management overhead with pay-as-you-go pricing |
| Security considerations | RBAC on-premises encryption | Uses IAM policies, bucket policies, and AWS KMS for encryption at rest and in transit |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
