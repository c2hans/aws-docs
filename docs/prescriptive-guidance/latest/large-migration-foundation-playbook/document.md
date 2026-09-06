---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/document.html
---

# Document your migration principles
<a name="document"></a>

After reviewing the landing zone and on-premises considerations, you should document your answers and decisions. These become the migration principles that guide the rest of the project.

Do the following:

1. Open the attached *Migration principles template* (Microsoft Word format).

1. Review the infrastructure, operations, and security considerations in the Landing zone considerations for a large migration and On-premises considerations for a large migration sections of this guide, and discuss the questions with the recommended teams.

1. Document the infrastructure, operations, and security decisions in your migration principles document. For examples of how to record these decisions, see the following table.

1. As needed for your use case, add new categories, items, and principles. For example, you might want to record migration principles for portfolio assessment or project management decisions.

The following is an example of how you might record your decisions to some of the questions in this guide.

|
|
| Category | Item | Principle |
| --- |--- |--- |
| Infrastructure | DNS server | Use Amazon-provided DNS as the primary DNS server for all Amazon Elastic Compute Cloud (Amazon EC2) instances. Set up a conditional forwarder that forwards queries to an on-premises DNS server. |
| Security groups | Use a temporary security group to permit all standard infrastructure traffic between the source and target environments. |
| EC2 instance types | If utilization data is available from a discovery tool, such as Flexera One or modelizeIT, use this information to help determine the target instance type.<br />If utilization data is not available, size the target instance based on the provisioned central processing unit (CPU) and memory of the on-premises infrastructure.<br />  |
| Operations | Clean up | Servers remain in the staging area until the migration phase is complete, at the end of the hypercare period. |
| AWS Backup | By default, the tag applied to each instance is backup = true. If backups are not required, the migration teams should change the tag to false. |
| Monitoring | Use Amazon CloudWatch for monitoring of EC2 instances. After cutover, remove the existing monitoring agent from the target EC2 instances. |
| Security | Active Directory | Build a domain controller in each VPC, and link the subnet of that VPC to your Active Directory site. For more information, see [Designing the Site Topology](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology). This configures all clients to use the correct domain controller. |
| Server access | Users must retrieve a password from CyberArk to connect to the source machines. |
| AWS Management Console access | Users must use federated login to access the AWS Management Console. |
