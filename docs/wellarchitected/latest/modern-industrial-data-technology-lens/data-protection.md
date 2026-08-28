---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/data-protection.html
---

# Data protection
<a name="data-protection"></a>

|  MIDASEC05: How do you manage access to industrial data within your workloads?  |
| --- |
|   |

 Establish clear and granular access controls for industrial data based on job roles and operational responsibilities. Implement centralized identity management systems, proper authorization models (ABAC or RBAC), and secure data sharing protocols to verify that only authorized personnel can access specific manufacturing data resources. These best practices help you maintain security and meet compliance requirements.

|  MIDASEC06: How do you securely and efficiently share data in industrial environments?  |
| --- |
|   |

 Implement secure and standardized protocols for sharing industrial data both internally and externally across manufacturing environments. Establish clear data ownership responsibilities, implement secure data exchange mechanisms like MQTT over TLS or OPC-UA with encryption, and maintain proper access controls to help protect data confidentiality and integrity while enabling effective collaboration across the industrial environment.

**Topics**
+ [MIDASEC05-BP01 Define access permissions](midasec05-bp01.md)
+ [MIDASEC05-BP02 Build user identity solutions](midasec05-bp02.md)
+ [MIDASEC05-BP03 Implement data authorization models](midasec05-bp03.md)
+ [MIDASEC06-BP01 Use secure data exchange protocols](midasec06-bp01.md)
+ [MIDASEC06-BP02 Establish clear data ownership and sharing agreements](midasec06-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
