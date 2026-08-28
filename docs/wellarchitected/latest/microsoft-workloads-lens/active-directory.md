---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/active-directory.html
---

# Active directory
<a name="active-directory"></a>

 Active Directory is a critical component for many Microsoft workloads, and optimizing its deployment on AWS can lead to significant cost savings and operational efficiencies. AWS offers multiple options to support Active Directory needs, including AWS Managed Microsoft AD, AD Connector, and self-managed Active Directory on EC2. Each option provides different benefits in terms of management overhead, scalability, and cost. By evaluating these options against specific workload requirements, organizations can choose the most cost-effective and operationally efficient Active Directory solution for their AWS environment.

|  MSFTCOST06: How do you save on Active Directory for your Microsoft workload?  |
| --- |
|   |

 Microsoft Active Directory has been a widely used identity management solution in Windows networks for decades. It delivers authentication and access protocols, such as LDAP and Kerberos. When deploying Active Directory on AWS, consider the options to make sure you are saving on direct or operational costs for your Microsoft workload

**Topics**
+ [MSFTCOST06-BP01 Use AWS Managed Microsoft Active Directory](msftcost06-bp01.md)
+ [MSFTCOST06-BP02 Use AD Connector](msftcost06-bp02.md)
+ [MSFTCOST06-BP03 Use self-managed Active Directory on Amazon EC2](msftcost06-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
