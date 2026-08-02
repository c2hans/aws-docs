---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-foundation-playbook/on-premises.html
---

# On-premises considerations for a large migration
<a name="on-premises"></a>

On-premises infrastructure that supports your business operations must also be prepared for the large migration. By preparing the current infrastructure, you can help reduce the impact of the large migration to the business operations and application users.

This section reviews the infrastructure, operations, and security questions that you should consider when preparing your on-premises infrastructure for the large migration. As you answer the questions in this section, these decisions become *migration principles*, which you document according to the instructions in [Document your decisions as large migration principles](document.md).

## Infrastructure considerations
<a name="on-premises-infra"></a>

|
|
| Have you considered? | Description | Actions |
| --- |--- |--- |
| Have you designed the on-premises DNS and routers to support traffic to and from target AWS accounts? | Because of the large number of servers and target AWS accounts, it is important to confirm that different networking components are configured correctly to support the migration strategies and scale. | Review the design of routing tables, and make sure there are correct routes between the AWS accounts and on-premises data centers. Also, make sure the DNS server is able to support DNS queries from both on-premises servers and AWS resources. |
| How will the migration team access both the on-premises and AWS environments? | The migration team needs to access the source and target servers to perform migration activities, such as install a replication agent on a source server or uninstall old software on a target server. | Review the existing authentication and authorization mechanisms and build a strategy to grant access. You can use an Active Directory group, IAM role, and Security Assertion Markup Language 2.0 (SAML 2.0) federation to allow single sign-on to the AWS account. We recommend creating a local admin user in case there are any authentication issues with Active Directory. |
| Are there any known congestion points in the current network configuration that would slow data throughput during the migration? | A large migration requires lots of bandwidth to replicate the data from on-premises data center to the cloud. Understanding any existing congestion points or limitations helps you better plan the migration. | Review the network configuration with the networking team to better understand the network path from the source machines to the target AWS accounts. Identify potential congestion points, such as a connection that is shared between the migration and production workloads. |

## Operations considerations
<a name="on-premises-ops"></a>

|
|
| Have you considered? | Description | Actions |
| --- |--- |--- |
| Do you have any scheduled blocked days, also known as *change freezes*, that could impact the migration? | A change freeze during migration can take critical resources and time away from an ongoing migration project. | Review the change management process with the operations team, and take blocked days into consideration when you plan cutover windows. |
| Have you reserved change days for the migration? | Change management processes can be complex, and some organizations allow changes only in certain maintenance windows. | According to your change management process, schedule changes at least five waves in advance. This helps prevent delays. |
| Have all of the servers in scope for the migration been recently rebooted? | System changes or uninstalled patches might cause issues during the migration, which would necessitate long cutover windows or rolling back the server. The best practice is to confirm that the server has been recently rebooted on the target side before migrating. | Review the dates of the last server reboots. If a server has not been restarted within the last 90 days, schedule a restart before migrating the server. |
| How does the disaster recovery and business continuity plan work today, and has this been factored into the landing zone design? | Disaster recovery and business continuity plans are critical components of meeting the recovery time objective (RTO) and recovery point objective (RPO) of the application. You need to make sure these plans work for both your on-premises and AWS workloads during the transition period. | Review the existing disaster recovery and business continuity plans and make sure the plans work for your target AWS account. If not, design new plans before moving workload to the AWS Cloud. |

## Security considerations
<a name="on-premises-security"></a>

|
|
| Have you considered? | Description | Actions |
| --- |--- |--- |
| Have you created firewall rules to support the large migration? | Depending on the processes in your organization, it can take a long time to complete a change request for firewall configurations. | Review the existing firewall change process with security team, and design a strategy for large migration firewall changes accordingly. You might need to design a custom process for the large migration project, or you might need to submit changes early in the project. It is recommended that you consider using an AWS virtual private cloud (VPC) as an extension to your data center and avoid building firewall rules that are too complex, which could significantly delay the large migration. |
| Have you set up Active Directory in the AWS environment? | Active Directory is used for authentication and authorization. You need to make sure the target account workloads are able to connect to the domain controller for authentication and authorization. You can either add a new domain controller in the target VPC, or you can allow the AWS workload to connect to the on-premises domain controllers. | Review the Active Directory design with your security and infrastructure teams. Make sure the target AWS account has connectivity to the correct domain controller. Make sure that the target AWS subnet CIDR blocks are in the correct Active Directory sites so that the workloads in AWS are able to connect to the nearest domain controllers. |
| Have you identified third-party connections and application interdependencies? | Third-party connections and application interdependencies require that you modify the firewall rule, network access control list, and security group. | During the deep dive session with the application owners, review the external dependencies for each application. Submit a request to modify firewall rules and the network access control list and change security groups accordingly, based on the third-party dependency requirements. |
| Does your on-premises environment have any additional security tools that control access and processes running on the systems, such as CyberArk? | You might need to assess and update these security tools in order to allow the migration tools to function in the AWS landing zone. | Review the access policy in your source environment. If a security tool is being used in the access policy, confirm that the tool functions in the AWS Cloud, and then make sure that the migration team has access to both the source and target environments. If any changes are required, add these steps into your migration runbooks. |
